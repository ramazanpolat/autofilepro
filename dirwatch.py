import threading
import time
from pathlib import Path
from threading import Thread
from time import sleep
from typing import List
import os
import sys
import argparse
import signal

command = "%s"


def signal_handler(signal, frame):
    sys.exit(0)


def run_command(file_name):
    os.system(command % file_name)


class DirWatch:
    def __init__(self, name, directory, file_filter, interval=1):
        self.interval = interval
        self.name = name
        self.file_filter = file_filter
        self.directory = directory
        self.file_snapshot = self.get_files()

    def added_files(self):
        new_snapshot = self.get_files()
        result: List[Path] = []
        for f in new_snapshot:
            if f not in self.file_snapshot:
                result.append(f)
        self.file_snapshot = new_snapshot
        return result

    def get_files(self):
        # files = os.listdir(self.directory)
        p = Path(self.directory)
        return [x for x in p.glob(self.file_filter) if x.is_file()]

    def start_watching_thread(self, callback=None):
        Thread(target=self.start_watching, args=(callback,), daemon=True).start()

    def start_watching(self, callback=None):
        while True:
            sleep(self.interval)
            added_files = self.added_files()
            if added_files:
                if callback:
                    for file in added_files:
                        # print(str(file))
                        callback(str(file))


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    parser = argparse.ArgumentParser(description="Watch a directory for new files.")
    parser.add_argument('--dir', dest='dir', metavar='-D', type=str, help='Directory to watch', default='.')
    parser.add_argument('--filter', dest='filter', metavar='-F', type=str, help='File filter', default='*.*')
    parser.add_argument('--send', dest='send', metavar='-C', type=str, help='send', default='echo %s')
    parser.add_argument('--interval', dest='interval', metavar='-I', type=int, help='interval', default=1)

    args = parser.parse_args()
    # print("args.send:", args.send)
    # print("args.dir:", args.dir)
    # print("args.filter:", args.filter)
    # print("args.period:", args.period)

    command = args.send
    dw = DirWatch(name="File", directory=args.dir, file_filter=args.filter, interval=args.interval)
    dw.get_files()
    dw.start_watching_thread(callback=run_command)
    while True:
        time.sleep(10)
    # forever = threading.Event()
    # forever.wait()

from pathlib import Path
from threading import Thread
from time import sleep
from typing import List


class DirWatcher:
    def __init__(self, name, directory, file_filter):
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
            sleep(1)
            added_files = self.added_files()
            if added_files:
                print('Added files:', added_files)
                if callback:
                    for file in added_files:
                        callback(file)


if __name__ == '__main__':
    dw = DirWatcher(name="txt", directory="./input", file_filter="*.py")
    dw.get_files()
    dw.start_watching_thread(callback=print)
    print("After thread")
    input("PRESS ANY KEY...")

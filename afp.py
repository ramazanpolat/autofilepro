import config
from dirwatcher import DirWatcher
from processors import PROCESSORS

phases = config.phases

if __name__ == '__main__':
    print('---=== AUTO FILE PROCESSOR ===---')

    for phase in phases:
        print('PHASE(%s)' % (phase['name']))
        # print(phase)
        processor = phase['processor']
        print('\tprocessor:', processor)
        dw = DirWatcher(name=phase['name'], directory=phase['input_dir'], file_filter=phase['file_filter'])
        print('\tDirWatcher(%s) is watching  "%s"...' % (phase['name'], phase['input_dir']))
        # dw.start_watching_thread(callback=processor)
        dw.start_watching_thread(callback=PROCESSORS[processor])

    while True:
        inp = input('Enter "q" to quit\n')
        if inp == 'q':
            break

# Design Patterns

'''
The Observer Pattern objects are represented as observers that wait for an
event to trigger. An Observer attaches to the subject once a specified event
occurs. When the event occurs, the subject tells the observers that it has
occurred.
'''

import threading
import time
import pdb


class Downloader(threading.Thread):
    def run(self):
        print('Downloading...')
        for i in range(1, 5):
            self.i = i
            time.sleep(2)
            print(f'Chunk {i}')
        print('[Downloader]: Done!')
        return 'Hello, world!'


class Worker(threading.Thread):
    def run(self):
        for i in range(1, 5):
            print(f'Worker Running: {i} ({t.i})')
            time.sleep(1)
            t.join()
        print('[Worker]: Done!')


t = Downloader()
t.start()
time.sleep(1)

def main():
    for i in range(3):
        ti = Worker()
        ti.start()


if __name__ == '__main__':
    main()

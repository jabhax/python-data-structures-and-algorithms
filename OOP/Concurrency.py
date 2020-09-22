# Design Patterns

'''
Concurrency is often misunderstood as parallelism. Concurrency implies
scheduling independent code to be executed in a systematic manner. This is an
example focusing on the execution of concurrency for an operating system using
Python.
'''

import os
import time
import threading as T
import multiprocessing as MP


class CustomThreader:
    def __init__(self, workers=4):
        self.NUM_WORKERS = workers
        self._start_time = None

    def _print_t_info(self):
        print(f'PID: {os.getpid()}, PNAME: {MP.current_process().name}, TNAME: {T.current_thread().name}')

    def sleep(self):
        self._print_t_info()
        time.sleep(1)

    def serial_time(self):
        self._start_time = time.time()
        for _ in range(self.NUM_WORKERS): self.sleep()
        end_time = time.time()
        print(f'Serial time={(end_time - self._start_time)}\n')

    def threads_time(self):
        self._start_time = time.time()
        threads = [T.Thread(target=self.sleep) for _ in range(self.NUM_WORKERS)]
        [t.start() for t in threads]
        [t.join() for t in threads]
        end_time = time.time()
        print(f'Threads time={(end_time - self._start_time)}\n')

    def parallel_time(self):
        self._start_time = time.time()
        processes = [MP.Process(target=self.sleep) for _ in range(self.NUM_WORKERS)]
        [p.start() for p in processes]
        [p.join() for p in processes]
        end_time = time.time()
        print(f'Parallel time={(end_time - self._start_time)}\n')


def main():
    ct = CustomThreader()
    ct.serial_time()
    ct.threads_time()
    ct.parallel_time()


if __name__ == '__main__':
    main()

# https: // docs.python.org/3/library/multiprocessing.html

from multiprocessing import Process
import os


def child_function():
    pid = os.getpid()
    for i in range(20):
        print('child process id: ', pid)


if __name__ == '__main__':
    childs = []
    for i in range(3):
        p = Process(target=child_function)
        childs.append(p)
        p.start()
    for i in range(20):
        string_to_print = ''
        for i in childs:
            string_to_print = string_to_print + str(i.pid) + ',  '
        print(string_to_print)

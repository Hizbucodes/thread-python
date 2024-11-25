import threading
import time
import sys

class PrintThread1(threading.Thread):
    def __init__(self, name, lock):
        super(PrintThread1, self).__init__()
        self.name = name
        self.lock = lock

    def run(self):
        for i in range(1, 10):
            try:
                time.sleep(1)
            except Exception as e:
                print(e)
            with self.lock:
                sys.stdout.write(self.name)
                sys.stdout.flush()

if __name__ == "__main__":
    lock = threading.Lock()

    a = PrintThread1("*", lock)
    b = PrintThread1("-", lock)
    c = PrintThread1("=", lock)

    a.start()
    b.start()
    c.start()

    a.join()
    b.join()
    c.join()

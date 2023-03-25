import threading
import time

ticket = 100
# 创建锁
lock = threading.RLock()

class MyThread(threading.Thread):

    def run(self):
        global ticket
        while ticket > 0:
            # 加锁，获取到锁，其它线程先排队等着
            lock.acquire()
            if ticket < 1:
                lock.release()
                return
            ticket = ticket - 1
            time.sleep(0.1)
            name = threading.currentThread().getName()
            # if ticket > 0:
            print(f'{name}卖了1张票，还剩{ticket}张')
            lock.release()
        pass

for num in range(5):
    th = MyThread()
    th.setName(f'th-{num}')
    th.start()
    pass
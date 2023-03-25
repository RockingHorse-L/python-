import threading

class MyThread(threading.Thread):
    #线程执行的任务
    def run(self):
        print(threading.currentThread())
        pass

# #创建线程
# th = MyThread()
# th.setName('thread-01')
# #开启线程
# th.start()
#
# th2 = MyThread()
# th2.setName('thread-02')
# #开启线程
# th2.start()
#
# th3 = MyThread()
# th3.setName('thread-03')
# #开启线程
# th3.start()

for num in range(5):
    th = MyThread()
    th.setName(f'thread-{num}')
    #开启线程
    th.start()
    pass
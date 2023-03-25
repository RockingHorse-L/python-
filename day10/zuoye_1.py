import threading

# 1. 执行任务 函数
def task(*args):
    # print('执行任务')
    print(threading.currentThread())
    # print(args)
    pass


# 创建线程
# target 当前线程执行的任务
# args 任务执行的适合传参
# name 线程的名字
thread = threading.Thread(target=task, args=('sunny', 18), name= 'thread-01')
#开启线程
thread.start()

thread02 = threading.Thread(target=task, args=('sunny', 18), name='thread-02')
#开启线程
thread02.start()
print(thread02.is_alive())
print(thread02.ident)
print(thread02.getName())
# print(thread.native_id)
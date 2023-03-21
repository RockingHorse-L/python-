#短路与 运行到的第二个条件False结果就会为False不会再执行后面的Ture
print(True and False and True)

#0被看成是False，返回0
print(0.1 and 1 and 0 and '张三' and '')

#结合其他数据类型被当成bool值处理，以及短路性最终返回hello
print(0 or '' or [] or 'hello' or None)
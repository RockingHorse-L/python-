flag = int(input('请登录或者注册,登录请输入1，注册请输入2：'))
if flag == 2:
    print('注册：')
    file = open('database.txt', 'a', encoding='UTF-8')
    username = input('请输入用户名：')
    password = input('请输入密码：')
    file.write(username + '|' + password + '\n')
    file.close()
if flag == 1:
    file = open('database.txt', 'r', encoding='UTF-8')
    username = input('请输入用户名：')
    password = input('请输入密码：')
    lines = file.readlines()
    # print(lines)
    for line in lines:
        userInfo = line.strip('\n').split('|')
        print(userInfo)
        if userInfo[0] == username and userInfo[1] == password:
            success = 1
    if success:
        print('登录成功')
    else:
        print('用户名或密码错误')
    # if username == userNameFile and password == passWordFile:
    #     print('登录成功')
    # else:
    #     print('用户名或密码错误')
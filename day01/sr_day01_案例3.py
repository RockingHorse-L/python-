"""
    个人名片
    需求：提示用户输入姓名，公司，职位，电话，公司地址
"""
name = input("用户名：")
company = input("公司名：")
number = input("电话号码：")
post = input("职位：")
address = input("公司地址：")

#方法一
sep = '*'*35
info = f"""
        {sep}
        
        姓名：{name}         电话：{number}
        职位：{post}         公司：{company}
        公司地址：{address}
        
        {sep}
"""
print(info)

#方法二
# print('*'*30)
# print(f"姓名：{name}",' '*5, f"电话：{number}")
# print(f"职位：{post}",' '*5, f"公司：{company}\n"
#       f"公司地址：{address}\n",
#       "*"*30)

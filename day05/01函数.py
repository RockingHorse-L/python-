"""
    9*9乘法表
"""
def mulTable(rownum):

    row = 1
    while row <= rownum:
        col = 0
        while col < row:
            col += 1
            print(f"{col} * {row} = {col * row}" , end='\t')
        row += 1
        print()

rownum = int(input('please enter you number：'))
mulTable(rownum)
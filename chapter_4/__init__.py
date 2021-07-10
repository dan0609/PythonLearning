magicians = ['alice', 'david', 'carolina']

# 打印magicians
# for magician in magicians:
#     print(magician)

# 输出alice , david , carolina

if __name__ == '__main__':
    result = ""
    length = len(magicians)
    for index in range(0,length):
        if index != length - 1:
            result = magicians[index] + ' , '
        else:
            result = magicians[index]
    print(result)
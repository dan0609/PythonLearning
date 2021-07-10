# Q1:打印magicians
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)

# Q2:输出alice , david , carolina
# if __name__ == '__main__':
#     magicians = ['alice', 'david', 'carolina']
#     result = ""
#     length = len(magicians)
#     for index in range(0,length):
#         if index != length - 1:
#             result = magicians[index] + ' , '
#         else:
#             result = magicians[index]
#     print(result)

# Q3: 计算 input的总和
# if __name__ == '__main__':
#     input = [1, 2, 3]
#     result = 0
#     length = len(input)
#     for i in input:
#         result = result + i
#     print(result)

# Q4:把input1中input2的单词过滤掉

if __name__ == '__main__':
    input1 = "I have a student"
    input2 = "aeiou"
    result = ''
    input1list = []
    for i in input1:
        input1list.append(i)
    for i in input1list:
        for j in input2:
            if i == j:
                 input1list.remove(i)
    for i in input1list:
        result = result + i
    print(result)
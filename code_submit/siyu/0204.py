# Q1 Write a function fibo() that takes an integer n as a parameter and displays the numbers in the Fibonacci sequence up to rank n. The Fibonacci sequence is a sequence of integers in which each term is the sum of the two preceding terms.The term of rank n, denoted fn is defined by f0 = 0, f1 = 1 and fn = fn-1 + fn-2 for n > 2.For example, the call fibo(5) will display: 0 1 1 2 3


# def fibo(n):

#     fn = [0, 1]
#     if n.isdigit():
#         n = int(n)
#         if n == 1 or n == 2:
#             print(fn[n-1])

#         elif n > 2:
#             for i in range(2, n):
#                 fn.append(fn[i-1]+fn[i-2])
#             for x in range(len(fn)):
#                 print(fn[x], end=" ")
#         else:
#             print("please input an integer:", end=" ")
#             fibo(input())
#     else:
#         print("please input an integer:", end=" ")
#         fibo(input())


# print("input an integer:", end=" ")
# integer = input()
# fibo(integer)


# Q2
# def bigrams(string):
#     String2 = []
#     for i in range(len(string)):
#         if string[i] != " ":
#             String2.append(string[i])
#     for x in range(len(String2)-1):
#         print(String2[x], end="")
#         print(String2[x+1])


# bigrams("the moon")

# 不用append：-------------
def bigrams(string):
    for i in range(len(string)):
        if string[i] == " ":
            del string[i]
            bigrams(string)
    for x in range(len(string)-1):
        print(string[x], end="")
        print(string[x+1])


bigrams("the moon")

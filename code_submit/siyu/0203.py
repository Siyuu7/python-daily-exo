# A list S of integers is sorted (in descending order) if and only if S[i+1] <= S[i] for all possible values of i. Write a function that takes as parameter a list of integers, and returns True if the list is sorted, False otherwise.The only predefined functions that can be used are len(), range().
# S = [2, 4, 5, 7, 5, 3, 6]
# # S = [2, 3, 4, 5, 6, 7, 8]
# # S = [8, 7, 6, 5, 4, 3, 2]

# for i in range(len(S)-1):
#     if S[i+1] <= S[i]:

#         if i == len(S)-2:
#             print("OK")
#         continue
#     else:
#         print("NOTOK")
#         break


# -Write a function that takes as input a list of words, and returns the average length of the words in the list, as well as the number of words of length greater than or equal to this average length.The only predefined functions that can be used are len(), range().

List = ["a", "list", "of", "words"]
length = 0
number = 0
for i in range(len(List)):
    s = len(List[i])
    length = s + length
print("the average length of the words is " + str(length/len(List)))

for i in range(len(List)):
    if len(List[i]) >= length/len(List):
        number = number+1
print("the number of words of length greater than or equal to this average length is " + str(number))

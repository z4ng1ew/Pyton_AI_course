# words = ["1first", "second", "third"]
# #
# # for word in words: # Цикл берет список words и последовательно, один за другим, присваивает каждый его элемент переменной word.
# #     print(word)
# #
# #
#
#
# i = 0
# while i < len(words):
#     print(words[i])
#     i+=1


numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers1.insert(2, 100)

numbers1.extend([11, 12, 13, 14, 15, 16, 17, 18, 19])


i = 0

while i < len(numbers1):
    print(numbers1[i])
    i += 1


# numbers2 = [1, 5, 6, 7, 8, 9, 10]
#
# if numbers2  == numbers1:
#     print("numbers2 is equal to numbers1")
# else:
#     print("numbers2 is not equal to numbers1")
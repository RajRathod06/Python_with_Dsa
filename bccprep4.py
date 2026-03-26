# Linear Search 

# def addition(a,b):
#     return a + b
# result = addition(2,3)
# print(result)

# def linear_search(list, target):
    # for i in range(len(list)):
    #     if list[i] == target:
    #         return i
    # return -1

#     i = 0
#     while i < len(list):
#         if list[i] == target:
#             return i
#         i += 1
#     return -1
# list = [10, 20, 30, 40, 50]
# target = int(input("Enter the target value: "))
# index = linear_search(list, target)
# print("Target found at index:", index)


list=[10,20,30,40,50]
target = int(input("Enter the target value: "))

if target in list:
    index = list.index(target)
    print("target found at index:", index)
else:
    print("target not found in the list")
    
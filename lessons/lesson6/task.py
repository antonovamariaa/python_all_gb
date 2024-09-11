# def func(a=None):
#     if a is None:
#         a = []
#     a.append(1)
#     print(a)

# func()
# func([4, 5, 6])



# #task1 var 1
# def func_input(n):
#     print("Вводим элементы нового списка")
#     new_list =  []
#     for i in range(int(n)):
#         buffer = input("Введите новый элемент: ")
#         new_list.append(buffer)
#     return new_list

# def func_sort(n_1,n_2):
#     list_1 = set(func_input(n_1))
#     list_2 = set(func_input(n_2))
#     list_1 = list_1.difference(list_2)
#     print(f"Результат операции: {list_1}")

# n_1 = int(input("Введите количество элементов первого набора: "))
# n_2 = int(input("Введите количество элементов второго набора: "))

# func_sort(n_1,n_2)



# #task1 var 2
# def func(my_list, yours_list):
#     answer = list()
#     for value in my_list:
#         if value not in yours_list:
#             answer.append(value)
#     return answer

# def generation(m):
#     my_list = list()
#     for i in range(m):
#         value = int(input("Введите элемент первого  множества: "))
#         my_list.append(value)
#     return my_list


# m = int(input("Введите количество элементов первого множества: "))
# my_list = generation(m)

# k = int(input("Введите количество элементов второго множества: "))
# yours_list = generation(k)




# #task2
# def func(array):
#     count = 0
#     for i in range(1, len(array) - 1):
#         if array[i - 1] < array[i] > array[i + 1]:
#             count += 1
#     return count

# array  = [1, 5, 1, 5, 1, 5, 2]
# print(func(array))


# #task3 var1
# def f(a = []):
#     count = 0
#     for i in range(len(a)):
#         if a[i] in a[::i+1 ]:
#             count += 1
#     return count

# print(f([1, 2, 1, 2, 2, 3, 4]))


# #task3 var2
# list_n = [1, 2, 1, 2, 2, 3, 4]
# count = 0
# for i in range(len(list_n)-1):
#         count +=  list_n[i+1:].count(list_n[i])
# print(count)


# #task3 var3
# def search_dbl(start_list):
#     count = 0
#     for i in range(len(start_list) - 1):
#         for j in range(i+1, len(start_list)):
#             if start_list[i] == start_list[j]:
#                 count += 1
#     return count

# start_list = [1, 2, 1, 2, 2, 3, 4]
# print(search_dbl(start_list))



# #task4 mini boss

# def get_summ(n):
#     count = 0
#     for i in range(1, n):
#         if n % i == 0:
#             count += i
#     return count


# k = 300
# for num_1 in range(1, k):
#     num_2 = get_summ(num_1)
#     sum_del_num_2 = get_summ(num_2)
    
#     if (num_1 == sum_del_num_2) and (num_1 != num_2) and (num_1 < num_2):
#         print(num_1, num_2)










# # Напишите программу, которая принимает на вход
# # строку, и отслеживает, сколько раз каждый символ
# # уже встречался. Количество повторов добавляется к
# # символам с помощью постфикса формата _n.
# # Input: a a a b c a a d c d d
# # Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# # Для решения данной задачи используйте функцию
# # .split()

# input = ("a a a b c a a d c d d")
# my_list = input.split()
# my_dict = {}

# for i in my_list:
#     # print(i)
#     if i not in my_dict:
#         my_dict[i] = 0
#         print(i+' ',end='')
#     else:
#         print(i,end='')
#         my_dict[i] += 1
#         print('_' + str(my_dict[i]) +' ',end='')


# # Пользователь вводит текст(строка). Словом считается
# # последовательность непробельных символов идущих
# # подряд, слова разделены одним или большим числом
# # пробелов. Определите, сколько различных слов
# # содержится в этом тексте.
# # Input: She sells sea shells on the sea shore The shells
# # that she sells are sea shells I'm sure.So if she sells sea
# # shells on the sea shore I'm sure that the shells are sea
# # shore shells
# # Output: 13

# input = ('''She sells sea shells on the sea shore The shells that she sells are sea shells 
#I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells''')
# new = input.split()
# new = set(new)
# print(new)
# print(len(new))



# # Ваня и Петя поспорили, кто быстрее решит
# # следующую задачу: “Задана последовательность
# # неотрицательных целых чисел. Требуется определить
# # значение наибольшего элемента
# # последовательности, которая завершается первым
# # встретившимся нулем (число 0 не входит в
# # последовательность)”. Однако 2 друга оказались не
# # такими смышлеными. Никто из ребят не смог до
# # конца сделать это задание. Они решили так: у кого
# # будет меньше ошибок в коде, тот и выиграл спор. За
# # помощью товарищи обратились к Вам, студентам.

# num = -1
# maxnum = 0

# while num != 0:
#     num = int(input("input num: "))
#     if num == 0:
#         break
#     if num >= maxnum:
#         maxnum = num

# print(maxnum)



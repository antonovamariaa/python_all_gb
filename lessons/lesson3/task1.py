#arr = [1, 1, 2, 0, -1, 3, 4, 4]
#count = 0

#for i in range(len(arr)):
#    if (arr[i]) not in arr[:i]:  #not in и in проверяет сразу весь массив, входит ли элемент в него
                                    # :i - срез массива, генерирует новый список элементов, используя границы
                                    # левая граница:правая граница невключительно, если неуказано, то берется включительно
                                    # :: шаг 2
#      0  1  2  3  4
#arr = [1, 2, 3, 4, 5]

# arr[1:3] -> [2, 3]
# arr[:3] -> [1, 2, 3]
# arr[2:] -> [3, 4, 5]
# arr[:] -> [1, 2, 3, 4, 5]
# arr[::2] -> [1, 3, 5]
#        count+=1
#print(count)

#arr = set(arr)  #очень полезная вещь для удаления повтор элементов
##print(len(arr))


#my_list = [1, 1, 2, 0, -1, 3, 4, 4]
#already_seen = []

#for i in range(len(my_list)):
#    for j in range(len(already_seen)):
#        if my_list[i] == already_seen[j]:
#            break
#    else:
#        already_seen.append(my_list[i])

#print(len(already_seen))





#  k = 2
#         -5 -4 -3 -2 -1
#          0  1  2  3  4
#my_list = [1, 2, 3, 4, 5]
#          3, 4, 5, 1, 2
#          4, 5, 1, 2, 3

#k = int(input('-> '))
#k %= len(my_list)

#print(my_list[-k:] + [:-k])

#arr =  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 
#for i in range(len(arr)):
#    print (arr[i])





#all_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, \
#            {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 

#all_vals = []

#for small_dict in all_dicts:
#    for val in small_dict.values():
#        if val not in all_vals:
#            all_vals.append(val)
            
#print(all_vals)

arr = [0, -1, 5, 2, 3]
count = 0
for i in range (1, len(arr)):
    if arr[i] > arr[(i-1)]:
        count += 1

print (count)




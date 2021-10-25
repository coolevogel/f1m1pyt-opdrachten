list = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3] 

list_of_floats = []
for item in list:
    list_of_floats.append(float(item))

print(list_of_floats)

print (list[0]+list[1])
for element in list:
     print(element)

list.append(93.1)
for element in list:
    print(element)

var1 = list.pop(0) + list.pop(0)

print(var1)
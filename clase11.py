import random 
list1 = [random.randint(1, 100) for _ in range(20)]
list2 = list1
print('Lista 1, en memoria {}'.format(id(list1)),'Lista 2, en memoria {}'.format(id(list1)), list1, list2, ' ', sep='\n')
del list1[::2]
print('Lista 1, en memoria {}'.format(id(list1)),'Lista 2, en memoria {}'.format(id(list1)), list1, list2,' ', sep='\n')
list3 = [random.randint(1, 100) for _ in range(20)]
list4 = list3[:]
print('Lista 3, en memoria {}'.format(id(list3)),'Lista 4, en memoria {}'.format(id(list4)), list3, list4,' ', sep='\n')
del list3[1::2]
print('Lista 3, en memoria {}'.format(id(list3)),'Lista 4, en memoria {}'.format(id(list4)), list3, list4,' ', sep='\n')

def covertList(list):
    list.insert(len(list)-1,'and')
    temp = ', '.join(list[:len(list)-2]) + ', ' + ' '.join(list[len(list)-2:])
    print(temp)
    return temp

spam = ['a', 'b', 'c', 'd', 'e', 'f']

covertList(spam)

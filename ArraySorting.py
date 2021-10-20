def returnElement(array,point,n):
    array.sort()
    print(array)
    if point == 'end':

        return array[len(array)-n]
    else:
        return array[n-1]
if __name__ == '__main__':
    point = input('Where do you want to search the nth value start/end\n->')
    size = int(input('Enter size of the array\n->'))
    n = int(input('Enter nth number\n->'))
    array = []
    print('Enter the array : -> ')
    for i in range(size):
        array.append(int(input()))
    

    result = returnElement(array,point,n)
    print('Result is {}'.format(result))



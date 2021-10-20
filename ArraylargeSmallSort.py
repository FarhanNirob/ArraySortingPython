def returnElement(array, type_of_sorting):
    number = ""
    if type_of_sorting == 'smallest':
        array.sort()

        for i in array:
            
            number = number + str(i)
    else:
        array.sort(reverse=True)
        for i in array:
            
            number = number + str(i)

    try:

        return int(number)
    except:
        return number

if __name__ == '__main__':
    type_of_sorting = input('How do you want to sort the array (smallest/largest)\n->')
    size = int(input('Enter size of the array\n->'))
    array = []
    print('Enter the array : -> ')
    for i in range(size):
        array.append(int(input()))
    result = returnElement(array, type_of_sorting)

    print('Result is {}'.format(result))
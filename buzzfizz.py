def div(n):
    mylist = []
    for i in range(n + 1)[1:]:
        if (i % 3 == 0) and (i % 5 == 0):
            mylist.append('BuzzFizz')
            continue
        elif (i % 5 == 0):
            mylist.append('Fizz')
            continue
        elif (i % 3 == 0):
            mylist.append('Buzz')
            continue
        else:
            pass

        mylist.append(i)
    return mylist

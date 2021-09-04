#mylist = []

#def myfunc(*arg):
    #for item in arg:
        #if item % 2 == 0:
            #mylist.append(item)
    #print(mylist) 

    #for item in arg:
        #if (item % 2) == 0:
           # mylist.append(item)
            #return mylist


#myfunc(3,4,5,6)

def myfunc(**kworgs):
    if 'word' in kworgs:
        print("words: {}".format(kworgs['word']))

myfunc(word="castle")
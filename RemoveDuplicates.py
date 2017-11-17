Alist = [1,2,2,2,3,3,4,5,5,6,7,7,8,10]

def remove_duplicates(someList):
    newList = []
    #print someList[0]
    newList.append(someList[0])
    #print newList[0]
    for i in someList:
        #if(i is not in newList, add it
        print "i " + str(i)
        #print "someList[i] " + str(someList[i])
        #if someList[i] not in newList: 
        print "newList " + str(newList)
        if i not in newList:
        #for n in newList:
            #if i != n:
            #if curr_x -1 > 0 and (curr_x-1 , curr_y) not in myList: 
            #print "i " + str(i)
            print "not in, append" + str(i)
            newList.append(i)
            #print "newList " + str(newList)
    return newList            

print remove_duplicates(Alist)

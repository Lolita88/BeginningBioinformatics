def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k) #count = 
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    return FrequentPatterns
    
def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 
def remove_duplicates(someList):
    newList = []
    #print someList[0]
    newList.append(someList[0])
    #print newList[0]
    for i in someList:
        #if i is not in newList, add it
        #print "i " + str(i)
        #print "newList " + str(newList)
        if i not in newList:
           #print "i " + str(i)
            #print "not in, append" + str(i)
            newList.append(i)
            #print "newList " + str(newList)
    return newList            
       

    
#DNA = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
#num = 4num = 5
#print FrequentWords(DNA, num)"""
words = FrequentWords('CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT', 3)

# this join function strips out the '[],
result = ' '.join(remove_duplicates(words))
print result
#print str(remove_duplicates(words))
# Finally, print the words variable.
#print remove_duplicates(words)
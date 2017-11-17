def Skew(Genome):
    skew = {}
    skew[0] = 0
    n = len(Genome)
    #print n #21
    for i in range(1, n + 1):
    # loop through genome length 0-20
    #for i in range(0, n):
        #print "i " + str(i)
        #print "Genome[i-1] " + str(Genome[i-1])
        if Genome[i-1] == "G":
            # G add
            skew[i] = skew[i-1] +1
            #print skew[i-1] +1
        elif Genome[i-1] == "C":
            #C subtract
            #print "i " + str(i) 
            #print "skew[i-1] -1 " + str(skew[i-1] -1)
            skew[i] = skew[i-1] -1
        else:
            #print "hi"
            #print skew[i-1]
            skew[i] = skew[i-1]
        #print "skew " + str(skew)
        #Every time we encounter a G, Skew[i] is equal to Skew[i-1]+1; every time we #encounter a C, Skew[i] is equal to Skew[i-1]-1; otherwise, Skew[i] is equal to Skew[i-1].
    #print skew
    return skew
    # The following returns with the formatted list
    #return ' '.join([str(skew[i]) for i in sorted(skew.keys())])

def MinimumSkew(Genome):
    tempSkew = Skew(Genome)
    #v=list(tempSkew.values())
    #k=list(tempSkew.keys())
    #print v
    #print k
    
    min_value = min(tempSkew.values())
    min_keys = [k for k in tempSkew if tempSkew[k] == min_value]

    it = tempSkew.items()
    min_key = 0
    min_value = 0
    num_mins = 1
    for k, v in it:
        if v < min_value:
            num_mins = 1
            min_key, min_value = k, v
        elif v == min_value:
            num_mins += 1
        
    return min_keys
def MaximumSkew(Genome):
    tempSkew = Skew(Genome)
    #v=list(tempSkew.values())
    #k=list(tempSkew.keys())
    #print v
    #print k
    
    max_value = max(tempSkew.values())
    max_keys = [k for k in tempSkew if tempSkew[k] == max_value]

    it = tempSkew.items()
    max_key = 0
    max_value = 0
    num_max = 1
    for k, v in it:
        if v > max_value:
            num_max += 1
            max_key, max_value = k, v
        elif v == max_value:
            num_max += 1
        
    return max_keys
    #return ' '.join(str(x) for x in min_keys)
#for it to work in class, just call, don't call with print
print (MinimumSkew("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"))  
#print (MaximumSkew("CATTCCAGTACTTCGATGATGGCGTGAAGA")) 
   

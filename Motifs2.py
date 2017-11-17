def Count(Motifs):
    count = {} #empty dict
    k = len(Motifs[0])
    #print k
    # We then range over all nucleotides symbol and 
    # create a list of zeroes corresponding to count[symbol]
    for symbol in "ACGT":
        count[symbol] = [] #empty list
        #print "symbol " + str(symbol)
        for j in range(k):
            count[symbol].append(0)
    # six zeroes under each nucleotide symbol
    #print count

    # Range over all elements symbol = Motifs[i][j] of the count matrix 
    # and add 1 to count[symbol][j].
    t = len(Motifs)
    #print "t " + str(t)
    for i in range(t): #loops through each row of data
        #print "i " + str(i)
        for j in range(k): #loops through each column
            #print "j " + str(j)
            symbol = Motifs[i][j]
            #print "symbol " + symbol
            count[symbol][j] += 1 #saves count of each nucleotide per column
            #print count[symbol][j]
    #count.keys().sort() #not a sorted dict type so won't return as ACGT but was ok for problem set
    #print count   
    return count  

def Profile(Motifs):
    count = Count(Motifs)
    #print "profileMatrix " + str(profileMatrix)
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    print "t " + str(t)
    print "k " + str(k)  
    #for i in 'ACGT' :
    for i in count: #gets the key from count (ACGT)
        print i
        for j in k: #gets the ith nucleotide in the column
            print j
            profile[i][j] = count[i][j]/t
    return profile

#stringList = ["AACGTA","CCCGTT","CACCTT","GGATTA","TTCCGG"]
#stringList = ["GTACAACTGT", "CAACTATGAA", "TCCTACAGGA", "AAGCAAGGGT", "GCGTACGACC", "TCGTCAGCGT", "AACAAGGTCA", "CTCAGGCGTC", "GGATCCAGGT", "GGCAAGTACC"]
stringList = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
print Profile(stringList)
print Count(stringList)
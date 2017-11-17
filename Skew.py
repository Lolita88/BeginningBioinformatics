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
    return skew
    # The following returns with the formatted list
    #return ' '.join([str(skew[i]) for i in sorted(skew.keys())])
print Skew("CATTCCAGTACTTCGATGATGGCGTGAAGA")
#Skew("CATTCCAGTACTTCGATGATGGCGTGAAGA")

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
# this returns a list on one line, no commas or brackets from a #dictionary
#import sys
#skew = Skew(sys.stdin.read().strip())
#print(' '.join([str(skew[i]) for i in sorted(skew.keys())]))

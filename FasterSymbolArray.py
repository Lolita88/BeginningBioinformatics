def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    #print "n " + str(n) # n = 135
    ExtendedGenome = Genome + Genome[0:n//2] # Genome plus first half more
    #print Genome[0:n//2]
    array[0] = PatternCount(symbol, Genome[0:n//2]) # looking for symbol in first half = 7
    #print array[0] # = 7 times
    #first window is half of Genome
    for i in range(1, n): # 1-135
        # symbol is CC atm
        print "ExtendedGenome[i-1] " + str(ExtendedGenome[i-1])
        print "ExtendedGenome[i+(n//2)-1] " + str(ExtendedGenome[i+(n//2)-1])
        print "array[i-1] " + str(array[i-1])
        array[i] = array[i-1]
        
        if ExtendedGenome[i-1] == symbol:
            print "gets in first"
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            print "gets in second"
            array[i] = array[i]+1
    return array
    
def PatternCount(Pattern, Text):
    count = 0
    for i in range(0, len(Text)-len(Pattern) +1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count + 1		
    return count		
    
print (FasterSymbolArray("AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT", "CC"))
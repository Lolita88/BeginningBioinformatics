# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    positions = [] # initializing list of positions
    count = 0
    
    #for every i in the range of 0 to length of text: if (call function) Hamming Distance with parameters (slice Text from i to length of pattern, pattern) is less than or equal to d: postions.append[i]

    for i in range(0, len(Text)-len(Pattern)+1):
        #print Text[i:i+8]
        #print HammingDistance(Pattern, Text[i:i+8]
        if(HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d):
             positions.append(i)
             count += 1
    return count
    
def HammingDistance(genome1, genome2):
    distance = 0
    for x,y in zip(genome1, genome2):
        if x != y :
            distance += 1 
    return distance
print (ApproximatePatternCount("GTGCCG", "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT", 3))
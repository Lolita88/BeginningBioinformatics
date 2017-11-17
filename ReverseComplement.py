# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern

def ReverseComplement(text):
    reversedString = []
    #print reversedString
    theLength = len(text) - 1
    #print "theLength " + str(theLength)
    i = 0
    n = theLength
    for r in text:
    	while i <= theLength:
    	    #while not at end, add next value and move backwards
    		#print text[n]
        	reversedString.append(text[n])
        	i = i + 1
        	n = n -1
    
    #return ''.join(reversedString)
    # replace the nucleotides with their complement
	return ''.join(complement(reversedString))

# Input:  A string of Nucleotides
# Output: The complement string of Nucleotide
def complement(Nucleotide):
	#print(Nucleotide) 
	comp = []
	for i in Nucleotide:
		if i == 'A' :
			comp.append("T")
		elif i == 'T':
			comp.append("A")
		elif i == 'G':
			comp.append("C")
		else :
			comp.append("G")
	return ''.join(comp)
	
#print (complement("AAAACCCGGT"))
print ReverseComplement("GCTAGCT")


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
#import sys
#print(ReverseComplement(sys.stdin.read().strip()))
#imports data from a local file to dir and strips white space
v_cholerae = open('Vibrio_cholerae2.txt').read().strip()

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


def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    #print "complement " + complement(Pattern)
    for i in range(len(Genome)-len(Pattern)+1):
        if (Genome[i:i+len(Pattern)] == Pattern): 
        #or (Genome[i:i+len(Pattern)] == complement(Pattern)):
        	positions.append(i)
    #return str(positions)
    #positions = str(positions)
    #print type(positions)
    #test = ["a","b","c"]
    #print ' '.join(test)
    return ' '.join(str(x) for x in positions)
    #.join(str(x) for x in list_of_ints)

    
print PatternMatching("ATGATCAAG", v_cholerae)


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
#import sys
#lines = sys.stdin.read().splitlines()
#print(' '.join([str(i) for i in PatternMatching(lines[0],lines[1])]))
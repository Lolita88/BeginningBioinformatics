#e_coli = open('http://bioinformaticsalgorithms.com/data/realdatasets/Replication/E_coli.txt').read().strip()
import urllib2
req = urllib2.Request('http://bioinformaticsalgorithms.com/data/realdatasets/Replication/E_coli.txt')
response = urllib2.urlopen(req)
e_coli = response.read().strip()


def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    #print Genome[0:n//2] #prints range 0 to length/2 no float,rounded down //
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        #print ExtendedGenome[i:i+(n//2)]
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
        #print ExtendedGenome[i:i+(n//2)]
    return array
    
def PatternCount(Pattern, Text):
    count = 0
    for i in range(0, len(Text)-len(Pattern) +1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count + 1		
    return count		

print SymbolArray(e_coli, "AGCTTTTCA")
#print #(SymbolArray("#AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTT#TCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT", "CC"))
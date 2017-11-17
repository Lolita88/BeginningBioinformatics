#DosR = open('DosR.txt').read() #import from local file
# coding: utf-8
#!/usr/bin/python
import math
import random

def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    # range over all nucleotides symbol and create a list of zeroes corresponding to count[symbol]
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    # six zeroes under each nucleotide symbol
    # Range over all elements symbol = Motifs[i][j] of the count matrix and add 1 to count[symbol][j].
    t = len(Motifs)
    for i in range(t): #loops through each row of data
        for j in range(k): #loops through each column
            symbol = Motifs[i][j]
            count[symbol][j] += 1 #saves count of each nucleotide per column 
    return count

def CountWithPseudocounts(Motifs): 
    #returns the count matrix of Motifs with pseudocounts as a dictionary of lists
    #same as count but offset using pseudocounts to handle zero values
    count = {}
    k = len(Motifs[0])
    # We then range over all nucleotides symbol and create a list of zeroes corresponding to count[symbol]
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)
    # six zeroes under each nucleotide symbol
    # Range over all elements symbol = Motifs[i][j] of the count matrix and add 1 to count[symbol][j].
    t = len(Motifs)
    for i in range(t): #loops through each row of data
        for j in range(k): #loops through each column
            symbol = Motifs[i][j]
            count[symbol][j] += 1 #saves count of each nucleotide per column
    return count  

def Profile(Motifs):
    profileMatrix = Count(Motifs)
    #print "profileMatrix " + str(profileMatrix)
    t = len(Motifs)
    for i in profileMatrix:
        for j in range(len(profileMatrix[i])):
            profileMatrix[i][j] = float(profileMatrix[i][j]) / float(t)
    return profileMatrix

def ProfileWithPseudocounts(Motifs):
    #takes a list of strings Motifs as input and returns the profile matrix of Motifs with pseudocounts as a dictionary of lists
    profileMatrix = CountWithPseudocounts(Motifs)
    t = len(Motifs)
    for i in profileMatrix:
        for j in range(len(profileMatrix[i])):
            profileMatrix[i][j] = float(profileMatrix[i][j]) / (float(t) + 4)
    return profileMatrix   

def Consensus(Motifs):
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Score(Motifs):
    consensus = Consensus(Motifs)
    score = 0
    for i in range (len(Motifs)):
        for j in range (len(Motifs[i])):
            if consensus[j] != Motifs[i][j]:
                score += 1
    return score

def Pr(Text, Profile):
    # returns probability number of text 
    p = 1
    for i in range(len(Text)):
        #At position i of Text, we set p equal to p times the value of Profile 
        # corresponding to symbol Text[i] and column i, which is just Profile[Text[i]][i].
        p *= Profile[Text[i]][i]
    return p
      
def ProfileMostProbablePattern(Text, k, Profile):
    bestPr = -1
    bestPattern = ""
    k = int(k)
    for i in range(len(Text)-k+1): #loop through text until almost end, no index error
        Pattern = Text[i:i+k] #loop through pattern
        if Pr(Pattern, Profile) > bestPr: #call Pr on each Pattern and Profile, if > set
            bestPr=Pr(Pattern, Profile) #best probability
            bestPattern=Pattern #update pattern with new match
    return bestPattern

def GreedyMotifSearch(Dna, k, t):
    count = 1
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    temp = BestMotifs[0]        
    for i in range(len(BestMotifs)):
        if BestMotifs[i] != temp:
            temp = BestMotifs[i]
            count += 1   
    return BestMotifs, count
    #return ' '.join(BestMotifs, count)

def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    count = 1
    BestMotifs = []
    temp = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
            temp.append(BestMotifs[0])     
    for i in range(len(BestMotifs)):
        if BestMotifs[i] not in temp:
            temp.append(BestMotifs[i])
            count += 1  
    return BestMotifs, count
    
def GetEntropy(Profile):   
    totalEntropy = 0 #will be sum of column totals
    num = 0
    column = 0
    k = len(Profile["A"])
    for j in range (k): #for each column
        for symbol in "ACGT":
            entropy = [] #reset entropy each time
            entropy.append(Profile[symbol][j])
            for i in range(len(entropy)):
                #print entropy[i]
                if entropy[i] != 0:
                    totalEntropy += entropy[i] * math.log(entropy[i], 2)
                    #else do nothing, add 0
                    #totalEntropy = -(entropy[0] * math.log(entropy[0], 2) + 
                    #entropy[1] * math.log(entropy[1], 2))  
                    #entropy[2] * math.log(entropy[2], 2))  
                    #entropy[3] * math.log(entropy[3], 2))    
                    #math.log(x[, base])
    return -totalEntropy

def Motifs(Profile, Dna):
    kmers = []
    #takes a profile matrix Profile corresponding to a list of strings Dna as input 
    #and returns a list of the Profile-most probable k-mers in each string from Dna
    k = len(Profile["A"]) 
    for i in range(len(Dna)):
        kmers.append(ProfileMostProbablePattern(Dna[i], k, Profile))
    return kmers

def RandomMotifs(Dna, k, t):
    #uses random.randint to choose a random k-mer from each 
    #of t different strings Dna, and returns a list of t strings
    #random.randint(1, M)
    kmers = []
    for i in range(len(Dna)):
        j = random.randint(0, len(Dna[0])-k-1)
        kmers.append(Dna[i][j:j+k])
    return kmers 

def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs 

def Normalize(Probabilities):
    #This function takes a dictionary Probabilities whose keys are k-mers and whose values are the probabilities 
    # of these k-mers (which do not necessarily sum to 1). The function should divide each value in Probabilities 
    # by the sum of all values in  Probabilities, then return the resulting dictionary.
    normKmers = {}
    kmerSum = 0
    for k,v in Probabilities.items():
        kmerSum += v
    for k,v in Probabilities.items():
        normKmers[k] = v/kmerSum
    return normKmers
def WeightedDie(Probabilities):
    #takes a dictionary Probabilities whose keys are k-mers and whose values are the probabilities of 
    # these k-mers. The function should return a randomly chosen k-mer key with respect to the values 
    # in Probabilities.
    ranNum = random.uniform(0,1)
    count = 0
    #for each face of the die, add Pr(face) to the "count" variable. If "count" > the random number, then return the face
    for k,v in Probabilities.items():
        count += v
        if count > ranNum:
            return k

def ProfileGeneratedString(Text, profile, k):
    # takes a string Text, a profile matrix profile , and an integer k as input.  
    # It should then return a randomly generated k-mer from Text whose probabilities are generated from profile 
    n = len(Text)
    probabilities = {}
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)

def GibbsSampler(Dna, k, t, N):
    #form motifs by randomly selecting a kmer in each seq of dna
    motifs = RandomMotifs(Dna, k, t)
    BestMotifs = motifs
    #print BestMotifs
    BestScore = Score(BestMotifs)
    #print BestScore 
    for j in range(N):
        i = random.randint(0,t-1)
        #randomly choose one of the selected kmers and remove from motifs
        motifs.pop(i)
        #create profile matrix from remaining kmers in motifs
        profile = ProfileWithPseudocounts(motifs)
        #for the missing kmer, calculate Pr(kmer/Profile)resulting in n-k+1 probabilities
        motifsI = ProfileGeneratedString(Dna[i], profile, k)
        #roll a die(with n-k+1 sides) where probability of ending up at side
        #i is proportional to p of i.
        #Choose a new starting position based on rolling the die.
        #Add the kmer starting at this position to motifs
        #insert and compare, this is the algorithm
        motifs.insert(i, motifsI)
        CurrScore = Score(motifs)
        if CurrScore < BestScore:
            BestMotifs = motifs
    return BestMotifs


k = 15
t = 10
N = 100
#Dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
#print GibbsSampler(Dna, k, t, N)
#CurrMotifs = GibbsSampler(Dna, k, t, N)
#BestMotifs = CurrMotifs
#for i in range(20):
    #if Score(CurrMotifs) > Score(BestMotifs):
        #BestMotifs = GibbsSampler(Dna, k, t, N)
#print BestMotifs

#Text = "AAACCCAAACCC"
#profile = {'A': [0.5, 0.1], 'C': [0.3, 0.2], 'G': [0.2, 0.4], 'T': [0.0, 0.3]}
#k = 2
#print ProfileGeneratedString(Text, profile, k)
#Probabilities = {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}
#print WeightedDie(Probabilities)
#Profile = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}
#print Normalize(Profile)
#k = 3
#t = 5
#k = 15
#t = 10
#N = 100
#Dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
#Profile =  { 'A': [0.8, 0.0, 0.0, 0.2 ],'C': [ 0.0, 0.6, 0.2, 0.0], 'G': [ 0.2 ,0.2 ,0.8, 0.0], 'T': [ 0.0, 0.2, 0.0, 0.8]}   
#Dna = ['TTACCTTAAC','GATGTCTGTC','ACGGCGTTAG','CCCTAACGAG','CGTCAGAGGT']
#print RandomizedMotifSearch(DosR, k, t)

#for i in range(N):
    #BestMotifs = RandomizedMotifSearch(Dna, k, t)
#print (BestMotifs)
#print (Score(BestMotifs))
#print RandomizedMotifSearch(Dna, k, t)
#print RandomMotifs(Dna, k, t)
#print Motifs(Profile, Dna)
#print ProfileMostProbablePattern("TTACCTTAAC", 4, Profile)

#motif = ["TCGGGGGTTTTT","CCGGTGACTTAC","ACGGGGATTTTC","TTGGGGACTTTT","AAGGGGACTTCC","TTGGGGACTTCC","TCGGGGATTCAT","TCGGGGATTCCT","TAGGGGAACTAC","TCGGGTATAACC"]
#print(Score(motif))

#testProfile = {'A':[0.4,0.3,0.0,0.1,0.0,0.9,],'C':[0.2,0.3,0.0,0.4,0.0,0.1,],'G':[0.1,0.3,1.0,0.1,0.5,0.0,],'T':[0.3,0.1,0.0,0.4,0.5,0.0]}
#print Consensus(testProfile)
#print Pr("TCGGTA", testProfile)
#print(GetEntropy(Profile(motif)))

#k = 3
#t = 5
#k = 15
#t = 10
#Dna = DosR
#Dna = "GGCGTTCAGGCAAAGAATCAGTCACAAGGAGTTCGCCACGTCAATCACCAATAATATTCG"
#Dna = ["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC","CACGTCAATCAC","CAATAATATTCG"]
#print GreedyMotifSearchWithPseudocounts(Dna, k, t)
#LIST = [GreedyMotifSearchWithPseudocounts(Dna, k, t)]
#print( ", ".join( repr(e) for e in LIST ) )
#print(", ".join(LIST))
#print(GreedyMotifSearch(Dna, k, t)
#x, y = GreedyMotifSearchWithPseudocounts(Dna, k, t)
#print (x)
#print (y)
#Dna = Dna.splitlines()
#print('\n'.join(GreedyMotifSearch(Dna,k,t)))
#print(GreedyMotifSearch(Dna, k, t))
#stringList = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
#stringList = ["GTACAACTGT", "CAACTATGAA", "TCCTACAGGA", "AAGCAAGGGT", "GCGTACGACC", "TCGTCAGCGT", "AACAAGGTCA", "CTCAGGCGTC", "GGATCCAGGT", "GGCAAGTACC"]
#print Consensus(stringList)
#print ProfileWithPseudocounts(stringList)
#print CountWithPseudocounts(stringList)
#Text = "ACGGGGATTACC"
#Profile = "0.2 0.2 0.0 0.0 0.0 0.0 0.9 0.1 0.1 0.1 0.3 0.0\n0.1 0.6 0.0 0.0 0.0 0.0 0.0 0.4 0.1 0.2 0.4 0.6\n0.0 0.0 1.0 1.0 0.9 0.9 0.1 0.0 0.0 0.0 0.0 0.0\n0.7 0.2 0.0 0.0 0.1 0.1 0.0 0.5 0.8 0.7 0.3 0.4\n"
#Text = "TCGGGGGCCACC"
#Profile = "0.2 0.2 0.0 0.0 0.0 0.0 0.9 0.1 0.1 0.1 0.3 0.0\n0.1 0.6 0.0 0.0 0.0 0.0 0.0 0.4 0.1 0.2 0.4 0.6\n0.0 0.0 1.0 1.0 0.9 0.9 0.1 0.0 0.0 0.0 0.0 0.0\n0.7 0.2 0.0 0.0 0.1 0.1 0.0 0.5 0.8 0.7 0.3 0.4\n"
#Text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
#k = "5"
#Profile = "0.2 0.2 0.3 0.2 0.3\n0.4 0.3 0.1 0.5 0.1\n0.3 0.3 0.5 0.2 0.4\n0.1 0.2 0.1 0.1 0.2\n"


#lines = Profile.splitlines()
#Text = lines[0]
#k = int(lines[0])
#A = [float(c) for c in lines[0].split()]
#C = [float(c) for c in lines[1].split()]
#G = [float(c) for c in lines[2].split()]
#T = [float(c) for c in lines[3].split()]
#Profile = {'A':A, 'C':C, 'G':G, 'T':T}
#print(Pr(Text,Profile))
#print (ProfileMostProbablePattern(Text, k, Profile))
#print (Profile(stringList))
#print Count(stringList)

#print Score(stringList)
#Score(stringList)
#print Pr("ACGGGGATTACC","0.2 0.2 0.0 0.0 0.0 0.0 0.9 0.1 0.1 0.1 0.3 0.0 0.1 0.6 0.0 0.0 0.0 0.0 0.0 0.4 0.1 0.2 0.4 0.6 0.0 0.0 1.0 1.0 0.9 0.9 0.1 0.0 0.0 0.0 0.0 0.0 0.7 0.2 0.0 0.0 0.1 0.1 0.0 0.5 0.8 0.7 0.3 0.4")

#How is it possible that randomly chosen k-mers have led us to the correct implanted k-mer?
#Because there is a message hidden in the DNA strings, randomly choosing k-mers from the DNA strings will skew the randomly chosen motifs towards the hidden message. 
#This is because there is a probability that the random selection will 'hit' a hidden message. Once the hidden message has been hit, it will skew the motif selection to the hidden message. The hidden messages are more likely to be chosen than random chance under these conditions. 
#The hidden message may also display properties of symmetry that may help its selection, since hitting half the motif may help skew the search as well. 
Dna = ["ATGAGGTC","GCCCTAGA","AAATAGAT","TTGTGCTA"]

M = ['GTC','CCC','ATA','GCT']
BestMotifs = M

Profile = ProfileWithPseudocounts(M)
M = Motifs(Profile, Dna)
if Score(M) < Score(BestMotifs):
    BestMotifs = M
print BestMotifs 

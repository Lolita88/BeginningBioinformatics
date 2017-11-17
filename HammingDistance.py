def HammingDistance(genome1, genome2):
    distance = 0
    for x,y in zip(genome1, genome2):
    #for x in genome1:
        if x != y :
            distance += 1 
    return distance
print (HammingDistance("TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC", "GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA"))
            
    
# Copy your PatternCount function from the previous step below this line
def PatternCount(Pattern, Text):
    count = 0
    #print len(Text)
    #print len(Text)-len(Pattern)+1 
    for i in range(0, len(Text)-len(Pattern)+1):
     	#print Text[i:i+len(Pattern)]
        if Text[i:i+len(Pattern)] == Pattern:
            #print Text[i:i+len(Pattern)]
            count = count + 1		
    return count		
	

# Now, set Text equal to the ori of Vibrio cholerae and Pattern equal to "TGATCA"
Text = 'ACTGTACGATGATGTGTGTCAAAG'
Pattern = "TGT"

# Finally, print the result of calling PatternCount on Text and Pattern.
# Don't forget to use the notation print() with parentheses included!
#print(PatternCount(Pattern, Text))
print PatternCount(Pattern, Text)



"""
import urllib.request
with urllib.request.urlopen('http://bioinformaticsalgorithms.com/data/Salmonella_enterica.txt') as response:
   #pageData1 = str(response.read()
   pageData1 = [x.rstrip() for x in response.readlines()]
#print (" ".join(str(x) for x in pageData1))
print(pageData1)
#print(pageData1)
"""
import urllib.request
response0 = urllib.request.urlopen('http://bioinformaticsalgorithms.com/data/Salmonella_enterica.txt')
pageData1 = str(response0.read())
response0.close()
print(pageData1)


"""
#python2
import urllib2
response0 = urllib2.urlopen('http://bioinformaticsalgorithms.com/data/Salmonella_enterica.txt')
pageData1 = str(response0.read())
response0.close()
print(pageData1)
"""

# req = urllib2.Request('http://bioinformaticsalgorithms.com/data/challengedatasets/DosR.txt')
# with urllib2.urlopen(req) as response:
#     pageData = str(response.read())

# pageDataFormatted = pageData.replace('\\r\\n', '\r\n')
# print(pageDataFormatted)


#import from local file
#DosR = open('DosR.txt').read()
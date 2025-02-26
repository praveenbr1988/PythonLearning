word1 = "pqrqwe"
word2 = "abc"
w1= len(word1)
w2= len(word2)
newword=""

if w1==w2 :
    for x in range (w1):
        newword= newword + word1[x] + word2[x]
    print (newword)

if w1<w2 :
    for x in range (w1):
        newword= newword + word1[x] + word2[x]
    newword=newword + word2[w1:w2]
    print (newword)

if w1>w2 :
    for x in range (w2):
        newword= newword + word1[x] + word2[x]
    newword=newword + word1[w2:w1]
    print (newword)
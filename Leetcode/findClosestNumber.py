nums = [10,-4,-2,1,4,8,-1,2]
closest = ""
for x in nums:
    if closest=="" or abs(x)<abs(int(closest)) or (abs(x)==abs(int(closest)) and x >0) :
        closest=x
print (closest)

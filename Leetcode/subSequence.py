class subseqVal:

    def isSubsequence(self, s1, s2) -> bool:

        if s1 == '': return True
        if s1 == s2: return True
        if len(s2) < len(s1): return False

        j=0
        for i in range(len(s2)):
            if s1[j] == s2[i]:
                if j == len(s1)-1:
                    return True
                j+=1

        return False

obj = subseqVal()
s1 = (input("Enter string1: ")).lower()
s2 = (input("Enter string2: ")).lower()
result = obj.isSubsequence(s1, s2)

if result is True:
    print(f"{s1} is subsequence of {s2}")
else:
    print(f"{s1} is not subsequence of {s2}")


# Time is O(n) because we use only one for loop
# Space is O(1) because we have not used any spl DS
count = 0
for i in range(138241,674034):
    s = str(i)
    if sorted(s) == list(s) and (s[0]==s[1] or s[1]==s[2] or s[2]==s[3] or s[3]==s[4] or s[4]==s[5]):
        count+=1
print(count)

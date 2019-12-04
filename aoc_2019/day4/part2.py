icount = 0
for i in range(138241,674034):
    s = str(i)
    if sorted(s) == list(s):
        if ((s[0]==s[1] and s[1]!=s[2]) or (s[1]==s[2] and s[2]!=s[3]  and s[1]!=s[0]) or 
            (s[2]==s[3] and s[3]!=s[4] and s[2]!=s[1]) or (s[3]==s[4] and s[4]!=s[5] and s[3]!=s[2]) or 
            (s[4]==s[5] and s[4]!=s[3])):
            count+=1
print(count)

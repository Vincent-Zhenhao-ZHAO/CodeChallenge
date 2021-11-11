s = "abacsd"
Target_list = ""
Target_len = 0
for i in range(len(s)):
    l,r = i,i
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if (r-l+1) > Target_len:
            Target_list = s[l:r+1]
            Target_len = r-l+1
        l -= 1
        r += 1
    l,r = i, i+1
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if (r-l+1) > Target_len:
            Target_list = s[l:r+1]
            Target_len = r-l+1
        l -= 1
        r += 1
print(Target_list)
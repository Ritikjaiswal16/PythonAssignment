s=input("Enter file Path -: ")
print(s[s.index('.')+1:])


s=input("Enter Full path -: ")
t=s[::-1]
t='fdp.'+t[t.index('.')+1:t.index('/')]
print(t[::-1])

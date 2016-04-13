#计数字符串中连续出现的次数
s = raw_input()
tmp = 1
now = ''
sout = []
count = 0
i = 0
for i in range(len(s)):
    if count == 0:
        if s[i].isalpha():
            now = s[i]
            count = 1
    elif s[i] == now:
        count = count + 1
    elif s[i].isalpha():
        sout.append(now)
        sout.append(str(count))
        now = s[i]
        count = 1
sout.append(now)
sout.append(str(count))
print "".join(list(sout))

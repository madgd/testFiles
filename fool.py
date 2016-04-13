#愚人节礼物
try:
    while True:
        s = raw_input()
        q = []
        flag = 1000
        dep = 0
        for i in range(len(s)):
            if s[i] == '(':
                q.append(s[i])
                dep = dep + 1
            elif s[i] == ')':
                q.pop(0)
                dep = dep - 1
            elif s[i] == 'A':
                if(flag > dep):
                    flag = dep
        print flag
except EOFError:
    pass

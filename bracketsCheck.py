import sys


string = sys.stdin.readline()
def judge(string):
	storeList = [0,0,0]
	last = []
	for i in string:
		if i == '(':
			storeList[0] += 1
			last.append('(')
		if i == '[':
			storeList[1] += 1
			last.append('[')
		if i == '{':
			storeList[2] += 1
			last.append('{')

		if i == ')':
			storeList[0] += -1
			if not last or last.pop() != '(':
				return False
		if i == ']':
			storeList[1] += -1
			if not last or last.pop() != '[':
				return False
		if i == '}':
			storeList[2] += -1
			if not last or last.pop() != '{':
				return False

	for i in storeList:
		if i != 0:
			return False
	return True


print judge(string)

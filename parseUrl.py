# coding: utf-8
#  解析url

url = "http://i0.sinaimg.cn:8080/blog/register.jsp?type=a&name=test1234"

firstColon = url.find(":")
secondColon = url.find(':', firstColon + 1)
#print secondColon
firstQuestion = url.find("?")
firstSingleSplash = url.find('/', secondColon + 1)

protocol = url[0:firstColon]

host = url[url.find(":") + 3 : secondColon]

port = url[secondColon + 1:firstSingleSplash]

path = url[firstSingleSplash:firstQuestion]

params = url[firstQuestion+1:].split("&")
paramsDict = {}
for i in params:
    tmp = i.split('=')
    paramsDict[tmp[0]] = tmp[1]

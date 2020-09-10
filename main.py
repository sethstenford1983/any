import re

def fn(a):
    y = re.match("^\d+\-\d+\-\d+\s\d+\:(\d+)\:\d+$",a)
    if y is None:
        print('не понимаю')
    else:
        t = y.groups()
        return t[0]
print(fn("2018-01-09 12:32:04"))
print('hello')



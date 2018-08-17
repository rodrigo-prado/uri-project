d = int(input())
y = d // 365
d = d - y*365
m = d // 30
d = d - m*30
print("{0} ano(s)".format(y))
print("{0} mes(es)".format(m))
print("{0} dia(s)".format(d))
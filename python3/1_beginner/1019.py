s = int(input()) # duration in seconds
m = s // 60
h = m // 60
s = s - m*60
m = m - h*60
print("{0}:{1}:{2}".format(h, m, s))
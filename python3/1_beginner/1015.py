import math

def distance(a, b, c, d):
	return math.sqrt(math.pow((c - a), 2) + math.pow((d - b), 2))

p1_x, p1_y = map(float, input().split()[:2])
p2_x, p2_y = map(float, input().split()[:2])

d = distance(p1_x, p1_y, p2_x, p2_y)

print("{0:.4f}".format(d))

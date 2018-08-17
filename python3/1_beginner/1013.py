def maiorAouB(a, b):
	return int((a + b + abs(a - b)) / 2)

a, b, c = input().split()
ia = int(a)
ib = int(b)
ic = int(c)

maiorEntreAeB = maiorAouB(ia, ib)
maiorEntreAeBeC = maiorAouB(maiorEntreAeB, ic)

print("{0} eh o maior".format(maiorEntreAeBeC))
def imprimeNota(v, n):
	#print(v)
	#print(n)
	#if v >= n:
		i = v // n
		print("{0} nota(s) de R$ {1},00".format(i, n))
		return int(v - i*n)
	#else:
	#	return v

v = int(input())
print(v)

v = imprimeNota(v, 100)
v = imprimeNota(v, 50)
v = imprimeNota(v, 20)
v = imprimeNota(v, 10)
v = imprimeNota(v, 5)
v = imprimeNota(v, 2)
v = imprimeNota(v, 1)

def imprimeNota(v, n):
	i = v // n
	print("{0} nota(s) de R$ {1}.00".format(i, (n // 100)))
	return int(v - i*n)
	
def imprimeMoeda(v, n):
	if n == 100:
		i = v // n
		print("{0} moeda(s) de R$ {1}.00".format(i, (n // 100)))
		return int(v - i*n)
	else:
		i = v // n
		print("{0} moeda(s) de R$ 0.{1:02}".format(i, n))
		return int(v - i*n)

v = float(input())
i = int(v * 100)
#print(v)
print("NOTAS:")
i = imprimeNota(i, 10000)
i = imprimeNota(i, 5000)
i = imprimeNota(i, 2000)
i = imprimeNota(i, 1000)
i = imprimeNota(i, 500)
i = imprimeNota(i, 200)
print("MOEDAS:")
i = imprimeMoeda(i, 100)
i = imprimeMoeda(i, 50)
i = imprimeMoeda(i, 25)
i = imprimeMoeda(i, 10)
i = imprimeMoeda(i, 5)
i = imprimeMoeda(i, 1)

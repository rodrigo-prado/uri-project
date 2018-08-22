item, qtd = map(int,input().split()[:2])
#qtd = int(input())
total = 0.0
if item == 1:
	total += qtd * 4.0
elif item == 2:
	total += qtd * 4.5
elif item == 3:
	total += qtd * 5.0
elif item == 4:
	total += qtd * 2.0
elif item == 5:
	total += qtd * 1.5
print("Total: R$ {0:.2f}".format(total))

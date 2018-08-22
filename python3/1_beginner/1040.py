n1, n2, n3, n4 = map(float, input().split()[:4])
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4)) / 10
print("Media: {0:.1f}".format(media))
if media >= 7.0:
	print("Aluno aprovado.")
elif media < 5.0:
	print("Aluno reprovado.")
elif media >= 5.0 and media <= 7.0:
	print("Aluno em exame.")
	n5 = float(input())
	print("Nota do exame: {0:.1f}".format(n5))
	mediaFinal = (media + n5) / 2
	if mediaFinal >= 5.0:
		print("Aluno aprovado.")
	elif media < 5.0:
		print("Aluno reprovado.")
	print("Media final: {0:.1f}".format(mediaFinal))

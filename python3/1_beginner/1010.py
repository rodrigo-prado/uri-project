p1_code, p1_units, p1_price = input().split()
p2_code, p2_units, p2_price = input().split()
value = int(p1_units)*float(p1_price) + int(p2_units)*float(p2_price)
print("VALOR A PAGAR: R$ {0:.2f}".format(value))

a, b, c = input().split()
fa = float(a)
fb = float(b)
fc = float(c)
pi = 3.14159
tria = fa*fc/2
circ = pi*fc*fc
trap = (fa+fb)*fc/2
squa = fb*fb
rect = fa*fb
print("TRIANGULO: {0:.3f}".format(tria))
print("CIRCULO: {0:.3f}".format(circ))
print("TRAPEZIO: {0:.3f}".format(trap))
print("QUADRADO: {0:.3f}".format(squa))
print("RETANGULO: {0:.3f}".format(rect))
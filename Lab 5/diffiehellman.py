import random
def exp_rapida(base, exponente, modulo):
	x = 1
	y = base % modulo
	b = exponente
	while (b > 0):
		if ((b % 2) == 0):  # Si b es par...
			y = (y * y) % modulo
			b = b / 2
		else:  # Si b es impar...
			x = (x * y) % modulo
			b = b - 1
	return x

def PandG():
        L=[]
        pri=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,97]
        P= random.choice(primos)
        G= random.randrange(1,P)
        L.append(P)
        L.append(g)
        return L

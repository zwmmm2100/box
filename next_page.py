import sys   
sys.setrecursionlimit(5000) #例如这里设置为十万  

def xxx(x):
	x = x + 1
	print('good!' + str(x))
	return xxx(x)


xxx(1)
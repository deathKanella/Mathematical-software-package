import numpy as np
import matplotlib.pyplot as plt
import math
import csv

print("7 вариант")
print("Построение графика функции y = a * ln(b+c*x)")

plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y = a * ln(b+c*x)')
plt.legend()

#a = float(input("Введите a : "))
#b = float(input("Введите b : "))
#c = float(input("Введите c : "))

a = []
b = []
c = []

#Чтение из файла
with open('f1.tsv', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter='	')
	for row in plots:
		a.append(float(row[0]))
		b.append(float(row[1]))
		c.append(float(row[2]))
		
i = 0
while i<len(a):
	def func (x):
	
		if x == 0:
			return 1.0
		return math.log(b[i] + c[i]*x)
	
# Шаг между точками
	dx = 0.01
	xmin = -b[i]/c[i]
	xmax = 20.0

	k = 0

	x = []
	y = []

	while xmin<= xmax :
		xmin += dx
		x.append(xmin)
	
	
	x.reverse()
	
	while k < len(x):
		y.append( a[i] * func(x[k]))
		k += 1
	y.reverse()

# !!! Нарисуем одномерный график
	plt.plot (x, y)

# !!! Покажем окно с нарисованным графиком
	plt.show()
	i+=1









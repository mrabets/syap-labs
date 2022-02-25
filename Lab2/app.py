from math import * 

x = float(input('a = '))
y = float(input('b = '))

numerator = 2*(log(sqrt(x**2 + y**2))) + log(sqrt(1 + (x - y)**2))
denominator = 3*(x**2 + y**2)*(x**4 + y**4)

z = numerator / denominator

print("z = %.2f" % z)
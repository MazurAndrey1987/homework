import math

a = 10
b = 20
c = 30
result = (a + b * (c/2))
print("При результате a = %d, b = %d, c = %d равно %f" % (a, b, c, result))

a = 10
b = 20
result = ((a**2 + b**2) % 2)
print("При результате a = %d, b = %d равно %f" % (a, b, result))

a = 10
b = 20
c = 30
result = ((a + b) / 12 * c % 4 + b)
print("При результате a = %d, b = %d, c = %d, b = %d равно %f" % (a, b, c, b, result))

a = 10
b = 20
c = 30
result = ((a - b*c) * (a + b) % c)
print("При результате a = %d, b = %d, c = %d равно %f" % (a, b, c, result))

a = 10
b = 20
c = 30
result = ((abs(a - b)) / ((a + b)**3) - math.cos(c))
print("При результате a = %d, b = %d, равно %f" % (a, b, c, result))

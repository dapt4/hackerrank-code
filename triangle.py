import math
def process(a, b):
    c = math.sqrt((a**2)+(b**2))
    c /= 2
    operation = -(((c**2)-(b**2)-(c**2))/(2*b*c))
    degrees = math.degrees(math.acos(operation))
    angle = round(degrees)
    print(f'{angle}\u00b0')
    
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    process(a, b)

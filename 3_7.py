import math

def p1(): 
    x = 0.1
    while x < 2.1:
        print (x, "\t", (math.pow(x,2) + (5 * math.sin(x))))
        x += 0.2

def main(): 
    p1() 
    return 0 

if __name__ == '__main__':
    main()
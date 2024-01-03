print("Number Pattern - ")
def halfPyramid(rows):
    print("Half-Pyramid :")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print('')

def inverted_halfPyramid(rows):
    print("Inverted Half-Pyramid :")
    b = 0
    for i in range(rows,0,-1):
        b+=1
        for j in range(1,i+1):
            print(b,end=' ')
        print(" ")

def pascalTriangle(rows):
    print("Pascal's Triangle :")
    coef = 1
    for i in range(1,rows+1):
        for space in range(1,rows-i+1):
            print(" ",end="")
        for j in range(0,i):
            if j==0 or i==0:
                coef = 1
            else:
                coef = coef*(i-j)//j
            print(coef,end=" ")
        print()

halfPyramid(5)
inverted_halfPyramid(5)
pascalTriangle(5)

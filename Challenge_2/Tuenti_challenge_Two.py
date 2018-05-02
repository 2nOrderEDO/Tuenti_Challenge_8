import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'TestInput_2.txt'),'r') as f:
    data = f.readlines()

with open(os.path.join(__location__, 'output.txt'),'w') as output:
    j = 0
    for x in data[1:]:
        j += 1
        x = x.strip('\n')
        base = len(x)
        y = range(0,base)
        maximo = sorted(y,key=int)
        minimo = sorted(y,key=int,reverse=True)
        minimo[base-1],minimo[base-2] = minimo[base-2],minimo[base-1]
        base_matrix = [base**i for i in range(base)]

        A = 0
        for i in range(0,len(maximo)):
            A += maximo[i]*base_matrix[i]

        B = 0
        for i in range(0,len(minimo)):
            B += minimo[i]*base_matrix[i]

        out = 'Case #' + str(j) + ': ' + str(A-B)
        print(out)
        output.write(out +'\n')


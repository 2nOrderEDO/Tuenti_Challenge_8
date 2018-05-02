import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'TestInput_1.txt'),"r") as f:
    data = f.readlines()

with open(os.path.join(__location__, 'Output.txt'),'w') as output:

    n = 0
    for x in data[1:]:
        n+=1
        NM = [int(n) for n in x.split()]
        holes = NM[0]*NM[1]-NM[0]-NM[1]+1
        out = "Case #" + str(n) +': '+ str(holes)
        print(out)
        output.write(out + '\n')


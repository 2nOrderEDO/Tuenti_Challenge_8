import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'submitInput_4.txt'),"r") as f:
    data = f.readlines()

from operator import add
from operator import sub

def SearchFor(what,where): #Returns the position of 'what' in the two dimensional list 'where'

    x = [x for x in where if what in x][0]

    return [where.index(x),x.index(what)]
    # for j in where:
    #     if j.index(what) != ValueError:
    #         return [where.index(j),j.index(what)]

def Euclid(A,B): #Not really Euclid but Manhattan
    tmp = list(map(sub,A,B))
    tmp = list(map(abs,tmp))
    return (tmp[0]+tmp[1])*10

def Calc_Frontier(Pos):
    frontier = []
    for x in r: #Calculate next allowed nodes
        if board[Pos[0]][Pos[1]] == '*':
            k = list(map(add,[l*2 for l in x],Pos))
        else:
            k = list(map(add,x,Pos))
        if  k[0] < 0 or k[1] < 0 or k[0] >= NM[0] or k[1] >= NM[1] or board[k[0]][k[1]] == '#':
            continue
        frontier.append(k)
    return frontier

def return_path(visited,Start,Goal):
    route = []
    Destino = [m[1] for m in reversed(visited)]
    Origen =  [m[0] for m in reversed(visited)]
    x = Goal
    while x != Start:
        route.append(x)
        x = Origen[Destino.index(x)]
    return route

def A_Star(Start,Goal): #Pain takenly implemented
    closedSet = []
    openSet = [[Start, Euclid(Start,Goal)]]
    camefrom = []

    while len(openSet) != 0:
        current = openSet[0] #Current node is the one with the minimum score f
        if current[0] == Goal:
            return return_path(camefrom,Start,Goal)
            #We reached our goal, retrieve the route
        openSet.remove(current)
        closedSet.append(current[0]) #We move the node coordinate to the closed coordinates list
        frontier = Calc_Frontier(current[0]) #Calculate the neightbour nodes (frontier) of current node coordiante
        #Note about the Heuristic: Accumulating distances is much worse than adding euclid distance, thats is way 
        #is multiplied by two.
        for x in frontier:
            if x in closedSet:  #If the node in the frontier is already closed, dont visit it again
                continue
            openSet_positions = [k[0] for k in openSet]
            if x not in openSet_positions: #If is a new node, calculate it's f score
                score_f = Euclid(x,Goal) + current[1]*2 #Which is the cost of the previous node (Current) + heuristic
                openSet.append([x,score_f]) #Move it to the open set with is f score
                camefrom.append([current[0],x])

            openSet.sort(key=lambda j: j[1]) #Order the open set by minimum f score
    return False
    #Todavia no tengo arreglado como saltar al siguiente mapa


with open(os.path.join(__location__, 'Output.txt'),'w') as output:
    r = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]] #Knight movement unit vector
    r2 = [[4,2],[4,-2],[-4,2],[-4,-2],[2,4],[2,-4],[-2,4],[-2,-4]]
    C = int(data[0])

    n = 0
    i = 1
    while n < C:
        n += 1
        board = []
        NM = data[i].strip('\n')
        NM = NM.split(' ')
        NM = list(map(int,NM))

        for j in range(1,NM[0]+1):  #Get de map
            tmp = data[i+j]
            board.append(tmp.strip('\n'))
        i += NM[0]+1

        S = SearchFor('S',board) #Localice the Knight
        P = SearchFor('P',board) # the Princess
        D = SearchFor('D',board) #and the safe location
        tmp1 = []
        tmp2 = []

        tmp1 = A_Star(S,P) #find de sortest path possible

        if tmp1 == False:
            print("Case #" + str(n) +': '+'IMPOSSIBLE')
            output.write("Case #" + str(n) +': '+'IMPOSSIBLE\n')
            continue
        else:
            tmp2 = A_Star(P,D) #find de sortest path possible
            if tmp2 == False:
                print("Case #" + str(n) +': '+'IMPOSSIBLE')
                output.write("Case #" + str(n) +': '+'IMPOSSIBLE\n')
                continue

        out = "Case #" + str(n) +': '+ str(len(tmp1+tmp2))
        output.write(out + '\n')

        print(out + ' ' + str(n) + '/' + str(C))

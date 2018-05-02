import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

rst = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
song = ['C','G','A']
dic = {'Ab': 'G#','Bb': 'A#','B#': 'C','Cb': 'B','Db': 'C#','Eb': 'D#','E#': 'F','Fb': 'E','Gb': 'F#'}

W = 2
H = 1
s2 = set(song)
major = [W, W, H, W, W, W, H]
minor = [W, H, W, W, H, W, W]
vector_major = [sum(major[0:x]) for x in range(0,len(major))]
vector_minor = [sum(minor[0:x]) for x in range(0,len(minor))]


def rotate(l, n):
    return l[n:] + l[:n]

with open(os.path.join(__location__, 'submitinput.txt'),"r") as f:
    data = f.readlines()

with open(os.path.join(__location__, 'Output.txt'),'w') as output:
    n = 1
    for song in data:
        song = song.strip('\n')
        if song == '0':
            output.write('Case #'+str(n)+ ': '+'MA MA# MB MC MC# MD MD# ME MF MF# MG MG# mA mA# mB mC mC# mD mD# mE mF mF# mG mG#\n')
            n +=1
            continue
        song = song.split()
        song = [dic.get(c, c) for c in song] #Translate with dictionary leaving non found items unchanged
        song = set(song)
        if not song.issubset(rst):
            continue                #if the line does not contain musical notes, skip
        result_ma = []
        result_mi = []
        lst = rst

        for i in lst: #Generate A major. This could have been generated just once
            heptatonic = [lst[x] for x in vector_major]
            s1 = set(heptatonic)
            if song.issubset(s1):
                    result_ma.append('M'+str(heptatonic[0]))
            lst = rotate(lst,1)
        lst = rst
        for i in lst:
            heptatonic = [lst[x] for x in vector_minor]
            s1 = set(heptatonic)
            if song.issubset(s1):
                    result_mi.append('m'+str(heptatonic[0]))
            lst = rotate(lst,1)

        result_ma = sorted(result_ma)
        result_mi = sorted(result_mi)
        if len(result_ma) == 0 and len(result_mi) == 0:
            output.write('Case #'+str(n)+ ': '+'None\n')
        else:
            output.write('Case #' + str(n) + ': '+ ' '.join(result_ma) +' '+' '.join(result_mi) + '\n')
        n += 1
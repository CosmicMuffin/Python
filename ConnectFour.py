import sys

#connect four
print("Welcome to Connect Four!")

name1 = input('Enter name of Player 1 (X):')
name2 = input('Enter name of Player 2 (O):')

x = ' X '
o = ' O '

# the lists containing the positions of tokens
c1 = ['   ','   ','   ','   ','   ','   ']
c2 = ['   ','   ','   ','   ','   ','   ']
c3 = ['   ','   ','   ','   ','   ','   ']
c4 = ['   ','   ','   ','   ','   ','   ']
c5 = ['   ','   ','   ','   ','   ','   ']
c6 = ['   ','   ','   ','   ','   ','   ']
c7 = ['   ','   ','   ','   ','   ','   ']

das = [c1, c2, c3, c4, c5, c6, c7]

# drops tokens in the respective column
def drop(List, lett):
    t = -1
    ind = 0
    for i in List:
        t+=1
        if i == '   ':
            ind = t
            break
    List[ind] = lett

# player 1 plays using this
def play1():
    print(f"{name1}'s turn")
    q = int(input('Enter Column Number:'))
    if q == 1:
        drop(c1,x)
    elif q == 2:
        drop(c2,x)
    elif q == 3:
        drop(c3,x)
    elif q == 4:
        drop(c4,x)
    elif q == 5:
        drop(c5,x)
    elif q == 6:
        drop(c6,x)
    elif q == 7:
        drop(c7,x)
    print(f"""
|{c1[5]}|{c2[5]}|{c3[5]}|{c4[5]}|{c5[5]}|{c6[5]}|{c7[5]}|
|{c1[4]}|{c2[4]}|{c3[4]}|{c4[4]}|{c5[4]}|{c6[4]}|{c7[4]}|
|{c1[3]}|{c2[3]}|{c3[3]}|{c4[3]}|{c5[3]}|{c6[3]}|{c7[3]}|
|{c1[2]}|{c2[2]}|{c3[2]}|{c4[2]}|{c5[2]}|{c6[2]}|{c7[2]}|
|{c1[1]}|{c2[1]}|{c3[1]}|{c4[1]}|{c5[1]}|{c6[1]}|{c7[1]}|
|{c1[0]}|{c2[0]}|{c3[0]}|{c4[0]}|{c5[0]}|{c6[0]}|{c7[0]}|
  1   2   3   4   5   6   7
""")

# player 2 plays using this
def play2():
    print(f"{name2}'s turn")
    q = int(input('Enter Column Number:'))
    if q == 1:
        drop(c1,o)
    elif q == 2:
        drop(c2,o)
    elif q == 3:
        drop(c3,o)
    elif q == 4:
        drop(c4,o)
    elif q == 5:
        drop(c5,o)
    elif q == 6:
        drop(c6,o)
    elif q == 7:
        drop(c7,o)
    print(f"""
|{c1[5]}|{c2[5]}|{c3[5]}|{c4[5]}|{c5[5]}|{c6[5]}|{c7[5]}|
|{c1[4]}|{c2[4]}|{c3[4]}|{c4[4]}|{c5[4]}|{c6[4]}|{c7[4]}|
|{c1[3]}|{c2[3]}|{c3[3]}|{c4[3]}|{c5[3]}|{c6[3]}|{c7[3]}|
|{c1[2]}|{c2[2]}|{c3[2]}|{c4[2]}|{c5[2]}|{c6[2]}|{c7[2]}|
|{c1[1]}|{c2[1]}|{c3[1]}|{c4[1]}|{c5[1]}|{c6[1]}|{c7[1]}|
|{c1[0]}|{c2[0]}|{c3[0]}|{c4[0]}|{c5[0]}|{c6[0]}|{c7[0]}|
  1   2   3   4   5   6   7
""")

# check if someone won
def winCheck(name):
    # check for vertical wins
    for i in das:
        for j in range(3):
            if i[j] == '   ':
                pass
            else:
                if i[j]==i[j+1]==i[j+2]==i[j+3]:
                    print(f'{name} wins!!!')
                    sys.exit('Game Over')

    # check for horizontal wins
    w = []
    for i in range(6):
        for j in das:
            w.append(j[i])
        for p in range(4):
            if w[p] == '   ':
                pass
            else:
                if w[p] == w[p + 1] == w[p + 2] == w[p + 3]:
                    print(f'{name} wins!!!')
                    sys.exit('Game Over')

    # check for diagonal wins
    d1 = [c1[2], c2[3], c3[4], c4[5]]
    d2 = [c1[1], c2[2], c3[3], c4[4], c5[5]]
    d3 = [c1[0], c2[1], c3[2], c4[3], c5[4], c6[5]]
    d4 = [c2[0], c3[1], c4[2], c5[3], c6[4], c7[5]]
    d5 = [c3[0], c4[1], c5[2], c6[3], c7[4]]
    d6 = [c4[0], c5[1], c6[2], c7[3]]
    d7 = [c1[2], c2[3], c3[4], c4[5]]
    d8 = [c1[1], c2[2], c3[3], c4[4], c5[5]]
    d9 = [c1[0], c2[1], c3[2], c4[3], c5[4], c6[5]]
    d10 = [c2[0], c3[1], c4[2], c5[3], c6[4], c7[5]]
    d11 = [c3[0], c4[1], c5[2], c6[3], c7[4]]
    d12 = [c4[0], c5[1], c6[2], c7[3]]
    v = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12]

    for i in v:
        for j in range(len(i)-3):
            if i[j] != '   ':
                if i[j] == i[j + 1] == i[j + 2] == i[j + 3]:
                    print(f'{name} wins!!!')
                    sys.exit('Game Over')


# connect four virtual board
f"""
|{c1[5]}|{c2[5]}|{c3[5]}|{c4[5]}|{c5[5]}|{c6[5]}|{c7[5]}|
|{c1[4]}|{c2[4]}|{c3[4]}|{c4[4]}|{c5[4]}|{c6[4]}|{c7[4]}|
|{c1[3]}|{c2[3]}|{c3[3]}|{c4[3]}|{c5[3]}|{c6[3]}|{c7[3]}|
|{c1[2]}|{c2[2]}|{c3[2]}|{c4[2]}|{c5[2]}|{c6[2]}|{c7[2]}|
|{c1[1]}|{c2[1]}|{c3[1]}|{c4[1]}|{c5[1]}|{c6[1]}|{c7[1]}|
|{c1[0]}|{c2[0]}|{c3[0]}|{c4[0]}|{c5[0]}|{c6[0]}|{c7[0]}|
  1   2   3   4   5   6   7
"""

print('The Game has started!')
print(f"""
|{c1[5]}|{c2[5]}|{c3[5]}|{c4[5]}|{c5[5]}|{c6[5]}|{c7[5]}|
|{c1[4]}|{c2[4]}|{c3[4]}|{c4[4]}|{c5[4]}|{c6[4]}|{c7[4]}|
|{c1[3]}|{c2[3]}|{c3[3]}|{c4[3]}|{c5[3]}|{c6[3]}|{c7[3]}|
|{c1[2]}|{c2[2]}|{c3[2]}|{c4[2]}|{c5[2]}|{c6[2]}|{c7[2]}|
|{c1[1]}|{c2[1]}|{c3[1]}|{c4[1]}|{c5[1]}|{c6[1]}|{c7[1]}|
|{c1[0]}|{c2[0]}|{c3[0]}|{c4[0]}|{c5[0]}|{c6[0]}|{c7[0]}|
  1   2   3   4   5   6   7
""")


ite = 0
while(True):
    ite += 1
    if ite % 2 == 1:
        play1()
        winCheck(name1)
    else:
        play2()
        winCheck(name2)

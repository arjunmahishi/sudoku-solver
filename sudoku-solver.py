import os

def getLayout(debug=False):
    layout = []
    if not debug:
        sudoRows = open("sudoku.txt").read().strip().split('\n')
        for row in sudoRows:
            sudoRow = row.strip().replace("| ", "").split(" ")
            if sudoRow[0] != "-":
                layout.append(sudoRow)
    else:
        for i in range(9):
            layout.append('. . . . . . . . .'.split(' '))
    return layout

def display(layout):
    for row in range(len(layout)):
        print "\t",
        for i in range(9):
            if (i)%3 == 0 and i != 0:
                print '|',
            print layout[row][i] ,
        print    
        if (row+1)%3 == 0 and row != 8:
            print "\t---------------------" 

def getGrid(x,y,layout):
    numbers = []
    for limit in range(2,9,3):
        if x <= limit :
            for sublimit in range(2,9,3):
                if y <= sublimit:
                    for i in range(limit-2, limit+1):
                        for j in range(sublimit-2, sublimit+1):
                            numbers.append(layout[i][j])
                    return numbers

def isSafe(n,x,y,layout):
    n = str(n)
    if n in getGrid(x,y,layout):
        return False
    for i in range(9):
        if layout[x][i] == n:
            return False
        if layout[i][y] == n:
            return False
    return True

def solve(layout):
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            if layout[i][j] != ".":
                continue
            for n in range(1,10):
                if isSafe(n, i, j, layout):
                    layout[i][j] = str(n)
                    os.system("clear")
                    display(layout)
                    print 
                    if i == len(layout)-1 and j == len(layout)-1:
                        return True
                    if solve(layout):
                        return True
                    layout[i][j] = "."

            return False

if solve(getLayout()):
    print "\n\nSolved"
else:
    print "\n\nCan't Solve"
def getLayout(debug=False):
    layout = []
    for i in range(9):
        if not debug:
            row = raw_input('row number ' + str(i+1) + " : ").split(' ')
            layout.append(row)    # all the numbers are in the form of char
        else:
            layout.append('. . . . . . . . .'.split(' '))
    return layout

def reset():
	layout = getLayout(True)
	open("sudoku.txt", "w").close()
	with open("sudoku.txt", 'a') as obj:
		for row in range(len(layout)):
			for i in range(9):
				if (i)%3 == 0 and i != 0:
				    obj.write('| ')
				obj.write(layout[row][i] + " ")
			obj.write("\n")    
			if (row+1)%3 == 0 and row != 8:
				obj.write("- - - - - - - - - - -\n") 

reset()
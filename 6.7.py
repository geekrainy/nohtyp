tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose', 'test'],
             ['a', 'b'],
             [1, 2, 3]]

def printTable(table):
    colWidths = [0] * len(table)
    maxLength = 0
    for i in range(len(table)):
        if len(table[i]) > maxLength:
            maxLength = len(table[i])
            
        for j in range(len(table[i])):
            if len(str(table[i][j])) > colWidths[i]:
                colWidths[i] = len(str(table[i][j]))

    for i in range(maxLength):
        for j in range(len(table)):
            if len(table[j]) < maxLength:
                temp = [''] * (maxLength - len(table[j]))
                table[j] = table[j] + temp
    
            if j == 0:
                print(str(table[j][i]).rjust(colWidths[j]), end=' ')
            else:
                print(str(table[j][i]).ljust(colWidths[j]), end=' ')

        print('')

printTable(tableData)

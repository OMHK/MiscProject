tabledata = [['doors', 'windows','vents','floors'],
             ['tables','chairs','desks','curtains'],
             ['carpets','electronics','hangers','closets']]
def tableprint(table):
    longest = 5
    for lines in tabledata:
        for words in lines:
            if len(words) > longest:
                longest = len(words)
        width = longest
        print(longest)
    x = len(table[0])
    y = len(table)
    for words in range(x):
        for lines in range(y):
            print(table[lines][words].rjust(longest),end = '' )
tableprint(tabledata)
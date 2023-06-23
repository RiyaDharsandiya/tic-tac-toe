'tic tac toe'
list1=[['*','*','*'],['*','*','*'],['*','*','*']]
def display_(list1):
    print(' ',0,1,2,sep='   ',end='\n\n')
    r=0
    for row in list1:
        print(r,end='')
        r+=1
        for col in row:
             print('  ',col,end='')
        print()

display_(list1)
p=0
list1=[['*','*','*'],['*','*','*'],['*','*','*']]
def win(p,list1):
    if list1[0][0]==list1[0][1]==list1[0][2]and list1[0][0]!='*':
        print('\nplayer ',list1[0][0],'is the winner')
        display_(list1)
       
    elif list1[0][0]==list1[1][0]==list1[2][0]and list1[0][0]!='*':
        print('\nplayer ',list1[0][0],'is the winner')
        display_(list1)
    elif list1[2][0]==list1[2][1]==list1[2][2]and list1[2][0]!='*':
        print('\nplayer ',list1[2][0],'is the winner')
        display_(list1)
    elif list1[0][2]==list1[1][2]==list1[2][2]and list1[2][2]!='*':
        print('\nplayer ',list1[0][2],'is the winner')
        display_(list1)
    elif list1[1][0]==list1[1][1]==list1[1][2]and list1[1][2]!='*':
        print('\nplayer ',list1[1][0],'is the winner')
        display_(list1)
    elif list1[0][0]==list1[1][1]==list1[2][2]and list1[0][0]!='*':
        print('\nplayer ',list1[0][0],'is the winner')
        display_(list1)
    elif list1[0][2]==list1[1][1]==list1[2][0]and list1[1][1]!='*':
        print('\nplayer ',list1[0][2],'is the winner')
        display_(list1)

    else:
        return True
while win(p,list1):
    display_(list1)
    if(p==0):
        print('player X turn')
    else:
        print('player O turn')
        
    x=int(input('enter row='))
    y=int(input('enter column='))

    if p==0:
        list1[x][y]='X'
        p+=1
    else:
        list1[x][y]='O'
        p=0
        

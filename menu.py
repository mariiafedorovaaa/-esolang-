
import pygame

a=660
b=900
RES = WIDTH, HEIGHT = a, b
RES = WIDTH+200, HEIGHT
TILE = 30
W, H = a // TILE, b // TILE
FPS = 9
waitFPS = 3
Time_stop = 0
running_man=1

running=[[0]*H]*W
fild=[0]*W
obj=[0]*W
gen=[0]*W
pr=[0]*W
inc=[0]*W
Dudlicator=[0]*W
Converter=[0]*W
pushed=[0]*W
input_rect1 = pygame.Rect(a+30.5, 580, 140, 32)
for i in range (W):
    obj[i]=[0]*H
    gen[i]=[0]*H
    pr[i]=[0]*H
    inc[i]=[0]*H
    fild[i]=[0]*H
    Dudlicator[i]=['']*H
    Converter[i]=['']*H
    pushed[i]=[0]*H

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
user_text_direction = ['']*15
user_text_value = ''
user_text_ticks=''
user_text_direction1=''
user_text_directiondud = ''
user_text_directiondud11 = ''
user_text_directiondud12 = ''
user_text_directiondud13 = ''
user_text_direction2=''
user_text_directionres=''
user_text_action = ''
input_rect1 = pygame.Rect(a+30, 580, 140, 32)
input_rect2 = pygame.Rect(a+30, 680, 140, 32)
input_rect3 = pygame.Rect(a+30, 750, 140, 32)
input_rectdud1 = pygame.Rect(a+30, 580, 140, 32)
input_rectdud11 = pygame.Rect(a+30, 640, 140, 32)
input_rectdud12 = pygame.Rect(a+30, 700, 140, 32)
input_rectdud13 = pygame.Rect(a+30, 750, 140, 32)
input_rect4 = pygame.Rect(a+30, 580, 140, 32)
input_rect5 = pygame.Rect(a+30, 640, 140, 32)
input_rect6 = pygame.Rect(a+30, 700, 140, 32)
input_rect7 = pygame.Rect(a+30, 756, 140, 32)
'''obj[2][3]=[25,3]
obj[7][5]=[25,4]
obj[2][4]=[25,2]
gen[5][6]=[2,1,5]
pr[5][2]=1'''
Dudlicator[17][10]='d'
fild[17][10]=3
Dudlicator[8][10]='r'
fild[8][10]=3
Dudlicator[8][18]='u'
fild[8][18]=3
Dudlicator[17][18]='l'
fild[17][18]=3
Converter[4][4]='r+d=l'
fild[4][4]=5

def run (past:list,c,d,e:int):
    global fild
    global pushed
    f = [0] * c
    running=[0]*c
    for i in range(c):
        f[i] = [0] * d
        running[i]=[0]*d

    fx=0
    fy=0
    for x in range(0, c):
        for y in range(0, d):
            if past[x][y]!=0:
                fx = x
                fy = y
                if past[x][y][1]==1:
                    fy=(y+1)% d
                elif past[x][y][1] == 2:
                    fx=(x+1)% c
                elif past[x][y][1] == 3:
                    fy=(y-1)% d
                elif past[x][y][1] == 4:
                    fx=(x-1) % c
                if fild[fx][fy]==20:
                    fx=fx
                elif (f[fx][fy]==0) and (fild[fx][fy]==0) and (past[fx][fy]==0) and e==0:
                    running[x][y]=1
                elif (f[fx][fy]==0) and (fild[fx][fy]==0) and (past[fx][fy]==0):
                    f[fx][fy] =[past[x][y][0],past[x][y][1]]
                else:
                    f[x][y] = [past[x][y][0],past[x][y][1]]
                    if (fild[fx][fy]!=0) and (e==1):
                        #if (fild[fx][fy]==3) and (pushed[fx][fy]==0):
                            #dublicate(past,c,d,fx,fy)
                        pushed[fx][fy]=fild[fx][fy]

    if e==1:
        #print (f)
        #print (past)
        return f
    elif e==0:
        return running

def spawn (past,gn:list,c,d,e:int):
    f = [0] * c
    for i in range(c):
        f[i] = [0] * d
    fx = 0
    fy = 0

    for x in range(0, c):
        for y in range(0, d):
            if gn[x][y] != 0:
                if e % gn[x][y][2]==0:
                    fx=x
                    fy=y
                    past[fx][fy]=[gn[x][y][0],gn[x][y][1]]
    return (past)
def dublicate(past:list,c,d,l,m:int):
    global Dudlicator
    global pushed
    f = past
    fx = -2 #иммено его мы и будем закидывать
    fy = -2
    k=0
    if Dudlicator[l][m]!='':
        if pushed[l][m]==3:
            x=l
            y=m
            fx = -2  # иммено его мы и будем закидывать
            fy = -2
            if Dudlicator[x][y] != '':
                if (Dudlicator[x][y].find('u')==-1) and (past[x][(y-1)%d]!=0):
                    if past[x][(y-1)%d][1] == 1:
                        fx=x
                        fy=(y-1)%d
                elif (Dudlicator[x][y].find('d')==-1) and (past[x][(y + 1)%d] != 0):
                    if past[x][(y + 1)%d][1] == 3:
                        fx=x
                        fy=(y+1)%d
                elif (Dudlicator[x][y].find('r')==-1) and (past[(x + 1)%c][y] != 0):
                    if past[(x + 1)%c][y][1] == 4:
                        fx=(x+1)%c
                        fy=y
                elif (Dudlicator[x][y].find('l')==-1) and (past[(x - 1)%c][y] != 0):
                    if past[(x-1)%c][y][1]==2:
                        fx=(x-1)%c
                        fy=y
                if (fx!=-2):
                    for i in Dudlicator[x][y]:
                        if (i=='d') and (f[x][(y + 1)%d]==0) and (past[x][(y + 1)%d]==0):
                            f[x][(y + 1)%d]=[past[fx][fy][0],1]
                            k=1
                        if (i=='r') and (f[(x + 1)%c][y]==0) and (past[(x + 1)%c][y]==0):
                            f[(x + 1)%c][y]=[past[fx][fy][0],2]
                            k=1
                        if (i=='l') and (f[(x - 1)%c][y]==0) and (past[(x - 1)%c][y]==0):
                            f[(x - 1)%c][y]=[past[fx][fy][0],4]
                            k=1
                        if (i=='u') and (f[x][(y-1)%d]==0) and (past[x][(y-1)%d]==0):
                            f[x][(y-1)%d]=[past[fx][fy][0],3]
                            k=1
                if k==1:
                    f[fx][fy]=0
    return f
def convert (past:list,c,d,x,y:int):
    global Converter
    global pushed
    f = past
    px1=-2
    py1=-2
    px2=-2
    py2=-2
    fx = -2  # иммено его мы и будем закидывать
    fy = -2
    k = 0
    if Converter[x][y] != '':
        if pushed[x][y] == 5:
            one=Converter[x][y][0]
            two=Converter[x][y][2]
            oper=Converter[x][y][1]
            res=Converter[x][y][4]
            px1=Who(past,x,y,one,0)[0]
            py1=Who(past,x,y,one,0)[1]
            px2 = Who(past, x, y, two,0)[0]
            py2 = Who(past, x, y, two,0)[1]
            fx = Who(past, x, y, res,1)[0]
            fy = Who(past, x, y, res,1)[1]
            #print(fx,' ',fy,' ',px1,' ',py1,' ',px2,' ',py2)
            if (f[fx][fy]==0) and (past[px1][py1]!=0) and (past[px2][py2]!=0):
                if oper=='+':
                    f[fx][fy]=[past[px1][py1][0]+past[px2][py2][0],'0drul'.find(res)]
                if oper=='-':
                    f[fx][fy]=[past[px1][py1][0]-past[px2][py2][0],'0drul'.find(res)]
                if oper == '*':
                    f[fx][fy] = [past[px1][py1][0] * past[px2][py2][0], '0drul'.find(res)]
                if oper == '/':
                    f[fx][fy] = [past[px1][py1][0] // past[px2][py2][0], '0drul'.find(res)]
                if oper == '%':
                    f[fx][fy] = [past[px1][py1][0] % past[px2][py2][0], '0drul'.find(res)]
                past[px1][py1]=0
                past[px2][py2]=0
    return f


def Who (past:list,x,y,two,one:int):
    px2 = -2
    py2 = -2
    if one==1:
        if (two == 'u'):
            px2 = x
            py2 = y - 1
        elif (two == 'd'):
            px2 = x
            py2 = y + 1
        elif (two == 'r'):
            px2 = x + 1
            py2 = y
        elif (two == 'l'):
            px2 = x - 1
            py2 = y
    elif (two == 'u') and ((past[x][y - 1] != 0) or (one>0)):
        if (past[x][y - 1][1]== 1) or (one>0):
            px2 = x
            py2 = y - 1
    elif (two == 'd') and ((past[x][y + 1] != 0)or (one>0)):
        if (past[x][y + 1][1]== 3) or (one>0):
            px2 = x
            py2 = y + 1
    elif (two == 'r') and ((past[x + 1][y] != 0)or (one>0)):
        if (past[x + 1][y][1]== 4)or (one>0) :
            px2 = x + 1
            py2 = y
    elif (two=='l') and ((past[x - 1][y] != 0)or (one>0)):
        if (past[x - 1][y][1]== 2) or (one>0):
            px2 = x - 1
            py2 = y
    return [px2,py2]




screen = pygame.display.set_mode(RES)
menu_color = (200, 200, 200)
cell_color = (100, 100, 100)
font = pygame.font.Font(None, 30)
color_passive = pygame.Color('white')
color = color_passive
active = 0
cell_vvod = 0
def draw_menu():
    # Draw the menu background
        menu_rect = pygame.Rect(a, 0, 200, 900)
        pygame.draw.rect(screen, menu_color, menu_rect)

    # Draw the cells in the upper part of the menu
        global cell_rect1
        global cell_rect2
        global cell_rect3
        global cell_rect4
        global cell_rect5
        cell_rect1 = pygame.Rect(a + 20, 50, 160, 80)
        pygame.draw.rect(screen, cell_color, cell_rect1)
        cell_text1 = font.render("Object".format(1), True, (255, 255, 255))
        screen.blit(cell_text1, (a + 40, 35 + 50))
        cell_rect2 = pygame.Rect(a + 20, 150, 160, 80)
        pygame.draw.rect(screen, 'gold', cell_rect2)
        cell_text2 = font.render("Printer".format(2), True, (255, 255, 255))
        screen.blit(cell_text2, (a + 40, 35 + 150))
        cell_rect3 = pygame.Rect(a + 20, 250, 160, 80)
        pygame.draw.rect(screen, 'blue', cell_rect3)
        cell_text3 = font.render("Dublicator".format(3), True, (255, 255, 255))
        screen.blit(cell_text3, (a + 40, 35 + 250))
        cell_rect4 = pygame.Rect(a + 20, 350, 160, 80)
        pygame.draw.rect(screen, 'green', cell_rect4)
        cell_text4 = font.render("Generator".format(4), True, (255, 255, 255))
        screen.blit(cell_text4, (a + 40, 35 + 350))
        cell_rect5 = pygame.Rect(a + 20, 450, 160, 80)
        pygame.draw.rect(screen, 'orange', cell_rect5)
        cell_text5 = font.render("Converter".format(1), True, (255, 255, 255))
        screen.blit(cell_text5, (a + 40, 35 + 450))

    # Draw the settings in the lower part of the menu
        if cell_vvod==1:
            direction_text = font.render("Direction: ", True, (0, 0, 0))
            screen.blit(direction_text, (a+20, 550))
            amount_text = font.render("Value: ", True, (0, 0, 0))
            screen.blit(amount_text, (a+20, 650))
        elif cell_vvod==2:
            pass
        elif cell_vvod==3:
            direction_text1 = font.render("Down: ", True, (0, 0, 0))
            screen.blit(direction_text1, (a+20, 550))
            direction_text2 = font.render("Right: ", True, (0, 0, 0))
            screen.blit(direction_text2, (a+20, 620))
            direction_text3 = font.render("Up: ", True, (0, 0, 0))
            screen.blit(direction_text3, (a+20, 675))
            direction_text4 = font.render("Left: ", True, (0, 0, 0))
            screen.blit(direction_text4, (a+20, 730))
        elif cell_vvod==4:
            direction_text = font.render("Direction: ", True, (0, 0, 0))
            screen.blit(direction_text, (a+20, 550))
            amount_text = font.render("Value: ", True, (0, 0, 0))
            screen.blit(amount_text, (a+20, 650))
            ticks_text = font.render('Ticks:', True, (0, 0, 0))
            screen.blit(ticks_text, (a + 20, 720))
        elif cell_vvod==5:
            direction1_text = font.render("Direction1: ", True, (0, 0, 0))
            screen.blit(direction1_text, (a+20, 550))
            direction2_text = font.render("Direction2: ", True, (0, 0, 0))
            screen.blit(direction2_text, (a + 20, 620))
            directionres_text = font.render("Result direction: ", True, (0, 0, 0))
            screen.blit(directionres_text, (a+20, 680))
            action_text =  font.render("Action: ", True, (0, 0, 0))
            screen.blit(action_text, (a+20, 733))

        pygame.display.update()


# Define the event handling function
def handle_events():
    global user_text_ticks
    global user_text_direction
    global user_text_direction1
    global user_text_direction2
    global user_text_directiondud
    global user_text_directiondud11
    global user_text_directiondud12
    global user_text_directiondud13
    global user_text_directionres
    global user_text_value
    global user_text_action
    global active
    global cell_vvod
    global Time_stop
    global running_man
    global running
    global fild
    global W
    global H
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos[0])

            if cell_rect1.collidepoint(mouse_pos):
                print("Cell clicked! "+str(1))
                cell_vvod=1
            if cell_rect2.collidepoint(mouse_pos):
                print("Cell clicked! "+str(2))
                cell_vvod=2
            if cell_rect3.collidepoint(mouse_pos):
                print("Cell clicked! " + str(3))
                cell_vvod = 3
            if cell_rect4.collidepoint(mouse_pos):
                print("Cell clicked! " + str(4))
                cell_vvod = 4
            if cell_rect5.collidepoint(mouse_pos):
                print("Cell clicked! " + str(5))
                cell_vvod = 5
            if (mouse_pos[0]<a) and (mouse_pos[1]<b) and (cell_vvod==1) and (user_text_direction[1]!='') and (user_text_value!=''):
                obj[mouse_pos[0] // TILE][mouse_pos[1] // TILE]=[int(user_text_value),'0DRUL'.find(user_text_direction[1][0])]
            if (mouse_pos[0] < a) and (mouse_pos[1] < b) and (cell_vvod == 2):
                pr[mouse_pos[0]//TILE][mouse_pos[1]//TILE]=1
            if (mouse_pos[0]<a) and (mouse_pos[1]<b) and (cell_vvod==3) and (user_text_direction[3]!=''):
                Dudlicator[mouse_pos[0] // TILE][mouse_pos[1] // TILE] = '0drul'['0DRUL'.find(user_text_direction[3][0])]+'0drul'['0DRUL'.find(user_text_direction[5][0])]+'0drul'['0DRUL'.find(user_text_direction[6][0])]+'0drul'['0DRUL'.find(user_text_direction[7][0])]
                fild[mouse_pos[0] // TILE][mouse_pos[1] // TILE]=3
            if (mouse_pos[0]<a) and (mouse_pos[1]<b) and (cell_vvod==4) and (user_text_direction[4]!='') and (user_text_ticks!='')and(user_text_value!=''):
                gen[mouse_pos[0] // TILE][mouse_pos[1] // TILE]=[int(user_text_value),'0DRUL'.find(user_text_direction[4][0]),int(user_text_ticks)]


            if input_rect1.collidepoint(event.pos):
                active = 1
                print(1)
            elif input_rect2.collidepoint(event.pos):
                active = 2
                print(2)
            elif input_rect3.collidepoint(event.pos):
                active = 3
                print(3)
            elif input_rect4.collidepoint(event.pos):
                active = 4
                print(4)
            elif input_rect5.collidepoint(event.pos):
                active = 5
                print(5)
            elif input_rect6.collidepoint(event.pos):
                active = 6
                print(6)
            elif input_rectdud1.collidepoint(event.pos):
                active = 7
                print('12345')
            elif input_rectdud11.collidepoint(event.pos):
                active = 8
                print('1234')
            elif input_rectdud12.collidepoint(event.pos):
                active = 9
                print('123456')
            elif input_rectdud13.collidepoint(event.pos):
                active = 10
                print('234567')
            elif input_rect7.collidepoint(event.pos):
                active = 11
                print(1)
            else:
                active = 0
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                Time_stop=(Time_stop+1)%2
            if event.key==pygame.K_q:
                running_man=(running_man+1)%2
                if running_man==1:
                    running=[0]*W
                    for i in range(W):
                        running[i]=[0]*H
            if active == 1 and cell_vvod == 1:
                if event.key == pygame.K_RETURN:
                    user_text_direction[1] = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text_direction[1] = user_text_direction[1][:-1]
                elif event.key == pygame.K_RIGHT:
                    user_text_direction[1] = ''
                    user_text_direction[1] += 'Right'
                elif event.key == pygame.K_LEFT:
                    user_text_direction[1] = ''
                    user_text_direction[1] += 'Left'
                elif event.key == pygame.K_UP:
                    user_text_direction[1] = ''
                    user_text_direction[1] += 'Up'
                elif event.key == pygame.K_DOWN:
                    user_text_direction[1] = ''
                    user_text_direction[1] += 'Down'
                else:
                    print('error')
            elif active == 7:
                if event.key == pygame.K_RETURN:
                    user_text_directiondud = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text_directiondud = user_text_directiondud[:-1]
                elif event.key == pygame.K_1:
                    user_text_directiondud = '1'
                    user_text_direction[5] = 'Down'
                elif event.key == pygame.K_0:
                    user_text_directiondud = '0'
                    user_text_direction[5] = '0'
                else:
                    print('error')
            elif active == 8:
                if event.key == pygame.K_RETURN:
                    user_text_directiondud11 = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text_directiondud11 = user_text_directiondud11[:-1]
                elif event.key == pygame.K_1:
                    user_text_directiondud11 = '1'
                    user_text_direction[6] ='Right'
                elif event.key == pygame.K_0:
                    user_text_directiondud11 = '0'
                    user_text_direction[6] = '0'
                else:
                    print('error')
            elif active == 9:
                if event.key == pygame.K_RETURN:
                    user_text_directiondud12 = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text_directiondud12 = user_text_directiondud12[:-1]
                elif event.key == pygame.K_1:
                    user_text_directiondud12 = '1'
                    user_text_direction[7] ='Up'
                elif event.key == pygame.K_0:
                    user_text_directiondud12 = '0'
                    user_text_direction[7] = '0'
                else:
                    print('error')
            elif active == 10:
                if event.key == pygame.K_RETURN:
                    user_text_directiondud13 = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text_directiondud13 = user_text_directiondud13[:-1]
                elif event.key == pygame.K_1:
                    user_text_directiondud13 = '1'
                    user_text_direction[8] = 'Left'
                elif event.key == pygame.K_0:
                    user_text_directiondud13 = '0'
                    user_text_direction[8] = '0'
                else:
                    print('error')
            elif active == 1 and cell_vvod == 4:
                if event.key == pygame.K_RETURN:
                    user_text_direction[4] = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text_direction[4] = user_text_direction[4][:-1]
                elif event.key == pygame.K_RIGHT:
                    user_text_direction[4] = ''
                    user_text_direction[4] += 'Right'
                elif event.key == pygame.K_LEFT:
                    user_text_direction[4] = ''
                    user_text_direction[4] += 'Left'
                elif event.key == pygame.K_UP:
                    user_text_direction[4] = ''
                    user_text_direction[4] += 'Up'
                elif event.key == pygame.K_DOWN:
                    user_text_direction[4] = ''
                    user_text_direction[4] += 'Down'
                else:
                    print('error')
            elif active == 2:
                if event.key == pygame.K_RETURN:
                    user_text_value = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text_value = user_text_value[:-1]
                else:
                    u=''
                    u+=event.unicode
                    if ('1234567890'.find(u)==-1) or (len(user_text_value)>3):
                        u=u
                    else:
                        user_text_value += event.unicode
            elif active == 3:
                if event.key == pygame.K_RETURN:
                    user_text_ticks = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text_ticks = user_text_ticks[:-1]
                else:
                    user_text_ticks+=event.unicode
                    if ('1234567890'.find(user_text_ticks)==-1) or (len(user_text_ticks)>=3):
                        user_text_ticks=user_text_ticks
                    else:
                        user_text_ticks += event.unicode
            elif active == 4:
                if event.key == pygame.K_RETURN:
                    user_text_direction1 = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text_direction1 = user_text_direction1[:-1]
                elif event.key == pygame.K_RIGHT:
                    user_text_direction1 = ''
                    user_text_direction1 += 'Right'
                elif event.key == pygame.K_LEFT:
                    user_text_direction1 = ''
                    user_text_direction1 += 'Left'
                elif event.key == pygame.K_UP:
                    user_text_direction1 = ''
                    user_text_direction1 += 'Up'
                elif event.key == pygame.K_DOWN:
                    user_text_direction1 = ''
                    user_text_direction1 += 'Down'
                else:
                    print('error')
            elif active == 5:
                if event.key == pygame.K_RETURN:
                    user_text_direction2 = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text_direction2 = user_text_direction2[:-1]
                elif event.key == pygame.K_RIGHT:
                    user_text_direction2 = ''
                    user_text_direction2 += 'Right'
                elif event.key == pygame.K_LEFT:
                    user_text_direction2 = ''
                    user_text_direction2 += 'Left'
                elif event.key == pygame.K_UP:
                    user_text_direction2 = ''
                    user_text_direction2 += 'Up'
                elif event.key == pygame.K_DOWN:
                    user_text_direction2 = ''
                    user_text_direction2 += 'Down'
                else:
                    print('error')
            elif active == 6:
                if event.key == pygame.K_RETURN:
                    user_text_directionres = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text_directionres = user_text_directionres[:-1]
                elif event.key == pygame.K_RIGHT:
                    user_text_directionres = ''
                    user_text_directionres += 'Right'
                elif event.key == pygame.K_LEFT:
                    user_text_directionres = ''
                    user_text_directionres += 'Left'
                elif event.key == pygame.K_UP:
                    user_text_directionres = ''
                    user_text_directionres += 'Up'
                elif event.key == pygame.K_DOWN:
                    user_text_directionres = ''
                    user_text_directionres += 'Down'
                else:
                    print('error')
            elif active == 11:
                if event.key == pygame.K_RETURN:
                    user_text_action = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text_action = user_text_action[:-1]
                else:
                    user_text_action=''
                    user_text_action+=event.unicode
                    if (len(user_text_action)>1) or user_text_action != '-' or user_text_action != '+' or user_text_action != ':' or user_text_action != '*' or user_text_action != '%':
                        user_text_action=user_text_action
                    else:
                        user_text_action += event.unicode
t=0

while True:

    t=t+Time_stop
    handle_events()
    surface.fill(pygame.Color('white'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]

    draw_menu()
    # Handle events
    if cell_vvod == 1:
        pygame.draw.rect(screen, color, input_rect1)
        text_surface1 = font.render(user_text_direction[1], True, (0, 0, 0))
        pygame.draw.rect(screen, color, input_rect2)
        text_surface2 = font.render(user_text_value, True, (0, 0, 0))
        # render at position stated in arguments

        screen.blit(text_surface1, (input_rect1.x, input_rect1.y + 20))
        screen.blit(text_surface2, (input_rect2.x, input_rect2.y + 20))
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect1.w = max(100, text_surface1.get_width() + 10)
        input_rect2.w = max(100, text_surface2.get_width() + 10)
    elif cell_vvod == 3:
        pygame.draw.rect(screen, color, input_rectdud1)
        text_surface3 = font.render(user_text_directiondud, True, (0, 0, 0))
        screen.blit(text_surface3, (input_rectdud1.x, input_rectdud1.y + 20))
        input_rectdud1.w = max(100, text_surface3.get_width() + 10)
        pygame.draw.rect(screen, color, input_rectdud11)
        text_surface77 = font.render(user_text_directiondud11, True, (0, 0, 0))
        screen.blit(text_surface77, (input_rectdud11.x, input_rectdud11.y + 20))
        input_rectdud11.w = max(100, text_surface77.get_width() + 10)
        pygame.draw.rect(screen, color, input_rectdud12)
        text_surface88 = font.render(user_text_directiondud12, True, (0, 0, 0))
        screen.blit(text_surface88, (input_rectdud12.x, input_rectdud12.y + 20))
        input_rectdud12.w = max(100, text_surface88.get_width() + 10)
        pygame.draw.rect(screen, color, input_rectdud13)
        text_surface99 = font.render(user_text_directiondud13, True, (0, 0, 0))
        screen.blit(text_surface99, (input_rectdud13.x, input_rectdud13.y + 20))
        input_rectdud13.w = max(100, text_surface99.get_width() + 10)
    elif cell_vvod == 4:
        pygame.draw.rect(screen, color, input_rect1)
        text_surface4 = font.render(user_text_direction[4], True, (0, 0, 0))
        pygame.draw.rect(screen, color, input_rect2)
        text_surface5 = font.render(user_text_value, True, (0, 0, 0))
        pygame.draw.rect(screen, color, input_rect3)
        text_surface6 = font.render(user_text_ticks, True, (0, 0, 0))
        # render at position stated in arguments

        screen.blit(text_surface4, (input_rect1.x, input_rect1.y + 20))
        screen.blit(text_surface5, (input_rect2.x, input_rect2.y + 20))
        screen.blit(text_surface6, (input_rect3.x, input_rect3.y + 20))
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect1.w = max(100, text_surface4.get_width() + 10)
        input_rect2.w = max(100, text_surface5.get_width() + 10)
        input_rect3.w = max(100, text_surface6.get_width() + 10)
    elif cell_vvod == 5:
        pygame.draw.rect(screen, color, input_rect4)
        text_surface7 = font.render(user_text_direction1, True, (0, 0, 0))
        pygame.draw.rect(screen, color, input_rect5)
        text_surface8 = font.render(user_text_direction2, True, (0, 0, 0))
        pygame.draw.rect(screen, color, input_rect6)
        text_surface9 = font.render(user_text_directionres, True, (0, 0, 0))
        pygame.draw.rect(screen, color, input_rect7)
        text_surface10 = font.render(user_text_action, True, (0, 0, 0))
        # render at position stated in arguments

        screen.blit(text_surface7, (input_rect4.x, input_rect4.y + 20))
        screen.blit(text_surface8, (input_rect5.x, input_rect5.y + 20))
        screen.blit(text_surface9, (input_rect6.x, input_rect6.y + 20))
        screen.blit(text_surface10, (input_rect7.x, input_rect7.y + 20))
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect4.w = max(100, text_surface7.get_width() + 10)
        input_rect5.w = max(100, text_surface8.get_width() + 10)
        input_rect6.w = max(100, text_surface9.get_width() + 10)
        input_rect7.w = max(100, text_surface10.get_width() + 10)

    for x in range(0, W ):
        for y in range(0, H ):
            if (pr[x][y] == 1):
                pygame.draw.rect(surface, pygame.Color('yellow'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
            if gen[x][y] != 0:
                pygame.draw.rect(surface, pygame.Color('green'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
            if obj[x][y]!=0:
                if obj[x][y][1]==1:
                    pygame.draw.rect(surface, pygame.Color('red'), (x * TILE + 3.5, y * TILE + 3.5+(((t-1)%waitFPS)*TILE*running[x][y])/waitFPS, TILE - 6, TILE - 6))
                    pygame.draw.rect(surface, pygame.Color('black'), (x * TILE + 3.5, y * TILE + TILE*0.7+(((t-1)%waitFPS)*TILE*running[x][y])/waitFPS, TILE-6, TILE*0.25))
                if obj[x][y][1]==2:
                    pygame.draw.rect(surface, pygame.Color('red'), (x * TILE + 3.5+(((t-1)%waitFPS)*TILE*running[x][y])/waitFPS, y * TILE + 3.5, TILE - 6, TILE - 6))
                    pygame.draw.rect(surface, pygame.Color('black'), (x * TILE + TILE*0.7+(((t-1)%waitFPS)*TILE*running[x][y])/waitFPS, y * TILE+ 3.5 , TILE*0.25, TILE-6))
                if obj[x][y][1]==3:
                    pygame.draw.rect(surface, pygame.Color('red'), (x * TILE + 3.5, y * TILE + 3.5-(((t-1)%waitFPS)*TILE*running[x][y])/waitFPS, TILE - 6, TILE - 6))
                    pygame.draw.rect(surface, pygame.Color('black'), (x * TILE + 3.5, y * TILE +TILE*0.1-(((t-1)%waitFPS)*TILE*running[x][y])/waitFPS, TILE-6, TILE*0.25))
                if obj[x][y][1]==4:
                    pygame.draw.rect(surface, pygame.Color('red'), (x * TILE + 3.5-(((t-1)%waitFPS)*TILE*running[x][y])/waitFPS, y * TILE + 3.5, TILE - 6, TILE - 6))
                    pygame.draw.rect(surface, pygame.Color('black'), (x * TILE + TILE*0.1-(((t-1)%waitFPS)*TILE*running[x][y])/waitFPS, y * TILE + 3.5 , TILE*0.25, TILE-6))
                if pr[x][y]!=0:
                    print (obj[x][y][0])

            if Dudlicator[x][y] !='':
                pygame.draw.rect(surface, pygame.Color('blue'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
                if pushed[x][y]!=0:
                    pygame.draw.rect(surface, pygame.Color('darkblue'), (x * TILE + 3, y * TILE + 3, TILE - 5, TILE - 5))
            if Converter[x][y]!='':
                pygame.draw.rect(surface, pygame.Color('orange'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
    if Time_stop==1:
        if t % waitFPS==0:
            pushed = [0] * W
            for i in range(W):
                pushed[i] = [0] * H
            obj = run(obj, W, H, 1)
            obj = spawn(obj, gen, W, H, t)
            #print (pushed)

            for i in range(W):
                for j in range(H):
                    obj = dublicate(obj, W, H, i, j)
                    obj = convert(obj, W, H, i, j)

            if running_man==0:
                running=run(obj,W,H,0)




    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)

'''
Меню+
Можно поставить переменную+
Добавлено:
   Генератор
   Переменная
   Принтер
   Дубликатор
Надо добавить:
   Преобразователь
   Сравниватель
   If
   Стена
Надо исправить:
   переменные не видят спец. объекты перед собой
   генератор может уничтожить переменную
  можно поставить переменную на спец. объект
  доделать меню, чтобы можно было поставить любой объект
'''

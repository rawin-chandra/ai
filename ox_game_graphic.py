import pygame

pygame.init()
screen = pygame.display.set_mode((900,600))

clock = pygame.time.Clock() 

data = [[-1,-1,-1],
        [-1,-1,-1],
        [-1,-1,-1]
       ]


def display():
    x = " "
    y = " "
    val = ""
    
    os.system('cls')
    print("")

    if turn == True:
        print("TURN = X (User)")
    else:
        print("TURN = O (A.I.)")

    for i in range(3):
        for m in range(3):
            if data[i][m] == 0:                
                print("O", end ="  | ")
            elif data[i][m] == 1:
                print("X", end ="  | ")
            else:
                print(" ", end ="  | ")
        print("")
        print("---------------")

def set_data(row,col):
    data[row][col] = 1

def point_cal(row,col):
    #calculate point for this state    
    row_point = 0
    col_point = 0
    diag_point = 0
    #find position that suddenly win and return 500
    #scan in row
    count = 0
    for c in range(3):
        if data[row][c] == 0:
            count += 1
    if count >= 2:
        return 500
    #scan in column
    count = 0
    for r in range(3):        
        if data[r][col] == 0:
            count += 1
    if count >= 2:
        return 500

    #scan in diagonal
    if (row == 0 and col == 0) or (row == 1 and col == 1) or (row == 2 and col == 2):
        count = 0
        if data[0][0] == 0:
            count += 1
        if data[1][1] == 0:
            count += 1
        if data[2][2] == 0:
            count += 1
        if count >= 2:
            return 500
    if (row == 0 and col == 2) or (row == 1 and col == 1) or (row == 2 and col == 0):
        count = 0
        if data[0][2] == 0:
            count += 1
        if data[1][1] == 0:
            count += 1
        if data[2][0] == 0:
            count += 1
        if count >= 2:
            return 500
   

    #try to block opponent win   
    #scan in row
    count = 0
    for c in range(3):
        if data[row][c] == 1:
            count += 1
    if count >= 2:
        return 300
    #scan in column
    count = 0
    for r in range(3):
        if data[r][col] == 1:            
            count += 1
    if count >= 2:
        return 300

    #scan in diagonal
    if (row == 0 and col == 0) or (row == 1 and col == 1) or (row == 2 and col == 2):
        count = 0
        if data[0][0] == 1:
            count += 1
        if data[1][1] == 1:
            count += 1
        if data[2][2] == 1:
            count += 1
        if count >= 2:
            return 300
    if (row == 0 and col == 2) or (row == 1 and col == 1) or (row == 2 and col == 0):
        count = 0
        if data[0][2] == 1:
            count += 1
        if data[1][1] == 1:
            count += 1
        if data[2][0] == 1:
            count += 1
        if count >= 2:
            return 300

    #set point by chance to win
    #scan in row
    for c in range(3):
        if data[row][c] != 0:
            row_point = row_point + 1
    #scan in column
    for r in range(3):
        if data[r][col] != 0:
            col_point = col_point + 1
    #scan in diagonal
    if row == 0 and col == 0:
        diag_point = diag_point + 1
    elif row == 1 and col == 1:
        diag_point = diag_point + 1
    elif row == 2 and col == 2:
        diag_point = diag_point + 1
    elif row == 2 and col == 2:
        diag_point = diag_point + 1
    elif row == 0 and col == 2:
        diag_point = diag_point + 1

    return (row_point + col_point + diag_point)


def ai_cal():    
    #state space search
    #breath first search
    max = 0   
    select_row = 0
    select_col = 0

    for row in range(3):
        for col in range(3):
            if data[row][col] == -1:
                p = point_cal(row,col)
                if p > max:
                    max = p
                    select_row = row
                    select_col = col
    
    print(" AI choose " , select_row , " " , select_col)
    data[select_row][select_col] = 0

def check_finish():
#check game end?    
    #check in row
    for row in range(3):
        o_point = 0
        for col in range(3):
            if data[row][col] == 0:
                o_point = o_point + 1
        if o_point == 3:            
            return 1

        x_point = 0
        for col in range(3):
            if data[row][col] == 1:
                x_point = x_point + 1
        if x_point == 3:            
            return 2
    #check in column
    for col in range(3):
        o_point = 0
        for row in range(3):
            if data[row][col] == 0:
                o_point = o_point + 1
        if o_point == 3:            
            return 1

        x_point = 0
        for row in range(3):
            if data[row][col] == 1:
                x_point = x_point + 1
        if x_point == 3:           
            return 2

    #check in diagonal   
    if data[0][0] == 0 and data[1][1] == 0 and data[2][2] == 0:        
        return 1
    if data[0][0] == 1 and data[1][1] == 1 and data[2][2] == 1:        
        return 2
    if data[0][2] == 0 and data[1][1] == 0 and data[2][0] == 0:        
        return 1
    if data[0][2] == 1 and data[1][1] == 1 and data[2][0] == 1:        
        return 2

    #check draw
    count = 0
    for row in range(3):
        for col in range(3):
            if data[row][col] == -1:
                count += 1
    if count == 0:
        return 3

    return 0

done = False
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)
myfont = pygame.font.SysFont('Comic Sans MS', 30)
TURN = True

def draw_x():
    global screen
    for i in range(3):
        for m in range(3):
            if data[i][m] == 1: 
                pygame.draw.line(screen, GREEN, (m * 300,i * 200), ((m * 300) + 300,(i * 200) + 200), 5)
                pygame.draw.line(screen, GREEN, ((m * 300) + 300,i * 200), (m * 300 ,(i * 200)+ 200), 5)
    
def draw_y():
    global screen
    for i in range(3):
        for m in range(3):
            if data[i][m] == 0: 
                pygame.draw.circle(screen, RED, ( (m * 300) + 150,(i * 200) + 100)  ,80,5 )
                

def check_mouse_pos(x,y):
    col = x / 300 
    row = y / 200    
    set_data(int(row) ,int(col)) 
    
def draw_finish(res):   
    global screen     
    if res == 1:
                word2 = "O (A.I.) is WIN!!!!"
                textsurface2 = myfont.render(word2, False, (0, 0, 0))
                print(" O (A.I.) is WIN!!!! ")
                screen.blit(textsurface2,(200 ,150))
    elif res == 2:
                word2 = "X (User) is WIN!!!!"
                textsurface2 = myfont.render(word2, False, (0, 0, 0))
                print(" X (User) is WIN!!!! ")
                screen.blit(textsurface2,(200 ,150))
    elif res == 3:
                word2 = "Draw!!!"
                textsurface2 = myfont.render(word2, False, (0, 0, 0))
                print(" Draw!!! ") 
                screen.blit(textsurface2,(200 ,150))

while not done:   #game loop      

    if TURN == True:
        word = "TURN : You"
    else:
        word = "TURN : Comp"
    textsurface = myfont.render(word, False, (0, 0, 0))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()            
            check_mouse_pos(pos[0],pos[1])
            TURN = False
            ai_cal()            
            
    screen.fill((255,255,255))     
    
    xx = 300
    for i in range(2):
        pygame.draw.line(screen, BLUE, (xx,0), (xx,600), 5) 
        xx += 300
    xx = 200
    for i in range(2):
        pygame.draw.line(screen, BLUE, (0,xx), (900,xx), 5) 
        xx += 200
    
    draw_x()
    draw_y()
    
    res = check_finish()
    draw_finish(res)
    #screen.blit(back,(0,0))
    screen.blit(textsurface,(10 ,20))
    pygame.display.flip()    
    clock.tick(30);  
    
    
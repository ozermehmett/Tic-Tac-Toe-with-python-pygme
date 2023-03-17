import pygame, sys, random

pygame.init()
W, H = 500, 500   #ekran oranı

GREEN=(0,240,0)   #renkler
BLUE = (0,191,255)
ORANGE = (255,125,64)
PURPLE = (186,85,211)
SKYBLUE = (132,112,255)
WHITE = (255,255,255)   
BLACK = (0,0,0)

liste = [] #oyunun döndüğü liste
hamlePC = []   #pc nin yapabileceği hamlelerin tutulacağı liste
screen = pygame.display.set_mode((W, H))   #ekranı oluşturduk
clock = pygame.time.Clock()     #frame sayısını belirlemek için nesnemizi tanımladık

font = pygame.font.SysFont(None, 50)
win1 = font.render("X kazandı!", True, ORANGE)
win2 = font.render("O kazandı!", True, ORANGE)


for i in range(3):    #listemizi oyun alanına göe oluştrduk
        liste.append(3*[" "])

def oyunAlani():    #oyuun alanini çizen fonk.
    for i in range(2):
        pygame.draw.line(screen,GREEN,[100,i*100+200],[400,i*100+200],5)
        pygame.draw.line(screen,GREEN,[i*100+200,100],[i*100+200,400],5)


def ciz(liste):   #taslari cizen fonk.
    font = pygame.font.SysFont(None, 80)
    player1 = font.render("X", True, BLUE)
    pc = font.render("O", True, BLUE)
    for i in range(3):
        for j in range(3):
            if liste[i][j] == "X":
                screen.blit(player1, (130+i*100, 130+j*100))

            elif liste[i][j] == "O":
                screen.blit(pc, (130+i*100, 130+j*100))
                
def button():   #kazanan durumunda yeniden oynama butonu cizen fonk.
    font = pygame.font.SysFont(None, 40)
    pygame.draw.rect(screen, SKYBLUE, (135,420,230,60), 0)
    buttonD = font.render("YENİDEN OYNA", True, WHITE)
    screen.blit(buttonD, (150, 435))
    
def buttonClicked(x,y):   #butonun tıklamalarını kontrol eden fonk.
    global liste
    if x-135 > 0 and x-365 < 0 and y - 420 > 0 and y - 480 < 0:
       for i in range(3):
           for j in range(3):
               liste[i][j] = " "
       screen.fill(BLACK)
       oyunAlani()
       return True

def player(x,y):   #gelen tiklamalari algilayip listeye yerlestiren fonk
    if x > 100 and y > 100 and x < 400 and y < 400:
        x -= 100
        y -= 100
        if x <= 100:
            if y <= 100:
                if liste[0][0] == " ":
                    liste[0][0] = "X"
                    return True
                else:
                    return False
            elif y <= 200:
                if liste[0][1] == " ":
                    liste[0][1] = "X"
                    return True
                else:
                    return False
            else:
                if liste[0][2] == " ":
                    liste[0][2] = "X"
                    return True
                else:
                    return False
        elif x <= 200:
            if y <= 100:
                if liste[1][0] == " ":
                    liste[1][0] = "X"
                    return True
                else:
                    return False
            elif y <= 200:
                if liste[1][1] == " ":
                    liste[1][1] = "X"
                    return True
                else:
                    return False
            else:
                if liste[1][2] == " ":
                    liste[1][2] = "X"
                    return True
                else:
                    return False
        else:
            if y <= 100:
                if liste[2][0] == " ":
                    liste[2][0] = "X"
                    return True
                else:
                    return False
            elif y <= 200:
                if liste[2][1] == " ":
                    liste[2][1] = "X"
                    return True
                else:
                    return False
            else:
                if liste[2][2] == " ":
                    liste[2][2] = "X"
                    return True
                else:
                    return False
    return False

def kontrol(liste):    #oyun bitti mi diye kontrol eden fonk. 
    global win
    for row in liste:
            if row[0] == row[1] == row[2] != " ":
                if row[0] == "X" or row[0] == "O":
                    pygame.draw.line(screen,PURPLE,[(liste.index(row)+2)*100-50,100],[(liste.index(row)+2)*100-50,400],5)
                    pygame.display.update()
                    return True
    for col in range(3):
        if liste[0][col] == liste[1][col] == liste[2][col] != " ":
            if row[0] == "X" or row[0] == "O":
                pygame.draw.line(screen,PURPLE,[100,100*(col+1)+50],[400,100*(col+1)+50],5)
                pygame.display.update()
                return True
    if liste[0][0] == liste[1][1] == liste[2][2] != " ":
        if row[0] == "X" or row[0] == "O":
            pygame.draw.line(screen,PURPLE,[100,100],[400,400],5)
            pygame.display.update()
            return True
    if liste[0][2] == liste[1][1] == liste[2][0] != " ":
        if row[0] == "X" or row[0] == "O":
            pygame.draw.line(screen,PURPLE,[400,100],[100,400],5)
            pygame.display.update()
            return True

oyunAlani()  #oyun alanini cizdirdik
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if player(x,y): #gelen x,y koordinatlari uyumluysa listeye ekledik
                ciz(liste) 
                if kontrol(liste):
                    button()
                    screen.blit(win1, (150, 30))
                


                else:   
                    for i in range(3):
                        for j in range(3):
                            if liste[i][j] == " ":  #oyuncu hamle yaptiysa ve listede bos eleman varsa bunlarin listesii alir 
                                hamlePC.append([i,j])
                    if hamlePC:  #listede eleman varsa rastgele birine hamle yapar
                        a = random.choice(hamlePC)
                        liste[a[0]][a[1]] = "O"
                        ciz(liste)
                        hamlePC.clear()
                        kontrol(liste)
                        if kontrol(liste):
                            button()
                            screen.blit(win2, (150, 30))
                    
                        
           
            buttonClicked(x,y)          
    pygame.display.update()
    clock.tick(5)


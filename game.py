import pygame
pygame.mixer.pre_init(44100,-16,1,512)
import random
pygame.init()
SHIRINA_OKNA, VISOTA_OKNA= 900, 400
FPS = 60
#_______________________________________________________________-
OKNO = pygame.display.set_mode((SHIRINA_OKNA, VISOTA_OKNA))
pygame.display.set_caption("COSMO-ЗАЯ")
pygame.display.set_icon(pygame.image.load('iconka.bmp'))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
SHRIFT= pygame.font.SysFont('arial',30)
SHRIFT_MENU=pygame.font.SysFont('arial',20)
pygame.mixer.music.load('back.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
serdecki=pygame.mixer.Sound('collect.ogg')
serdecki.set_volume(0.1)
gameover_music=pygame.mixer.Sound('gameover.ogg')
gameover_music.set_volume(0.1)
vistrel=pygame.mixer.Sound('piu.ogg')
vistrel.set_volume(0.1)
NLO=pygame.mixer.Sound('nlo-inoplanetnyie-zvukovyie-effektyi-43128.ogg')
NLO.set_volume(0.05)
hlopok=pygame.mixer.Sound('hlopok.ogg')
udar=pygame.mixer.Sound('udar.ogg')
FLAG=False
speed=4
xdvij=200
ydvij=100
fall=2
schet=0
hight_score=0
hp=3
hp_color=(255,255,255)
PLAYER1=pygame.image.load('zai1.png').convert_alpha()
PLAYER2=pygame.image.load('zai4.png').convert_alpha()
PLAYER3=pygame.image.load('zai3.png').convert_alpha()
PLAYER_GAS=pygame.image.load('zai2.png').convert_alpha()
mouse=400,200
enemys=[]
count=0
timer_enemy=180
timer_heart=150
timer_alien=400
timer_light=50
random_positiony = random.randint(200, 300)
random_positiony_heart = random.randint(100, 300)
random_positiony_alien = random.randint(200, 300)
random_angle = 2
color_menu=(255, 255, 0)
color_tutorial=(255,255,255)
TOP_LINE=[]
TOP_LINE_2=[]
BOTTOM_LINE=[]
BOTTOM_LINE_2=[]
hearth_image=pygame.image.load('heart.png').convert_alpha()
hearts=[]
alien_image=pygame.image.load('alien.png').convert_alpha()
aliens=[]
light_image=pygame.image.load('light.png').convert_alpha()
lights=[]
move_light=5
FON=[]
fon_image=pygame.image.load('fon2.png')
FON.append(pygame.Rect(0,0,300,400))
restart=pygame.image.load('Restart.png')
m_menu=pygame.image.load('menu.png')
triangle1=pygame.image.load('triangle1.png')
triangle2=pygame.image.load('triangle2.png')
en=pygame.image.load('Sprite-0002.png').convert_alpha()
birds=[pygame.image.load('Sprite-0002.png').convert_alpha(),pygame.image.load('Sprite-0003.png').convert_alpha(),pygame.image.load('Sprite-0004.png').convert_alpha()]
#____________________________________________________________________
class Cursor():
    def __init__(self,x,y,color,size,contur):
        self.x=x
        self.y=y
        self.color=color
        self.size=size
        self.contur=contur
        pygame.draw.circle(OKNO, color, (x, y), size, contur)
        pygame.draw.circle(OKNO, color, (x-15, y),1 )
        pygame.draw.circle(OKNO, color, (x+15, y), 1)
        pygame.draw.circle(OKNO, color, (x, y-15), 1)
        pygame.draw.circle(OKNO, color,(x, y+15), 1)
        pygame.draw.circle(OKNO, color, (x, y), 1)
play = True
state="menu"
while play:
    if state == "menu":
        OKNO.blit(m_menu, (0,0))
        text_menu = SHRIFT.render("ИГРАТЬ", 1, (color_menu))
        position_menu = text_menu.get_rect(center=(600, 250))
        OKNO.blit(text_menu, position_menu)
        text_menu2 = SHRIFT_MENU.render('для выхода нажмите "ESC"', 1, (128, 128, 128))
        OKNO.blit(text_menu2, (650, 350))
        text_tutorial = SHRIFT.render("ОБУЧЕНИЕ", 1, (color_tutorial))
        position_tutorial = text_tutorial.get_rect(center=(600, 300))
        OKNO.blit(text_tutorial, position_tutorial)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    play=False

        mouse=pygame.mouse.get_pos()
        cursor3=Cursor(mouse[0],mouse[1],(255,255,0),10,0)
        buttonL, buttonM, buttonR = pygame.mouse.get_pressed()
        if position_menu.collidepoint(mouse[0],mouse[1]):
            color_menu=(255, 255, 0)
            if buttonL == True:
                state="start"
        elif position_tutorial.collidepoint(mouse[0],mouse[1]):
            color_tutorial=(255, 255, 0)
            if buttonL == True:
                state="tutorial"
        else:
            color_menu=(255, 255, 255)
            color_tutorial=(255,255,255)

        pygame.display.update()
        clock.tick(FPS)
    elif state=="tutorial":
        OKNO.blit(restart, (0, 0))
        text_menu = SHRIFT.render('ПОДЪЕМНАЯ СИЛА: "L.SHIFT"', 1, (255, 255, 255))
        OKNO.blit(text_menu, (200, 50))
        OKNO.blit(PLAYER_GAS, (580, 30))
        text_menu2 = SHRIFT.render('СТРЕЛЬБА ПО ВРАГАМ: "ЛКМ" ', 1, (255, 255, 255))
        OKNO.blit(text_menu2, (200, 150))
        OKNO.blit(alien_image, (580, 150))
        OKNO.blit(en, (650, 155))
        text_menu3 = SHRIFT.render('ОСТЕРЕГАЙТЕСЬ: ', 1, (255, 255, 255))
        OKNO.blit(text_menu3, (200, 100))
        OKNO.blit(light_image, (450,100))
        text_menu5 = SHRIFT_MENU.render('назад в меню: нажмите "ESC"', 1, (255, 255, 255))
        OKNO.blit(text_menu5, (650, 350))
        text_menu4 = SHRIFT.render('ПЕРЕМЕЩЕНИЕ: ВЛЕВО "A" ВПРАВО "D"', 1, (255, 255, 255))
        OKNO.blit(text_menu4, (200, 200))
        text_menu6 = SHRIFT.render('ПОДБИРАЙТЕ:', 1, (255, 255, 255))
        OKNO.blit(text_menu6, (200, 250))
        OKNO.blit(hearth_image, (400, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                state="menu"
        pygame.display.update()
        clock.tick(FPS)
    elif state=="start":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                state="gameover"
            elif event.type == pygame.MOUSEMOTION:
                pos = event.pos
                mouse = pos
            elif event.type == pygame.KEYDOWN and event.mod == pygame.KMOD_LSHIFT:
                fall = -5
                FLAG=True
            else:
                fall = 2
                FLAG = False
        ydvij += fall
        timer_enemy-=1
        timer_heart-=1
        timer_alien-=1
        timer_light-=1
        # ___________________________________________________________________
        for f in range(len(FON) - 1, -1, -1):
            ffon = FON[f]
            ffon.x -= 1
            if ffon.right < 0:
                FON.remove(ffon)
            if FON[len(FON)-1].right<=SHIRINA_OKNA:
                FON.append(pygame.Rect(FON[len(FON)-1].right,0,300,400))
        for fons in FON:
            OKNO.blit(fon_image,fons)
        # ---------------------------------------------------------

        heart_view=pygame.draw.rect(OKNO, pygame.Color('white'),(10,50, 10,10))
        heart_rect_image = hearth_image.get_rect(center=heart_view.center)
        OKNO.blit(hearth_image, heart_rect_image)
        buttonL, buttonM, buttonR = pygame.mouse.get_pressed()
        if buttonL == True:
            colorM = [255,0,0]
            vistrel.play()
        elif buttonM == True: colorM = [128,128,128]
        elif buttonR == True: colorM = [128,128,128]
        else: colorM = [255,255,255]


#----------------------------------------------------------------------------
        if len(enemys) == 0 and timer_enemy == 0:
            rect_enemy = en.get_rect(center=(900, random_positiony))
            enemys.append(rect_enemy)
        if count+1>=60:
            count=0
        for enemy in enemys:
            OKNO.blit(birds[count//20], rect_enemy)
            count+=1
            enemy.x -= 3
            enemy.y+=random_angle
            if enemy.bottom>=VISOTA_OKNA-40 or enemy.top<=40:
                random_angle=-random_angle
            if enemy.right < 0:
                enemys.remove(enemy)
                timer_enemy = random.randint(60, 100)
                random_positiony = random.randint(200, 300)
                random_angle = random.randint(-3, 3)
            elif rect_enemy.collidepoint(pygame.mouse.get_pos()) and buttonL==True:
                enemys.remove(enemy)
                timer_enemy = random.randint(60, 100)
                random_positiony = random.randint(200, 300)
                random_angle = random.randint(-3, 3)
            elif rect_PLAYER.colliderect(enemy):
                hp-=1
                hlopok.play()
                enemys.remove(enemy)
                timer_enemy = random.randint(60, 100)
                random_positiony = random.randint(200, 300)
                random_angle = random.randint(-3, 3)

    #----------------------------------------------
        if len(lights) == 0 and timer_light == 0:
                rect_light = light_image.get_rect(center=(900, 60))
                lights.append(rect_light)
        for light in lights:
            OKNO.blit(light_image, rect_light)
            light.x -= 5
            light.y +=move_light
            if light.bottom==VISOTA_OKNA-40 or light.top<40:
                move_light=-move_light
            if light.right < 0:
                lights.remove(light)
                timer_light = random.randint(300, 400)
            elif rect_PLAYER.colliderect(light):
                hp-=1
                udar.play()
                lights.remove(light)
                timer_light = random.randint(300, 400)
#---------------------------------------------------------------
        if len(hearts) == 0 and timer_heart == 0:
            rect_hearth = hearth_image.get_rect(center=(900, random_positiony_heart))
            hearts.append(rect_hearth)
        for heart in hearts:
            OKNO.blit(hearth_image, rect_hearth)
            heart.x -= 6
            if heart.right < 0:
                hearts.remove(heart)
                timer_heart = random.randint(100, 300)
                random_positiony_heart = random.randint(100, 300)
            elif rect_PLAYER.colliderect(heart):
                hp+=1
                serdecki.play()
                hearts.remove(heart)
                timer_heart = random.randint(100, 300)
                random_positiony_heart = random.randint(100, 300)
    #-----------------------------------------------------------
        if len(aliens) == 0 and timer_alien == 0:
            rect_alien = alien_image.get_rect(center=(900, random_positiony_alien))
            aliens.append(rect_alien)
            NLO.play()
        for alien in aliens:
            OKNO.blit(alien_image, rect_alien)
            alien.x -= 10
            if alien.right < 0:
                aliens.remove(alien)
                timer_alien = random.randint(500,1000)
                random_positiony_alien = random.randint(200, 300)
            elif rect_PLAYER.colliderect(alien):
                hp-=1
                udar.play()
                aliens.remove(alien)
                timer_alien = random.randint(500,1000)
                random_positiony_alien = random.randint(200, 300)
            elif rect_alien.collidepoint(pygame.mouse.get_pos()) and buttonL==True:
                aliens.remove(alien)
                timer_alien = random.randint(500,1000)
                random_positiony_alien = random.randint(200, 300)
    #_____________________________________________

        text_hp = SHRIFT.render(str(hp), 1, (hp_color))
        position_hp = text_hp.get_rect(center=(50, 55))
        OKNO.blit(text_hp, position_hp)

        schet+=1
        text=SHRIFT.render(str(schet),1,(255,255,255))
        OKNO.blit(text,(800,50))
    #_______________________________________________
        if len(TOP_LINE) == 0 or TOP_LINE[len(TOP_LINE)-1].x ==820:
            TOP_LINE.append(pygame.Rect(SHIRINA_OKNA,0,40,40))
        for block in TOP_LINE:
            pygame.draw.rect(OKNO,pygame.Color('white'),block)
            rect1=triangle1.get_rect(center=block.center)
            OKNO.blit(triangle1, rect1)
        for i in range(len(TOP_LINE)-1,-1,-1):
            blok=TOP_LINE[i]
            blok.x -= 5
            if blok.x < -80: TOP_LINE.remove(blok)
        if TOP_LINE[len(TOP_LINE)-1].x ==860:
            TOP_LINE_2.append(pygame.Rect(SHIRINA_OKNA, 0, 40, 40))
        for block in TOP_LINE_2:
            pygame.draw.rect(OKNO, pygame.Color('white'), block)
            rect2 = triangle2.get_rect(center=block.center)
            OKNO.blit(triangle2, rect2)
        for i in range(len(TOP_LINE_2) - 1, -1, -1):
            blok = TOP_LINE_2[i]
            blok.x -= 5
            if blok.x <-40: TOP_LINE_2.remove(blok)

        if len(BOTTOM_LINE) == 0 or BOTTOM_LINE[len(BOTTOM_LINE)-1].x ==820:
            BOTTOM_LINE.append(pygame.Rect(SHIRINA_OKNA,VISOTA_OKNA-40,40,40))
        for block in BOTTOM_LINE:
            pygame.draw.rect(OKNO,pygame.Color('white'),block)
            rect1=triangle1.get_rect(center=block.center)
            OKNO.blit(triangle1, rect1)
        for i in range(len(BOTTOM_LINE)-1,-1,-1):
            blok=BOTTOM_LINE[i]
            blok.x -= 5
            if blok.x < -80: BOTTOM_LINE.remove(blok)
        if BOTTOM_LINE[len(BOTTOM_LINE)-1].x ==860:
            BOTTOM_LINE_2.append(pygame.Rect(SHIRINA_OKNA, VISOTA_OKNA-40, 40, 40))
        for block in BOTTOM_LINE_2:
            pygame.draw.rect(OKNO, pygame.Color('white'), block)
            rect2 = triangle2.get_rect(center=block.center)
            OKNO.blit(triangle2, rect2)
        for i in range(len(BOTTOM_LINE_2) - 1, -1, -1):
            blok = BOTTOM_LINE_2[i]
            blok.x -= 5
            if blok.x <-40: BOTTOM_LINE_2.remove(blok)
 # ----------------------------------------------
        player = PLAYER1
        rect_PLAYER = player.get_rect(center=(xdvij, ydvij))
        cursorPX, cursorPY = mouse
        klavisha = pygame.key.get_pressed()
        if klavisha[pygame.K_d]:
            xdvij += speed
        elif klavisha[pygame.K_a]:
            xdvij -= speed
        if cursorPY > ydvij+30:
             player=PLAYER2
        elif cursorPY < ydvij-30:
            player=PLAYER3
        elif cursorPY >= ydvij+30 and cursorPY<=ydvij-30 :
            player=PLAYER1
        elif FLAG ==True:
            player=PLAYER_GAS
        else: player=PLAYER1
        if rect_PLAYER.x<0:
            rect_PLAYER.x=0
        elif rect_PLAYER.x>SHIRINA_OKNA-rect_PLAYER.height:
            rect_PLAYER.x=SHIRINA_OKNA-rect_PLAYER.height
        if rect_PLAYER.y<=40:
            rect_PLAYER.y=40
        elif rect_PLAYER.bottom>VISOTA_OKNA-30:
            gameover_music.play()
            state ="gameover"
        OKNO.blit(player,rect_PLAYER)
        if hp==0:
            gameover_music.play()
            state="gameover"
        cursor1=Cursor(cursorPX, cursorPY, colorM,10,1)
        pygame.display.update()
        clock.tick(FPS)
    elif state=="gameover":
        OKNO.blit(restart, (0,0))
        text_menu = SHRIFT.render('ДЛЯ РЕСТАРТА НАЖМИТЕ "SPACE"', 1, (255, 255, 0))
        OKNO.blit(text_menu, (200, 100))
        text_menu2 = SHRIFT.render("ВАШ СЧЕТ : ", 1, (255, 255, 255))
        OKNO.blit(text_menu2, (300, 150))
        text_menu2 = SHRIFT.render(str(schet), 1, (255, 255, 255))
        OKNO.blit(text_menu2, (500, 150))
        text_menu3 = SHRIFT_MENU.render('для выхода нажмите "ESC"', 1, (255, 255, 255))
        OKNO.blit(text_menu3, (650, 350))
        text_menu4 = SHRIFT.render("ВАШ ЛИЧНЫЙ РЕКОРД: ", 1, (255, 255, 255))
        OKNO.blit(text_menu4, (300, 200))
        text_menu5 = SHRIFT.render(str(hight_score), 1, (255, 255, 255))
        OKNO.blit(text_menu5, (600, 200))

        if hight_score<schet:
            hight_score=schet

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            elif event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                play=False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                xdvij = 200
                ydvij = 100
                schet = 0
                hp = 3
                enemys = []
                TOP_LINE = []
                TOP_LINE_2 = []
                BOTTOM_LINE = []
                BOTTOM_LINE_2 = []
                timer_enemy = 180
                timer_heart = 150
                hearts = []
                aliens = []
                timer_alien = 300
                lights = []
                move_light = 5
                timer_light = 50
                state="start"
        pygame.display.update()
        clock.tick(FPS)


pygame.quit()


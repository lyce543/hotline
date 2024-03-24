import pygame

pygame.init()
pygame.mixer.init()

white = (255, 255, 255)
yellow = (255, 255, 0)
light_blue = (200, 250, 255)
black = (0, 0, 0)
green = (0, 255, 0)
dark_green = (0, 150, 0)
red = (255, 0, 0)

window = pygame.display.set_mode((500, 500))
window.fill(light_blue)
clock = pygame.time.Clock()

racket_x = 200
racket_y = 330

game_over = False


class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = light_blue
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Picture(Area):
    def __init__(self, fillname, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(fillname)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def draw(self, shift_x=10, shift_y=0):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.text = text
        self.font = pygame.font.Font("Forte", fsize)
        self.image = self.font.render(text, True, text_color)

    def draw(self, shift_x=10, shift_y=0):
        pygame.draw.rect(window, self.fill_color, self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


game_over = True
prolog=True
menu = False
final=True
prol=Picture("prol.png")
level1 = Picture("F:\python\level1.png")
level2 = Picture("level2.png")
gg = Picture("F:\python\gg.png", 50, 380, 58, 56)
granizay = Picture("F:\python\granizay.png")
granizax = Picture("F:\python\granizax.png")
granizay1 = Picture("F:\python\granizay.png", 495, 0)
granizax1 = Picture("F:\python\granizax.png", 0, 495)
stenay = Picture("F:\python\stenay.png", 156, 341, 5, 159)
stenay1 = Picture("F:\python\stenay1.png", 156, 0, 5, 183)
bl = Picture("F:\python\ilard.png", 356, 9, 128, 60)
div=Picture("sofa.png")
stenax = Picture("F:\python\stenax.png", 159, 181, 257, 5)
stenax2 = Picture("F:\python\stenax.png", 159, 340, 257, 5)
pr = Picture("F:\python\pr.png", 40, 30, 66, 39)
pr1 = Picture("F:\python\pr1.png", 190, 100, 66, 39)
pr2 = Picture("F:\python\pr1.png", 400, 250, 66, 39)
pr3 = Picture("F:\python\pr2.png", 190, 400, 66, 39)
pyl = Picture("F:\python\pyl.png")
win = Picture("F:\python\win.png")
over = Picture("F:\python\over.png")
menub = Picture("загружено.png")
button_image = pygame.image.load('ng.png')
button_rect = button_image.get_rect()
button_rect.center = (250,250)

di1=True
d1 = pygame.image.load('diakog1.png')
d1_rect = button_image.get_rect()
d1_rect.center = (175,100)

di2=False
d2 = pygame.image.load('diakog2.png')
d2_rect = button_image.get_rect()
d2_rect.center = (175,100)

bullets = []  # List to store the bullets
bulletsr = []
bulletsl = []
bulletsd = []

stena = []
p=5
q = 2
up = 3
down = 3
right = 3
left = 3


move_right = False
move_left = False
move_up = False
move_down = False
cout = 3
start_x = 159
start_y = 181
rotation_interval = 1000  # Интервал поворота в миллисекундах
rotation_interval1 = 1000
last_rotation_time = pygame.time.get_ticks()  # Время последнего поворота
b=0
n=0
v=0
c=0
m=1
l=1
k=1
j=1
pygame.mixer.music.load("F:\python\menus.mp3")
pygame.mixer.music.set_volume(0.1)  
pygame.mixer.music.play(-1)


while not menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = True  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                menu=True
                prolog=False
    menub.draw()
    window.blit(button_image, button_rect)
    pygame.display.update()
    clock.tick(40)

pygame.mixer.music.load("hotline_miami_04. M.O.O.N - Crystals.mp3")
pygame.mixer.music.set_volume(0.1)  
pygame.mixer.music.play(-1)
gg = Picture("F:\python\gg.png", 200, 200, 58, 56)
while not prolog:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            prolog = True  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if d1_rect.collidepoint(event.pos) and di2==False:
                    di1=False
                    di2=True
            elif event.button == 3:
                if d2_rect.collidepoint(event.pos) and di1==False:
                    di2=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True
                gg.image = pygame.image.load("F:\python\gg_right.png")
            if event.key == pygame.K_a:
                move_left = True
                gg.image = pygame.image.load("F:\python\gg_left.png")
            if event.key == pygame.K_w:
                move_up = True
                gg.image = pygame.image.load("F:\python\gg_up.png")
            if event.key == pygame.K_s:
                move_down = True
                gg.image = pygame.image.load("F:\python\gg_down.png")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
                move_down = False
    if move_right:
        if gg.rect.x + right <= 450:
            # Проверка столкновения с объектами bl, stenay, stenay1, stenax и stenax2
            gg.rect.x += right
    if move_left:
        if gg.rect.x - left >= 0:
            gg.rect.x -= left

    if move_up:
        if gg.rect.y - up >= 0:         
            gg.rect.y -= up
    
    if move_down:
        if gg.rect.y + down <= 450:
            gg.rect.y += down

    if gg.rect.y > 500:
        down = 0
    if gg.rect.y < 0:
        down = 0
    if gg.rect.x > 450:
        right = 0
    if gg.rect.x < 0:
        left = 0
                
    if gg.rect.y<50:
        prolog=True
        game_over=False


    prol.draw()
    gg.draw()
    if di1==True:
        window.blit(d1, d1_rect)
    if di2==True:
        window.blit(d2, d2_rect)
    pygame.display.update()
    clock.tick(40)

pygame.mixer.music.load("F:\python\muz.mp3")
pygame.mixer.music.set_volume(0.1)  
pygame.mixer.music.play(-1)
gg = Picture("F:\python\gg.png", 50, 380, 58, 56)
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True
                gg.image = pygame.image.load("F:\python\gg_right.png")
            if event.key == pygame.K_a:
                move_left = True
                gg.image = pygame.image.load("F:\python\gg_left.png")
            if event.key == pygame.K_w:
                move_up = True
                gg.image = pygame.image.load("F:\python\gg_up.png")
            if event.key == pygame.K_s:
                move_down = True
                gg.image = pygame.image.load("F:\python\gg_down.png")
            if event.key == pygame.K_SPACE:
                if move_up == True:
                    bullet = Picture(
                        "F:\python\pyl.png",
                        gg.rect.x + gg.rect.height - 15,
                        gg.rect.y - pyl.rect.height,
                    )
                    bullets.append(bullet)
                
                    
                if move_right == True:
                    bulletr = Picture(
                        "F:\python\pylx.png",
                        gg.rect.x + gg.rect.height,
                        gg.rect.y + gg.rect.width - 18,
                    )
                    bulletsr.append(bulletr)
                if move_left == True:
                    bulletl = Picture(
                        "F:\python\pylx.png",
                        gg.rect.x - pyl.rect.width,
                        gg.rect.y + pyl.rect.height,
                    )
                    bulletsl.append(bulletl)
                if move_down == True:
                    bulletd = Picture(
                        "F:\python\pyl.png",
                        gg.rect.x + pyl.rect.width,
                        gg.rect.y + gg.rect.width,
                    )
                    bulletsd.append(bulletd)
                    

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
                move_down = False
    
    if move_right:
        if gg.rect.x + right <= 450:
            # Проверка столкновения с объектами bl, stenay, stenay1, stenax и stenax2
            if (
                not gg.rect.colliderect(bl.rect)
                and not gg.rect.colliderect(stenay.rect)
                and not gg.rect.colliderect(stenay1.rect)
                and not gg.rect.colliderect(stenax.rect)
                and not gg.rect.colliderect(stenax2.rect)
            ):
                gg.rect.x += right
            else:
                move_right = False
                gg.rect.x -= 3

    if move_left:
        if gg.rect.x - left >= 0:
            # Проверка столкновения с объектами stenay, stenay1, stenax и stenax2
            if (
                not gg.rect.colliderect(stenay.rect)
                and not gg.rect.colliderect(stenay1.rect)
                and not gg.rect.colliderect(stenax.rect)
                and not gg.rect.colliderect(stenax2.rect)
            ):
                gg.rect.x -= left
            else:
                move_left = False
                gg.rect.x += 3

    if move_up:
        if gg.rect.y - up >= 0:
            # Проверка столкновения с объектами bl, stenay, stenay1, stenax и stenax2
            if (
                not gg.rect.colliderect(bl.rect)
                and not gg.rect.colliderect(stenay.rect)
                and not gg.rect.colliderect(stenay1.rect)
                and not gg.rect.colliderect(stenax.rect)
                and not gg.rect.colliderect(stenax2.rect)
            ):
                gg.rect.y -= up
            else:
                move_up = False
                gg.rect.y += 3

    if move_down:
        if gg.rect.y + down <= 450:
            # Проверка столкновения с объектами bl, stenay, stenay1, stenax и stenax2
            if (
                not gg.rect.colliderect(bl.rect)
                and not gg.rect.colliderect(stenay.rect)
                and not gg.rect.colliderect(stenay1.rect)
                and not gg.rect.colliderect(stenax.rect)
                and not gg.rect.colliderect(stenax2.rect)
            ):
                gg.rect.y += down
            else:
                move_down = False
                gg.rect.y -= 3

    if gg.rect.y > 500:
        down = 0
    if gg.rect.y < 0:
        down = 0
    if gg.rect.x > 450:
        right = 0
    if gg.rect.x < 0:
        left = 0



    current_time = pygame.time.get_ticks()
    if current_time - last_rotation_time >= rotation_interval:
        if l==1:
            pr.image = pygame.transform.rotate(
                pr.image, 90
            )  # Поворот изображения на 90 градусов
        if m==1:
            pr1.image = pygame.transform.rotate(pr1.image, 90)  # Поворот изображения на 90 градусов
        if k==1:
            pr2.image = pygame.transform.rotate(pr1.image, 90)
        if j==1:
            pr3.image = pygame.transform.rotate(pr3.image, 90)
        last_rotation_time = current_time
        b +=1
        n+=1
        v+=1
        c+=1
        if b==4:
            b=0
        if n==4:
            n=0
        if v==4:
            v=0 
        if c==4:
            c=0   
        # Создание пули при повороте
        if l==1:
            if b==0:
                bulletr = Picture(
                    "F:\python\pylx.png",
                    pr.rect.x + pr.rect.height,
                    pr.rect.y + pr.rect.width - 18,
                )
                bulletsr.append(bulletr)
            if b==1:
                bullet = Picture(
                    "F:\python\pyl.png",
                    pr.rect.x + pyl.rect.height,
                    pr.rect.y - pyl.rect.height,
                )
                bullets.append(bullet)
            if b==2:
                bulletl = Picture(
                    "F:\python\pylx.png",
                    pr.rect.x + pr.rect.height,
                    pr.rect.y + pr.rect.width - 18,
                )
                bulletsl.append(bulletl)
            if b==3:
                bulletd = Picture(
                    "F:\python\pyl.png",
                    pr.rect.x + pyl.rect.width + pyl.rect.height,
                    pr.rect.y + pr.rect.height + pyl.rect.height,
                )
                bulletsd.append(bulletd)

        if m ==1:
            if n==1:
                bulletr = Picture(
                    "F:\python\pylx.png",
                    pr1.rect.x + pr.rect.height +30,
                    pr1.rect.y + 15,
                )
                bulletsr.append(bulletr)
            if n==2:
                bullet = Picture(
                    "F:\python\pyl.png",
                    pr1.rect.x + pyl.rect.height,
                    pr1.rect.y - pyl.rect.height,
                )
                bullets.append(bullet)
            if n==3:
                bulletl = Picture(
                    "F:\python\pylx.png",
                    pr1.rect.x + pr.rect.height,
                    pr1.rect.y + pr.rect.width - 18,
                )
                bulletsl.append(bulletl)
            if n==0:
                bulletd = Picture(
                    "F:\python\pyl.png",
                    pr1.rect.x + pyl.rect.width + pyl.rect.height,
                    pr1.rect.y + pr.rect.height + pyl.rect.height,
                )
                bulletsd.append(bulletd)
        
        if k ==1:
            if v==0:
                bulletr = Picture(
                    "F:\python\pylx.png",
                    pr2.rect.x + pr.rect.height +30,
                    pr2.rect.y + 15,
                )
                bulletsr.append(bulletr)
            if v==1:
                bullet = Picture(
                    "F:\python\pyl.png",
                    pr2.rect.x + pyl.rect.height,
                    pr2.rect.y - pyl.rect.height,
                )
                bullets.append(bullet)
            if v==2:
                bulletl = Picture(
                    "F:\python\pylx.png",
                    pr2.rect.x + pr.rect.height,
                    pr2.rect.y + pr.rect.width - 18,
                )
                bulletsl.append(bulletl)
            if v==3:
                bulletd = Picture(
                    "F:\python\pyl.png",
                    pr2.rect.x + pyl.rect.width + pyl.rect.height,
                    pr2.rect.y + pr.rect.height + pyl.rect.height,
                )
                bulletsd.append(bulletd)


        if j ==1:
            if c==2:
                bulletr = Picture(
                    "F:\python\pylx.png",
                    pr3.rect.x + pr.rect.height +30,
                    pr3.rect.y + 15,
                )
                bulletsr.append(bulletr)
            if c==3:
                bullet = Picture(
                    "F:\python\pyl.png",
                    pr3.rect.x + pyl.rect.height,
                    pr3.rect.y - pyl.rect.height,
                )
                bullets.append(bullet)
            if c==0:
                bulletl = Picture(
                    "F:\python\pylx.png",
                    pr3.rect.x + pr.rect.height,
                    pr3.rect.y + pr.rect.width - 18,
                )
                bulletsl.append(bulletl)
            if c==1:
                bulletd = Picture(
                    "F:\python\pyl.png",
                    pr3.rect.x + pyl.rect.width + pyl.rect.height,
                    pr3.rect.y + pr.rect.height + pyl.rect.height,
                )
                bulletsd.append(bulletd)
        

    score=0
        
    level1.draw()
    pr.draw()
    pr1.draw()
    pr2.draw()
    pr3.draw()
    gg.draw()
    stenay.draw()
    stenay1.draw()
    granizay.draw()
    granizax.draw()
    granizay1.draw()
    granizax1.draw()
    bl.draw()
    stenax.draw()
    stenax2.draw()
    
    # Update and draw the bullets

    for bullet in bullets:
        bullet.rect.y -= p  # Move the bullet upwards
        bullet.draw()  # Draw the bullet

        if (
            bullet.rect.colliderect(stenax.rect)
            or bullet.rect.colliderect(stenax2.rect)
            or bullet.rect.colliderect(bl.rect)
        ):
            bullets.remove(bullet)
        if bullet.rect.colliderect(pr.rect):
           score+=1
           l=0
           pr.image = pygame.image.load("F:\python\pom.png")
           bullets.remove(bullet)
        if bullet.rect.colliderect(gg.rect):
            m=2
            l=2
            k=2
            j=2
            p=0
            move_down=False
            move_left=False
            move_right=False
            move_up=False
            over.draw()
            

    for bulletr in bulletsr:
        bulletr.rect.x += p  # Move the bullet upwards
        bulletr.draw()  # Draw the bullet

        if (
            bulletr.rect.colliderect(stenay.rect)
            or bulletr.rect.colliderect(stenay1.rect)
            or bulletr.rect.colliderect(bl.rect)
        ):
            bulletsr.remove(bulletr)
        if bulletr.rect.colliderect(pr2.rect):
           score+=1
           k=0
           pr2.image = pygame.image.load("F:\python\pom.png")
           bulletsr.remove(bulletr)
        if bulletr.rect.colliderect(gg.rect):
            m=2
            l=2
            k=2
            j=2
            p=0
            move_down=False
            move_left=False
            move_right=False
            move_up=False
            over.draw()
                     

        
    for bulletl in bulletsl:
        bulletl.rect.x -= p  # Move the bullet to the left
        bulletl.draw()

        if (
            bulletl.rect.colliderect(stenay.rect)
            or bulletl.rect.colliderect(stenay1.rect)
            or bulletl.rect.colliderect(bl.rect)
        ):
            bulletsl.remove(bulletl)
        if bulletl.rect.colliderect(pr1.rect):
           score+=1
           m=0
           pr1.image = pygame.image.load("F:\python\pom.png")
           bulletsl.remove(bulletl)
        if bulletl.rect.colliderect(pr3.rect):
           score+=1
           j=0
           pr3.image = pygame.image.load("F:\python\pom.png")
           bulletsl.remove(bulletl)
        if bulletl.rect.colliderect(gg.rect):
            m=2
            l=2
            k=2
            j=2
            p=0
            move_down=False
            move_left=False
            move_right=False
            move_up=False
            over.draw()
            

    for bulletd in bulletsd:
        bulletd.rect.y += p  # Move the bullet downwards
        bulletd.draw()

        if (
            bulletd.rect.colliderect(stenax.rect)
            or bulletd.rect.colliderect(stenax2.rect)
            or bulletd.rect.colliderect(bl.rect)
        ):
            bulletsd.remove(bulletd)
        if bulletd.rect.colliderect(gg.rect):
            m=2
            l=2
            k=2
            j=2
            p=0
            move_down=False
            move_left=False
            move_right=False
            move_up=False
            over.draw()
            
        
            

            
    if m==0 and l==0 and k==0 and j==0:
        level1 = Picture("F:\python\level1_5.png")
        if gg.rect.y<100 and gg.rect.x<50:
            game_over=True
            final=False

    # Remove bullets that have gone off-screen
    bullets = [bullet for bullet in bullets if bullet.rect.y > 0]
    bulletsr = [bulletr for bulletr in bulletsr if bulletr.rect.x > 0]
    bulletsl = [bulletl for bulletl in bulletsl if bulletl.rect.x < 500]
    bulletsd = [bulletd for bulletd in bulletsd if bulletd.rect.y < 500]

    pygame.display.update()
    clock.tick(40)


b=0
n=0
v=0
c=0
m=1
l=1
k=1
j=1

gg = Picture("F:\python\gg.png", 430, 60, 58, 56)
granizay = Picture("F:\python\granizay.png")
granizax = Picture("F:\python\granizax.png")
granizay1 = Picture("F:\python\granizay.png", 495, 0)
granizax1 = Picture("F:\python\granizax.png", 0, 495)
stenay = Picture("F:\python\stenay.png", 182, 174, 5, 159)
stenay1 = Picture("F:\python\stenay1.png", 182, 0, 5, 183)
sofa=Picture("sofa.png",187,192,59,123)
stenax = Picture("F:\python\stenax.png", 340, 181, 257, 5)
stenax2 = Picture("F:\python\stenax.png", 340, 340, 257, 5)
pr = Picture("F:\python\pr.png", 40, 30, 66, 39)
pr1 = Picture("F:\python\pr1.png", 400, 250, 66, 39)
pr2 = Picture("F:\python\pr1.png", 190, 100, 66, 39)
pr3 = Picture("F:\python\pr2.png", 400, 400, 66, 39)

while not final:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            final = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True
                gg.image = pygame.image.load("F:\python\gg_right.png")
            if event.key == pygame.K_a:
                move_left = True
                gg.image = pygame.image.load("F:\python\gg_left.png")
            if event.key == pygame.K_w:
                move_up = True
                gg.image = pygame.image.load("F:\python\gg_up.png")
            if event.key == pygame.K_s:
                move_down = True
                gg.image = pygame.image.load("F:\python\gg_down.png")
            if event.key == pygame.K_SPACE:
                if move_up == True:
                    bullet = Picture(
                        "F:\python\pyl.png",
                        gg.rect.x + gg.rect.height - 15,
                        gg.rect.y - pyl.rect.height,
                    )
                    bullets.append(bullet)
                
                    
                if move_right == True:
                    bulletr = Picture(
                        "F:\python\pylx.png",
                        gg.rect.x + gg.rect.height,
                        gg.rect.y + gg.rect.width - 18,
                    )
                    bulletsr.append(bulletr)
                if move_left == True:
                    bulletl = Picture(
                        "F:\python\pylx.png",
                        gg.rect.x - pyl.rect.width,
                        gg.rect.y + pyl.rect.height,
                    )
                    bulletsl.append(bulletl)
                if move_down == True:
                    bulletd = Picture(
                        "F:\python\pyl.png",
                        gg.rect.x + pyl.rect.width,
                        gg.rect.y + gg.rect.width,
                    )
                    bulletsd.append(bulletd)
                    

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
                move_down = False
    
    if move_right:
        if gg.rect.x + right <= 450:
            # Проверка столкновения с объектами bl, stenay, stenay1, stenax и stenax2
            if (
                not gg.rect.colliderect(sofa.rect)
                and not gg.rect.colliderect(stenay.rect)
                and not gg.rect.colliderect(stenay1.rect)
                and not gg.rect.colliderect(stenax.rect)
                and not gg.rect.colliderect(stenax2.rect)
            ):
                gg.rect.x += right
            else:
                move_right = False
                gg.rect.x -= 3

    if move_left:
        if gg.rect.x - left >= 0:
            # Проверка столкновения с объектами stenay, stenay1, stenax и stenax2
            if (not gg.rect.colliderect(sofa.rect)
                and not gg.rect.colliderect(stenay.rect)
                and not gg.rect.colliderect(stenay1.rect)
                and not gg.rect.colliderect(stenax.rect)
                and not gg.rect.colliderect(stenax2.rect)
            ):
                gg.rect.x -= left
            else:
                move_left = False
                gg.rect.x += 3

    if move_up:
        if gg.rect.y - up >= 0:
            # Проверка столкновения с объектами bl, stenay, stenay1, stenax и stenax2
            if (
                not gg.rect.colliderect(sofa.rect)
                and not gg.rect.colliderect(stenay.rect)
                and not gg.rect.colliderect(stenay1.rect)
                and not gg.rect.colliderect(stenax.rect)
                and not gg.rect.colliderect(stenax2.rect)
            ):
                gg.rect.y -= up
            else:
                move_up = False
                gg.rect.y += 3

    if move_down:
        if gg.rect.y + down <= 450:
            # Проверка столкновения с объектами bl, stenay, stenay1, stenax и stenax2
            if (
                not gg.rect.colliderect(sofa.rect)
                and not gg.rect.colliderect(stenay.rect)
                and not gg.rect.colliderect(stenay1.rect)
                and not gg.rect.colliderect(stenax.rect)
                and not gg.rect.colliderect(stenax2.rect)
            ):
                gg.rect.y += down
            else:
                move_down = False
                gg.rect.y -= 3

    if gg.rect.y > 500:
        down = 0
    if gg.rect.y < 0:
        down = 0
    if gg.rect.x > 450:
        right = 0
    if gg.rect.x < 0:
        left = 0



    current_time = pygame.time.get_ticks()
    if current_time - last_rotation_time >= rotation_interval:
        if l==1:
            pr.image = pygame.transform.rotate(
                pr.image, 90
            )  # Поворот изображения на 90 градусов
        if m==1:
            pr1.image = pygame.transform.rotate(pr1.image, 90)  # Поворот изображения на 90 градусов
        if k==1:
            pr2.image = pygame.transform.rotate(pr1.image, 90)
        if j==1:
            pr3.image = pygame.transform.rotate(pr3.image, 90)
        last_rotation_time = current_time
        b +=1
        n+=1
        v+=1
        c+=1
        if b==4:
            b=0
        if n==4:
            n=0
        if v==4:
            v=0 
        if c==4:
            c=0   
        # Создание пули при повороте
        if l==1:
            if b==0:
                bulletr = Picture(
                    "F:\python\pylx.png",
                    pr.rect.x + pr.rect.height,
                    pr.rect.y + pr.rect.width - 18,
                )
                bulletsr.append(bulletr)
            if b==1:
                bullet = Picture(
                    "F:\python\pyl.png",
                    pr.rect.x + pyl.rect.height,
                    pr.rect.y - pyl.rect.height,
                )
                bullets.append(bullet)
            if b==2:
                bulletl = Picture(
                    "F:\python\pylx.png",
                    pr.rect.x + pr.rect.height,
                    pr.rect.y + pr.rect.width - 18,
                )
                bulletsl.append(bulletl)
            if b==3:
                bulletd = Picture(
                    "F:\python\pyl.png",
                    pr.rect.x + pyl.rect.width + pyl.rect.height,
                    pr.rect.y + pr.rect.height + pyl.rect.height,
                )
                bulletsd.append(bulletd)

        if m ==1:
            if n==1:
                bulletr = Picture(
                    "F:\python\pylx.png",
                    pr1.rect.x + pr.rect.height +30,
                    pr1.rect.y + 15,
                )
                bulletsr.append(bulletr)
            if n==2:
                bullet = Picture(
                    "F:\python\pyl.png",
                    pr1.rect.x + pyl.rect.height,
                    pr1.rect.y - pyl.rect.height,
                )
                bullets.append(bullet)
            if n==3:
                bulletl = Picture(
                    "F:\python\pylx.png",
                    pr1.rect.x + pr.rect.height,
                    pr1.rect.y + pr.rect.width - 18,
                )
                bulletsl.append(bulletl)
            if n==0:
                bulletd = Picture(
                    "F:\python\pyl.png",
                    pr1.rect.x + pyl.rect.width + pyl.rect.height,
                    pr1.rect.y + pr.rect.height + pyl.rect.height,
                )
                bulletsd.append(bulletd)
        
        if k ==1:
            if v==0:
                bulletr = Picture(
                    "F:\python\pylx.png",
                    pr2.rect.x + pr.rect.height +30,
                    pr2.rect.y + 15,
                )
                bulletsr.append(bulletr)
            if v==1:
                bullet = Picture(
                    "F:\python\pyl.png",
                    pr2.rect.x + pyl.rect.height,
                    pr2.rect.y - pyl.rect.height,
                )
                bullets.append(bullet)
            if v==2:
                bulletl = Picture(
                    "F:\python\pylx.png",
                    pr2.rect.x + pr.rect.height,
                    pr2.rect.y + pr.rect.width - 18,
                )
                bulletsl.append(bulletl)
            if v==3:
                bulletd = Picture(
                    "F:\python\pyl.png",
                    pr2.rect.x + pyl.rect.width + pyl.rect.height,
                    pr2.rect.y + pr.rect.height + pyl.rect.height,
                )
                bulletsd.append(bulletd)


        if j ==1:
            if c==2:
                bulletr = Picture(
                    "F:\python\pylx.png",
                    pr3.rect.x + pr.rect.height +30,
                    pr3.rect.y + 15,
                )
                bulletsr.append(bulletr)
            if c==3:
                bullet = Picture(
                    "F:\python\pyl.png",
                    pr3.rect.x + pyl.rect.height,
                    pr3.rect.y - pyl.rect.height,
                )
                bullets.append(bullet)
            if c==0:
                bulletl = Picture(
                    "F:\python\pylx.png",
                    pr3.rect.x + pr.rect.height,
                    pr3.rect.y + pr.rect.width - 18,
                )
                bulletsl.append(bulletl)
            if c==1:
                bulletd = Picture(
                    "F:\python\pyl.png",
                    pr3.rect.x + pyl.rect.width + pyl.rect.height,
                    pr3.rect.y + pr.rect.height + pyl.rect.height,
                )
                bulletsd.append(bulletd)
        

    score=0
        
    level2.draw()
    pr.draw()
    pr1.draw()
    pr2.draw()
    pr3.draw()
    gg.draw()
    sofa.draw()
    stenay.draw()
    stenay1.draw()
    granizay.draw()
    granizax.draw()
    granizay1.draw()
    granizax1.draw()
    stenax.draw()
    stenax2.draw()
    
    # Update and draw the bullets

    for bullet in bullets:
        bullet.rect.y -= p  # Move the bullet upwards
        bullet.draw()  # Draw the bullet

        if (
            bullet.rect.colliderect(stenax.rect)
            or bullet.rect.colliderect(stenax2.rect)
            or bullet.rect.colliderect(sofa.rect)
        ):
            bullets.remove(bullet)
        if bullet.rect.colliderect(pr.rect):
           score+=1
           l=0
           pr.image = pygame.image.load("F:\python\pom.png")
           bullets.remove(bullet)
        if bullet.rect.colliderect(gg.rect):
            m=2
            l=2
            k=2
            j=2
            p=0
            move_down=False
            move_left=False
            move_right=False
            move_up=False
            over.draw()
            

    for bulletr in bulletsr:
        bulletr.rect.x += p  # Move the bullet upwards
        bulletr.draw()  # Draw the bullet

        if (
            bulletr.rect.colliderect(stenay.rect)
            or bulletr.rect.colliderect(stenay1.rect)
            or bulletr.rect.colliderect(sofa.rect)
        ):
            bulletsr.remove(bulletr)
        if bulletr.rect.colliderect(pr2.rect):
           k=0
           pr2.image = pygame.image.load("F:\python\pom.png")
           bulletsr.remove(bulletr)
        if bulletr.rect.colliderect(pr.rect):
           l=0
           pr.image = pygame.image.load("F:\python\pom.png")
           bulletsr.remove(bulletr)
        if bulletr.rect.colliderect(pr1.rect):
           m=0
           pr1.image = pygame.image.load("F:\python\pom.png")
           bulletsr.remove(bulletr)
        if bulletr.rect.colliderect(pr3.rect):
           j=0
           pr3.image = pygame.image.load("F:\python\pom.png")
           bulletsr.remove(bulletr)
        if bulletr.rect.colliderect(gg.rect):
            m=2
            l=2
            k=2
            j=2
            p=0
            move_down=False
            move_left=False
            move_right=False
            move_up=False
            over.draw()
                     

        
    for bulletl in bulletsl:
        bulletl.rect.x -= p  # Move the bullet to the left
        bulletl.draw()

        if (
            bulletl.rect.colliderect(stenay.rect)
            or bulletl.rect.colliderect(stenay1.rect)
            or bulletl.rect.colliderect(sofa.rect)
        ):
            bulletsl.remove(bulletl)
        if bulletl.rect.colliderect(pr1.rect):
           score+=1
           m=0
           pr1.image = pygame.image.load("F:\python\pom.png")
           bulletsl.remove(bulletl)
        if bulletl.rect.colliderect(pr3.rect):
           score+=1
           j=0
           pr3.image = pygame.image.load("F:\python\pom.png")
           bulletsl.remove(bulletl)
        if bulletl.rect.colliderect(pr.rect):
           score+=1
           l=0
           pr.image = pygame.image.load("F:\python\pom.png")
           bulletsl.remove(bulletl)
        if bulletl.rect.colliderect(pr2.rect):
           score+=1
           k=0
           pr2.image = pygame.image.load("F:\python\pom.png")
           bulletsl.remove(bulletl)   
        if bulletl.rect.colliderect(gg.rect):
            m=2
            l=2
            k=2
            j=2
            p=0
            move_down=False
            move_left=False
            move_right=False
            move_up=False
            over.draw()
            

    for bulletd in bulletsd:
        bulletd.rect.y += p  # Move the bullet downwards
        bulletd.draw()

        if (
            bulletd.rect.colliderect(stenax.rect)
            or bulletd.rect.colliderect(stenax2.rect)
            or bulletd.rect.colliderect(sofa.rect)
        ):
            bulletsd.remove(bulletd)
        if bulletd.rect.colliderect(gg.rect):
            m=2
            l=2
            k=2
            j=2
            p=0
            move_down=False
            move_left=False
            move_right=False
            move_up=False
            over.draw()
            
        
            

            
    if m==0 and l==0 and k==0 and j==0:
        win.draw()

    # Remove bullets that have gone off-screen
    bullets = [bullet for bullet in bullets if bullet.rect.y > 0]
    bulletsr = [bulletr for bulletr in bulletsr if bulletr.rect.x > 0]
    bulletsl = [bulletl for bulletl in bulletsl if bulletl.rect.x < 500]
    bulletsd = [bulletd for bulletd in bulletsd if bulletd.rect.y < 500]

    pygame.display.update()
    clock.tick(40)
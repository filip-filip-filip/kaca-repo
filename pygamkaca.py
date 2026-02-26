import pygame
import random
import time

pygame.init()

visina, dolzina = 500,500


#Napiši snake-game v pygamu
#koda od prej ti lahko sliži za inspiracijo (npr dolzina kace s kvadratki -> to pride prav)

#za projekt naredite github repo, in spremembe sproti comitatje addajte in pushajte
#na koncu morajo biti v repozitoriju vsaj 3 vecji commiti

#1. dodatna naloga:
#naredi branch "izgled"
#v tem brancu naredi logiko, da ko igra tece, lahko pritisnes gumb "space" kar celotni kaci nastavi nakljucno barvo

#2. dodatna naloga:
#naredi branch "multiplayer"
#v tem branchu naredi logiko, da sta na zacetku igre 2 kaci, ena se upravlja z wasd, druga z gumbi s puscicami
#ce se aca zabije vase, v drugo kaco ali v steno, izgubi

#3. dodatna naloga
#naredi megre obeh branchov

ekran = pygame.display.set_mode((visina,dolzina))
bela = (255,255,255)
črna = (0,0,0)
rdeča = (255,0,0)
zelena = (0,255,0)
modra = (0,0,255)

clock = pygame.time.Clock()
smer = "desno"
speed = 50
run = True
kvad1 = pygame.Rect(0,0,50,50)
kvad2 = pygame.Rect(0,0,50,50)
kvad3 = pygame.Rect(random.randint(0,500),random.randint(0,500),50,50)
lenght = 3
prejsnji = []
koordkac = []


obratzanke = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text2 = font.render("score: " + str(lenght+1), True, črna)
textRect2 = text2.get_rect()
textRect2.center = (85, 50)


font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('KONEC!!!!!!!      D:', True, rdeča, bela)
textRect = text.get_rect()
textRect.center = (250, 250)
def konc():
    run=False
    ekran.blit(text,textRect)

    pygame.display.update()
    time.sleep(3)
    
    pygame.quit()
    



pygame.draw.rect(ekran,(0,255,0),kvad3)

while run:
    text2 = font.render("score: " + str(lenght+1), True, črna, bela)



    xy = [kvad1.x,kvad1.y]
    
    
    
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()

    

    ekran.fill((255,255,255))
    
    
    pygame.draw.rect(ekran,(0,255,0),kvad1)
    for i in koordkac:
        if koordkac.count(i) > 1:
            konc()
    #premikanje
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]:
        smer = "dol"
    if pressed[pygame.K_UP]:
        smer = "gor"
    if pressed[pygame.K_LEFT]:
        smer = "levo"
    if pressed[pygame.K_RIGHT]:
        smer = "desno"
    
    pygame.draw.rect(ekran,(255,0,0),kvad3)

    if obratzanke == 30:
        if smer == "desno":
            kvad1.x = kvad1.x + speed
        if smer == "levo":
            kvad1.x = kvad1.x - speed
        if smer == "gor":
            kvad1.y = kvad1.y - speed
        if smer == "dol":
            kvad1.y = kvad1.y + speed
        prejsnji.append(xy)
        koordkac = prejsnji[-lenght:]
        


    if kvad1.colliderect(kvad3):
        kvad3 = pygame.Rect(random.randint(0,500),random.randint(0,500),50,50)
        lenght +=1

    for i in koordkac:
        kvad2 = pygame.Rect(i[0],i[1],50,50)
        pygame.draw.rect(ekran,(0,255,0),kvad2)

    
    if kvad1.x > 450:
        konc()
    if kvad1.x < 0:
        konc()
    if kvad1.y > 450:
        konc()
    if kvad1.y < 0:
        konc()
    for i in koordkac:
        if koordkac.count(i) > 1:
            konc()


        
    obratzanke += 1
    if obratzanke == 31:
        obratzanke = 0

    ekran.blit(text2,textRect2)
    pygame.display.update()
    

    
    

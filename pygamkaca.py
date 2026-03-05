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
smer2 = "levo"
speed = 50
run = True
jabb = [50,100,150,200,250,300,350,400,450]
kvad1 = pygame.Rect(0,0,50,50)
kvad2 = pygame.Rect(0,0,50,50)
kvad3 = pygame.Rect(random.choice(jabb),random.choice(jabb),50,50)
kvad4 = pygame.Rect(200,300,50,50)

lenght = 3
prejsnji = []
koordkac = []
lenght2 = 3
prejsnji2 = []
koordkac2 = []


obratzanke = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text2 = font.render("score: " + str(lenght+1), True, črna, (255,255,255))
text2.set_alpha(127)
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
barva = zelena


while run:



    for i in koordkac:
        if 0 < koordkac2.count(i):
            konc()
    

    
    obratzanke += 1
    text2 = font.render("score: " + str(lenght+1), True, črna, bela)



    xy = [kvad1.x,kvad1.y]
    xy2 = [kvad4.x,kvad4.y]
    
    
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()

    

    ekran.fill((255,255,255))
    
    
    pygame.draw.rect(ekran,barva,kvad1)
    for i in koordkac:
        if koordkac.count(i) > 1:
            konc()

    for i in koordkac2:
        if koordkac2.count(i) > 6:
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

    if pressed[pygame.K_SPACE]:
        barva  = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        
    if pressed[pygame.K_s]:
        smer2 = "dol"
    if pressed[pygame.K_w]:
        smer2 = "gor"
    if pressed[pygame.K_a]:
        smer2 = "levo"
    if pressed[pygame.K_d]:
        smer2 = "desno"

    
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

        if smer2 == "desno":
            kvad4.x = kvad4.x + speed
            
        if smer2 == "levo":
            kvad4.x = kvad4.x - speed
            
        if smer2 == "gor":
            kvad4.y = kvad4.y - speed
            
        if smer2 == "dol":
            kvad4.y = kvad4.y + speed
            
        prejsnji2.append([kvad4.x,kvad4.y])
        koordkac2 = prejsnji2[-lenght2:]
        


    if kvad1.colliderect(kvad3):
        kvad3 = pygame.Rect(random.choice(jabb),random.choice(jabb),50,50)
        lenght +=1

    if kvad4.colliderect(kvad3):
        kvad3 = pygame.Rect(random.choice(jabb),random.choice(jabb),50,50)
        lenght2 +=1

    for i in koordkac:
        kvad2 = pygame.Rect(i[0],i[1],50,50)
        pygame.draw.rect(ekran,barva,kvad2)

    for i in koordkac2:
        kvad4 = pygame.Rect(i[0],i[1],50,50)
        pygame.draw.rect(ekran,barva,kvad4)

    
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
            
    if kvad4.x > 450:
        konc()
    if kvad4.x < 0:
        konc()
    if kvad4.y > 450:
        konc()
    if kvad4.y < 0:
        konc()
# NE DELLLLLLLLLLALLLLALALLALALALLALALALLALALALLALALLALALALLLLLLLLLLLLLLLL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! takoj neha
      
    for i in koordkac2:
        if koordkac2.count(i) > 6:
            konc()


        
  
    if obratzanke == 31:
        obratzanke = 0

    ekran.blit(text2,textRect2)
    pygame.display.update()
    

    
    

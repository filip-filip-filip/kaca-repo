import pygame
import random
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
lenght = 7
prejsnji = []
koordkac = []

obratzanke = 0

def konc():
    run=False
    pygame.quit()





while run:




    xy = [kvad1.x,kvad1.y]
    
    
    pygame.display.update()
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()

    

    ekran.fill((255,255,255))
    
    


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
    
    pygame.draw.rect(ekran,(0,255,0),kvad1)

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
        koordkac = prejsnji[-lenght:-1]
        print(prejsnji)
        print(koordkac)


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

    obratzanke += 1
    if obratzanke == 31:
        obratzanke = 0 
    

    
    

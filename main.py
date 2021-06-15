import random
import pygame

pygame.init()
x = 336
y = 400
pos_x = random.randrange(260, 450, 50)
pos_y = 200
velocidade = 10
velocidade_carros = velocidade
y_tela = -1387

fundo = pygame.image.load('data/pista.png')

carro_amarelo = pygame.image.load('data/carro_amarelo.png')
carro_azul = pygame.image.load('data/carro_azul.png')
carro_azul_rosa = pygame.image.load('data/carro_azul_rosa.png')
carro_dourado = pygame.image.load('data/carro_dourado.png')
carro_prata = pygame.image.load('data/carro_prata.png')
carro_verde = pygame.image.load('data/carro_verde.png')
carro_vermelho = pygame.image.load('data/carro_vermelho.png')
carro_vermelho_amarelo = pygame.image.load('data/carro_vermelho_amarelo.png')

carro_principal = carro_vermelho_amarelo

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Game')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if (y <= -157):
        y = -157
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if (y >= 457):
        y = 457
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if (x >= 450):
        x = 450
    if comandos[pygame.K_LEFT]:
        x -= velocidade
    if (x <= 260):
        x = 260
    if (pos_y >= 757):
        pos_y = -157
        pos_x = random.randrange(260, 450, 50)
        velocidade_carros += 1
    if (y_tela >= 0):
        y -= velocidade
        pos_y -= 10
        if (pos_y <= -157):
            pos_y = -157
        y_tela = 0
        velocidade_carros = 0
    pos_y += velocidade_carros
    y_tela += velocidade_carros / 2

    janela.blit(fundo, (0, y_tela))
    janela.blit(carro_principal, (x, y))
    janela.blit(carro_azul, (pos_x, pos_y))
    pygame.display.update()

pygame.quit()

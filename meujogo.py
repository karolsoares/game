# Aluna: Karoline Zantedeschi Soares
#1 Semestre: Ciências da Computação

import pygame 
import os
from PIL import Image
import random
import time 

pygame.init()

largura= 870
altura= 670

display = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Homem pedra by Karol")
fps= pygame.time.Clock()

#[ini] redimensionar image
def redimensionar(input_dir, output_dir, indice, larg, alt): # coloca-se o diretório, a pasta, o indice para acahr na lista, qual largura e altura a imagem terá
    lista= os.listdir(input_dir) # coloca as imagens que forem passasdas pela inupt_dir em listas
    imagem= Image.open(os.path.join(input_dir, lista[indice]))# a tupla pega o diretorio e o indici da imagem, e depois de redimencionada cria uma nova imagem com as novas larg e alt
    redimensionada= imagem.resize((larg, alt))
    redimensionada.save(os.path.join(output_dir, lista[indice]))#devolve a imagem redimensionada 

diretorio= '/Users\karo1\OneDrive\Área de Trabalho\CODES PYTHON\Gameeducacional\imagens'
#[fim] redimensionar image

# [ini] variaveis das imagens
icone= pygame.image.load("imagens/icone.png")
pygame.display.set_icon(icone)
redimensionar(diretorio, 'imagens', 1, 50, 50 )#redimensionar icone
fundo= pygame.image.load("imagens/fundo3.jpg")
personagem= pygame.image.load("imagens/personagem.png")
redimensionar(diretorio, 'imagens', 3, 184, 234 )# redimensionar personagem
moeda= pygame.image.load("imagens/moedinha.png")
moeda1= pygame.image.load("imagens/moedinha.png")
moeda2= pygame.image.load("imagens/moedinha.png")
moeda3= pygame.image.load("imagens/moedinha.png")
moeda4= pygame.image.load("imagens/moedinha.png")
redimensionar(diretorio, 'imagens', 2, 70, 70 )# redimensionar moeda
# [fim] variaveis das imagens

#[ini] cores
preto= (0, 0, 0)
azul= (50, 130, 150)
chao= (100, 80, 60)
branco= (255, 255, 255)
#[fim] cores

def text_objects(texto, fonte):
    textSurface= fonte.render(texto, True, preto)
    return textSurface, textSurface.get_rect()

def message_display(text):
    fonte= pygame.font.Font("freesansbold.ttf", 20)
    TextSurf, TextRect= text_objects(text, fonte)
    TextRect.center= ((largura/15), (altura/15))
    display.blit(TextSurf, TextRect)

def ponto():
    message_display("ponto:")



def jogo():
    #[ini] posição dos elementos
    personagemPosicaoX= largura * 0.05
    posicaoInicialX= largura * 0.05
    personagemLargura= 184
    personagemPosicaoY= altura * 0.58
    posicaoInicialY=  altura * 0.58
    moedaPosicaoX= largura * 0.40
    moedaPosicaoY=  altura * 0.75
    #[fim]posição dos elementos

    movimentoX= 0
    movimentoY= 0
    while True:
        #[ini] interação do usuário
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
        #[fim] interação do usuário

        #[ini] movimento 
            if evento.type == pygame.KEYDOWN:# quando pressionada
                if evento.key == pygame.K_LEFT:
                    movimentoX= -2
                elif evento.key == pygame.K_RIGHT:
                    movimentoX= 2
                if evento.key == pygame.K_SPACE:  #movimenta pra cima 
                    movimentoY= -8
                elif evento.key == pygame.K_DOWN: #movimenta pra baixo
                    movimentoY= 5
            if evento.type == pygame.KEYUP: #quando solta
                movimentoX= 0
                movimentoY=0

        personagemPosicaoX = personagemPosicaoX + movimentoX
        personagemPosicaoY= personagemPosicaoY + movimentoY
        if personagemPosicaoY > posicaoInicialY:
            personagemPosicaoY= posicaoInicialY
        elif personagemPosicaoY  < posicaoInicialY - 16:
            personagemPosicaoY = personagemPosicaoY + 8
        #[fim] movimento

        #[ini] verifica posicao de imagem como se fosse passar a tela
        if personagemPosicaoX > 750:
            personagemPosicaoX = largura * -0.05
            moedaPosicaoX= 5

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                if personagemPosicaoX == largura * -0.05:
                    personagemPosicaoX= 750
        #[fim] verifica posicao de imagem como se fosse passar a tela      
        
        #[ini] pontos e colisao
        if personagemPosicaoX + personagemLargura / 1.5 > moedaPosicaoX:
            moedaPosicaoX += moedaPosicaoX # ERRO
            ponto()

        
            
        #[fim] pontos e colisao

        # [ini] imagens na tela
        display.fill(branco)
        display.blit(fundo, (0, 0))
        display.blit(personagem, (personagemPosicaoX, personagemPosicaoY))
        display.blit(moeda, (moedaPosicaoX, moedaPosicaoY)) 
        
        #[fim] imagnes na tela

        pygame.display.update()

        fps.tick(60)

jogo()
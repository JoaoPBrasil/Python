import pygame
import time

pygame.init()

largura, altura = 400, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Simulador de Semáforo")

verde_img = pygame.image.load("verde.png")
amarelo_img = pygame.image.load("amarelo.png")
vermelho_img = pygame.image.load("vermelho.png")

def exibir_imagem(imagem):
    tela.fill((0, 0, 0))  # Preencher a tela com a cor preta
    tela.blit(imagem, (100, 150))  # Exibir a imagem no centro da tela
    pygame.display.update()

def main():
    rodando = True
    clock = pygame.time.Clock()

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        exibir_imagem(verde_img)
        time.sleep(2)  # Espera de 2 segundos

        exibir_imagem(amarelo_img)
        time.sleep(1)  # Espera de 1 segundo

        exibir_imagem(vermelho_img)
        time.sleep(2)  # Espera de 2 segundos

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

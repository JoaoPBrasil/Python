import pygame
import time

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

notas = {
    'C': 'som/Do.mp3',  # Dó
    'D': 'som/Re.mp3',  # Ré
    'E': 'som/Mi.mp3',  # Mi
    'F': 'som/Fa.mp3',  # Fá
    'G': 'som/Sol.mp3', # Sol
    'A': 'som/La.mp3',  # Lá
    'B': 'som/Si.mp3',  # Si
}

teclas = {
    pygame.K_a: 'C',  # 'A' -> Dó
    pygame.K_s: 'D',  # 'S' -> Ré
    pygame.K_d: 'E',  # 'D' -> Mi
    pygame.K_f: 'F',  # 'F' -> Fá
    pygame.K_g: 'G',  # 'G' -> Sol
    pygame.K_h: 'A',  # 'H' -> Lá
    pygame.K_j: 'B',  # 'J' -> Si
}

largura, altura = 700, 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Piano Interativo")

sons = {nota: pygame.mixer.Sound(caminho) for nota, caminho in notas.items()}

def desenhar_teclas():
    tela.fill(WHITE)
    largura_tecla = largura // 7  # Dividir a tela em 7 teclas

    for i, tecla in enumerate(teclas):
        x = i * largura_tecla
        cor = GREEN if teclas[tecla] == 'C' else RED if teclas[tecla] == 'D' else \
            BLUE if teclas[tecla] == 'E' else YELLOW if teclas[tecla] == 'F' else \
            ORANGE if teclas[tecla] == 'G' else PURPLE if teclas[tecla] == 'A' else WHITE
        pygame.draw.rect(tela, cor, (x, 0, largura_tecla, altura))
    
    pygame.display.update()

def tocar_nota(nota):
    if nota in sons:
        sons[nota].play()

def main():
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                for i, tecla in enumerate(teclas):
                    x = i * (largura // 7)
                    if x <= evento.pos[0] <= x + (largura // 7):
                        tocar_nota(teclas[tecla])
            elif evento.type == pygame.KEYDOWN:
                
                if evento.key in teclas:
                    tocar_nota(teclas[evento.key])

        desenhar_teclas()  # Atualiza as teclas desenhadas na tela

        pygame.display.update()  # Atualiza a tela
        pygame.time.Clock().tick(60)  # Limita a taxa de atualização

    pygame.quit()

if __name__ == "__main__":
    main()

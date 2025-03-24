import pygame
import time

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

notas = {
    'Do': 'som/Do.mp3',
    'Re': 'som/Re.mp3',
    'Mi': 'som/Mi.mp3',
    'Fa': 'som/Fa.mp3',
    'Sol': 'som/Sol.mp3',
    'La': 'som/La.mp3',
    'Si': 'som/Si.mp3'
}

cores = {
    'Do': RED,
    'Re': GREEN,
    'Mi': BLUE,
    'Fa': YELLOW,
    'Sol': (255, 165, 0),  # Laranja
    'La': (255, 105, 180),  # Rosa
    'Si': (0, 255, 255)     # Ciano
}

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Notas Musicais")

def tocar_nota(nota):
    som = pygame.mixer.Sound(notas[nota])
    som.play()

def exibir_retangulo(cor):
    tela.fill(WHITE)  # Preencher o fundo com branco
    pygame.draw.rect(tela, cor, pygame.Rect(300, 200, 200, 100))  # Retângulo na tela
    pygame.display.update()

def main():
    rodando = True
    clock = pygame.time.Clock()

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
        
        for nota, cor in cores.items():
            exibir_retangulo(cor)
            tocar_nota(nota)
            time.sleep(1)  # Esperar 1 segundo para a próxima nota

        pygame.time.delay(1000)  # Esperar 1 segundo antes de repetir o ciclo

    pygame.quit()

if __name__ == "__main__":
    main()

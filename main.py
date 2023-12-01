import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('baboon.jpg')

# Dividir a imagem em canais RGB
canal_azul, canal_verde, canal_vermelho = cv2.split(imagem)

# Calcular a média dos pixels em cada canal RGB
media_R = np.mean(canal_vermelho)
media_G = np.mean(canal_verde)
media_B = np.mean(canal_azul)

# Converter a imagem para o modelo de cores CMY
imagem_cmy = 255 - imagem

# Dividir a imagem CMY em canais
canal_ciano, canal_magenta, canal_amarelo = cv2.split(imagem_cmy)

# Calcular a média dos pixels em cada canal CMY
media_C = np.mean(canal_ciano)
media_M = np.mean(canal_magenta)
media_Y = np.mean(canal_amarelo)

# Exibir os resultados
print(f'Média R: {media_R:.2f}')
print(f'Média G: {media_G:.2f}')
print(f'Média B: {media_B:.2f}')
print(f'Média C: {media_C:.2f}')
print(f'Média M: {media_M:.2f}')
print(f'Média Y: {media_Y:.2f}')

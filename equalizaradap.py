import cv2
from matplotlib import image
import numpy as np
import argparse
ap=argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='informar caminho de entrada da imagem a ser ocr')
args=vars(ap.parse_args())
image=cv2.imread (args['image'],cv2.IMREAD_GRAYSCALE)
res=cv2.resize(image, dsize=(1000,1000), interpolation=cv2.INTER_CUBIC)

kernel = np.array([[-1,-1,-1], [-1,9.1,-1], [-1,-1,-1]])
img1= cv2.filter2D(res, -2, kernel)
#blur=cv2.GaussianBlur(img,(5,5),0)
ret3, limiar3=cv2.threshold(img1,110,260, cv2.THRESH_BINARY)

clahe= cv2.createCLAHE (clipLimit=2.0, tileGridSize=(9,9))
cl1=clahe.apply(limiar3)

#status= cv2.imwrite('/home/dev-07/Downloads/testes1.jpeg',limiar3)
#print ('imagem salva no sistema', status)
cv2.namedWindow ('carregando a imagem')
cv2.imshow('carregando a imagem', limiar3) 
k=cv2.waitKey() 

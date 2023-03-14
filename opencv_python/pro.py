import cv2 #importando a biblioteca 
img = cv2.imread('glc_img/glaucoma_1.jpg') #lendo a imagem 
rows, cols, _ = img.shape
#************************
print("Rows", rows)
print("Cols", cols)
#************************
#Cut image 
cut_image = img[80: 130, 0: 210]

cv2.imshow("Imagem cortada", cut_image)
cv2.imshow("imagem", img)
cv2.waitKey(0)

#cv2.imshow('Imagem', img) #printando a imagem 
#cv2.waitKey(0) #comando pra deixar a imagem estável 

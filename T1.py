# Nome: Luis Paulo Falchi Justino
# NUSP: 8937479

import cv2
import numpy as np
import sys

# Given a function, frequency and size, draws to a file and shows it on the screen
# the output.
def draw(filename, N, f, Q):
    pts = np.zeros([N,N], np.float)

    # Fills the points array
    for i in np.arange(N):
        for j in np.arange(N):
            if f == 1:
                pts[i][j] = (255**2*(i + j))/(N*N)
            elif f == 2:
                pts[i][j] = np.abs(np.sin(i/Q))*255
            elif f == 3:
                pts[i][j] = (((i/Q)**2 + 2*(j/Q)**2)*255)%256
            elif f == 4:
                pts[i][j] = np.random.randint(0, 255)
            else:
                print("Invalid function.")

    print(pts)

    cv2.imwrite(filename, pts)
    cv2.imshow('teste', pts)
    cv2.waitKey(0)

draw(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]))

''' Funções de teste:

draw('img1.png', 512, 1, 1)
draw('img2.png', 512, 2, 15)
draw('img3.png', 512, 3, 290)
draw('img4.png', 512, 4, 1)
'''
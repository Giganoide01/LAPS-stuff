import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
import psnr 
#import ssim

def psnr(ref, teste):
    
    # RFZ: precisa converter aqui para grayscale (?)
    l = plt.imread(ref)#[:,:,1]
    #print(l.shape)

    #f = open('arquivo.txt','w')
    #f.write(ref + )
    #for i in range(1, 9):

    k = plt.imread(teste)#[:,:,1]
    psrn = psnr.psnr(l, k)

    return psnr

def ssim (ref, teste):
    
    j = 0
    a = plt.imread(ref)[:,:,j]
    b = plt.imread(teste)[:,:,j]
    ssim0 = psnr.msim(a, b)

    j = j+1
    a = plt.imread(ref)[:,:,j]
    b = plt.imread(teste)[:,:,j]
    ssim1 = psnr.msim(a, b)

    j = j+1
    a = plt.imread(ref)[:,:,j]
    b = plt.imread(teste)[:,:,j]
    ssim2 = psnr.msim(a, b)
    ssim = (ssim0 + ssim1 + ssim2)/3
    return ssim
        #f.write('img' + str(i) + ' ' + psrn2 + ' ' + ssim2 + '\n')
    
        #i  = i + 1

    #f.close()
    #arquivo = open('arquivo.txt', 'r')
    #print(arquivo.readlines())
    #arquivo.close()

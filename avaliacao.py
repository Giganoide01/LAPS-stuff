import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pearson
import spearman
import outlier
import regressaoLinear
import levenbergMarquart
import anova

def avaliacao(metrica, arq):
    
    arquivo = open('arquivo.txt', 'r')              #abrir o arquivo
    subjectscores = open(arq, 'r')  #ler arquivo

    conteudo_texto = arquivo.read()                 #
    conteudo_texto1 = subjectscores.read()          #

    a = conteudo_texto.split('\n')                  # separar por quebra de linha
    c = a[:-1]                                       #tirar ultimo elemento

    aa = conteudo_texto1.split('\n')                #separar por espaco
    cc = aa[:-1]


    arquivo.close()                                 #fechar arquivo
    subjectscores.close()

    x = np.array([])
    y = np.array([])
    l = np.array([])
    total_pontos = 0
                                                #plotar grafico
    for i in xrange(0, len(cc)):
        w = cc[i].split('\t')                           #buscar linha
        q = len(w)                                  #tamanho da linha
        ww = w[2:q]                                 #tirar primeiro elemento
        total_pontos = len(ww) + total_pontos
        b = c[i].split(';')                         #separar por ,
        psnr = b[metrica]                                 #buscar psnr
        h = np.asarray(ww[0:13])                    #criando vetor com media de mos
        t = h.astype(np.float)
        v = np.mean(t)
        if (psnr !=str('inf')):
            x = np.insert(x,0,psnr)                 #guardar
            y = np.insert(y,0,v)                    #vetor media mos
        r = float(psnr)                             #converter para float
        p = q-1.0                                   #tamanho da linha menos o 1 item
        d = np.zeros(p)                             #criar vetor de 0s
        dd = d + r                                  #criar vetor de psnr do tm d mos
        #plt.plot(dd, ww, 'o', color='r')           #plotar psnr x mos
    
   
        out = outlier.outlier(t)                    #calcular outliers
        l = np.append(l, out)                       #vetor com n de outliers por coluna mos

    razao_outliers = np.sum(l)/total_pontos
    coeficiente_spearman = spearman.spearman(x,y)   #spearman/s = stats.spearmanr(x,y)
    coeficiente_pearson = pearson.pearson(x,y)      #pearson/p = stats.pearsonr(x,y)
    coeficiente_anova_F, coeficiente_anova_p, relacao_anova = anova.anova(x,y)
    
    a, b = regressaoLinear.regressaoLinear(x,y)      #regressao linear
    x, t, y, v = levenbergMarquart.levenberg(x,y)   #funcao logistica
    linear = '(' + str(a) + ')*x + (' + str(b) + ')'
    logistica = '(' + str(v[0])+ ') * (' + str(0.5) + '-(' + str(v[1]) + ')/(exp(' + str(v[1]) + '*(x-(' + str(v[2])+ '))))) + (' + str(v[3])+ ') * x+(' + str(v[4]) + ')'
    
    
    
    return razao_outliers, coeficiente_spearman, coeficiente_pearson, coeficiente_anova_F, coeficiente_anova_p, relacao_anova, logistica, linear




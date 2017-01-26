from  scipy import stats

def anova(x,y):
    
    F, p = stats.f_oneway(x,y)
    
    if F>p:
        realcao = 'Os dados nao estao bem relacionados'
    else:
        relacao = 'Os dados estao bem relacionados'
        
    return F, p, relacao

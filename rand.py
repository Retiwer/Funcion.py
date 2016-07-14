def Paises_Cluster(Var, labels):
    w0 = []
    w1 = []
    w2 = []
    w3 = []
    w4 = []
    w5 = []
    
    w10 = []
    w11 = []
    w12 = []
    w13 = []
    w14 = []
    w15 = []
    
    w=[]
    z2=[]
    
    Ind, aux = np.unique(Var, return_counts=True)    #Ver cuantos elementos                                                  #unicos estan en la                                                   #lista
    
    
    for i in range (len(aux)):
        if aux[i] >= 35:
            w.append(Ind[i]) #Indice de Paises
            z2.append(aux[i]) #Cantidad de Paises
    
    
    for i in range (len(Var)):
        if Var[i] ==  w [0]:
            w0.append(i)    #lugares de Veces que Bolivia se Repite
    #--------
    for i in range (len(Var)):
        if Var[i] ==  w [1]:
            w1.append(i)    #lugares de Veces que Bolivia se Repite
    #--------
    for i in range (len(Var)):
        if Var[i] ==  w [2]:
            w2.append(i)    #lugares de Veces que Bolivia se Repite
    #--------
    for i in range (len(Var)):
        if Var[i] ==  w [3]:
            w3.append(i)    #lugares de Veces que Bolivia se Repite
    #--------
    for i in range (len(Var)):
        if Var[i] ==  w [4]:
            w4.append(i)    #lugares de Veces que Bolivia se Repite
    #--------
    for i in range (len(Var)):
        if Var[i] ==  w [5]:
            w5.append(i)    #lugares de Veces que Bolivia se Repite
    
    
    for i in range (len(w0)):
        w10.append(labels[w0[i]])
    #--------
    for i in range (len(w1)):
        w11.append(labels[w1[i]])
    #--------
    for i in range (len(w2)):
        w12.append(labels[w2[i]])
    #--------
    for i in range (len(w3)):
        w13.append(labels[w3[i]])
    #--------
    for i in range (len(w4)):
        w14.append(labels[w4[i]])
    #--------
    for i in range (len(w5)):
        w15.append(labels[w5[i]])
    
    
    Ind10, Aux10 = np.unique(w10, return_counts=True)    #Ver cuantos elementos                                                  #unicos estan en la                                                   #lista
    #--------
    Ind11, Aux11 = np.unique(w11, return_counts=True)    #Ver cuantos elementos                                                  #unicos estan en la                                                   #lista
    #--------
    Ind12, Aux12 = np.unique(w12, return_counts=True)    #Ver cuantos elementos                                                  #unicos estan en la                                                   #lista
    #--------
    Ind13, Aux13 = np.unique(w13, return_counts=True)    #Ver cuantos elementos                                                  #unicos estan en la                                                   #lista
    #--------
    Ind14, Aux14 = np.unique(w14, return_counts=True)    #Ver cuantos elementos                                                  #unicos estan en la                                                   #lista
    #--------
    Ind15, Aux15 = np.unique(w15, return_counts=True)    #Ver cuantos elementos                                                  #unicos estan en la                                                   #lista

    
    
    
    a10 = 0
    a11 = 0
    for i in range (len(Ind10)):
        if Aux10[i] >= a10:
            a10 = Aux10[i]
            a11 = i
    #-----  
    a20 = 0
    a21 = 0
    for i in range (len(Ind11)):
        if Aux11[i] >= a20:
            a20 = Aux11[i]
            a21 = i
    #-----
    a30 = 0
    a31 = 0
    for i in range (len(Ind12)):
        if Aux12[i] >= a30:
            a30 = Aux12[i]
            a31 = i
    #-----
    a40 = 0
    a41 = 0
    for i in range (len(Ind13)):
        if Aux13[i] >= a40:
            a40 = Aux13[i]
            a41 = i
    #-----
    a50 = 0
    a51 = 0
    for i in range (len(Ind14)):
        if Aux14[i] >= a50:
            a50 = Aux14[i]
            a51 = i
    #-----
    a60 = 0
    a61 = 0
    for i in range (len(Ind15)):
        if Aux15[i] >= a60:
            a60 = Aux15[i]
            a61 = i
            
    wx=[a11,a21,a31,a41,a51,a61]
    print w
    print z2
    print wx
    
    print ""
    print "Pais"
    print w[0]
    print "Cantidad"
    print z2[0]
    print "Clusters"
    print Aux10
    print "Mayor"
    print a10
    print "Posicion"
    print a11
    
    print ""
    print "----------------"
    print "Pais"
    print w[1]
    print "Cantidad"
    print z2[1]
    print "Clusters"
    print Aux11
    print "Mayor"
    print a20
    print "Posicion"
    print a21
    
    print ""
    print "----------------"
    print "Pais"
    print w[2]
    print "Cantidad"
    print z2[2]
    print "Clusters"
    print Aux12
    print "Mayor"
    print a30
    print "Posicion"
    print a31
    
    print ""
    print "----------------"
    print "Pais"
    print w[3]
    print "Cantidad"
    print z2[3]
    print "Clusters"
    print Aux13
    print "Mayor"
    print a40
    print "Posicion"
    print a41
    
    print ""
    print "----------------"
    print "Pais"
    print w[4]
    print "Cantidad"
    print z2[4]
    print "Clusters"
    print Aux14
    print "Mayor"
    print a50
    print "Posicion"
    print a51
    
    print ""
    print "----------------"
    print "Pais"
    print w[5]
    print "Cantidad"
    print z2[5]
    print "Clusters"
    print Aux15
    print "Mayor"
    print a60
    print "Posicion"
    print a61    
    
    return (wx)




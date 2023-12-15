#------------------importe les bibli nessisaire-------------------------------#
from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
import numpy as np
from scipy import misc, rand
import matplotlib.pyplot as plt
import math
from numpy import linalg as la
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

from sympy import symbols, diff
from sympy.utilities.lambdify import lambdify
from sympy.solvers import solve

import sympy as sp
from sympy.functions import exp,log
from sympy import cos,sin,pi
from sympy.abc import x
import sys
import time 

#---declaration des variables globale ----------------------------------------#
start_time = time.time()
xzero = []
compteur = 0
x1, x2, x3 ,x4,x5,x6,x7,x8,x9,x10,x11 ,x12 ,x13 ,x14 ,x15 ,x16 ,x17 ,x18 ,x19 ,x20 = sp.symbols('x[1] x[2] x[3] x[4] x[5] x[6] x[7] x[8] x[9] x[10] x[11] x[12] x[13] x[14] x[15] x[16] x[17] x[18] x[19] x[20]',real=True)
x = np.array([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20])

class GradientDes :
    
    def __init__(self,fenetre10):
        self.fenetre10 = fenetre10
        #-----------le titre--------------------------------------------------#
        self.fenetre10.title(" Gradient descent ")
        #-----------------la geometrerde la fenetre---------------------------#
        self.fenetre10.geometry("1000x720+150+50")
        #-----------------le coleure de bag-----------------------------------#
        self.fenetre10.config(bg="#ADBABF")   
        #-----------bloquer le redimentionnement de la fenetre----------------# 
        self.fenetre10.resizable(width=False, height=False)
        #--------------logo de l'application----------------------------------#
        #self.fenetre10.iconbitmap("images/logoimag.ico")
        #==============self.frame1  ==========================================#
        self.frame1 = Frame( self.fenetre10, bg="#ADBABF", highlightbackground="#182350",highlightthickness=2)
        self.frame1.place(x=48,y=30, height=660,width=900)
        #===============title=================================================#
        title = Label( self.fenetre10,text=" Gradient descent ",font=("Comic Sans MS", 17,"bold"), bg="#ADBABF",fg="#E8F1F1").place(x=390,y=5)
       
        #----------------les entrer de l'algorithme---------------------------#
        entrer = Label(self.frame1,text="Input { ",font=("Comic Sans MS", 16,"bold"), bg="#ADBABF",fg="#182350").place(x=10,y=10)
        
        #======================dimension =====================================#
        lorder = Label(self.frame1,text="The dimension       :",font=("Comic Sans MS", 15,"bold"), bg="#ADBABF").place(x=110,y=10)
        
        #---------------------------------------------------------------------#
        self.valdimension = IntVar() 
        self.txt_valdimension = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable= self.valdimension)
        self.txt_valdimension.place(x=440, y=13,width=160)
        self.valdimension.set("2")
        #--------------------------------le choix de pas----------------------#
        labdepas = Label(self.frame1,text="Line Search          :",font=("Comic Sans MS", 15,"bold"), bg="#ADBABF").place(x=110,y=60)
        
        self.valdespas = StringVar() 
        self.cmb_pad = ttk.Combobox(self.frame1, font=("times new romman", 13,"bold"),state='readonly',justify=CENTER, textvariable=self.valdespas)
        self.cmb_pad['values']=('Fixe','Approcher', 'Optimal')
        self.cmb_pad.place(x=440, y=63,width=160)
        self.cmb_pad.current(0)
        
        #------------------------pas Fixe-------------------------------------#
        self.var_fixe = IntVar()
        self.txt_fixe_Sect= Entry(self.frame1,font=("times new romman",14,"bold"),  bg="lightgray", fg="#182350", textvariable=self.var_fixe)
        self.txt_fixe_Sect.place(x=660, y=63,width=190)
        self.var_fixe.set(1)
        #------------------------pas Aprocher---------------------------------#
        self.valAppproch = StringVar() 
        self.cmb_valApp = ttk.Combobox(self.frame1, font=("times new romman", 14,"bold"),state='readonly',justify=CENTER, textvariable=self.valAppproch)
        self.cmb_valApp['values'] = ('Armijo', 'Wolf')
        self.cmb_valApp.current(0)
        self.cmb_valApp.place(x=660, y=13,width=190)
    
        #-----------------button ---------------------------------------------#
        Order_Button  = Button(self.frame1,font=("times new romman",13, "bold"),text="Next", bg="#A8D37A", activebackground ="#3E574F", activeforeground="#A22B2B",borderwidth = 2, command =self.valdexzero).place(x=740 ,y=110,width=110)
        #--Compteur qui compte le nomber des valeur sisie par l'utilisateur---#
        self.nbrdexzero = StringVar()
        self.txt_nbrdexzero = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="red", textvariable= self.nbrdexzero)
        self.txt_nbrdexzero.place(x=440,y=163,width=100)
        self.nbrdexzero.set(" 0 / "+ str(self.txt_valdimension.get()))
        #-----------------button De sisire nouveaux Xzero--------------------#
        NewX_Button  = Button(self.frame1,font=("times new romman",12, "bold"),text="New Xzero", bg="#CBDDDD", activebackground ="#3E574F", activeforeground="#A22B2B",borderwidth = 2, command =self.NewXzero).place(x=660 ,y=160,width=190)
       
        #=================le point initiale x0 ===============================#
        intervale = Label(self.frame1,text="Le point initiale x0  :",font=("Comic Sans MS", 15,"bold"),bg="#ADBABF").place(x=110,y=110)
        
        #================vale de x0 ==========================================#
        self.txt_val = Label(self.frame1,text="Xzero  ",font=("Comic Sans MS", 15,"bold"),bg="#ADBABF").place(x=370,y=110)
        self.txtvar = DoubleVar()
        self.txt_valx = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable= self.txtvar)
        self.txt_valx.place(x=440,y=113,width=290)
        self.txtvar.set("")
        
        #===================la fonction=======================================#
        self.fonc = Label(self.frame1,text="Function             :",font=("Comic Sans MS", 16,"bold"),bg="#ADBABF").place(x=110,y=215)
        self.foncFtion = Label(self.frame1,text="f(x) = ",font=("Comic Sans MS", 16,"bold"),bg="#ADBABF").place(x=355,y=215)
        self.tcrrft = DoubleVar()
        self.txt_fonctin = Entry(self.frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350", textvariable= self.tcrrft)
        self.txt_fonctin.place(x=440,y=218,width=407 )
        self.tcrrft.set("x0**2 + x1**2")
        
        #================la tolérence  =======================================#
        self.delt = Label(self.frame1,text="Tolerance            :",font=("Comic Sans MS", 15,"bold"),bg="#ADBABF").place(x=110,y=280)
        self.delT = Label(self.frame1,text="delta =",font=("Comic Sans MS", 15,"bold"),bg="#ADBABF").place(x=360,y=280)
        self.tolerenfonc = DoubleVar()
        self.txt_toler = Entry(self.frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350", textvariable=self.tolerenfonc)
        self.tolerenfonc.set(0.01)
        self.txt_toler.place(x=440,y=283,width=160)
        
        
        #=================fermer l'accolade===================================#
        self.coladfer = Label(self.frame1,text=" } Output   :",font=("Comic Sans MS", 15,"bold"),bg="#ADBABF",fg="#182350").place(x=10,y=315)
        
        #==============le frame1  ============================================#
        self.frame2=Frame( self.frame1,bg="#C4C6C6" ,highlightbackground="#182350",highlightthickness=3)
        self.frame2.place(x=10,y=360,height=285,width=875)
        
        #======================solution ======================================#
        #---------------la valeur exacte de la solution si l'algorithme arive a calculer x*--------------------------------#
        val_solution_exact = Label(self.frame2,text="The solution   ",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=10,y=10)
        #-----------------------------------------------x*-----------------------------------------------------------------#
        val_solNew = Label(self.frame2,text=" x*:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=140,y=10)
        self.varsolGradi = StringVar()
        self.txtSolExacNew = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="green", textvariable=self.varsolGradi)
        self.varsolGradi.set("")
        self.txtSolExacNew.place(x=190, y=13, width=670)
        
        
        #-----------------------val des nomber des itoration  i --------------#
        self.nbr_Sect_iteration = Label(self.frame2,text="Number of iterations ",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=80)
        self.txt_itera_Section = Label(self.frame2,text=" i :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=220,y=80)
        self.var_sect_itir = IntVar()
        self.txt_itera_Sect= Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="red", textvariable=self.var_sect_itir)
        self.var_sect_itir.set("")
        self.txt_itera_Sect.place(x=260,y=83,width=160)
      
        #---------------------------------------interprétation----------------------------------------------------#
        self.nbr_iterpretaSecti = Label(self.frame2,text="Interpretation   ",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=150)
        self.var_iterpreSect = StringVar()
        self.txt_iterpretatSect = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.var_iterpreSect)
        self.var_iterpreSect.set("")
        self.txt_iterpretatSect.place(x=155,y=153,width=700)

        #=========================================================== boutton Gradient descent =========================================================================================================#
        DesentGrad_Button  = Button(self.frame2,font=("times new romman",16,"bold"),text="Gradient descent ",bd=0,cursor="hand2",bg="#7F7526",fg="#E5E1D6",activebackground ="#7AA1E6",activeforeground="#BF846C",borderwidth = 5, command =self.gradient).place(x=320 ,y=220,width=240)
           
        #============================================================ Bouton le graphe de la fonction ===========================================================================================#
        graphedefa= Button(self.frame2,font=("times new romman",16,"bold"),text="graph of the fonction",bd=0,cursor="hand2",bg="#7B9764",fg="#E5E1D6",activebackground ="#CDD3C8",activeforeground="#BFF790",borderwidth = 5, command=self.graphe_de_fonction).place(x=10 ,y=220,width=240)
        
        #============================================================ Bouton quitt ============================================================================================================#
        quittbuttn= Button(self.frame2,font=("times new romman",16,"bold"),text="Quit ",bd=0,cursor="hand2",bg="#AD2E15", fg="#F3EEED",activebackground ="#CAE5E4",activeforeground="#E8A490",borderwidth = 5, command=self.quiter).place(x=640 ,y=220,width=220)
  
    
    #-------------Pour quiter-------------------------------------------------#       
    def quiter(self):
        self.fenetre10.destroy()
        
   #-------------Sisairune nouvel Xzero---------------------------------------#
    def NewXzero(self):
        try:
            #--------recuperer la valeur de dimension-------------------------#
            dimen = int(self.txt_valdimension.get())
            #--------vider la liste de xzero pour le modifier-----------------#
            xzero.clear()
            #--------returner le compteur a 0---------------------------------#
            global compteur
            compteur = 0
            #--------vider le champs de xzero---------------------------------#
            self.txt_valx.delete(0, END)
            #-returner le nombre des valeur sisais par le tulisa à O/dimensio-#
            self.nbrdexzero.set(str(compteur)+" / "+str(dimen))
        except Exception as es:                  
               MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre10) 
    
    #----------------pour vider les champs------------------------------------#
    def clearChamp(self):
        #----------vider le champs de solution--------------------------------#
        self.txtSolExacNew.delete(0, END)
        #----------vider le champs de nbr d'itiration-------------------------#
        self.txt_itera_Sect.delete(0, END)
        #----------vider le champ de l'interpretation-------------------------#
        self.txt_iterpretatSect.delete(0, END)
        
    #----------fonction pour calculer le gradient-----------------------------#    
    def gradientDFC(self, F, dim, eps=1e-5):
        def dE(x):
            v = np.zeros(dim)
            for i in range(dim):
                ei = np.zeros(dim)
                ei[i] = 1
                v[i] = (F(x + eps*ei) - F(x - eps*ei))/(2*eps)
            return v
        return dE
        
    
        
   
        
    #---recuperer la valeur de global xzero-----------------------------------#
    def valdexzero(self):
        global compteur
        global xzero
        try:
            #--------recuperer la valeur de dimension-------------------------#
            dimen = int(self.txt_valdimension.get())
            valdexze = self.txt_valx.get()
            if( dimen =="" or valdexze ==""):
                MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre10)
            elif( compteur >= dimen ):
                return
            else:
                xer = self.txtvar.get()
                xsuivant = float(self.txt_valx.get())
                #--- verifier que le dimension est sinificative---------------#
                if(dimen > 20 or dimen == 0):
                    #---une message d'erreur dans le cas contraire------------#
                    MessageBox.showerror("Error"," Entrer une valeur de dimension supérieur à 0 et inferieur à 20 SVP !", parent=self.fenetre10)
                elif(compteur < dimen):#le dimension est valide---------------#
                    #---recuperer les valeur pour l'une par une pour construie le vercteur de Xzero selon le dimesion--#
                    xzero.append(xsuivant)
                    #-----------vider le champs aprer chaque enter------------#
                    self.txt_valx.delete(0, END)
                    #---incrementer le compteur(nbr des valeur sisais)--------#
                    compteur+=1
                    #------------afecher le nmber des valeur sisais-----------#
                    self.nbrdexzero.set(str(compteur)+" / "+str(dimen))
                    
                else:
                    #---si le vecteur Xzero valide avec succés on affiche une message de validation
                    MessageBox.showinfo("Information"," le vecteur Xzero est sisais avec succée ", parent=self.fenetre10)
                    print("Xzero = "+xzero)
                if(compteur == dimen):
                    #---en fin on affiche le vecteur de Xzero complet---------#
                    self.txtvar.set(str(xzero))
        except Exception as es:                  
               MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre10) 
                       
    #-------------------Algorithme de Armijo----------------------------------#
    def armijo_rule(self, alpha_0, x, f, f_x, grad_x, d_x , c, beta): #d_x est la direction de descente d_x . grad_x <= 0
            # test f(x_new) <) f(x_0) + c alpha ps{d_x}{grad_x}
            def fonction(x):
                fonc = eval(f)
                return fonc
            test = 1
            alpha = alpha_0
            while test: 
                x_new = x+alpha*d_x
                if (fonction(x_new)<=f_x+c*alpha*np.dot(grad_x,d_x)):
                    test = 0
                else:
                    alpha = alpha*beta ## alpha/2
            return alpha
    #-------------------Algorithme de Wolf  ----------------------------------#
    def wolfe_rule(self, alpha_0, x, f, f_x, grad_x, d_x, c_1, c_2): #d_x est la direction de descente  d_x . grad_x < 0
            # test f(x_new) <= f(x_0) + c_1 alpha ps{d_x}{grad_x} et \ps{x_new}{d_x} => c_2 \ps{x_0}{d_x}
            # sinon alpha <- alpha * beta
            # On cherche au fur et mesure un opt dans [minorant, majorant]
            dim = np.max(np.shape(x))
            def fonction(x):
                fonc = eval(f)
                return fonc
            test = 1
            iteration = 0
            alpha = alpha_0
            minorant = 0
            majorant = 1000
            while (test)&(iteration<=1000): 
                x_new = x+alpha*d_x
                #------ le premier condition ---------#
                if (fonction(x_new)<=f_x+c_1*alpha*np.dot(grad_x,d_x))&(np.dot(self.gradientDFC(fonction,dim)(x),d_x) >= c_2*np.dot(grad_x,d_x) ):
                    test = 0
                #-------deuxieme condition ------#
                elif (fonction(x_new)>f_x+c_1*alpha*np.dot(grad_x,d_x)):
                    majorant = alpha
                    alpha = (majorant + minorant)/2
                    iteration = iteration +1
                else:
                    minorant = alpha
                    alpha = (majorant + minorant)/2
                    iteration = iteration +1
            return alpha
        
    #--------- méthode de gradient -------------------------------------------#
    def gradient(self):
        #--------------------------initialisation-----------------------------#
        iterations = 5000
        error_point = 1e-8
        error_grad = 1e-8
        #-------------appel a la fonction pour vider les champs---------------#
        self.clearChamp()
        #-------------recuperer les valeur sisair ----------------------------#
        func = self.txt_fonctin.get() #--la fonction--------------------------#
        delt = self.txt_toler.get()#---la tolerence---------------------------#
        
        if( func == ""  or delt == "" ):#--si les enter n'est pas sisais------#
             MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre10)
        else :
            try:
                #-------Dimension ----------#
                dim = np.max(np.shape(xzero))
                #--- Symboles des variable à respecter --------#
                for i in range(0, 20):
                  func = func.replace(f"x{i}",f"x[{i}]")
                
                
                func = func.replace("ex[0]p","exp")
                f = func
                
                #print(f)
                def fonction(x):
                    fonc = eval(f)
                    return fonc
                #--Initiation des données ------#
                x_list = np.zeros([dim, iterations])
                f_list = np.zeros(iterations)
                error_point_list = np.zeros(iterations)
                error_grad_list = np.zeros(iterations)
                x = xzero
                x_old = x
                #------- pas fixe------------------------#
                if(self.valdespas.get() == 'Fixe'):
                        h = self.var_fixe.get()#-recuperer la  valeur de pas--#
                        grad_x = self.gradientDFC(fonction, dim,1e-5)(x)
                        for i in range(iterations):
                            x = x - h * self.gradientDFC(fonction, dim,1e-5)(x) #--Nouvelle iteration ---#
                            grad_x = self.gradientDFC(fonction, dim,1e-5)(x)
                            f_x = fonction(x)
                            x_list[:,i] = x
                            f_list[i] = fonction(x)
                            error_point_list[i] = np.linalg.norm(x - x_old)
                            error_grad_list[i] = np.linalg.norm(grad_x)
                            #----------- visualisation d'etat d'avancement ------------------------#
                            
                            if i % 1000 == 0:
                                print("iter={}, x={}, f(x)={}".format(i+1, x, fonction(x)))
                    
                            if (error_point_list[i] < error_point) and (error_grad_list[i] < error_grad):
                                break
                            x_old = x
                            
                        
                        print("point error={}, grad error={}, iteration={}, x={}, f(x)={}".format(error_point_list[i], error_grad_list[i],i+1,x,fonction(x)))
                        #---------- Le temps d'execution ----------------#
                        print("DURÉE D'APPRENTISAGE(seconde) : ",time.time() - start_time)
                        #---------Affichage des resultat dans linterface------#
                        self.varsolGradi.set(x)#--affichage de solution-------#
                        self.var_sect_itir.set(i+1)#--nomber d'itiration------#
                        self.var_iterpreSect.set("La solution est trouvée avec succés utilisant le pas Fixe : "+str(h))#--petit l'interpretation
                
                #--------- pas optimal ------
                elif(self.valdespas.get() =='Optimal'):
                    self.var_fixe.set("")
                    grad_x = self.gradientDFC(fonction,dim,1e-5)(x)
                    f_x = fonction(x)
                    d_x = - grad_x
            
                    for i in range(iterations):
                        xalpha = sp.Symbol('x')
                        #--- La fontion phi obtenu de la fontion mére --#
                        falpha = x - xalpha * self.gradientDFC(fonction, dim, eps=1e-5)(x)
                        falpha = np.array(falpha).flatten()
                        fonc = fonction(falpha)
                        #------ cherche de voisinage par la methode de fibonacci-----------#
                        voizn = self.fibonacci(0, 10, str(fonc), 100) 
                        #------- solution par la methode de newtonraphson-----------#
                        alpha = self.newtonraphson(voizn, str(fonc), 0.01, 100)
                
                        x = x - alpha*self.gradientDFC(fonction,dim,1e-5)(x)
                        grad_x = self.gradientDFC(fonction,dim,1e-5)(x)
                        f_x = fonction(x)
                        x_list[:,i] = x
                        f_list[i] = fonction(x)
                        #---------- ||gradF(x)|| ---------------#
                        error_point_list[i] = np.linalg.norm(x - x_old)
                        #---------- ||xk - xk-1|| ---------------#
                        error_grad_list[i] = np.linalg.norm(grad_x)
                        #----------- visualisation d'etat d'avancement ------------------------#
                        
                        if i % 1000 == 0:
                            print("iter={}, x={}, f(x)={}".format(i+1, x, fonction(x)))
                
                        if (error_point_list[i] < error_point) or (error_grad_list[i] < error_grad):
                            break
                        x_old = x
                        
                    #---------- Le temps d'execution ----------------#
                    print("point error={}, grad error={}, iteration={}, x={}, f(x)={}".format(error_point_list[i], error_grad_list[i],i+1,x,fonction(x)))
                    print("DURÉE D'APPRENTISAGE(seconde) : ",time.time() - start_time)
                    #---------Affichage des resultat dans linterface--#
                    self.varsolGradi.set(x)#--affichage de solution---#
                    self.var_sect_itir.set(i+1)#--nomber d'itiration--#
                    self.var_iterpreSect.set("La solution est trouvée avec succés utilisant le pas Optimal (Fibonacci et Newton)  !")#--petit l'interpretation
                #-------- pas approcher -----------#        
                elif(self.valdespas.get() == 'Approcher'):
                    self.var_fixe.set("")
                    grad_x = self.gradientDFC(fonction,dim)(x)
                    d_x = -grad_x
                    f_x = fonction(x)
                    alpha_0 = 0.01
                    c = 0.1
                    beta=0.5
                    #---------------dans le cas de pas approcher Armijo-------#
                    if(self.valAppproch.get() == 'Armijo'):
                            h = self.armijo_rule(alpha_0, x, f, f_x, grad_x, d_x, c, beta)
                            for i in range(iterations):
                                x = x + h*d_x
                                grad_x = self.gradientDFC(fonction,dim)(x)
                                f_x = fonction(x)
                                d_x = -grad_x
                                alpha_0 = 0.01
                                h = self.armijo_rule(alpha_0, x, f, f_x, grad_x, d_x, c, beta)
                                x_list[:,i] = x
                                f_list[i] = f_x
                                #---------- ||xk - xk-1|| ---------------#
                                error_point_list[i] = np.linalg.norm(x - x_old)
                                #---------- ||gradF(x)|| ---------------#
                                error_grad_list[i] = np.linalg.norm(grad_x)
                                
                                #----------- visualisation d'etat d'avancement ------------------------#
                                if i % 1000 == 0:
                                    print("iter={}, x={}, f(x)={}".format(i+1, x, fonction(x)))
                        
                                if (error_point_list[i] < error_point)|(error_grad_list[i] < error_grad):
                                    break
                                x_old = x

                            #---------- Le temps d'execution ----------------#
        
                            print("point error={}, grad error={}, iteration={}, x={}, f(x)={}".format(error_point_list[i], error_grad_list[i],i+1,x,fonction(x)))
                            print("DURÉE D'APPRENTISAGE(seconde) : ",time.time() - start_time)
                            #---------Affichage des resultat dans linterface--#
                            self.varsolGradi.set(x)#--affichage de solution---#
                            self.var_sect_itir.set(i+1)#--nomber d'itiration--#
                            self.var_iterpreSect.set("La solution est trouvée avec succés utilisant le pas approcher Armijo  !")#petit l'interpretation
                    #---------------dans le cas de pas approcher Wolf---------#          
                    elif(self.valAppproch.get() == 'Wolf'):
                            self.var_fixe.set("")
                            c_1=0.1
                            c_2=0.9
                            h = self.wolfe_rule(alpha_0, x, f, f_x, grad_x, d_x, c_1, c_2)
                            for i in range(iterations):
                                x = x + h * d_x
                                grad_x = self.gradientDFC(fonction,dim)(x)
                                f_x = fonction(x)
                                d_x = -grad_x
                                alpha_0 = 0.01
                                h = self.wolfe_rule( alpha_0, x, f, f_x, grad_x, d_x, c_1, c_2)
                                x_list[:,i] = x
                                f_list[i] = f_x
                                #---------- ||xk - xk-1|| ---------------#
                                error_point_list[i] = np.linalg.norm(x - x_old)
                                #---------- ||gradF(x)|| ---------------#
                                error_grad_list[i] = np.linalg.norm(grad_x)
                                #----------- visualisation d'etat d'avancement ------------------------#
                                if i % 1000 == 0:
                                    print("iter={}, x={}, f(x)={}".format(i+1, x, fonction(x)))
                        
                                if (error_point_list[i] < error_point)|(error_grad_list[i] < error_grad):
                                    break
                                x_old = x
                                
                            print("point error={}, grad error={}, iteration={}, x={}, f(x)={}".format(error_point_list[i], error_grad_list[i],i+1,x,fonction(x))) 
                            print("DURÉE D'APPRENTISAGE(seconde) : ",time.time() - start_time)
                            #---------Affichage des resultat dans linterface--#
                            self.varsolGradi.set(x)#--affichage de solution---#
                            self.var_sect_itir.set(i+1)#--nomber d'itiration--#
                            self.var_iterpreSect.set("La solution est trouvée avec succés utilisant le pas approcher Wolf  !") #--petit l'interpretation                  
            except Exception as es:                  
               MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre10) 
    
            
    #----------Fibonacci -----------------------------------------------------#
    def fibonacci(self, xL1 : float, xU1 : float, f, n : int):
              xLk = xL1
              xUk = xU1
              def func(x):
                 func = eval(f)
                 return func
              x = sp.Symbol('x')
              deriv1 = sp.diff(func(x),x)
              deriv2 = sp.diff(func(x),x,x)
              def deriv1er(x):
                  deriv1er = eval(str(deriv1))
                  return deriv1er
              def deriv2eme(x):
                  deriv2eme = eval(str(deriv2))
                  return deriv2eme
              
              if((deriv1er(xL1)<0 and deriv1er(xU1)<0) or (deriv1er(xL1)>0 and deriv1er(xU1)>0)):
                  print("La fonction est monotone ou multimodale dans l'intervale [",xL1,",",xU1,"]")
                  sys.exit()
              xa1 = 0
              xb1 = 0
              fa1 = 0
              fb1 = 0
              F = []
              F.insert(0, 1)
              F.insert(1, 1)
              for k in range(2,n):
                valFk = F[k-1] + F[k-2]
                F.insert(k,valFk)
              z = len(F) - 1
              I = []
              I1 = xU1 - xL1
              I2 = (F[z-1]/F[z])*I1
              I.insert(0, 0)
              I.insert(1, I1)
              I.insert(2, I2)
              xa1 = xU1 - I[1]
              xb1 = xL1 + I[2]
              fa1 = func(xa1)
              fb1 = func(xb1)
              
              k = 1
              q = n - 2
              for j in range(n):
                  Ik2 = (F[n-k-1]/F[n-k])*I[k+1]
                  I.insert(k+2, Ik2)
                  if( fa1 >= fb1 ):
                        xLk = xa1
                        xa1 = xb1
                        xb1 = xLk + I[k+2]
                        fa1 = fb1
                        fb1 = func(xb1)
                        if( (k == q) or (xa1 > xb1)):
                            xapproch = xa1
                            fxapproch = func(xapproch)
                            #print("[",xb1,",",xa1,"] le point x* : ",xapproch," f(x*) :",fxapproch)
                            return xapproch
                            break
                        else:
                            k = k + 1
                  elif( fa1 < fb1 ):
                      xUK = xb1
                      xa1 = xUK - I[k+2]
                      xb1 = xa1
                      fb1 = fa1
                      fa1 = func(xa1)
                      if( (k == q) or (xa1 > xb1)):
                          xmin = xa1
                          fmin = func(xa1)
                          #print("le point x* : ",xmin," f(x*) :",fmin)
                          return xmin
                          break
                      else:
                          k = k + 1
           
    #------------Newton-------------------------------------------------------#
    def newtonraphson(self, xk : float, f, tole : float, nbrIter : int):
        xmoins = xk - 1
        xkplus = 0
        def func(x):
            func = eval(f)
            return func
        x = sp.Symbol('x')
        deriv1 = sp.diff(func(x),x)
        deriv2 = sp.diff(func(x),x,x)
        def deriv1er(x):
            deriv1er = eval(str(deriv1))
            return deriv1er
        def deriv2eme(x):
            deriv2eme = eval(str(deriv2))
            return deriv2eme
        for n in range(0,nbrIter):
            f1 = deriv1er(xk)
            f2 = deriv2eme(xk)
            if(f2 == 0):
                print("Impossible la derivee seconde egale à 0")
                break
            else :
                dist = xk - xmoins
                if(abs(dist)>=tole):
                    direction = -1 * f1/f2
                    xkplus = xk + direction
                    xmoinx = xk
                    xk = xkplus 
                else:
                    #print("La valeur apres ",n," iteration")
                    #print(xk)
                    break
                    return xk
        if(f2 > 0):
            #print("apres ",n," iteration le minimum est ",xk)
            return xk
        elif(f2 < 0):
            #print("apres ",n," iteration le maximum est ",xk)
            return xk
    
    #======================Le gaphe de la fonction============================#   
    def graphe_de_fonction(self):
            fonc = self.txt_fonctin.get()
            if(fonc =="" ):
                MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre10)
            elif(self.valop.get() == 2):
                try:
                    def fon(x, y):
                        evalfon = eval(fonc)
                        return evalfon
                    fig = plt.figure(figsize=(10, 8))
                    ax = fig.gca(projection='3d')
                    ax.set_title('3D Surface Plot of ' + ' f = ' + str(fonc))
                    ax.set_xlabel('x axis')
                    ax.set_ylabel('y axis')
                    ax.set_zlabel('z axis')

                    x = np.arange(-10, 10, 0.05)
                    y = np.arange(-10, 10, 0.05)
                    x, y = np.meshgrid(x, y)
                    
                    f = fon(x,y)
                    surface = ax.plot_surface(x, y, f, cmap=cm.coolwarm, linewidth=0)
                    fig.colorbar(surface, shrink=0.5)
                    plt.show()
                    
                except Exception as es:                  
                    MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre10) 
                   
            elif(self.valop.get() >= 3):
                MessageBox.showerror("Error"," le dimension est Supérieur a 2", parent=self.fenetre10) 

fenetre10 = Tk()
obj=GradientDes(fenetre10)
fenetre10.mainloop() 
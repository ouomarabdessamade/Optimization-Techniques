from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
import numpy as np
from scipy import misc 
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




class ConjugateGradient :
    varglob = 0
    def __init__(self, fenetr8):
        self.fenetr8=fenetr8
        #-----------le titre--------------------------------------------------#
        self.fenetr8.title(" Conjugate Gradient ")
        #-----------------la geometrerde la fenetre---------------------------#
        self.fenetr8.geometry("1000x720+150+50")
        #-----------------le coleure de bag-----------------------------------#
        self.fenetr8.config(bg="#919FA0")   
        #-----------bloquer le redimentionnement de la fenetre----------------# 
        self.fenetr8.resizable(width=False, height=False)
        #--------------logo de l'application----------------------------------#
        self.fenetr8.iconbitmap("images/logoimag.ico")
        #==============self.frame1  ===============================================#
        self.frame1 = Frame( self.fenetr8, bg="#919FA0", highlightbackground="#182350",highlightthickness=2)
        self.frame1.place(x=48,y=30, height=660,width=900)
        #===============title=================================================#
        title = Label( self.fenetr8,text=" Conjugate Gradient ",font=("Comic Sans MS", 17,"bold"), bg="#919FA0",fg="#D7E5EE").place(x=380,y=5)
       
        #----------------les entrer de l'algorithme---------------------------#
        entrer = Label(self.frame1,text="Input { ",font=("Comic Sans MS", 16,"bold"), bg="#919FA0",fg="#182350").place(x=10,y=10)
        
        #======================la dimension  =======================================#
        lorder = Label(self.frame1,text="The dimension       :",font=("Comic Sans MS", 15,"bold"), bg="#919FA0").place(x=110,y=30)
        
        #---------------------------------------------------------------------#
        self.valop = IntVar() 
        self.cmb_lorder = ttk.Combobox(self.frame1, font=("times new romman", 13,"bold"),state='readonly',justify=CENTER, textvariable=self.valop)
        self.cmb_lorder['values']=(" 2 "," 3 ")
        self.cmb_lorder.place(x=440, y=33,width=120)
        self.cmb_lorder.current(0)
        
        #-----------------button ----------------------------------------------------#
        Order_Button  = Button(self.frame1,font=("times new romman",12, "bold"),text="change dimension", bg="#CBDDDD", activebackground ="#3E574F", activeforeground="#A22B2B",borderwidth = 2, command = self.chengdim).place(x=620 ,y=133,width=215)
        #=================l'intervale ========================================#
        intervale = Label(self.frame1,text="Initial point x0      :",font=("Comic Sans MS", 15,"bold"),bg="#919FA0").place(x=110,y=110)
        
        #================vale de x1 ==========================================#
        txtval1 = Label(self.frame1,text="x[0]  ",font=("Comic Sans MS", 15, "bold"), bg="#919FA0").place(x=385,y=80)
        self.txtvar1 = DoubleVar()
        self.txt_valx1 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable= self.txtvar1)
        self.txt_valx1.place(x=440,y=83, width=60)
        self.txtvar1.set(0)
        
        #================la valeure de x2 ====================================#
        valbb2 = Label(self.frame1,text="x[1]  ",font=("Comic Sans MS", 15,"bold"), bg="#919FA0").place(x=385,y=120)
        self.txttvarr2 = DoubleVar()
        self.txt_valy2 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.txttvarr2)
        self.txt_valy2.place(x=440,y=123, width=60)
        self.txttvarr2.set(0)
        #================la valeure de x3====================================#
        self.vagx3 = StringVar()
        valbb2 = Label(self.frame1, font=("Comic Sans MS", 15,"bold"), bg="#919FA0", textvariable = self.vagx3 ).place(x=385,y=160)
        self.vagx3.set("")
        #===================la fonction=======================================#
        self.fonc = Label(self.frame1,text="Function             :", font=("Comic Sans MS", 16,"bold"), bg="#919FA0").place(x=110,y=210)
        self.foncFtion = Label(self.frame1,text="f(x) = ",font=("Comic Sans MS", 16,"bold"),bg="#919FA0").place(x=355,y=210)
        self.tcrrft = StringVar()
        self.txt_fonctin = Entry(self.frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350", textvariable= self.tcrrft)
        self.txt_fonctin.place(x=440,y=213,width=397 )
        self.tcrrft.set("x**2 + y**2 + z**2")
        #=================fermer l'accolade===================================#
        self.coladfer = Label(self.frame1,text=" } Output   :",font=("Comic Sans MS", 15,"bold"),bg="#919FA0",fg="#182350").place(x=10,y=280)
        
        #==============self.frame1  ===============================================#
        self.frame2=Frame( self.frame1,bg="#C4C6C6" ,highlightbackground="#181C1B",highlightthickness=2)
        self.frame2.place(x=10, y=330,height=320,width=875)
        
        #=================================================solution ===========================================#
        #---------------la valeur de la solution si l'algorithme arive a calculer x*--------------------------------#
        val_solution = Label(self.frame2,text="The solution   ",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=20,y=10)
        #------------------------------------ label de la solution optimale x* -----------------------------------------------#
        val_solConjuGrad = Label(self.frame2,text=" x*:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=240,y=20)
        self.varsolConjuGrad = StringVar()
        self.txtSolExacConjuGrad = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="green", textvariable=self.varsolConjuGrad)
        self.varsolConjuGrad.set("")
        self.txtSolExacConjuGrad.place(x=290, y=23, width=550)# , height= 30
        
        
        #--------------------------------val des nomber des itoration  i ----------------------------------------#
        self.nbr_Sect_iteration = Label(self.frame2,text="Number of iterations ",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=100)
        self.txt_itera_Section = Label(self.frame2,text=" i :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=100)
        self.var_sect_itir = IntVar()
        self.txt_itera_Sect= Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="red", textvariable=self.var_sect_itir)
        self.var_sect_itir.set("")
        self.txt_itera_Sect.place(x=290,y=103,width=160)
      
        #---------------------------------------Solution----------------------------------------------------------#

        #---------------------------------------interprétation----------------------------------------------------#
        self.nbr_iterpretaSecti = Label(self.frame2,text="Interpretation   ",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=180)
        self.var_iterpreSect = StringVar()
        self.txt_iterpretatSect = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.var_iterpreSect)
        self.var_iterpreSect.set("")
        self.txt_iterpretatSect.place(x=290,y=183,width=545)

        #------------------------------------------- boutton Quasi New --------------------------------------------------------------------#
        QuasiNew_Button  = Button(self.frame2,font=("times new romman",16,"bold"),text=" Conjugate Gradient",bd=0,cursor="hand2", bg="#78A7B0",fg="#E5E1D6",activebackground ="#7AA1E6",activeforeground="#BF846C",borderwidth = 5, command =self.ConjugateGradient).place(x=320 ,y=240,width=240)
           
        #------------------------------------ Bouton le graphe de la fonction ----------------------------------------------------=#
        graphedefa= Button(self.frame2,font=("times new romman",16,"bold"),text="graph of the fonction",bd=0,cursor="hand2",bg="#7B9764",fg="#E5E1D6",activebackground ="#CDD3C8",activeforeground="#BFF790",borderwidth = 5, command=self.graphe_de_fonction).place(x=10 ,y=240,width=240)
        
     
        #---------------------------Bouton quitt ----------------------------------------------------------------#
        quittbutnn= Button(self.frame2,font=("times new romman",16,"bold"),text="Quit ",bd=0,cursor="hand2",bg="#AD2E15", fg="#F3EEED", activebackground ="#CAE5E4",activeforeground="#E8A490",borderwidth = 5, command=self.quiter).place(x=640 ,y=240,width=200)
  
    
    #-------------Pour quiter------------------------------------#
    def quiter(self):
        self.fenetr8.destroy()
      
        
        
    #----------------method pour vider les champs------------------------------------#
    def clearChamp(self):
        self.txtSolExacConjuGrad.delete(0, END)
        self.txt_itera_Sect.delete(0, END)
        self.txt_iterpretatSect.delete(0, END)
    
    #--------------methd qui permet de prendre le changement de la dimension en concederation---------#
    def chengdim(self):
         global varglob
         if(self.valop.get()==3): 
             varglob = 1
             
             self.txttvarr3 = DoubleVar()
             self.txt_valy3 = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.txttvarr3)
             self.txt_valy3.place(x=440,y=163,width=60)
             self.txttvarr3.set("")
             self.vagx3.set("x[2]")
             
         elif(self.valop.get() == 2 and varglob == 1):    
             self.txt_valy3.destroy()
             self.vagx3.set(" ")
             varglob = 0
             
    #---------------------------l'lgorithm----------------------------------#

    # ----- en cas de dimention 2---------------------#
    # ------ la fonction ----------------------#
    def function2(self, x):
        #----- recuperer l'expression de la fonction en entree et convertir en string -----#
        func = self.txt_fonctin.get()
        f = str(func)
        #-------- prendre en compte x et y commes des variable de la fonction -----#
        x, y = symbols('x y', real=True)
        func = eval(f)
        return func

    # ---- la fonction gradient de f ----------------------#
    def grad2(self, f):
        x, y = symbols('x y', real=True)
        dx = diff(f(x), x)
        dy = diff(f(y), y)
        return np.transpose(np.array([dx, dy]))
    # ----- calcule des valeurs des composant de gradient------#
    def evalgrad2(self, point, fonc):
        Res = self.grad2(fonc)
        # print("Res = ", Res)
        fon1 = str(Res[0])
        fon2 = str(Res[1])
        x = point[0]
        y = point[1]
        # ------ par apport a x-------#
        def avalF1(x):
            x = point[0]
            y = point[1]
            t = eval(fon1)
            return t
        # ------ par apport a y-------#
        def avalF2(y):
            x = point[0]
            y = point[1]
            p = eval(fon2)
            return p
        # --- arrangement des valeurs dans un seul array--------#
        y1 = avalF1(x)
        y2 = avalF2(y)
        resultt = np.array([y1, y2]).flatten()
        return resultt

    # -----calcule de hessien--------------------------#
    def hessien2(self, f):
        # ------ definir x et y  comme des variable de la fonction f -----------#
        x, y = symbols('x y', real=True)
        H = np.array([x, y])
        Resgrad = self.grad2(f)
        M = Resgrad[0]
        print(M)
        N = Resgrad[1]
        def foncM(x):
            x, y = symbols('x y', real=True)
            a = eval(str(M))
            return a
        def foncN(x):
            x, y = symbols('x y', real=True)
            b = eval(str(N))
            return b
        dxx = diff(foncM(x), x)
        dxy = diff(foncM(x), y)
        dyx = diff(foncN(y), x)
        dyy = diff(foncN(y), y)
        H = np.array([[dxx, dxy], [dyx, dyy]])
        return H

#-------------les fonction de dimensio 3---------------#
    #---------- la fonction --------#
    def function3(self, x):
       func = self.tcrrft.get()
       f = str(func)
       x, y, z = symbols('x y z', real=True)
       func = eval(f)
       return func
    #---------- le gradient -----------#
    def grad3(self, f):
       x, y, z = symbols('x y z', real=True)
       dx = diff(f(x), x)
       dy = diff(f(y), y)
       dz = diff(f(z), z)
       return np.transpose(np.array([dx, dy, dz]))

    # -------le gradient en un point ---------#
    def evalgrad3(self, point, fonc):
       Res = self.grad3(fonc)
       # print("Res = ", Res)
       fon1 = Res[0]
       fon2 = Res[1]
       fon3 = Res[2]
       x = point[0]
       y = point[1]
       z = point[2]
       def avalF1(x):
           x = point[0]
           y = point[1]
           z = point[2]
           t = eval(str(fon1))
           return t
       def avalF2(y):
           x = point[0]
           y = point[1]
           z = point[2]
           p = eval(str(fon2))
           return p
       def avalF3(z):
           x = point[0]
           y = point[1]
           z = point[2]
           m = eval(str(fon3))
           return m
       y1 = avalF1(x)
       y2 = avalF2(y)
       y3 = avalF3(z)
       resultdeF = np.array([y1, y2, y3]).flatten()
       return resultdeF
    # -----calcule de hessien--------------------------#
    def hessien3(self, f):
        #------ definir x, y et z comme des variable de la fonction f -----------#
        x, y, z = symbols('x y z', real=True)
        H = np.array([x, y, z])
        #------ claculer de vecteur Rsgrad qui contient l'expression de gradient de f sur chaque variable de f ---------#
        Resgrad = self.grad3(f)
        #------ par apport a x -----#
        M = Resgrad[0]
        # ------ par apport a y -----#
        N = Resgrad[1]
        # ------ par apport a z -----#
        k = Resgrad[2]
        #----------- L'expression de la derivee de f par apport a x sous form d'une fonction --------------#
        def foncM(x):
            x, y, z = symbols('x y z', real=True)
            a = eval(str(M))
            return a
        #----------- L'expression de la derivee de f par apport a y sous form d'une fonction --------------#
        def foncN(x):
            x, y, z = symbols('x y z', real=True)
            b = eval(str(N))
            return b
        #----------- L'expression de la derivee de f par apport a z sous form d'une fonction --------------#
        def fonck(x):
            x, y, z = symbols('x y z', real=True)
            c = eval(str(k))
            return c
        dxx = diff(foncM(x), x)
        dxy = diff(foncM(x), y)
        dxz = diff(foncM(x), z)

        dyx = diff(foncN(y), x)
        dyy = diff(foncN(y), y)
        dyz = diff(foncN(y), z)

        dzx = diff(fonck(z), x)
        dzy = diff(fonck(z), y)
        dzz = diff(fonck(z), z)

        H = np.array([[dxx, dxy, dxz],
                      [dyx, dyy, dyz],
                      [dzx, dzy, dzz] ])
        return H
    #------------------- debut de la class de la methode de gradient conjugue----------#
    def ConjugateGradient(self):
        #-------- Supprimer l'ancien contenue des champs de saisie--------#
        self.clearChamp()
        #--------recuperer les entrees --------------#
        #------ recuperer
        val1 = self.txt_valx1.get()
        val2 = self.txt_valy2.get()
        func = self.txt_fonctin.get()
        
        if(val1 == "" or val2 ==""  or func =="" ):
             MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetr8)
        else :
             try:
                 k = 0
                 #------------------ En Cas de dimension 2 ------------------#,,,,
                 if(self.valop.get()==2):
                        dim = 2
                        #-------passage des valeurs initiales avec un casting en float---------#
                        x1 = float(val1)
                        x2 = float(val2)
                        #----------arrangement des valeurs initiales dans un seul vecteur x0 ---------#
                        x0 = np.array([x1, x2])
                        xk = np.transpose(x0)
                        # ---- inialiser la direction d0=-∇f(x0 )-----#
                        d0 = - self.evalgrad2(x0 ,self.function2)
                        dk = d0
                        # ------ definir la matrice Q qu'est la matrice Hessien, car f est de class C2--------#
                        Q = self.hessien2(self.function2)
                        #------ debut de la boucle for -------------#
                        for k in range(dim-1):
                            #-------- calcule de dk transpose -------#
                            dkt = np.transpose(dk)
                            #-------- si dk = 0 impossible d'apppliquer l'algorithme ---------#
                            vect2Nul = np.array([0, 0])
                            if (dkt[0] == vect2Nul[0] and dkt[1] == vect2Nul[1]):
                                MessageBox.showerror("Error", " Impossible d'apppliquer l'algorithme si la direction dk est nul", parent=self.fenetr8)
                            # ------- calcul de Transpo(ⅆ^k) * ⅆ^k ------------#
                            dkt_dk = np.dot(dkt,dk)
                            # ------- calcul de Q * ⅆ^k ------------#
                            Qdk = np.dot(Q,dk)
                            # ------- calcul de Transpose(ⅆ^k) * Q * ⅆ^k ------------#
                            dkt_Qdk = np.dot(dkt, Qdk)
                            # ------- calcul de      α_k =  (Transpo(ⅆ^k) * ⅆ^k)/(Transpo(ⅆ^k) * Q *ⅆ^k ) ------------#
                            alpha = dkt_dk / dkt_Qdk
                            # ------- calcul de x^(k+1) = x^k + α_k * ⅆ^k ------------#
                            xk = xk + alpha * dk
                            # ------- calcul de β_k=  (Transpo(∇f(x^k )) * Q * ⅆ^k) / (Transpo(ⅆ^k) * Q * ⅆ^k ) ------------#
                            beta = (np.dot(np.transpose(self.evalgrad2(xk , self.function2)), Qdk))/dkt_Qdk
                            # ------- calculer la direction ⅆ^(k+1) = -∇f(x^(k+1)) + β_k * ⅆ^k --------#
                            dk = np.transpose(- self.evalgrad2(xk, self.function2) + beta*dk)
                            # -------- L'incrementation de k par 1 ---------#
                            k=k+1
                        x=xk
                        #--------- Affichage de la solution ----------#
                        self.varsolConjuGrad.set(x)
                        # --------- Affichage de nombre des iterations ----------#
                        self.var_sect_itir.set(k)
                        # --------- Affichage de l'interpretation  ----------#
                        self.var_iterpreSect.set("Conjugate-Gradian : la solution est trouvée avec succés !")
                 #-------------------En Cas de dimension 3--------------------------------------------------#
                 elif(self.valop.get()==3):
                     #------- recuperer la troisieme valeur de X0 ----------#
                     val3 = self.txt_valy3.get()
                     dim = 3
                     # ---------passage des valeurs initiales avec un casting en float-----------#
                     x1 = float(val1)
                     x2 = float(val2)
                     x3 = float(val3)
                     # -----------arrangement des valeurs initiales dans un seul vecteur---------#
                     x0 = np.array([x1, x2, x3])
                     xk = np.transpose(x0)
                     #---- inialiser la direction d0=-∇f(x0 )-----#
                     d0 = - self.evalgrad3(x0, self.function3)
                     dk = d0
                     #------ definir la matrice Q qu'est la matrice Hessien, car f est de class C2--------#
                     Q = self.hessien3(self.function3)
                     #----- Debut de la boucle for -------------#
                     for k in range(dim - 1):
                         # -------- calcule de dk transpose -------#
                         dkt = np.transpose(dk)
                         # -------- si dk = 0 impossible d'apppliquer l'algorithme ---------#
                         vect3Nul= np.array([0, 0, 0])
                         if (dkt[0] == vect3Nul[0] and dkt[1] == vect3Nul[1] and dkt[2] == vect3Nul[2] ):
                             MessageBox.showerror("Error", " Impossible d'apppliquer l'algorithme si la direction dk est nul", parent=self.fenetr8)
                         #------- calcul de Transpo(ⅆ^k) * ⅆ^k ------------#
                         dkt_dk = np.dot(dkt, dk)
                         print("dkt_dk=", dkt_dk)
                         # ------- calcul de Q * ⅆ^k ------------#
                         Qdk = np.dot(Q, dk)
                         print("Qdk=",Qdk)
                         # ------- calcul de Transpo(ⅆ^k) * Q * ⅆ^k ------------#
                         dkt_Qdk = np.dot(np.transpose(dk), Qdk)
                         # ------- calcul de      α_k =  (Transpo(ⅆ^k) * ⅆ^k)/(Transpo(ⅆ^k) * Q *ⅆ^k ) ------------#
                         alpha = dkt_dk / dkt_Qdk
                         # ------- calcul de x^(k+1) = x^k + α_k * ⅆ^k ------------#
                         xk = xk + alpha * dk
                         # ------- calcul de β_k=  (Transpo(∇f(x^k )) * Q * ⅆ^k) / (Transpo(ⅆ^k) * Q * ⅆ^k ) ------------#
                         beta = (np.dot(np.transpose(self.evalgrad3(xk, self.function3)), Qdk)) / dkt_Qdk
                         # ------- calculer la direction ⅆ^(k+1) = -∇f(x^(k+1)) + β_k * ⅆ^k --------#
                         dk = - self.evalgrad3(xk, self.function3) + beta * dk
                         #-------- L'incrementation de k par 1 ---------#
                         k = k + 1
                     x = xk
                     # --------- Affichage de la solution ----------#
                     self.varsolConjuGrad.set(x)
                     # --------- Affichage de nombre des iterations ----------#
                     self.var_sect_itir.set(k)
                     # --------- Affichage de l'interpretation  ----------#
                     self.var_iterpreSect.set("Conjugate-Gradian : la solution est trouvée avec succés !")

             except Exception as es:
                MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetr8)


    
  
  
    #---------------Le gghaphe de la fonction--------------#
    def graphe_de_fonction(self):
            fonc = self.tcrrft.get()
            if(fonc =="" ):
                MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetr8)
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
                    MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetr8) 
                   
            elif(self.valop.get() == 3):
                 pass
                 #---le graphe de fonction 3D --------------------#
  
    


# fenet = Tk()
# obj = ConjugateGradient(fenet)
# fenet.mainloop()





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


l = "false"
class NewtonMultivar :
    
  def __init__(self,fenetre9):
        self.fenetre9=fenetre9
        #-----------le titre--------------------------------------------------#
        self.fenetre9.title(" Newthon ")
        #-----------------la geometrerde la fenetre---------------------------#
        self.fenetre9.geometry("1000x720+150+50")
        #-----------------le coleure de bag-----------------------------------#
        self.fenetre9.config(bg="#88A780")   
        #-----------bloquer le redimentionnement de la fenetre----------------# 
        self.fenetre9.resizable(width=False, height=False)
        #--------------logo de l'application----------------------------------#
        self.fenetre9.iconbitmap("images/logoimag.ico")
        #==============self.frame1  ===============================================#
        self.frame1 = Frame( self.fenetre9, bg="#88A780", highlightbackground="#DCE5D9",highlightthickness=2)
        self.frame1.place(x=48,y=30, height=660,width=900)
        #===============title=================================================#
        title = Label( self.fenetre9,text=" Newthon ",font=("Comic Sans MS", 17,"bold"), bg="#88A780",fg="#DCE5D9").place(x=405,y=5)
       
        #----------------les entrer de l'algorithme---------------------------#
        entrer = Label(self.frame1,text="Input { ",font=("Comic Sans MS", 16,"bold"), bg="#88A780",fg="#182350").place(x=10,y=10)
        
        #======================l'order  =======================================#
        lorder = Label(self.frame1,text="The dimension       :",font=("Comic Sans MS", 15,"bold"), bg="#88A780").place(x=110,y=10)
        
        #---------------------------------------------------------------------#
        self.valop = IntVar() 
        self.cmb_lorder = ttk.Combobox(self.frame1, font=("times new romman", 13,"bold"),state='readonly',justify=CENTER, textvariable=self.valop)
        self.cmb_lorder['values']=(" 2 "," 3 ")
        self.cmb_lorder.place(x=440, y=13,width=160)
        self.cmb_lorder.current(0)
        
         #--------------------------------le choix de pas---------------------#
        labdepas = Label(self.frame1,text="Line Search          :",font=("Comic Sans MS", 15,"bold"), bg="#88A780").place(x=110,y=50)
        
        self.valdespas = StringVar() 
        self.cmb_pad = ttk.Combobox(self.frame1, font=("times new romman", 13,"bold"),state='readonly',justify=CENTER, textvariable=self.valdespas)
        self.cmb_pad['values']=("Fixe","Approcher", "Optimal")
        self.cmb_pad.place(x=440, y=53,width=160)
        self.cmb_pad.current(0)
        
        #--------------------le pas fix---------------------------------------#
        self.var_fixe = IntVar()
        self.txt_fixe_Sect= Entry(self.frame1,font=("times new romman",14,"bold"),  bg="lightgray", fg="#182350", textvariable=self.var_fixe)
        self.txt_fixe_Sect.place(x=660, y=53,width=190)
        self.var_fixe.set(1)
        
        #-----------------button ----------------------------------------------------#
        Order_Button  = Button(self.frame1,font=("times new romman",12, "bold"),text="dimension", bg="#CBDDDD", activebackground ="#3E574F", activeforeground="#A22B2B",borderwidth = 2, command =self.changdim).place(x=660 ,y=130,width=190)
        #=================l'intervale ========================================#
        intervale = Label(self.frame1,text="Le point initiale x0  :",font=("Comic Sans MS", 15,"bold"),bg="#88A780").place(x=110,y=110)
        
        #================vale de x1 ==========================================#
        self.txt_val = Label(self.frame1,text="x[0]  ",font=("Comic Sans MS", 15,"bold"),bg="#88A780").place(x=385,y=90)
        self.txtvar = DoubleVar()
        self.txt_valx = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable= self.txtvar)
        self.txt_valx.place(x=440,y=93,width=160)
        self.txtvar.set(1)
        
        
        #================la valeure de x2 =====================================#
        self.val_b = Label(self.frame1,text="x[1]  ",font=("Comic Sans MS", 15,"bold"),bg="#88A780").place(x=385,y=130)
        self.txttvarr = DoubleVar()
        self.txt_valy = Entry(self.frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.txttvarr)
        self.txt_valy.place(x=440,y=133,width=160)
        self.txttvarr.set(1)
       
        #===================la fonction=======================================#
        self.fonc = Label(self.frame1,text="Function             :",font=("Comic Sans MS", 16,"bold"),bg="#88A780").place(x=110,y=205)
        self.foncFtion = Label(self.frame1,text="f(x) = ",font=("Comic Sans MS", 16,"bold"),bg="#88A780").place(x=355,y=205)
        self.tcrrft = DoubleVar()
        self.txt_fonctin = Entry(self.frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350", textvariable= self.tcrrft)
        self.txt_fonctin.place(x=440,y=208,width=397 )
        self.tcrrft.set("x**2  + y**2")
        
        #================la tolérence  =======================================#
        self.delt = Label(self.frame1,text="Tolerance            :",font=("Comic Sans MS", 15,"bold"),bg="#88A780").place(x=110,y=280)
        self.delT = Label(self.frame1,text="delta =",font=("Comic Sans MS", 15,"bold"),bg="#88A780").place(x=360,y=280)
        self.tolerenfonc = DoubleVar()
        self.txt_toler = Entry(self.frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350", textvariable=self.tolerenfonc)
        self.tolerenfonc.set(0.01)
        self.txt_toler.place(x=440,y=283,width=160)
        
        
        #=================fermer l'accolade===================================#
        self.coladfer = Label(self.frame1,text=" } Output   :",font=("Comic Sans MS", 15,"bold"),bg="#88A780",fg="#182350").place(x=10,y=315)
        
        #==============self.frame1  ===============================================#
        self.frame2=Frame( self.frame1,bg="#C4C6C6" ,highlightbackground="#182350",highlightthickness=3)
        self.frame2.place(x=10,y=360,height=285,width=875)
        
        #=================================================solution ===========================================#
        #---------------la valeur exacte de la solution si l'algorithme arive a calculer x*--------------------------------#
        val_solution_exact = Label(self.frame2,text="The solution   ",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=10,y=10)
        #-----------------------------------------------x*-----------------------------------------------------------------#
        val_solNew = Label(self.frame2,text=" x*:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=240,y=10)
        self.varsolNeew = StringVar()
        self.txtSolExacNew = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="green", textvariable=self.varsolNeew)
        self.varsolNeew.set("")
        self.txtSolExacNew.place(x=190, y=13, width=670)
        
        
        #--------------------------------val des nomber des itoration  i ----------------------------------------#
        self.nbr_Sect_iteration = Label(self.frame2,text="Number of iterations ",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=80)
        self.txt_itera_Section = Label(self.frame2,text=" i :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=80)
        self.var_sect_itir = IntVar()
        self.txt_itera_Sect= Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="red", textvariable=self.var_sect_itir)
        self.var_sect_itir.set("")
        self.txt_itera_Sect.place(x=290,y=83,width=160)
      
        #---------------------------------------Solution----------------------------------------------------------#

        #---------------------------------------interprétation----------------------------------------------------#
        self.nbr_iterpretaSecti = Label(self.frame2,text="Interpretation   ",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=150)
        self.var_iterpreSect = StringVar()
        self.txt_iterpretatSect = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.var_iterpreSect)
        self.var_iterpreSect.set("")
        self.txt_iterpretatSect.place(x=165,y=153,width=690)

        #=========================================================== boutton  New =========================================================================================================#
        New_Button  = Button(self.frame2,font=("times new romman",16,"bold"),text="Newthon ",bd=0,cursor="hand2",bg="#7F7526",fg="#E5E1D6",activebackground ="#7AA1E6",activeforeground="#BF846C",borderwidth = 5, command =self.NewtonMulti).place(x=320 ,y=220,width=240)
           
       #============================================================ Bouton le graphe de la fonction ===========================================================================================#
        graphedefa= Button(self.frame2,font=("times new romman",16,"bold"),text="graph of the fonction",bd=0,cursor="hand2",bg="#7B9764",fg="#E5E1D6",activebackground ="#CDD3C8",activeforeground="#BFF790",borderwidth = 5, command=self.graphe_de_fonction).place(x=10 ,y=220,width=240)
        
     
        #============================================================ Bouton quitt ============================================================================================================#
        quitt= Button(self.frame2,font=("times new romman",16,"bold"),text="Quit ",bd=0,cursor="hand2", bg="#AD2E15", fg="#F3EEED",activebackground ="#CAE5E4",activeforeground="#E8A490",borderwidth = 5, command=self.quiter).place(x=640 ,y=220,width=220)
  
    
  #----une fonction pour changer la dimention-------------------------------#   
  def changdim(self):
        self.clearChamp()
        #---des variable globale pour gerer l'interface-----------------------#
        global txt_valx3
        global vardetext
        global l
       
        self.txtVarx3 = DoubleVar()
        #---si le dimension est egal a 3--------------------------------------#
        if(self.valop.get()==3):  
            l = "true"
            vardetext = StringVar() 
            txt_val = Label(self.frame1, font=("Comic Sans MS", 15,"bold"),bg="#88A780", textvariable= vardetext).place(x=385,y=170)
            vardetext.set("x[2]")
            txt_valx3 = Entry(self.frame1,font=("times new romman", 14,"bold"), bg="lightgray",fg="#182350", textvariable= self.txtVarx3)
            txt_valx3.place(x=440,y=173,width=160)
            self.txtVarx3.set("")
        #---si le dimension est egal a 2--------------------------------------#
        elif(self.valop.get() == 2):
            if(l == "true"):
                vardetext.set("")
                txt_valx3.destroy()
            else:
                return
       
            
             
    #-------------Pour quiter------------------------------------#       
  def quiter(self):
       self.fenetre9.destroy()
        
        
     #----------------pour vider les comps------------------------------------#
  def clearChamp(self):
        self.txtSolExacNew.delete(0, END)
        self.txt_itera_Sect.delete(0, END)
        self.txt_iterpretatSect.delete(0, END)
  
  def NewtonMulti (self):
      self.clearChamp()
      val1 = self.txt_valx.get() # la valeur de x0 initiale
      val2 = self.txt_valy.get() # la valeur de y0 initiale
      func = self.txt_fonctin.get()
      func = func.replace("x","x[0]") # dans cette partie on change la forme de la fonction
      func = func.replace("y","x[1]") # que l'utilisateur saisie pour pouvoire l'evaluer etc..
      func = func.replace("z","x[2]") # les variables x,y et z deviennent x[0],x[1] et x[2]
      func = func.replace("ex[0]p","exp")
      f = func
      delt = self.txt_toler.get()
      if(val1 =="" or val2 ==""  or func ==""  or delt =="" ):
           MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre7)
      else :
          try:
              # la methode newton avec deux variables
                    if(self.valop.get() == 2 ):
                        xun = float(val1)
                        xdeux = float(val2)
                        delta = float(delt)
                        xo = np.array([xun,xdeux]) # le point initiale
                        def fonction(x):
                            fonc = eval(f)
                            return fonc
                        x1 = sp.Symbol("x[0]")
                        x2 = sp.Symbol("x[1]")
                        xd = (x1,x2)
                        # calcule de la derivée première de la fonction f par rapport a x puis y
                        dervX1 = sp.diff(fonction(xd),x1)
                        dervX2 = sp.diff(fonction(xd),x2)
                        # calcule de la derivée seconde de la fonction f par rapport a xx , xy , yx , yy
                        dervSecX1 = sp.diff(fonction(xd),x1,x1)
                        dervSecX1X2 = sp.diff(fonction(xd),x1,x2)
                        dervSecX2X1 = sp.diff(fonction(xd),x2,x1)
                        dervSecX2 = sp.diff(fonction(xd),x2,x2)
                        # la fonction qui calcule le gradient
                        def gradF(x):
                              
                              deriverX1 = eval(str(dervX1)) # derivée par rapport a x
                              deriverX2 = eval(str(dervX2)) # derivée par rapport a y
                              gradF = np.array([deriverX1,deriverX2],float)
                              return gradF
                        # ma fonction qui calcule hessien
                        def hessien(x):
                              x1x1 = eval(str(dervSecX1)) # derivée par rapport a xx
                              x1x2 = eval(str(dervSecX1X2)) # derivée par rapport a xy
                              x2x1 = eval(str(dervSecX2X1)) # derivée par rapport a yx
                              x2x2 = eval(str(dervSecX2)) # derivée par rapport a yy
                              H = np.mat([[x1x1,x1x2],[x2x1,x2x2]],float)
                              return H
                        # fonction qui donne l'inverse du hessien en verifiant s'il est définie positive ou pas
                        def inverseH(H):
                              if(verifierDP(H)):
                                  inverse = np.linalg.inv(H)
                              else:
                                  inverse = np.linalg.inv(0.1*np.eye(2)+H)
                              return inverse
                        # la verification qu'une matrice est définie positive pa le calcule des valeurs propres
                        def verifierDP(H):
                              valProp = np.linalg.eigvals(H)
                              result = True
                              if(valProp[0] > 0 and valProp[1] > 0):
                                  result = True
                              else:
                                  result = False
                              return result
                        # la direction de descente initiale
                        directionk = -1 * np.dot(inverseH(hessien(xo)) , gradF(xo))
                        normed = np.linalg.norm(directionk)
                        k = 0
                        # le premier cas avec un pas alpha0 fixe
                        if( self.valdespas.get()=="Fixe"):
                                nbrAlpha = self.txt_fixe_Sect.get()
                                if( nbrAlpha == ""):
                                      MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre9)
                                else:
                                    if(verifierDP(hessien(xo))):
                                        while(normed > delta):
                                            alpha = float(nbrAlpha)
                                            xk = xo + alpha * directionk
                                            xo = np.array(xk).flatten()
                                            
                                            directionk = -1 * np.dot(inverseH(hessien(xo)) , gradF(xo))
                                            normed = np.linalg.norm(directionk)
                                            k = k + 1
                                            
                                        sol =  xo.flatten()
                                        self.varsolNeew.set(sol)
                                        self.var_sect_itir.set(k)
                                        self.var_iterpreSect.set("la solution est trouvée avec succés par le pas Fixe : "+str(nbrAlpha))
                                    else :
                                        MessageBox.showerror("Error"," La fonction n'est pas définie positrive", parent=self.fenetre9)
                        # deuxieme cas avec le pas optimale où on a utiliser fiboncci et newton-raphson
                        if( self.valdespas.get()=="Optimal"):
                                    self.txt_fixe_Sect.delete(0, END)
                                    if(verifierDP(hessien(xo))):
                                        while(normed > delta):
                                            
                                            xalpha = sp.Symbol('x')
                                            falpha = xo + xalpha * directionk
                                            falpha = np.array(falpha).flatten()
                                            fonc = fonction(falpha)
                                            voizn = self.fibonacci(0, 10, str(fonc), 100)
                                            print("voizn fibonacci = ", voizn)
                                            alpha = self.newtonraphson(voizn, str(fonc), 0.01, 100)
                                            print("le pas optimal dans l'itération  "+str(k+1)+"  est : ", alpha)
                                            xk = xo + alpha * directionk
                                            xo = np.array(xk).flatten()
                                            
                                            directionk = -1 * np.dot(inverseH(hessien(xo)) , gradF(xo))
                                            normed = np.linalg.norm(directionk)
                                            k = k + 1
                                            
                                        sol =  xo.flatten()
                                        self.varsolNeew.set(sol)
                                        self.var_sect_itir.set(k)
                                        self.var_iterpreSect.set("la solution est trouvée avec succés par le pas Optimal:Fibonacci-Newton")
                                    else :
                                        MessageBox.showerror("Error"," La fonction n'est pas définie positrive", parent=self.fenetre9)
                        # Troisieme cas où on va calculer le pas par la régle d'armijo
                        elif(self.valdespas.get() =="Approcher") :
                                self.txt_fixe_Sect.delete(0, END)
                                alpha = 2
                                epsil = 0.1
                                nu = 3
                                alphak = alpha
                                if(verifierDP(hessien(xo))):
                                    while(normed > delta):
                                        xalpha = sp.Symbol('x')
                                        falpha = xo + xalpha * directionk
                                        falpha = np.array(falpha).flatten()
                                        fonc = str(fonction(falpha))
                                        def phy(x):
                                          p = eval(fonc)
                                          return p
                                        deriv1 = sp.diff(phy(xalpha),xalpha)
                                        def deriv1er(x):
                                          deriv1er = eval(str(deriv1))
                                          return deriv1er
                                        # verification de la condition 3 définie dans l'algorithme
                                        if phy(alphak) <= epsil * deriv1er(0) + phy(0) :
                                          while phy(nu * alphak) <= phy(0) + epsil * deriv1er(0) * nu * alphak :
                                            alphak = nu * alphak
                                            k = k+1
                                        # 3 n'est pas verifier alors 4 est verifier
                                        else:
                                          while phy(alphak) > epsil * alphak * deriv1er(0) + phy(0):
                                            alphak = alphak / nu
                                            k = k+1
                                        alpha = alphak
                                        directionk = -1 * np.dot(inverseH(hessien(xo)) , gradF(xo))
                                        normed = np.linalg.norm(directionk)
                                        k = k + 1
                                        
                                        xk = xo + alpha * directionk
                                        xo = np.array(xk).flatten()
                                    sol =  xo.flatten()
                                    self.varsolNeew.set(sol)
                                    self.var_sect_itir.set(k)
                                    self.var_iterpreSect.set("la solution est trouvée avec succés par le pas Approcher : Armijo ")
                                else :
                                    MessageBox.showerror("Error"," La fonction n'est pas définie positrive", parent=self.fenetre9)
                    # Newton pour 3 variables, même principe qu'on a utiliser pour newton 2 variables
                    elif(self.valop.get() == 3 ):
                        val3 = txt_valx3.get()
                        if(val3 == ""):
                            MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre7)
                        else:
                            xun = float(val1)
                            xdeux = float(val2)
                            xtrois = float(val3)
                            delta = float(delt)
                            xo = np.array([xun,xdeux,xtrois])
                            print(xo)
                            def fonction(x):
                                fonc = eval(f)
                                return fonc
                            x1 = sp.Symbol("x[0]")
                            x2 = sp.Symbol("x[1]")
                            x3 = sp.Symbol("x[2]")
                            xd = (x1,x2,x3)
                            dervX1 = sp.diff(fonction(xd),x1) # par rapport a x
                            dervX2 = sp.diff(fonction(xd),x2) # par rapport a y
                            dervX3 = sp.diff(fonction(xd),x3) # par rapport a z
            
                            dervSecX1 = sp.diff(fonction(xd),x1,x1) # par rapport a xx
                            dervSecX1X2 = sp.diff(fonction(xd),x1,x2) # par rapport a xy
                            dervSecX1X3 = sp.diff(fonction(xd),x1,x3) # par rapport a xz
                            dervSecX2X1 = sp.diff(fonction(xd),x2,x1) # par rapport a yx
                            dervSecX2 = sp.diff(fonction(xd),x2,x2) # par rapport a yy
                            dervSecX2X3 = sp.diff(fonction(xd),x2,x3) # par rapport a yz
                            dervSecX3X1 = sp.diff(fonction(xd),x3,x1) # par rapport a zx
                            dervSecX3X2 = sp.diff(fonction(xd),x3,x2) # par rapport a zy
                            dervSecX3 = sp.diff(fonction(xd),x3,x3) # par rapport a zz
                            
                            def gradF(x):
            
                                deriverX1 = eval(str(dervX1))
                                deriverX2 = eval(str(dervX2))
                                deriverX3 = eval(str(dervX3))
                                gradF = np.array([deriverX1,deriverX2,deriverX3],float)
                                # print(gradF)
                                return gradF
                            def hessien(x):
                                x1x1 = eval(str(dervSecX1))
                                x1x2 = eval(str(dervSecX1X2))
                                x1x3 = eval(str(dervSecX1X3))
                                x2x1 = eval(str(dervSecX2X1))
                                x2x2 = eval(str(dervSecX2))
                                x2x3 = eval(str(dervSecX2X3))
                                x3x1 = eval(str(dervSecX3X1))
                                x3x2 = eval(str(dervSecX3X2))
                                x3x3 = eval(str(dervSecX3))
                                H = np.mat([[x1x1,x1x2,x1x3],[x2x1,x2x2,x2x3],[x3x1,x3x2,x3x3]],float)
                                # print(H)
                                return H
                            def inverseH(H):
                                  if(verifierDP(H)):
                                      inverse = np.linalg.inv(H)
                                  else:
                                      inverse = np.linalg.inv(0.1*np.eye(3)+H)
                                  return inverse
                            def verifierDP(H):
                                valProp = np.linalg.eigvals(H)
                                result = True
                                if(valProp[0] > 0 and valProp[1] > 0 and valProp[2] > 0):
                                    result = True
                                else:
                                    result = False
                                return result
                            directionk = -1 * np.dot(inverseH(hessien(xo)) , gradF(xo))
                            normed = np.linalg.norm(directionk)
                            k = 0
                            if( self.valdespas.get()=="Fixe"):
                                    nbrAlpha = self.txt_fixe_Sect.get()
                                    if( nbrAlpha == ""):
                                          MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre9)
                                    else:
                                        if(verifierDP(hessien(xo))):
                                            while(normed > delta):
                                                alpha = float(nbrAlpha)
                                                xk = xo + alpha * directionk
                                                xo = np.array(xk).flatten()
                                                
                                                directionk = -1 * np.dot(inverseH(hessien(xo)) , gradF(xo))
                                                normed = np.linalg.norm(directionk)
                                                k = k + 1
                                                
                                            sol =  xo.flatten()
                                            self.varsolNeew.set(sol)
                                            self.var_sect_itir.set(k)
                                            self.var_iterpreSect.set("la solution est trouvée avec succés par le pas Fixe : "+str(nbrAlpha))
                                        else :
                                            MessageBox.showerror("Error"," La fonction n'est pas définie positrive", parent=self.fenetre9)
                            if( self.valdespas.get()=="Optimal"): 
                                        self.txt_fixe_Sect.delete(0, END)                               
                                        if(verifierDP(hessien(xo))):
                                            while(normed > delta):
                                                
                                                xalpha = sp.Symbol('x')
                                                falpha = xo + xalpha * directionk
                                                falpha = np.array(falpha).flatten()
                                                fonc = fonction(falpha)
                                                voizn = self.fibonacci(0, 10, str(fonc), 100)
                                                print("voizn fibonacci = ", voizn)
                                                alpha = self.newtonraphson(voizn, str(fonc), 0.01, 100)
                                                print("le pas optimal dans l'itération  "+str(k+1)+"  est : ", alpha)
                                                xk = xo + alpha * directionk
                                                xo = np.array(xk).flatten()
                                                
                                                directionk = -1 * np.dot(inverseH(hessien(xo)) , gradF(xo))
                                                normed = np.linalg.norm(directionk)
                                                k = k + 1
                                                
                                            sol =  xo.flatten()
                                            self.varsolNeew.set(sol)
                                            self.var_sect_itir.set(k)
                                            self.var_iterpreSect.set("la solution est trouvée avec succés par le pas Optimal:Fibonacci-Newton")
                                        else :
                                            MessageBox.showerror("Error"," La fonction n'est pas définie positrive", parent=self.fenetre9)
                            elif(self.valdespas.get() =="Approcher") :
                                    self.txt_fixe_Sect.delete(0, END)
                                    alpha = 2
                                    epsil = 0.1
                                    nu = 3
                                    alphak = alpha
                                    if(verifierDP(hessien(xo))):
                                        while(normed > delta):
                                            xalpha = sp.Symbol('x')
                                            falpha = xo + xalpha * directionk
                                            falpha = np.array(falpha).flatten()
                                            fonc = str(fonction(falpha))
                                            def phy(x):
                                              p = eval(fonc)
                                              return p
                                            deriv1 = sp.diff(phy(xalpha),xalpha)
                                            def deriv1er(x):
                                              deriv1er = eval(str(deriv1))
                                              return deriv1er
                                            # verification de la condition 3 définie dans l'algorithme
                                            if phy(alphak) <= epsil * deriv1er(0) + phy(0) :
                                              while phy(nu * alphak) <= phy(0) + epsil * deriv1er(0) * nu * alphak :
                                                alphak = nu * alphak
                                                k = k+1
                                            # 3 n'est pas verifier alors 4 est verifier
                                            else:
                                              while phy(alphak) > epsil * alphak * deriv1er(0) + phy(0):
                                                alphak = alphak / nu
                                                k = k+1
                                            alpha = alphak
                                            directionk = -1 * np.dot(inverseH(hessien(xo)) , gradF(xo))
                                            normed = np.linalg.norm(directionk)
                                            k = k + 1
                                            
                                        sol =  xo.flatten()
                                        self.varsolNeew.set(sol)
                                        self.var_sect_itir.set(k)
                                        self.var_iterpreSect.set("la solution est trouvée avec succés par le pas Approcher : Armijo")

          except Exception as es:                  
              MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre9) 
  
  #----------Fibonacci -------------------------------------------------------#
  # La méthode de fibonacci qu'on utiliser pour trouver le voisinage du minimum
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
            # la suite de fibonacci
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
                        return xmin
                        break
                    else:
                        k = k + 1
         
  #------------Newton-------------------------------------------------------#
  # la méthode de newton qu'on itiliser pour trouver le minimum
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
                  break
                  return xk
      if(f2 > 0):
          return xk
      elif(f2 < 0):
          return xk


 #======================Le gghaphe de la fonction==========================#   
  def graphe_de_fonction(self):
         fonc = self.txt_fonctin.get()
         if(fonc =="" ):
             MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre7)
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
                 MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre7) 
                
         elif(self.valop.get() == 3):
              pass
              #---le graphe de fonction 3D --------------------#
            
     

fenetre9=Tk()
obj=NewtonMultivar(fenetre9)
fenetre9.mainloop() 

from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
import numpy as np
from scipy import misc 
import matplotlib.pyplot as plt
import math

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler

from matplotlib.figure import Figure



class NewtonClasse :
    def __init__(self,fenetre5):
        self.fenetre5=fenetre5
        #-----------le titre--------------------------------------------------#
        self.fenetre5.title("Newton Search")
        #-----------------la geometrerde la fenetre---------------------------#
        self.fenetre5.geometry("1000x720+150+50")
        #-----------------le coleure de bag-----------------------------------#
        self.fenetre5.config(bg="#95A0A3")   
        #-----------bloquer le redimentionnement de la fenetre----------------# 
        self.fenetre5.resizable(width=False, height=False)
        #--------------logo de l'application----------------------------------#
        self.fenetre5.iconbitmap("images/logoimag.ico")
        
        #==============Frame1  ===============================================#
        frame1=Frame( self.fenetre5, bg="#95A0A3", highlightbackground="#BBDD3E",highlightthickness=2)
        frame1.place(x=45,y=40,height=660,width=900)
        #===============title=================================================#
        title = Label( self.fenetre5,text="Newton Search",font=("Comic Sans MS", 17,"bold"), bg="#95A0A3",fg="#BBDD3E").place(x=400,y=5)
       
        #----------------les entrer de l'algorithme---------------------------#
        entrer = Label(frame1,text="Input { ",font=("Comic Sans MS", 15,"bold"), bg="#95A0A3",fg="#182350").place(x=10,y=10)
        
        #=================l'intervale ========================================#
        intervale = Label(frame1,text="The interval [a , b]   :",font=("Comic Sans MS", 15,"bold"),bg="#95A0A3").place(x=110,y=20)
        
        #================vale de a ===========================================#
        val_a = Label(frame1,text=" a :",font=("Comic Sans MS", 15,"bold"),bg="#95A0A3").place(x=400,y=20)
        self.txt_val_a = Entry(frame1,font=("times new romman",16,"bold"), bg="lightgray",fg="#182350")
        self.txt_val_a.place(x=440,y=23,width=160)
        
        #================la valeure de b =====================================#
        val_b = Label(frame1,text=" b :",font=("Comic Sans MS", 15,"bold"),bg="#95A0A3").place(x=630,y=20)
        self.txt_val_b = Entry(frame1,font=("times new romman",16,"bold"), bg="lightgray",fg="#182350")
        self.txt_val_b.place(x=675,y=23,width=160)
        
        #===================la fonction=======================================#
        fonc = Label(frame1,text="Function               : ",font=("Comic Sans MS", 16,"bold"),bg="#95A0A3").place(x=110,y=80)
        foncF = Label(frame1,text="f(x)  =",font=("Comic Sans MS", 16,"bold"),bg="#95A0A3").place(x=360,y=80)
        self.txt_fonc = Entry(frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350")
        self.txt_fonc.place(x=440,y=83,width=397 )
        
        #================la tolérence  =======================================#
        delta = Label(frame1,text="Tolerance              :",font=("Comic Sans MS", 15,"bold"),bg="#95A0A3").place(x=110,y=140)
        delTTa = Label(frame1,text="delta =",font=("Comic Sans MS", 15,"bold"),bg="#95A0A3").place(x=360,y=140)
        self.defouitDelta = DoubleVar()
        self.txt_delta = Entry(frame1,font=("times new romman", 16,"bold"), bg="lightgray",fg="#182350", textvariable=self.defouitDelta)
        self.defouitDelta.set(0.001)
        self.txt_delta.place(x=440,y=143,width=160)
        
        #===================Nomber d'etiration max============================#
        nbriteramax = Label(frame1,text="Number of iterations :",font=("Comic Sans MS", 15,"bold"),bg="#95A0A3").place(x=110,y=200)
        nbriteramax = Label(frame1,text="imax =",font=("Comic Sans MS", 15,"bold"),bg="#95A0A3").place(x=360,y=200)
        self.txt_nbriteramax = Entry(frame1,font=("times new romman", 16,"bold"), bg="lightgray",fg="#182350")
        self.txt_nbriteramax.place(x=440,y=203,width=160)
        
        #==============self.frame2  ==========================================#
        self.frameVois=Frame( frame1,bg="#C4C6C6" ,highlightbackground="#BBDD3E",highlightthickness=2)
        self.frameVois.place(x=10,y=260,height=100,width=875)
        #-----------------------la recherche de voisinage x0------------------#
        val_Voisin = Label(self.frameVois,text="La recherche de voisinage     :   xzero : ",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=10,y=0)
        #---------------------------------------------------------------------#
        self.varVoisin = DoubleVar()
        self.txt_voisi_newton = Entry(self.frameVois, font=("times new romman",16,"bold"), bg="lightgray",fg="green", textvariable=self.varVoisin)
        self.txt_voisi_newton.place(x=430, y=5, width=370)
        self.varVoisin.set("")
        
        #=================fermer l'accolade===================================#
        coladfer = Label(frame1,text=" } Output   :",font=("Comic Sans MS", 15,"bold"),bg="#95A0A3",fg="#182350").place(x=10,y=360)
        
        #==============Frame1  ===============================================#
        self.frame2=Frame( frame1,bg="#C4C6C6" ,highlightbackground="#BBDD3E",highlightthickness=3)
        self.frame2.place(x=10,y=400,height=250,width=875)
        
        #---------------la valeur exacte de la solution si l'algorithme arive a calculer x*--------------------------------#
        val_solNewton_exact = Label(self.frame2,text="The solution          :",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=10,y=10)
        #-----------------------------------------------x*-----------------------------------------------------------------#
        val_x_solNewton = Label(self.frame2,text=" x*:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=247,y=10)
        self.varsolutionNewton = DoubleVar()
        self.txt_solution_Newton = Entry(self.frame2,font=("times new romman",17,"bold"), bg="lightgray",fg="green", textvariable=self.varsolutionNewton)
        self.varsolutionNewton.set("")
        self.txt_solution_Newton.place(x=290, y=13, width=300)
        
        #--------------------------------val des nomber des itoration  i Bissection----------------------------------------#
        nbr_itera_Newton = Label(self.frame2,text="Number of iterations:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=70)
        self.val_itera_newton = Label(self.frame2,text=" i :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=70)
        self.var_Newton_itir = IntVar()
        self.txt_itera_Newton = Entry(self.frame2,font=("times new romman",17,"bold"), bg="lightgray",fg="red", textvariable=self.var_Newton_itir)
        self.var_Newton_itir.set("")
        self.txt_itera_Newton.place(x=290,y=73,width=300)
          
        #---------------------------------------interprétation---------------------------------------------------------------#
        nbr_iterpretatNewton = Label(self.frame2,text="Interpretation        :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=130)
        self.var_iterpreNewton = StringVar()
        self.txt_iterpretaNewton = Entry(self.frame2,font=("times new romman",16,"bold"), bg="lightgray",fg="#182350", textvariable=self.var_iterpreNewton)
        self.var_iterpreNewton.set("")
        self.txt_iterpretaNewton.place(x=290,y=133,width=550)
        
        #=========================================================== boutton Fibonaccipour la recherche de voisinage ====================================================================================================#
        Fibonacci_Button  = Button(self.frameVois,font=("times new romman",14,"bold"),text=" Fibonacci ",bd=0,cursor="hand2",bg="#B0C2C6", activebackground ="#7AA1E6",activeforeground="#BF846C",borderwidth = 2, command =self.fibonacciNewton).place(x=50 ,y=50,width=150)
          
        #============================================================ boutton Dichotomique la recherche de voisinage ====================================================================================================#
        dico_button = Button(self.frameVois,font=("times new romman",14,"bold"),text=" Dichotomous ",bd=0,cursor="hand2",bg="#B0C2C6" , activebackground ="#BFB3B5",activeforeground="#E5E1D6",borderwidth = 2,command=self.dichotomiqueNewton).place(x=250 ,y=50,width=150)
        
        #=========================================================== boutton Section d'or la recherche de voisinage =====================================================================================================#
        SectionDor_Button  = Button(self.frameVois,font=("times new romman",14,"bold"),text=" Section d'or ",bd=0,cursor="hand2",bg="#B0C2C6", activebackground ="#7AA1E6",activeforeground="#BF846C",borderwidth = 2, command =self.SectionDoreeNewton).place(x=450 ,y=50,width=150)
        
        #============================================================ Bouton Bissection la recherche de voisinage =======================================================================================================#
        Bissection_boutton = Button(self.frameVois,font=("times new romman",14,"bold"),text=" Bissection ",bd=0,cursor="hand2",bg="#B0C2C6", activebackground ="#AFAF0D",activeforeground="#0F5A7D",borderwidth = 2, command=self.BissectionNewton).place(x=650 ,y=50,width=150)
        
        
        #============================================================ Newten ============================================================================================================================================#
        Newten_boutten = Button(self.frame2,font=("times new romman",16,"bold"),text=" Newton ",bd=0,cursor="hand2",bg="#CD6C44",fg="#E5E1F7",activebackground ="#888C0C",activeforeground="#0575B0",borderwidth = 5,command=self.Newton).place(x=320 ,y=180,width=240)
        
        graphe= Button(self.frame2,font=("times new romman",16,"bold"),text="graph of the fonction",bd=0,cursor="hand2",bg="#7B9764",fg="#E5E1D6",activebackground ="#CDD3C8",activeforeground="#BFF790",borderwidth = 5, command=self.graphe_de_fonction).place(x=10 ,y=180,width=240)
        
        #============================================================ Bouton quit ============================================================================================================#
        quitbutton = Button(self.frame2,font=("times new romman",16,"bold"),text="Quit ",bd=0,cursor="hand2",bg="#811000",fg="#F9F2F1",activebackground ="#CAE5E4",activeforeground="#E8A490",borderwidth = 5, command=self.quiter).place(x=640 ,y=180,width=200)
        
        
    #-------------Pour quiter-------------------------------------------------#       
    def quiter(self):
       self.fenetre5.destroy()
    
    
    #----------------pour vider les champes-----------------------------------#
    def clearChamp(self):
        self.txt_solution_Newton.delete(0, END)
        self.txt_itera_Newton.delete(0, END)
        self.txt_iterpretaNewton.delete(0, END) 
        
        
        
  #--------------------fibonacci----------------------------------------------#
    def fibonacciNewton(self):
         self.clearChamp()
         self.txt_voisi_newton.delete(0, END)
         val1 = self.txt_val_a.get()
         val2 = self.txt_val_b.get()
         fon = self.txt_fonc.get()
         maxde_i = self.txt_nbriteramax.get()
         if(val1 =="" or val2 ==""  or fon =="" or maxde_i =="" ):
             MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre5)
         
         else:
              try:                  
                  a = float(val1)
                  b = float(val2)
                  max_iteratin = int(maxde_i)
                  if(a > b):
                      MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre5)
                  else:
                      def f(x):
                          y = eval(fon)
                          return y 
                         
                      fprimde_a = misc.derivative(f, a, dx=1.0, n=1, args=(), order=3) - 1
                      fprimde_b = misc.derivative(f, b, dx=1.0, n=1, args=(), order=3) - 1
                      
                      if(fprimde_a < 0 and  fprimde_b > 0):
                            plt.clf()
                            y = np.linspace(a, b, 1000)
                            j=1
                            #====la fonction est unimodal donc ok==================#
                            #-------- la suit de fibonacci------------------------#
                            def fib(n):
                                if n <= 1:
                                    return n
                                else:
                                    return fib(n - 1) + fib(n - 2)
                                 
                            fib_N = fib(max_iteratin)
                            fib_Nplus1 = fib(max_iteratin + 1)
                            fib_Nplus2 = fib(max_iteratin + 2)
                            #----------------d1--------------
                            d1 = abs(b - a)
                            
                            #------la calcule de x1 et x2-----------------------------
                            x1 = (fib_N / fib_Nplus2) * d1 + a
                            x2 = ( fib_Nplus1 / fib_Nplus2 )* d1 + a
                            
                            #____________________la boucle for _______________________
                            for i in range(1, max_iteratin):
                                if( f(x2) > f(x1) ):
                                    b = x2
                                    x2 = x1
                                    x1 = ((a * fib(max_iteratin - i + 1) + b * fib( max_iteratin - i)) / fib(max_iteratin - i + 2))
                                    j =j+1
                                else:
                                    a = x1
                                    x1 = x2
                                    x2 = ((b * fib(max_iteratin - i + 1) + a * fib(max_iteratin - i)) / fib(max_iteratin - i + 2))
                                    j = j+1
                                
                            #-----------------------------------------------------#       
                            x2 = x2 + 0.001
                            if(f(x2) > f(x1)): 
                                if(abs(a)< abs(x2)):
                                    xzero = a
                                else:
                                    xzero = x2
                            else: 
                                if(abs(b)< abs(x2)):
                                    xzero = b
                                else:
                                    xzero = x1
                           #===============retourn la valeur de xzero=============# 
                            self.varVoisin.set(xzero)  
                            self.var_iterpreNewton.set("Fibonacci : le voisinage est trouver avec succée! ")
                                    
                      else:
                           MessageBox.showwarning("Error","On ne peut pas Appliquer algorithme de Fibonacci sur cette fonction dans ces deux points. par ce que ona f'(a)*f'(b) > 0 !!",parent=self.fenetre5)
                           self.var_iterpreNewton.set("Fibonacci ne fonction pa car f'(a)*f'(b) > 0")
              except Exception as es:                  
                   MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre5)
  
    
  
    
  
     #=====================================Algorithme Dichotomique pour le voisinage=================================#
    def dichotomiqueNewton(self):
                 self.clearChamp()
                 self.txt_voisi_newton.delete(0, END)
                 val1 = self.txt_val_a.get()
                 val2 = self.txt_val_b.get()
                 deltta = self.txt_delta.get()
                 fonct = self.txt_fonc.get()
                 i_max = self.txt_nbriteramax.get()
                 if(val1 =="" or val2 =="" or deltta =="" or fonct =="" or i_max =="" ):
                     MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre5)

                 else:  
                     try:                  
                         a = float(val1)
                         b = float(val2)
                         delta = float(deltta)
                         itermax = int(i_max)
                         c = abs(b - a)
                         if(a > b):
                             MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre5)
                         else :
                                def f(x):
                                    y = eval(fonct)
                                    return y
                                
                                fpr_a = misc.derivative(f, a, dx=1.0, n=1, args=(), order=3) - 1
                                fpr_b = misc.derivative(f, b, dx=1.0, n=1, args=(), order=3) - 1
                                
                                if(fpr_a * fpr_b <= 0):
                                    i=1
                                    j=1001
                                    k=999
                                    while(c > delta and i < itermax):
                                        x = (a + b)/2
                                        fprim_x = misc.derivative(f, x, dx=1.0, n=1, args=(), order=3) - 1
                                        
                                        if(fpr_a * fprim_x < 0):
                                            b = x
                                        if(fpr_b * fprim_x <0):
                                            a = x
                                            
                                        if(j == a and k == b):
                                            break
                                        else:
                                            j = a
                                            k = b
                                            i+=1
       
                                        xzero = ((a+b)/2)+0.01
                                    
                                    self.varVoisin.set(xzero) 
                                    self.var_iterpreNewton.set("dichotomique :le voisinage est trouver avec succée! ")
                                else: 
                                    MessageBox.showwarning("Error","On ne peut pas Appliquer algorithme de Dichotomique sur cette fonction dans ces deux points. par ce que ona f'(a)*f'(b) > 0 !!",parent=self.fenetre5)
                                    self.var_iterpreNewton.set("Dichotomique ne fonction car : f'(a)*f'(b) > 0 !")
                             
                     except Exception as es:                  
                             MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre5)  
  
    
   #===================================Algorithme de Section dorée =========================================================================#
    def SectionDoreeNewton(self):
         self.clearChamp()
         self.txt_voisi_newton.delete(0, END)
         #==============les entrer de l'algorithme============================#
         val1 = self.txt_val_a.get()
         val2 = self.txt_val_b.get()
         fon = self.txt_fonc.get()
         deltta = self.txt_delta.get()
         if(val1 =="" or val2 ==""  or fon ==""  or deltta =="" ):
             MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre5)
         
         else:
              try:   
                  a = float(val1)
                  b = float(val2)
                  delta = float(deltta)
                  if(a > b):
                      MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre5)
                  else:
                      def f(x):
                          y = eval(fon)
                          return y 
                         
                      fprimde_a = misc.derivative(f, a, dx=1.0, n=1, args=(), order=3) - 1
                      fprimde_b = misc.derivative(f, b, dx=1.0, n=1, args=(), order=3) - 1
                      
                      if(fprimde_a < 0 and  fprimde_b > 0):
            
                          #---------initialisation de deux var nous permettent de sortie dans la boucle si l'intervale ne change pas ---------------#
                          j=100.01
                          i=199.0
                          #-------------nomber d'or--------------#
                          to = 0.5*(math.sqrt(5) - 1)
                          #-----début-----------------------------#
                          k = 1
                          d1 = abs(b - a)
                          x1 = a + (1 - to) * d1
                          x2 = a + to * d1
                          #------------------- la boucle while---------------------#
                          while( abs(b - a) > delta):
                              if( f(x1) > f(x2)):
                                  a = x1
                                  x1 = x2
                                  x2 = a + to * (abs(b - a))
                              else:
                                  b = x2
                                  x2 = x1
                                  x1 = a + (1 - to)* (abs(b - a))
                                  
                              if(x1==j and i==x2):
                                  break
                              else:    
                                  #----------Incrementation de k ---------------------#
                                  k = k+1   
                          #---------------------la sortie de la boucle while----------#  
                          a = x1
                          b = x2
                          #-------------Affichage de résultata-------------------------#
                          xzero = (a + b)/2 + 0.01
                          
                          self.varVoisin.set(xzero) 
                          self.var_iterpreNewton.set("Section d'or: le voisinage est trouver avec succée! ")   
                              
                      else:
                          MessageBox.showwarning("Error", "On ne peut pa appliquer l'algorithme de Section D'or sur cette fonction dans cette intervale !!  ")
     
              except Exception as es:                  
                    MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre5)  
  
    
  
     #------------------------Algoritheme de bissection-----------------------#
    def BissectionNewton(self):
            self.clearChamp()
            self.txt_voisi_newton.delete(0, END)
            #==============les entrer de l'algorithme=========================#
            val1 = self.txt_val_a.get()
            val2 = self.txt_val_b.get()
            fonctiont = self.txt_fonc.get()
            delTTa1 = self.txt_delta.get()
            if(val1 =="" or val2 =="" or delTTa1 =="" or fonctiont ==""):
                MessageBox.showerror("Error"," Remplir tout les champs SVP !!", parent=self.fenetre5)
            else: 
                try:                   
                     A = float(val1)
                     B = float(val2)
                     delta1 = float(delTTa1)
                     if(A > B):
                          MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre5)
                     else: 
                         #----------evaluation de la fonction ------------------#
                         def f(x):
                             y = eval(fonctiont)
                             return y 
                         
                         #-----------la calcule de dirivée de f en point a et b---# 
                         fprim_a = misc.derivative(f, A, dx=1.0, n=1, args=(), order=3) -1    
                         fprim_b = misc.derivative(f, B, dx=1.0, n=1, args=(), order=3) - 1
                         #----initialisation de deux var pour calculer le nomber des itiration 
                         j = 1243
                         k=1101
                         #----------------la condition de vérification------------#
                         if( fprim_a < 0 and fprim_b > 0):
                             while( abs(A - B) > delta1):
                                 #-------- la valeur de c ----------------------------#
                                 C = (B + A)/2
                                 aprim = misc.derivative(f, A, dx=1.0, n=1, args=(), order=3) -1 
                                 bprim = misc.derivative(f, B, dx=1.0, n=1, args=(), order=3) -1
                                 if( aprim < 0 and bprim > 0):
                                 #-----------------la dérivé au point c :--------------------------------#
                                     fprimDec = misc.derivative(f, C, dx=1.0, n=1, args=(), order=3) -1
                                     if(fprimDec <= 0):
                                           if(fprimDec == 0):
                                               #----------------------- la calcule de f seconde de f en poit c -------------#
                                                 fseconfDec = misc.derivative(f, C, dx=1.0, n=2, args=(), order=3)
                                                 if(fseconfDec > 0):
                                                     xzero = C + 0.001
                                                     self.varVoisin.set(xzero) 
                                                     self.var_iterpreNewton.set("Bissection: le voisinage est trouver avec succée! ")   
                                                     break
                                                 elif(fseconfDec < 0):
                                                     xzero = C + 0.001
                                                     self.varVoisin.set(xzero) 
                                                     self.var_iterpreNewton.set("Bissection: le voisinage est trouver avec succée! ")  
                                                     break   
                                                 else :
                                                     self.var_iterpreNewton.set("Ona une Point d inflexion dans le point : "+str(C))
                                                     MessageBox.showinfo("Error"," Ona une Point d'inflexion !!", parent=self.fenetre5)
                                                     break
                                           else :
                                               plt.plot(A, f(A), 'r.')
                                               A = C
                                               j = A
                                     else : 
                                             plt.plot(B, f(B), 'r.')
                                             B = C
                                             k = B
                                            
                                 elif(aprim > 0 and bprim < 0):
                                     C = (B + A)/2
                                     #----initialisation de deux var pour calculer le nomber des itiration 
                                     j = 1243
                                     k=1101
                                     if(fprimDec >= 0):
                                           if(fprimDec == 0):
                                               #----------------------- la calcule de f seconde de f en poit c -------------#
                                                 fseconfDec = misc.derivative(f, C, dx=1.0, n=2, args=(), order=3)
                                                 if(fseconfDec > 0):
                                                      xzero = C + 0.001
                                                      self.varVoisin.set(xzero) 
                                                      self.var_iterpreNewton.set("Bissection: le voisinage est trouver avec succée! ")  
                                                      break
                                                     
                                                 elif(fseconfDec < 0):
                                                      xzero = C + 0.001
                                                      self.varVoisin.set(xzero) 
                                                      self.var_iterpreNewton.set("Bissection: le voisinage est trouver avec succée! ")  
                                                      break
                                                 else :
                                                      self.var_iterpreNewton.set("Ona une Point d inflexion dans le point : "+str(C))
                                                      MessageBox.showinfo("Error"," Ona une Point d'inflexion !!", parent=self.fenetre5)
                                                      break
                                           else :
                                               if(j== A and k==B):
                                                    break
                                               else:
                                                    plt.plot(A, f(A), 'r.')
                                                    A = C
                                                    j=A
                                     else :
                                         if(A==j and k == B): 
                                             break
                                         else:  
                                             plt.plot(B, f(B), 'r.')
                                             B = C
                                             k= B
                                         
                                 elif((aprim > 0 and bprim > 0)or(aprim < 0 and bprim < 0)) :
                                     quit()
                                     
                             xzero = (A + B + 0.02)/2
                             self.varVoisin.set(xzero) 
                             self.var_iterpreNewton.set("Bissection: le voisinage est trouver avec succée! ")
                         else:
                             MessageBox.showwarning("Error","On ne peut pas Appliquer algorithme de Bissection sur cette fonctiontion dans ces deux points. par ce que ona f'(a)*f'(b) > 0 !!",parent=self.fenetre5)
                             self.var_iterpreNewton.set("Bissection ne fonctions pas car f'("+str(A)+")*f'("+str(B)+") > 0")
                             
                         
                except Exception as es:                  
                        MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre5)  
              
                                
       #------------------newton ----------------------------------------------#
    def Newton(self):
            self.clearChamp()
            val1 = self.txt_val_a.get()
            val2 = self.txt_val_b.get()
            xzero = self.txt_voisi_newton.get()
            deltta = self.txt_delta.get()
            fonct = self.txt_fonc.get()
            imax= self.txt_nbriteramax.get()
            if(deltta=="" or fonct =="" or imax==""):
                MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre5)
            elif(xzero ==""):
                MessageBox.showerror("Error"," Chercher le voisinage  svp! utilise l'un des algorithmes !", parent=self.fenetre5)   
            else:      
                try:  
                     A = float(val1)
                     B = float(val2)                    
                     xk = float(xzero)
                     delta = float(deltta)
                     itermax = int(imax)
                     #----------evaluation de la fonction --------------------#
                     def f(x):
                         y = eval(fonct)
                         return y
                     #-----ploter le graphe de f avec les point de depart-----#
                     plt.clf()
                     y = np.linspace(A, B, 1000)
                     plt.plot(y, f(y), label = "La courbe de f(x) ")
                     plt.plot(xk, f(xk), 'r.')
                     plt.title(" Newton ")
                     plt.xlabel("Abscisses")
                     plt.ylabel("Ordonnees")
                     
                     condition = True
                     i = 1
                     while(condition == True ):
                            #****************************la calcule des dérivées de la fonction  f(x) au point xzero**********************#
                            fprimX_k =  misc.derivative(f, xk, dx=1.0, n=1, args=(), order=3) - 1
                            fsecond_Xk = misc.derivative(f, xk, dx=1.0, n=2, args=(), order=3)
                            #--------------vérification avant de calculer la diréction au point xzero--------------------------------------#
                            if(fsecond_Xk != 0):
                                    #-------la calcule de direction de Newoton-----------------#
                                    direction = - fprimX_k/fsecond_Xk
                                    #------------------la calcule de Xk_plus1---------------------------#
                                    xk_plus1 =  xk + direction
                                    #-----pour tester |xk_plus1 - Xk| > delta et incrémenter le K ------# 
                                    if(abs(xk_plus1 - xk) > delta):
                                            xk = xk_plus1
                                            solution = xk_plus1
                                            plt.plot(solution, f(solution), 'r.')
                                            i=i+1
                                            if(i == itermax):        
                                                    break   
                                    else:
                                          #------pour sortir dans la boucle while----------------------------#   
                                          condition == False
                                          break
                              
                                                
                            else:
                                MessageBox.showwarning("Error"," f second de Xk = 0 , ona une point d'infléxion au point Xk !!!", parent=self.fenetre5)
                                self.var_iterpreNewton.set("f second de Xk = 0 , ona une point d'infléxion au point Xk !!")
                                break
                     
                     self.var_Newton_itir.set(i) 
                     self.varsolutionNewton.set(solution)
                     self.var_iterpreNewton.set("la solution x* est : "+str(solution))
                     plt.plot(solution, f(solution), label = "la solution x*")
                     plt.plot(solution, f(solution), 'g.')
                     plt.legend()
                     plt.show()
                except Exception as es:                  
                      MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre5)                   
             
        
    #======================Le gghaphe de la fonction==========================#   
    def graphe_de_fonction(self):
            val1 = self.txt_val_a.get()
            val2 = self.txt_val_b.get()
            fonc = self.txt_fonc.get()
            
            if(val1 =="" or val2 =="" or fonc =="" ):
                MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre5)
            elif(val1 > val2):
                MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre5)
            else :
                try:
                    a = float(val1)
                    b = float(val2)
                    
                    def f(x):
                        y = eval(fonc)
                        return y 
                    
                    root = Toplevel()
                    root.wm_title(" le Graphe de la fonction f ")
                    fig = Figure(figsize=(5, 4), dpi=100)
                    x = np.linspace(a, b, 1000)
                    fig.add_subplot(111).plot(x, f(x))

                    canvas = FigureCanvasTkAgg(fig, master=root)
                    canvas.draw()
                    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

                    toolbar = NavigationToolbar2Tk(canvas, root)
                    toolbar.update()
                    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
                    def on_key(event):
                        print("you pressed{}".format(event.key))
                        key_press_handler(event, canvas,toolbar)
        

                    canvas.mpl_connect("key_press_event", on_key)
                    root.mainloop()  
      
        
                except Exception as es:                  
                    MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre5) 
        
        
        
        
        
        
fenetre5=Tk()
obj=NewtonClasse(fenetre5)
fenetre5.mainloop()  
                                
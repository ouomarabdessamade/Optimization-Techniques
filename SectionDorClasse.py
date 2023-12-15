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



class SectionDor :
    def __init__(self,fenetre4):
        self.fenetre4=fenetre4
        #-----------le titre--------------------------------------------------#
        self.fenetre4.title("Section D'or ")
        #-----------------la geometrerde la fenetre---------------------------#
        self.fenetre4.geometry("1000x720+150+50")
        #-----------------le coleure de bag-----------------------------------#
        self.fenetre4.config(bg="#898E8F")   
        #-----------bloquer le redimentionnement de la fenetre----------------# 
        self.fenetre4.resizable(width=False, height=False)
        #--------------logo de l'application----------------------------------#
        self.fenetre4.iconbitmap("images/logoimag.ico")
        #==============Frame1  ===============================================#
        frame1=Frame( self.fenetre4, bg="#898E8F", highlightbackground="#F5ECC4",highlightthickness=2)
        frame1.place(x=48,y=40,height=660,width=900)
        #===============title=================================================#
        title = Label( self.fenetre4,text="Section D'or ",font=("Comic Sans MS", 17,"bold"), bg="#898E8F",fg="#F5ECC4").place(x=395,y=5)
       
        #----------------les entrer de l'algorithme---------------------------#
        entrer = Label(frame1,text="Input { ",font=("Comic Sans MS", 15,"bold"), bg="#898E8F",fg="#182350").place(x=10,y=10)
        
        #=================l'intervale ========================================#
        intervale = Label(frame1,text="The interval [a , b]   :",font=("Comic Sans MS", 15,"bold"),bg="#898E8F").place(x=110,y=50)
        
        #================vale de a ===========================================#
        self.txt_val = Label(frame1,text=" a :",font=("Comic Sans MS", 15,"bold"),bg="#898E8F").place(x=400,y=50)
        self.txt_val_a = Entry(frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350")
        self.txt_val_a.place(x=440,y=53,width=160)
        
        #================la valeure de b =====================================#
        self.val_b = Label(frame1,text=" b :",font=("Comic Sans MS", 15,"bold"),bg="#898E8F").place(x=630,y=50)
        self.txt_val_b = Entry(frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350")
        self.txt_val_b.place(x=675,y=53,width=160)
        
        #===================la fonction=======================================#
        self.fonc = Label(frame1,text="Function               : ",font=("Comic Sans MS", 16,"bold"),bg="#898E8F").place(x=110,y=110)
        self.foncF = Label(frame1,text="f(x)  =",font=("Comic Sans MS", 16,"bold"),bg="#898E8F").place(x=360,y=110)
        self.txt_fonc = Entry(frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350")
        self.txt_fonc.place(x=440,y=113,width=397 )
        
        #================la tolérence  =======================================#
        self.delta = Label(frame1,text="Tolerance              :",font=("Comic Sans MS", 15,"bold"),bg="#898E8F").place(x=110,y=170)
        self.delTTa = Label(frame1,text="delta =",font=("Comic Sans MS", 15,"bold"),bg="#898E8F").place(x=360,y=170)
        self.defouitDelta = DoubleVar()
        self.txt_delta = Entry(frame1,font=("times new romman", 16,"bold"), bg="lightgray",fg="#182350", textvariable=self.defouitDelta)
        self.defouitDelta.set(0.001)
        self.txt_delta.place(x=440,y=173,width=160)
        
        
        #=================fermer l'accolade===================================#
        self.coladfer = Label(frame1,text=" } Output   :",font=("Comic Sans MS", 15,"bold"),bg="#898E8F",fg="#182350").place(x=10,y=230)
        
        #==============Frame1  ===============================================#
        self.frame2=Frame( frame1,bg="#C4C6C6" ,highlightbackground="#182350",highlightthickness=3)
        self.frame2.place(x=10,y=290,height=360,width=875)
        
        #=================================================solution ===========================================#
        self.solution = Label(self.frame2,text="The interval [a , b]  :",font=("Comic Sans MS",15,"bold"), bg="#C4C6C6").place(x=10,y=20)
        #----------------------- la valeur de la solution a [a,b] -------------------------------------------------------#
        self.val_a_solutiFib = Label(self.frame2,text=" a :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=20)
        self.varSect = DoubleVar()
        self.txt_val_a_solutSect = Entry(self.frame2,font=("times new romman",16,"bold"), bg="lightgray",fg="#182350", textvariable=self.varSect)
        self.varSect.set("")
        self.txt_val_a_solutSect.place(x=290,y=23,width=250)
        
        
        #----------------------- la valeur de la solution b [a,b] --------------------------------------------------------#
        self.val_b_solutSect = Label(self.frame2,text=" b:",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=547,y=20)
        self.varSecB = DoubleVar()
        self.txt_val_solutionSecB = Entry(self.frame2,font=("times new romman",16,"bold"), bg="lightgray",fg="#182350", textvariable=self.varSecB)
        self.varSecB.set("")
        self.txt_val_solutionSecB.place(x=583,y=23,width=250)
        
        #--------------------------------val des nomber des itoration  i ----------------------------------------#
        self.nbr_Sect_iteration = Label(self.frame2,text="Number of iterations:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=110)
        self.txt_itera_Section = Label(self.frame2,text=" i :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=110)
        self.var_sect_itir = IntVar()
        self.txt_itera_Sect= Entry(self.frame2,font=("times new romman",16,"bold"), bg="lightgray",fg="red", textvariable=self.var_sect_itir)
        self.var_sect_itir.set("")
        self.txt_itera_Sect.place(x=290,y=113,width=250)
              
        #---------------------------------------interprétation---------------------------------------------------------------#
        self.nbr_iterpretaSecti = Label(self.frame2,text="Interpretation        :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=190)
        self.var_iterpreSect = StringVar()
        self.txt_iterpretatSect = Entry(self.frame2,font=("Comic Sans MS",16,"bold"), bg="lightgray",fg="green", textvariable=self.var_iterpreSect)
        self.var_iterpreSect.set("")
        self.txt_iterpretatSect.place(x=290,y=193,width=545)

        #=========================================================== boutton Section d'or =========================================================================================================#
        SectionDor_Button  = Button(self.frame2,font=("times new romman",16,"bold"),text=" Section d'or ",bd=0,cursor="hand2",bg="#AFAF0D",fg="#E5E1D6",activebackground ="#7AA1E6",activeforeground="#BF846C",borderwidth = 5, command =self.SectionDoree).place(x=320 ,y=270,width=240)
           
       #============================================================ Bouton le graphe de la fonction ===========================================================================================#
        graphedefa= Button(self.frame2,font=("times new romman",16,"bold"),text="graph of the fonction",bd=0,cursor="hand2",bg="#7B9764",fg="#E5E1D6",activebackground ="#CDD3C8",activeforeground="#BFF790",borderwidth = 5, command=self.graphe_de_fonction).place(x=10 ,y=270,width=240)
        
       #============================================================ Bouton quit ============================================================================================================#
        quitbuttonsec = Button(self.frame2 ,font=("times new romman",16,"bold"),text="Quit ",bd=0,cursor="hand2",bg="#811000",fg="#F9F2F1",activebackground ="#CAE5E4",activeforeground="#E8A490",borderwidth = 5, command=self.quiter).place(x=640 ,y=270,width=200)
        
        
   
    
   
     #-------------Pour quiter------------------------------------------------#       
    def quiter(self):
       self.fenetre4.destroy()
    



    #----------------pour vider les comps-------------------------------------#
    def clearChamp(self):
        #pour vider le champs de a dans l'intervale [a, b]
        self.txt_val_a_solutSect.delete(0, END)    #pour vider le champs de a dans l'intervale [a, b]         
        self.txt_val_solutionSecB.delete(0, END) #pour vider le champs de b dans l'intervale [a, b]
        self.txt_itera_Sect.delete(0, END)   #pour vider le champs de nbr d'itiration
        self.txt_iterpretatSect.delete(0, END) #pour vider le champs de l'interprétation 
        


        #===================================Algorithme de Section d'or =========================================================================#
    def SectionDoree(self):
         self.clearChamp() #appel a la fonction pour vider les champs avans d'appliquer l'algorithmes
         #==============les entrer de l'algorithme============================#
         val1 = self.txt_val_a.get() #récuperer la valeur de a
         val2 = self.txt_val_b.get() #récuperer la valeur de b
         fon = self.txt_fonc.get() #récuperer la fonction f(x)
         deltta = self.txt_delta.get() #récuperer la valeur de la tolérance
         if(val1 =="" or val2 ==""  or fon ==""  or deltta =="" ): #vérifier que tout les entere de l'alogo est saisie avec succée
             MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre4)
         else:
              try:   
                  a = float(val1) #convirtir les valeur en des float
                  b = float(val2)
                  delta = float(deltta)
                  
                  if(a > b):#dans le cas est l'intervale est invalid !!
                      MessageBox.showerror("Error","Intervale invalide !!\n Sisair deux entier tel que a < b ", parent=self.fenetre4)
                  else:
                      #-------définie une methode pour évaluer la fonction----#
                      def f(x):
                          y = eval(fon)
                          return y 
                      #----la calcule de fprim de a et f prim de b------------#   
                      fprimde_a = misc.derivative(f, a, dx=1.0, n=1, args=(), order=3) - 1
                      fprimde_b = misc.derivative(f, b, dx=1.0, n=1, args=(), order=3) - 1
                      
                      if(fprimde_a < 0 and  fprimde_b > 0):#vérifier que f est convexe en [a, b]
                          plt.clf() #vider le graphe pour ploter un nouvelle 
                          y = np.linspace(a, b, 1000)
                          plt.plot(y, f(y), label = "La courbe de f(x) ") 
                          plt.title(" Section d'or ")
                          plt.xlabel("Abscisses") #xlabel : l'abscisses
                          plt.ylabel("Ordonnees") #ylabel : l'ordonnees
                          plt.plot(a, f(a), 'r.') #ploter les deux point de depart
                          plt.plot(b, f(b), 'r.')
                          #---------initialisation de deux var nous permettent de sortie dans la boucle si l'intervale ne change pas ---------------#
                          j=100.01
                          i=199.0
                          #-------------nomber d'or---------------------------#
                          to = 0.5*(math.sqrt(5) - 1)
                          #-----début de l'lgorithme--------------------------#
                          k = 1 #-------------------compteur de nbr d'itiration
                          d1 = abs(b - a)#---initialisation de d--------------#
                          x1 = a + (1 - to) * d1 #la calcule de x1------------#
                          x2 = a + to * d1 #la calcule de x2------------------#
                          plt.plot(x1, f(x1), 'r.') #---plot xi et x2 dans----#
                          plt.plot(x2, f(x2), 'r.') #-le graphe de la fonction#
                          #------------------- la boucle while---------------------#
                          while( abs(b - a) > delta):
                              if( f(x1) > f(x2)):#si le cas  Alors :
                                  a = x1    #mise a jour de a par x1----------#
                                  x1 = x2   #mise a jour de x1 par x2---------#
                                  x2 = a + to * (abs(b - a)) #mise a jour de x2
                                  plt.plot(x2, f(x2), 'r.')  #ploter x1 dans le graphe pour garder les traces des point suiver l'algorithmes
                                  i = x2 #pour garder la dernier valeur de x2
                              else:#si non
                                  b = x2  #--mise b jour de a par x2----------#
                                  x2 = x1 #--mise a jour de x2 par x1---------#
                                  x1 = a + (1 - to)* (abs(b - a))#mise a jour de x1
                                  plt.plot(x1, f(x1), 'r.') #ploter x1 dans le graphe pour garder les traces des point suiver l'algorithmes
                                  j = x1 #pour garder la dernier valeur de x1
                              if(x1==j and i==x2): #ici on vérifier si la valeur de x1 et x2 trouver dans l'itiration k sont 
                                                   #les meme dans l'itiration k+1.pour sortie dans l'algorithme avec le nbr 
                                                   #d'itiration exacte
                                  break
                              else:    
                                  #----------Incrementation de k ---------------------#
                                  k = k+1   
                          #---------------------la sortie de la boucle while----------#  
                          a = x1
                          b = x2
                          #-------------Affichage de résultata-------------------------#
                          self.varSect.set(a)  #la dernier valeur de a trouver par l'algo
                          self.varSecB.set(b)  #la dernier valeur de b trouver par l'algo
                          self.var_sect_itir.set(k) #le nbr d'itiration trouver !
                          self.var_iterpreSect.set("la solution x* est dans l'intervale ["+str(a) +" , "+ str(b) +"]")#une petit interprétation
                          plt.plot(a, f(a), label="l'interval [a, b]") 
                          plt.plot(a, f(a), 'g+')#ici ona ploter les dernier valeur de a et b
                          plt.plot(b, f(b), 'g+') #c-a-d l'intervale qui contient notre solution
                          plt.legend()
                          plt.show()
                                 
                      else:#dons le cas ou la fonction n'est pas connvex dans l'interval [a, b]
                          MessageBox.showwarning("Error", "On ne peut pa appliquer l'algorithme de Section D'or sur cette fonction dans cette intervale !!  ")
                      
              except Exception as es:                  
                   MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre4)  



     #======================Le gghaphe de la fonction=========================#   
    def graphe_de_fonction(self):
            #------recuperer les valeur enter da,s l'interface----------------#
            val1 = self.txt_val_a.get()
            val2 = self.txt_val_b.get()
            fonc = self.txt_fonc.get()
            
            if(val1 =="" or val2 =="" or fonc =="" ):#verification
                MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre4)
            else :
                try:
                    a = float(val1) #convirtir en float
                    b = float(val2)
                    if(a > b):
                        MessageBox.showerror("Error","Intervale invalide !!\n Sisair deux entier tel que a < b ", parent=self.fenetre4)
                    else:
                        def f(x):#eval de f 
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
                    MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre4) 
        
        
        

fenetre4=Tk()
obj=SectionDor(fenetre4)
fenetre4.mainloop()  
                  


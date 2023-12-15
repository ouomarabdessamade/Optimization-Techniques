from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
import numpy as np
from scipy import misc 
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler

from matplotlib.figure import Figure



class Dichotomique :
    def __init__(self,fenetre2):
        self.fenetre2=fenetre2
        #-----------le titre--------------------------------------------------#
        self.fenetre2.title("Dichotomous Search")
        #-----------------la geometrerde la fenetre---------------------------#
        self.fenetre2.geometry("1000x720+150+50")
        #-----------------le coleure de bag-----------------------------------#
        self.fenetre2.config(bg="#C0CAB7")   
        #-----------bloquer le redimentionnement de la fenetre----------------# 
        self.fenetre2.resizable(width=False, height=False)
        #--------------logo de l'application----------------------------------#
        self.fenetre2.iconbitmap("images/logoimag.ico")
        
        #==============Frame1  ===============================================#
        frame1=Frame( self.fenetre2, bg="#C0CAB7", highlightbackground="#E96331",highlightthickness=2)
        frame1.place(x=45,y=40,height=660,width=900)
        #===============title=================================================#
        title = Label( self.fenetre2,text="Dichotomous Search",font=("Comic Sans MS", 17,"bold"), bg="#C0CAB7",fg="#E96331").place(x=360,y=5)
       
        #----------------les entrer de l'algorithme---------------------------#
        entrer = Label(frame1,text="Input { ",font=("Comic Sans MS", 15,"bold"), bg="#C0CAB7",fg="#182350").place(x=10,y=10)
        
        #=================l'intervale ========================================#
        intervale = Label(frame1,text="The interval [a , b]   :",font=("Comic Sans MS", 15,"bold"),bg="#C0CAB7").place(x=110,y=20)
        
        #================vale de a ===========================================#
        val_a = Label(frame1,text=" a :",font=("Comic Sans MS", 15,"bold"),bg="#C0CAB7").place(x=400,y=20)
        self.txt_val_a = Entry(frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350")
        self.txt_val_a.place(x=440,y=23,width=160)
        
        #================la valeure de b =====================================#
        val_b = Label(frame1,text=" b :",font=("Comic Sans MS", 15,"bold"),bg="#C0CAB7").place(x=630,y=20)
        self.txt_val_b = Entry(frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350")
        self.txt_val_b.place(x=675,y=23,width=160)
        
        #===================la fonction=======================================#
        fonc = Label(frame1,text="Function               : ",font=("Comic Sans MS", 16,"bold"),bg="#C0CAB7").place(x=110,y=80)
        foncF = Label(frame1,text="f(x)  =",font=("Comic Sans MS", 16,"bold"),bg="#C0CAB7").place(x=360,y=80)
        self.txt_fonc = Entry(frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350")
        self.txt_fonc.place(x=440,y=83,width=397 )
        
        #================la tolérence  =======================================#
        delta = Label(frame1,text="Tolerance              :",font=("Comic Sans MS", 15,"bold"),bg="#C0CAB7").place(x=110,y=140)
        delTTa = Label(frame1,text="delta =",font=("Comic Sans MS", 15,"bold"),bg="#C0CAB7").place(x=360,y=140)
        self.defouitDelta = DoubleVar()
        self.txt_delta = Entry(frame1,font=("times new romman", 15,"bold"), bg="lightgray",fg="#182350", textvariable=self.defouitDelta)
        self.defouitDelta.set(0.001)
        self.txt_delta.place(x=440,y=143,width=160)
        
        #===================Nomber d'etiration max============================#
        nbriteramax = Label(frame1,text="Number of iterations :",font=("Comic Sans MS", 15,"bold"),bg="#C0CAB7").place(x=110,y=200)
        nbriteraMax = Label(frame1,text="imax =",font=("Comic Sans MS", 15,"bold"),bg="#C0CAB7").place(x=360,y=200)
        self.txt_nbriteramax = Entry(frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350")
        self.txt_nbriteramax.place(x=440,y=203,width=160)
        
        #=================fermer l'accolade===================================#
        coladfer = Label(frame1,text=" } Output   :",font=("Comic Sans MS", 15,"bold"),bg="#C0CAB7",fg="#182350").place(x=10,y=260)
        
        #==============Frame1  ===============================================#
        frame2=Frame( frame1,bg="#C4C6C6" ,highlightbackground="#182350",highlightthickness=3)
        frame2.place(x=10,y=310,height=340,width=875)
        
        #=================================================solution Bissection===========================================#
        solution = Label(frame2,text="The interval [a , b]  :",font=("Comic Sans MS",15,"bold"), bg="#C4C6C6").place(x=10,y=20)
        #----------------------- la valeur de la solution a [a,b] -------------------------------------------------------#
        val_a_solution = Label(frame2,text=" a :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=20)
        self.vardichoA = DoubleVar()
        self.txt_val_a_solution = Entry(frame2,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350", textvariable=self.vardichoA)
        self.vardichoA.set("")
        self.txt_val_a_solution.place(x=290,y=23,width=250)
        
        
        #----------------------- la valeur de la solution b [a,b] --------------------------------------------------------#
        val_b_solution = Label(frame2,text=" b:",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=547,y=20)
        self.vardichoB = DoubleVar()
        self.txt_val_solutionB = Entry(frame2,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350", textvariable=self.vardichoB)
        self.vardichoB.set("")
        self.txt_val_solutionB.place(x=583,y=23,width=250)
        
        #--------------------------------val des nomber des itoration  i Bissection----------------------------------------#
        nbr_itera_max = Label(frame2,text="Number of iterations:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=110)
        val_itera_bissec = Label(frame2,text=" i :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=110)
        self.var_dicho_itir = IntVar()
        self.txt_itera_dicho = Entry(frame2,font=("times new romman", 17,"bold"), bg="lightgray",fg="red", textvariable=self.var_dicho_itir)
        self.var_dicho_itir.set("")
        self.txt_itera_dicho.place(x=290,y=113,width=250)
          
        #---------------------------------------interprétation---------------------------------------------------------------#
        nbr_iterpretatdicho = Label(frame2,text="Interpretation        :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=200)
        self.var_iterpretDicho = StringVar()
        self.txt_iterpretatdicho = Entry(frame2,font=("times new romman",17,"bold"), bg="lightgray",fg="green", textvariable=self.var_iterpretDicho)
        self.var_iterpretDicho.set("")
        self.txt_iterpretatdicho.place(x=290,y=203,width=545)
        
        
         #============================================================ boutton Dichotomique =====================================================================================================#
        dico_button = Button(frame2,font=("times new romman", 16,"bold"),text=" Dichotomous ",bd=0,cursor="hand2",bg="#87AC2A",fg="#E5E1D6",activebackground ="#BFB3B5",activeforeground="#E5E1D6",borderwidth = 5,command=self.dichotomique).place(x=320 ,y=270,width=240)
           
        
        #============================================================ Bouton le graphe de la fonction ===========================================================================================#
        graphedef= Button(frame2,font=("times new romman",16,"bold"),text="graph of the fonction",bd=0,cursor="hand2",bg="#7B9764",fg="#E5E1D6",activebackground ="#CDD3C8",activeforeground="#BFF790",borderwidth = 5, command=self.graphe_de_fonction).place(x=10 ,y=270,width=240)
        
     
        #============================================================ Bouton quitt ============================================================================================================#
        quibutt= Button(frame2,font=("times new romman",16,"bold"),text="Quit ",bd=0,cursor="hand2",bg="#811000",fg="#F9F2F1",activebackground ="#CAE5E4",activeforeground="#E8A490",borderwidth = 5, command=self.quiter).place(x=640 ,y=270,width=220)
        
       
     
        
    #-------------Pour quiter------------------------------------#       
    def quiter(self):
       self.fenetre2.destroy()
          
   
    #----------------pour vider les comps----------------------------------------#
    def clearChamp(self):
        self.txt_val_a_solution.delete(0, END)
        self.txt_val_solutionB.delete(0, END)
        self.txt_itera_dicho.delete(0, END)
        self.txt_iterpretatdicho.delete(0, END)
   
    #Hypoteses : La fonction est derivable , continue et convexe sur [a,b]
   
    #=====================================Algorithme Dichotomique=================================#
    def dichotomique(self):
                 plt.clf()
                 #------- pour ecraser les champs------#
                 self.clearChamp()
                 #------- ----------recuperer les valeurs sisies --------------#
                 #-------recuperer a----------#
                 val1 = self.txt_val_a.get()
                 # -------recuperer b----------#
                 val2 = self.txt_val_b.get()
                 # -------recuperer la tolerence delta----------#
                 deltta = self.txt_delta.get()
                 # -------recuperer la fonction----------#
                 fonct = self.txt_fonc.get()
                 # -------recuperer le nombre maximal des iterations----------#
                 i_max = self.txt_nbriteramax.get()
                 #--------- Error !! : si les champs sont vides --------#
                 if(val1 =="" or val2 =="" or deltta =="" or fonct =="" or i_max =="" ):
                     MessageBox.showerror("Error"," Remplir tout les champs svp !!", parent=self.fenetre2)
                 else:
                     try:
                         #------ convertir les valeurs de l'interval en valeurs reels -----#
                         #----- pour a-----#
                         a = float(val1)
                         # ----- pour b-----#
                         b = float(val2)
                         # ----- pour la tolerence -----#
                         delta = float(deltta)
                         # --------- Error !! : si a > b----------#
                         if (a > b):
                            MessageBox.showerror("Error", "Intervale invalide !! \n Sisair deux entier tel que a < b ",parent=self.fenetre2)
                         else :
                             # ----- convertir le nombre maximal des iterations en valeur entiere -----#
                             itermax = int(i_max)

                             #--------- definir la fonction --------#
                             def f(x):
                                 y = eval(fonct)
                                 return y
                             #----------- calculer la derive de f en a ------#
                             fpr_a = misc.derivative(f, a, dx=1.0, n=1, args=(), order=3) - 1
                             # Remarque !!:  cette methde (derivative) de scipy.misc ajoute un 1 c'est pour cela nous avons soustriats 1 ---3
                             # ----------- calculer la derive de f en b ------#
                             fpr_b = misc.derivative(f, b, dx=1.0, n=1, args=(), order=3) - 1
                             #---- Supposons que f est continue sur [a,b] ------#
                             # ---- tester si f'(x) = 0 admet une soulution sur [a,b] -----#
                             if(fpr_a * fpr_b <= 0):
                                 plt.clf()
                                 #----- creer un espace pour afficher le graph de f sur [a,b] avec 1000 points entre a et b-----#
                                 y = np.linspace(a, b, 1000)
                                 plt.plot(y, f(y), label = "La courbe de f(x) ")
                                 plt.title(" Dichotomique ")
                                 plt.xlabel("Abscisses")
                                 plt.ylabel("Ordonnees")
                                 #----- Afficher la trace de la  valeur initial de  a en fonctione de f  -----#
                                 plt.plot(a , f(a), 'r.')
                                 #----- Afficher la trace de la  valeur initial de  b en fonctione de f  -----#
                                 plt.plot(b , f(b), 'r.')
                                 #
                                 i=1
                                 j=1001
                                 k=999
                                 # ------- calculer la longueur de [a,b] initial -----#
                                 c = abs(b - a)
                                 #----- Tant que |b-a| > delta ET le nombre des iterations n'est pas puisee on va etrer dans la boucle ----#
                                 while(c > delta and i < itermax):
                                     #------ x : le  milieux de [a,b] -------#
                                     x = (a + b)/2
                                     #------- calculer f'(x) ----#
                                     fprim_x = misc.derivative(f, x, dx=1.0, n=1, args=(), order=3) - 1
                                     #------- Si f'(a) x f'(x) < ------#
                                     if(fpr_a * fprim_x < 0):
                                         b = x
                                         c = abs( b - a)
                                         #----- Afficher la trace des points (a,f(a)) par * ----#
                                         plt.plot(b, f(b), 'r*')
                                     # ------- Si f'(b) x f'(x) < ------#
                                     if(fpr_b * fprim_x <0):
                                         a = x
                                         c = abs(b - a)
                                         # ----- Afficher la trace des points (b,f(b)) par * ----#
                                         plt.plot(a, f(a), 'r*')
                                     #------ En cas de divergence ------#
                                     if(j == a and k == b):
                                         break
                                     else:
                                         j = a
                                         k = b
                                         i+=1
                                #---- Afficher les valeurs finales de a et b -------#
                                 self.vardichoA.set(a)
                                 self.vardichoB.set(b)
                                 #----- Afficher le nombre des iteration faites -------#
                                 self.var_dicho_itir.set(i)
                                 #------- Afficher une interpretation --------#
                                 self.var_iterpretDicho.set("la solution est dans l'intervale ["+str(a) +" , "+ str(b) +"]")
                                 plt.plot(a, f(a), label="l'interval [a, b]")
                                 plt.plot(a , f(a), 'g*')
                                 plt.plot(b, f(b), 'g*')
                                 plt.legend()
                                 plt.show()

                             else:
                                 MessageBox.showwarning("Error","On ne peut pas Appliquer algorithme de Dichotomique sur cette fonction dans ces deux points. par ce que ona f'(a)*f'(b) > 0 !!",parent=self.fenetre2)
                                 self.var_iterpretDicho.set("Dichotomique ne fonction car : f'("+ str(a)+ ")*f'("+str(b)+") > 0 !")


                     except Exception as es:                  
                             MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre2)  
          
   
    
    #-------------Le ghaphe de la fonction----------------#
    def graphe_de_fonction(self):
            val1 = self.txt_val_a.get()
            val2 = self.txt_val_b.get()
            fonc = self.txt_fonc.get()
            
            if(val1 =="" or val2 =="" or fonc =="" ):
                MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre2)
            elif(val1 > val2):
                MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre2)
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
                    MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre2) 
        
        
    
    
        
fenetre2=Tk()
obj=Dichotomique(fenetre2)
fenetre2.mainloop()

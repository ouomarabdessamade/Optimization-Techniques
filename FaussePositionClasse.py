from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
import numpy as np
from scipy import misc 
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler

from matplotlib.figure import Figure



class FaussePosition :
    def __init__(self,fenetre6):
        self.fenetre6=fenetre6
        #-----------le titre--------------------------------------------------#
        self.fenetre6.title("Fausse Position Search")
        #-----------------la geometrerde la fenetre---------------------------#
        self.fenetre6.geometry("1000x720+150+50")
        #-----------------le coleure de bag-----------------------------------#
        self.fenetre6.config(bg="#8B9A9C")   
        #-----------bloquer le redimentionnement de la fenetre----------------# 
        self.fenetre6.resizable(width=False, height=False)
        #--------------logo de l'application----------------------------------#
        self.fenetre6.iconbitmap("images/logoimag.ico")
        
        #==============Frame1  ===============================================#
        frame1=Frame( self.fenetre6, bg="#8B9A9C", highlightbackground="#F0EDDB",highlightthickness=2)
        frame1.place(x=45,y=40,height=660,width=900)
        #===============title=================================================#
        title = Label( self.fenetre6,text="Fausse Position Search",font=("Comic Sans MS", 17,"bold"), bg="#8B9A9C",fg="#F0EDDB").place(x=350,y=5)
       
        #----------------les entrer de l'algorithme---------------------------#
        entrer = Label(frame1,text="Input { ",font=("Comic Sans MS", 15,"bold"), bg="#8B9A9C",fg="#182350").place(x=10,y=10)
        
        #=================l'intervale ========================================#
        intervale = Label(frame1,text="The interval [a , b]   :",font=("Comic Sans MS", 15,"bold"),bg="#8B9A9C").place(x=110,y=20)
        
        #================vale de a ===========================================#
        val_a = Label(frame1,text=" a :",font=("Comic Sans MS", 15,"bold"),bg="#8B9A9C").place(x=400,y=20)
        self.txt_val_a = Entry(frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350")
        self.txt_val_a.place(x=440,y=23,width=160)
        
        #================la valeure de b =====================================#
        val_b = Label(frame1,text=" b :",font=("Comic Sans MS", 15,"bold"),bg="#8B9A9C").place(x=630,y=20)
        self.txt_val_b = Entry(frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350")
        self.txt_val_b.place(x=675,y=23,width=160)
        
        #===================la fonction=======================================#
        fonc = Label(frame1,text="Function               : ",font=("Comic Sans MS", 16,"bold"),bg="#8B9A9C").place(x=110,y=80)
        foncF = Label(frame1,text="f(x)  =",font=("Comic Sans MS", 16,"bold"),bg="#8B9A9C").place(x=360,y=80)
        self.txt_fonc = Entry(frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350")
        self.txt_fonc.place(x=440,y=83,width=397 ) 
        
        #================la tolérence  =======================================#
        delta = Label(frame1,text="Tolerance              :",font=("Comic Sans MS", 15,"bold"),bg="#8B9A9C").place(x=110,y=140)
        delTTa = Label(frame1,text="delta =",font=("Comic Sans MS", 15,"bold"),bg="#8B9A9C").place(x=360,y=140)
        self.defouitDelta = DoubleVar()
        self.txt_delta = Entry(frame1,font=("times new romman", 15,"bold"), bg="lightgray",fg="#182350", textvariable=self.defouitDelta)
        self.defouitDelta.set(0.001)
        self.txt_delta.place(x=440,y=143,width=160)
        
        #===================Nomber d'etiration max============================#
        nbriteramax = Label(frame1,text="Number of iterations :",font=("Comic Sans MS", 15,"bold"),bg="#8B9A9C").place(x=110,y=200)
        nbriteramax = Label(frame1,text="imax =",font=("Comic Sans MS", 15,"bold"),bg="#8B9A9C").place(x=360,y=200)
        self.txt_nbriteramax = Entry(frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350")
        self.txt_nbriteramax.place(x=440,y=203,width=160)
        
        #=================fermer l'accolade===================================#
        self.coladfer = Label(frame1,text=" } Output   :",font=("Comic Sans MS", 15,"bold"),bg="#8B9A9C",fg="#182350").place(x=10,y=260)
        
        #==============Frame1  ===============================================#
        frame2=Frame( frame1,bg="#C4C6C6" ,highlightbackground="#182350",highlightthickness=3)
        frame2.place(x=10,y=310,height=340,width=875)
        
        #---------------la valeur exacte de la solution si l'algorithme arive a calculer x*--------------------------------#
        val_solution_exact = Label(frame2,text="The solution          :",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=10,y=20)
        #-----------------------------------------------x*-----------------------------------------------------------------#
        val_x_solFauss = Label(frame2,text=" x*:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=247,y=20)
        self.varsolutionFauss = DoubleVar()
        self.txt_solution_exactFauss = Entry(frame2,font=("times new romman",16,"bold"), bg="lightgray",fg="green", textvariable=self.varsolutionFauss)
        self.varsolutionFauss.set("")
        self.txt_solution_exactFauss.place(x=290, y=23, width=300)
        
        #--------------------------------val des nomber des itoration  i Bissection----------------------------------------#
        self.val_itera_fausspos = Label(frame2,text="Number of iterations:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=100)
        self.val_itera_FaussPos = Label(frame2,text=" i :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=100)
        self.var_fausspos_itir = IntVar()
        self.txt_fausspos_new = Entry(frame2,font=("times new romman",16,"bold"), bg="lightgray",fg="red", textvariable=self.var_fausspos_itir)
        self.var_fausspos_itir.set("")
        self.txt_fausspos_new.place(x=290,y=103,width=300)
          
        #---------------------------------------interprétation---------------------------------------------------------------#
        self.nbr_iterpretatFauss = Label(frame2,text="Interpretation        :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=180)
        self.var_iterpreFauss = StringVar()
        self.txt_iterpretationFauss = Entry(frame2,font=("times new romman",16,"bold"), bg="lightgray",fg="#182350", textvariable=self.var_iterpreFauss)
        self.var_iterpreFauss.set("")
        self.txt_iterpretationFauss.place(x=290,y=183,width=545)
        
        #=========================================================== Bouton de Fausse Position =================================================================================================#
        Fausse_Position_boutton = Button(frame2,font=("times new romman",16,"bold"),text=" Fausse Position ",bd=0,cursor="hand2",bg="#4CA054",fg="#E5E1D6",activebackground ="#AFAF0D",activeforeground="#0F5A7D",borderwidth =5, command=self.Fausse_Position).place(x=320 ,y=270,width=270)
     
        #============================================================ Bouton le graphe de la fonction ===========================================================================================#
        graphedef= Button(frame2,font=("times new romman",16,"bold"),text="graph of the fonction",bd=0,cursor="hand2",bg="#7B9764",fg="#E5E1D6",activebackground ="#CDD3C8",activeforeground="#BFF790",borderwidth = 5, command=self.graphe_de_fonction).place(x=10 ,y=270,width=240)
        
     
        #============================================================ Bouton quit ============================================================================================================#
        Accull= Button(frame2,font=("times new romman",16,"bold"),text="Quit ",bd=0,cursor="hand2",bg="#811000",fg="#F9F2F1",activebackground ="#CAE5E4",activeforeground="#E8A490",borderwidth = 5, command=self.quiter).place(x=640 ,y=270,width=200)
        
       
     
        
     
        #----------------pour vider les comps---------------------------------#
    def clearChamp(self):
        self.txt_solution_exactFauss.delete(0, END)
        self.txt_fausspos_new.delete(0, END)
        self.txt_iterpretationFauss.delete(0, END)
        
        
        
  #-------------Pour quiter------------------------------------#       
    def quiter(self):
       self.fenetre6.destroy()
          
        
        
        
        
    #------------------------Algoritheme des Fausses Position et le graphe de f-----------------#
    def Fausse_Position(self):
            self.clearChamp()
            val1 = self.txt_val_a.get()
            val2 = self.txt_val_b.get()
            deltta = self.txt_delta.get()
            fonc = self.txt_fonc.get()
            imax= self.txt_nbriteramax.get()
            #----- Remplissage des inputs -------#
            if(val1 =="" or val2 =="" or deltta =="" or fonc =="" or imax=="" ):
                MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre6)
            else :
                try : 
                    
                     xk_moins_1 = float(val1)
                     x_k = float(val2)
                     delta = float(deltta)
                     itimax = int(imax)
                     if(xk_moins_1 > x_k):
                          MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre6)
                     else :
                         #------- Graph de la fonction ------------------#
                         def f(x):
                            y = eval(fonc)
                            return y 
                         plt.clf()
                         y = np.linspace(xk_moins_1, x_k, 1000)
                         plt.plot(y, f(y), label = "La courbe de f(x) ")
                         plt.title(" Fausse Position ")
                         plt.xlabel("Abscisses")
                         plt.ylabel("Ordonnees")
                         plt.plot(xk_moins_1, f(xk_moins_1), 'r.')
                         plt.plot(x_k, f(x_k), 'r.')
                         
                         #----------la calcule de dérivée de f en x_k-------------#
                         fprim_xk = misc.derivative(f, x_k, dx=1.0, n=1, args=(), order=3) - 1
    
                         #==========================Début=========================#
                         i=0
                         #============initialisation de a par une valure qlq======#
                         a=1010.01
                         while( (abs(xk_moins_1 - x_k ) > delta or abs(fprim_xk) > delta ) and i < itimax):
                            #---------la calcule des dérivées--------------------------#
                            fprime_k = misc.derivative(f, x_k, dx=1.0, n=1, args=(), order=3) - 1
                            fprime_k_moins1 = misc.derivative(f, xk_moins_1, dx=1.0, n=1, args=(), order=3) - 1
        
                            #--------la calcule de direction de fausse position--------#
                            d_k = - fprime_k * ( (xk_moins_1 - x_k)/(fprime_k_moins1 - fprime_k) )
        
                            #--------Calculer l’itération xk_plus1 = xk + dk ----------#
                            xk_plus1 = x_k + d_k
                            #---------Incrémentation de xk par xk + 1 -----------------#
                            xk_moins_1 = x_k
                            x_k = xk_plus1
        
                            #---------------fprim_xk ----------------------------------#
                            fprim_xk = misc.derivative(f, x_k, dx=1.0, n=1, args=(), order=3) - 1
                            Alpha = x_k
                            #===================les point xk dans le graphe============#
                            plt.plot(x_k, f(x_k), 'r.')
                        
                            #--------incrementation de nomber d'eteration --------------#
                            if(a == x_k):
                                break
                            else: 
                                a = x_k
                                i+=1
                            
                         
                         #===================Sortie de la bucle while=====================================================#
                         self.varsolutionFauss.set(Alpha)
                         self.var_fausspos_itir.set(i)
                         self.var_iterpreFauss.set("Fausse Position : la solution est trouver avec succée !")
                         
                         plt.plot(Alpha, f(Alpha), label='la solution x*')
                         plt.plot(Alpha, f(Alpha), 'g.')
                         plt.legend()
                         plt.show()
                             
                except Exception as es:                  
                    MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre6)  
                  
        
        
        
        
        
    #======================Le grhaphe de la fonction==========================#   
    def graphe_de_fonction(self):
            val1 = self.txt_val_a.get()
            val2 = self.txt_val_b.get()
            fonc = self.txt_fonc.get()
            #-----Vérifier le Remplissage des inputs -------#
            if(val1 =="" or val2 =="" or fonc =="" ):
                MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre6)
            elif(val1 > val2):
                MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre6)
            else :
                try:
                    a = float(val1)
                    b = float(val2)
                    
                    def f(x):
                        y = eval(fonc)
                        return y 
                    #--- fenetre de graph -----------#
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
                    MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre6) 
        
        
        
        
 
        
        
        
fenetre6=Tk()
obj=FaussePosition(fenetre6)
fenetre6.mainloop()  
                
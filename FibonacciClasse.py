from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
import numpy as np
from scipy import misc 
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler

from matplotlib.figure import Figure



class Fibonacci :
    def __init__(self,fenetre3):
        self.fenetre3=fenetre3
        #-----------le titre--------------------------------------------------#
        self.fenetre3.title("Fibonacci Search")
        #-----------------la geometrerde la fenetre---------------------------#
        self.fenetre3.geometry("1000x720+150+50")
        #-----------------le coleure de bag-----------------------------------#
        self.fenetre3.config(bg="#A3C178")   
        #-----------bloquer le redimentionnement de la fenetre----------------# 
        self.fenetre3.resizable(width=False, height=False)
        #--------------logo de l'application----------------------------------#
        self.fenetre3.iconbitmap("images/logoimag.ico")
        
        #==============Frame1  ===============================================#
        frame1=Frame( self.fenetre3, bg="#A3C178", highlightbackground="#D4D9CE",highlightthickness=2)
        frame1.place(x=45,y=40,height=660,width=900)
        #===============title=================================================#
        title = Label( self.fenetre3,text="Fibonacci Search",font=("Comic Sans MS", 17,"bold"), bg="#A3C178",fg="#D4D9CE").place(x=390,y=5)
       
        #----------------les entrer de l'algorithme---------------------------#
        entrer = Label(frame1,text="Input { ",font=("Comic Sans MS", 15,"bold"), bg="#A3C178",fg="#182350").place(x=10,y=10)
        
        #=================l'intervale ========================================#
        intervale = Label(frame1,text="The interval [a , b]   :",font=("Comic Sans MS", 15,"bold"),bg="#A3C178").place(x=110,y=20)
        
        #================vale de a ===========================================#
        self.val_a = Label(frame1,text=" a :",font=("Comic Sans MS", 15,"bold"),bg="#A3C178").place(x=400,y=20)
        self.txt_val_a = Entry(frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350")
        self.txt_val_a.place(x=440,y=23,width=160)
        
        #================la valeure de b =====================================#
        self.val_b = Label(frame1,text=" b :",font=("Comic Sans MS", 15,"bold"),bg="#A3C178").place(x=630,y=20)
        self.txt_val_b = Entry(frame1,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350")
        self.txt_val_b.place(x=675,y=23,width=160)
        
        #===================la fonction=======================================#
        self.fonc = Label(frame1,text="Function               : ",font=("Comic Sans MS", 16,"bold"),bg="#A3C178").place(x=110,y=80)
        self.foncF = Label(frame1,text="f(x)  =",font=("Comic Sans MS", 16,"bold"),bg="#A3C178").place(x=360,y=80)
        self.txt_fonc = Entry(frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350")
        self.txt_fonc.place(x=440,y=83,width=397 )
        
        #================la tolérence  =======================================#
        self.delta = Label(frame1,text="Tolerance              :",font=("Comic Sans MS", 15,"bold"),bg="#A3C178").place(x=110,y=140)
        self.delTTa = Label(frame1,text="delta =",font=("Comic Sans MS", 15,"bold"),bg="#A3C178").place(x=360,y=140)
        self.defouitDelta = DoubleVar()
        self.txt_delta = Entry(frame1,font=("times new romman", 15,"bold"), bg="lightgray",fg="#182350", textvariable=self.defouitDelta)
        self.defouitDelta.set(0.001)
        self.txt_delta.place(x=440,y=143,width=160)
        
        #===================Nomber d'etiration max============================#
        self.nbriteramax = Label(frame1,text="Number of iterations :",font=("Comic Sans MS", 15,"bold"),bg="#A3C178").place(x=110,y=200)
        self.nbriteramax = Label(frame1,text="imax =",font=("Comic Sans MS", 15,"bold"),bg="#A3C178").place(x=360,y=200)
        self.txt_nbriteramax = Entry(frame1,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350")
        self.txt_nbriteramax.place(x=440,y=203,width=160)
        
        #=================fermer l'accolade===================================#
        self.coladfer = Label(frame1,text=" } Output   :",font=("Comic Sans MS", 15,"bold"),bg="#A3C178",fg="#182350").place(x=10,y=260)
        
        #==============Frame1  ===============================================#
        frame2=Frame( frame1,bg="#C4C6C6" ,highlightbackground="#182350",highlightthickness=3)
        frame2.place(x=10,y=310,height=340,width=875)
        
        #=================================================solution Bissection===========================================#
        self.solution = Label(frame2,text="The interval [a , b]  :",font=("Comic Sans MS",15,"bold"), bg="#C4C6C6").place(x=10,y=20)
        #----------------------- la valeur de la solution a [a,b] -------------------------------------------------------#
        self.val_a_solutiFib = Label(frame2,text=" a :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=20)
        self.varFibA = DoubleVar()
        self.txt_val_a_solutFib = Entry(frame2,font=("times new romman",16,"bold"), bg="lightgray",fg="#182350", textvariable=self.varFibA)
        self.varFibA.set("")
        self.txt_val_a_solutFib.place(x=290,y=23,width=250)
        
        
        #----------------------- la valeur de la solution b [a,b] --------------------------------------------------------#
        self.val_b_solutiFib = Label(frame2,text=" b:",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=547,y=20)
        self.varFibB = DoubleVar()
        self.txt_val_solutionFibB = Entry(frame2,font=("times new romman",16,"bold"), bg="lightgray",fg="#182350", textvariable=self.varFibB)
        self.varFibB.set("")
        self.txt_val_solutionFibB.place(x=583,y=23,width=250)
        
        #--------------------------------val des nomber des itoration  i Bissection----------------------------------------#
        self.nbr_fib_iteration = Label(frame2,text="Number of iterations:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=110)
        self.val_itera_fib = Label(frame2,text=" i :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=110)
        self.var_fib_itir = IntVar()
        self.txt_itera_fib = Entry(frame2,font=("times new romman",16,"bold"), bg="lightgray",fg="red", textvariable=self.var_fib_itir)
        self.var_fib_itir.set("")
        self.txt_itera_fib.place(x=290,y=113,width=250)
        
        
        #---------------------------------------interprétation---------------------------------------------------------------#
        self.nbr_iterpretation = Label(frame2,text="Interpretation        :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=210)
        self.var_iterpreFib = StringVar()
        self.txt_iterpretatFib = Entry(frame2,font=("times new romman",16,"bold"), bg="lightgray",fg="green", textvariable=self.var_iterpreFib)
        self.var_iterpreFib.set("")
        self.txt_iterpretatFib.place(x=290,y=213,width=545)
        
       
        #=========================================================== boutton Fibonacci =========================================================================================================#
        Fibonacci_Button  = Button(frame2,font=("times new romman",16,"bold"),text=" Fibonacci ",bd=0,cursor="hand2",bg="#719B6F",fg="#E5E1D6",activebackground ="#7AA1E6",activeforeground="#BF846C",borderwidth = 5, command = self.fibonacci).place(x=320 ,y=270,width=270)
          
         #============================================================ Bouton le graphe de la fonction ===========================================================================================#
        graphe= Button(frame2,font=("times new romman",16,"bold"),text="graph of the fonction",bd=0,cursor="hand2",bg="#7B9764",fg="#E5E1D6",activebackground ="#CDD3C8",activeforeground="#BFF790",borderwidth = 5, command=self.graphe_de_fonction).place(x=10 ,y=270,width=240)
        
     
        #============================================================ Bouton quit ============================================================================================================#
        Accull= Button(frame2,font=("times new romman",16,"bold"),text="Quit ",bd=0,cursor="hand2",bg="#811000",fg="#F9F2F1",activebackground ="#CAE5E4",activeforeground="#E8A490",borderwidth = 5, command=self.quiter).place(x=640 ,y=270,width=200)
        
      
        
      
   #-------------Pour quiter------------------------------------#       
    def quiter(self):
       self.fenetre3.destroy()
       
       
    #----------------pour vider les comps-------------------------------------#
    def clearChamp(self):
        self.txt_val_a_solutFib.delete(0, END)
        self.txt_val_solutionFibB.delete(0, END)
        self.txt_iterpretatFib.delete(0, END)
        self.txt_itera_fib.delete(0, END)     
        
       
        
       
    #==============l'algorithme de fibonacci==================================#    
    def fibonacci(self):
         self.clearChamp()
         val1 = self.txt_val_a.get()
         val2 = self.txt_val_b.get()
         fon = self.txt_fonc.get()
         maxde_i = self.txt_nbriteramax.get()
         if(val1 =="" or val2 ==""  or fon =="" or maxde_i =="" ):
             MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre3)
         else:
              try:                  
                  a = float(val1)
                  b = float(val2)
                  max_iteratin = int(maxde_i)
                  if(a > b):
                      MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre3)
                  else:
                      def f(x):
                          y = eval(fon)
                          return y 
                         
                      fprimde_a = misc.derivative(f, a, dx=1.0, n=1, args=(), order=3) - 1
                      fprimde_b = misc.derivative(f, b, dx=1.0, n=1, args=(), order=3) - 1
                      
                      if(fprimde_a < 0 and  fprimde_b > 0):
                            plt.clf()
                            y = np.linspace(a, b, 1000)
                            plt.plot(y, f(y), label = "La courbe de f(x) ")
                            plt.title(" Fibonacci ")
                            plt.xlabel("Abscisses")
                            plt.ylabel("Ordonnees")
                            plt.plot(a , f(a) , 'r.')
                            plt.plot(b , f(b) , 'r.')
                            j=1
                            #====la fonction est unimodal donc ok=============#
                            #-------- la suit de fibonacci--------------------#
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
                            
                            #------la calcule de x1 et x2---------------------#
                            x1 = (fib_N / fib_Nplus2) * d1 + a
                            x2 = ( fib_Nplus1 / fib_Nplus2 )* d1 + a
                            
                            #____________________la boucle for _______________#
                            for i in range(1, max_iteratin):
                                if( f(x2) > f(x1) ):
                                    b = x2
                                    x2 = x1
                                    x1 = ((a * fib(max_iteratin - i + 1) + b * fib( max_iteratin - i)) / fib(max_iteratin - i + 2))
                                    #-------------les point dans le graphe--------#
                                    plt.plot(x1, f(x1), 'r.')
                                    j =j+1
                                else:
                                    a = x1
                                    x1 = x2
                                    x2 = ((b * fib(max_iteratin - i + 1) + a * fib(max_iteratin - i)) / fib(max_iteratin - i + 2))                          
                                    #-------------les point dans le graphe--------#
                                    plt.plot(x2, f(x2), 'r.')
                                    j = j+1
                                
                            #-------------------------------        
                            x2 = x2 + 0.001
                            if(f(x2) > f(x1)): #return [a ; x2]
                                self.varFibA.set(a)
                                self.varFibB.set(x2)
                                self.var_fib_itir.set(j)
                                self.var_iterpreFib.set("la solution x* est dans l'intervale ["+str(a) +" , "+ str(x2) +"]")
                                plt.plot(a, f(a), 'g.')
                                plt.plot(a, f(a), label="l'interval [a, b]")
                                plt.plot(x2, f(x2), 'g.')
                                plt.legend()
                                plt.show()
                            else: #return [x1 ; b]
                                self.varFibA.set(x1)
                                self.varFibB.set(b)
                                self.var_fib_itir.set(j)
                                self.var_iterpreFib.set("la solution x* est dans l'intervale ["+str(x1) +" , "+ str(b) +"]")
                                plt.plot(b, f(b), 'g+')
                                plt.plot(b, f(b), label="l'interval [a, b]")
                                plt.plot(x1, f(x1), 'g+')
                                plt.legend()
                                plt.show()
                                    
                      else:
                           MessageBox.showwarning("Error","On ne peut pas Appliquer algorithme de Fibonacci sur cette fonction dans ces deux points. par ce que ona f'(a)*f'(b) > 0 !!",parent=self.fenetre3)
                           self.var_iterpreFib.set("Fibonacci ne fonction pa car f'(a)*f'(b) > 0")
              except Exception as es:                  
                   MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre3)  
        
        
        
        
        
    #======================Le gghaphe de la fonction==========================#   
    def graphe_de_fonction(self):
            val1 = self.txt_val_a.get()
            val2 = self.txt_val_b.get()
            fonc = self.txt_fonc.get()
            
            if(val1 =="" or val2 =="" or fonc =="" ):
                MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre3)
            elif(val1 > val2):
                MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre3)
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
                    MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre3) 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
fenetre3=Tk()
obj=Fibonacci(fenetre3)
fenetre3.mainloop()  
                        
#--importer les biblio nécessaire
from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
import numpy as np
from scipy import misc 
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler

from matplotlib.figure import Figure


class Bissection :
    def __init__(self,fenetre1):#define le constrocteur
        self.fenetre1=fenetre1
        #-----------le titre--------------------------------------------------#
        self.fenetre1.title("Bissection Search")
        #-----------------la geometrerde la fenetre---------------------------#
        self.fenetre1.geometry("1000x720+150+50")
        #-----------------le coleure de bag-----------------------------------#
        self.fenetre1.config(bg="#94A6AB")   
        #-----------bloquer le redimentionnement de la fenetre----------------# 
        self.fenetre1.resizable(width=False, height=False)
        #--------------logo de l'application----------------------------------#
        self.fenetre1.iconbitmap("images/logoimag.ico")
        
        #============a creation de frame principale dans noter fenetre========#
        framprincipale=Frame( self.fenetre1, bg="#94A6AB", highlightbackground="#C8E3EC",highlightthickness=2)
        framprincipale.place(x=45,y=40,height=660,width=900)
        #---------------le titre----------------------------------------------#
        title = Label( self.fenetre1,text="Bissection Search",font=("Comic Sans MS", 17,"bold"), bg="#94A6AB",fg="#C8E3EC").place(x=380,y=5)
       
        #----------------les entrer de l'algorithme---------------------------#
        entrer1 = Label(framprincipale,text="Input { ",font=("Comic Sans MS", 15,"bold"), bg="#94A6AB",fg="#182350").place(x=10,y=10)
        
        #=================l'intervale ========================================#
        intervale1 = Label(framprincipale,text="The interval [a , b]   :",font=("Comic Sans MS", 15,"bold"),bg="#94A6AB").place(x=110,y=20)
        
        #================valeur de a =========================================#
        valeurA = Label(framprincipale,text=" a :",font=("Comic Sans MS", 15,"bold"),bg="#94A6AB").place(x=400,y=20)
        self.txtValeur_A = Entry(framprincipale,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350")
        self.txtValeur_A.place(x=440,y=23,width=160)
        
        #================la valeure de b =====================================#
        valeurdeB = Label(framprincipale,text=" b :",font=("Comic Sans MS", 15,"bold"),bg="#94A6AB").place(x=630,y=20)
        self.txtValeur_B = Entry(framprincipale,font=("times new romman",15,"bold"), bg="lightgray",fg="#182350")
        self.txtValeur_B.place(x=675,y=23,width=160)
        
        #===================la fonction=======================================#
        fonction22 = Label(framprincipale,text="Function               : ",font=("Comic Sans MS", 16,"bold"),bg="#94A6AB").place(x=110,y=80)
        fonction22F1 = Label(framprincipale,text="f(x)  =",font=("Comic Sans MS", 16,"bold"),bg="#94A6AB").place(x=360,y=80)
        self.txt_fonction = Entry(framprincipale,font=("times new romman", 17,"bold"), bg="lightgray",fg="#182350")
        self.txt_fonction.place(x=440,y=83,width=397 )
        
        #================la tolérence  =======================================#
        delta1 = Label(framprincipale,text="Tolerance              :",font=("Comic Sans MS", 15,"bold"),bg="#94A6AB").place(x=110,y=140)
        delTTa1 = Label(framprincipale,text="delta =",font=("Comic Sans MS", 15,"bold"),bg="#94A6AB").place(x=360,y=140)
        self.deltaBissection = DoubleVar()
        self.txtdelta1 = Entry(framprincipale,font=("times new romman", 15,"bold"), bg="lightgray",fg="#182350", textvariable=self.deltaBissection)
        self.deltaBissection.set(0.001)
        self.txtdelta1.place(x=440,y=143,width=160)
        
        #=================fermer l'accolade===================================#
        coladfer = Label(framprincipale,text=" } Output   :",font=("Comic Sans MS", 15,"bold"),bg="#94A6AB",fg="#182350").place(x=10,y=200)
        
        #==============la 2ime frame frame2 ==================================#
        self.frame2=Frame( framprincipale,bg="#C4C6C6" ,highlightbackground="#182350",highlightthickness=3)
        self.frame2.place(x=10,y=245,height=400,width=875)
        
        #====================solution trouver Bissection======================#
        solution = Label(self.frame2,text="The interval [a , b]  :",font=("Comic Sans MS",15,"bold"), bg="#C4C6C6").place(x=10,y=10)
        #------------------ la valeur de la solution  [a,b]------------------#
        valeurAsol = Label(self.frame2,text=" a :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=10)
        self.varDeA = DoubleVar()
        self.txtAsolut = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.varDeA)
        self.varDeA.set("")
        self.txtAsolut.place(x=290,y=13,width=250)
        
        #-------------------la valeur de la solution b [a,b] -----------------#
        valeurB_sol = Label(self.frame2,text=" b:",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=547,y=10)
        self.varDeBsol = DoubleVar()
        self.txtvalsolB = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="#182350", textvariable=self.varDeBsol)
        self.varDeBsol.set("")
        self.txtvalsolB.place(x=583,y=13,width=250)        
        
        #---------------la valeur exacte de la solution si l'algorithme arive a calculer x*--------------------------------#
        val_solution_exact = Label(self.frame2,text="The solution          :",font=("Comic Sans MS", 15,"bold"),bg="#C4C6C6").place(x=10,y=70)
        #-----------------------------------------------x*-----------------------------------------------------------------#
        val_x_sol = Label(self.frame2,text=" x*:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=247,y=70)
        self.varsolBissect = DoubleVar()
        self.txtSolExac = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="green", textvariable=self.varsolBissect)
        self.varsolBissect.set("")
        self.txtSolExac.place(x=290, y=73, width=250)
        
        #--------------------------------val des nomber des itération fait l'algorithme de Bissection-----------------------#
        nbr_itera_max = Label(self.frame2,text="Number of iterations:",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=140)
        val_itera_bissec = Label(self.frame2,text=" i :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=250,y=140)
        self.varbissecitir = IntVar()
        self.txt_itera_bissect = Entry(self.frame2,font=("Comic Sans MS",15,"bold"), bg="lightgray",fg="red", textvariable=self.varbissecitir)
        self.varbissecitir.set("")
        self.txt_itera_bissect.place(x=290,y=143,width=250)
          
        #---------------------------------------interprétation---------------------------------------------------------------#
        nbr_iterpre = Label(self.frame2,text="Interpretation        :",font=("Comic Sans MS", 15,"bold"), bg="#C4C6C6").place(x=10,y=210)
        self.var_iterpreBissec = StringVar()
        self.txtiterpretatBissec = Entry(self.frame2,font=("Comic Sans MS", 15,"bold"), bg="lightgray",fg="#182350", textvariable=self.var_iterpreBissec)
        self.txtiterpretatBissec.place(x=290,y=213,width=545)
        
        
        #============================================================ Bouton Bissection ========================================================================================================#
        Bissection_boutton = Button(self.frame2,font=("times new romman",16,"bold"),text=" Bissection ",bd=0,cursor="hand2",bg="#0575B0",fg="#E5E1D6",activebackground ="#CAE5E4",activeforeground="#0F5A7D",borderwidth = 5, command=self.Bissection).place(x=320 ,y=330,width=240)
        
        #============================================================ Bouton Accueil ========================================================================================================#
        Accull= Button(self.frame2,font=("times new romman",16,"bold"),text="Quit ",bd=0,cursor="hand2",bg="#811000",fg="#E5E1D6",activebackground ="#CAE5E4",activeforeground="#E8A490",borderwidth = 5, command=self.quiter).place(x=640 ,y=330,width=200)
        
        #============================================================ Bouton le graphe de la fonction ========================================================================================================#
        graphee= Button(self.frame2,font=("times new romman",16,"bold"),text="graph of the fonction",bd=0,cursor="hand2",bg="#7B9764",fg="#F9F2F1",activebackground ="#CDD3C8",activeforeground="#BFF790",borderwidth = 5, command=self.graphe_de_fonction).place(x=10 ,y=330,width=240)
        
     
     
       
        
     
    #-------------Pour quiter------------------------------------#       
    def quiter(self):
       self.fenetre1.destroy()
        
     
        
     #----------------pour vider les comps----------------------------------------#
    def clearChamp(self):
        self.txtAsolut.delete(0, END)   #pour vider le champs de a dans l'intervale [a, b]
        self.txtvalsolB.delete(0, END)    #pour vider le champs de b dans l'intervale [a, b]
        self.txtSolExac.delete(0, END)      #pour vider le champs de solution exacte x*
        self.txt_itera_bissect.delete(0, END)  #pour vider le champs de nbr d'itiration
        self.txtiterpretatBissec.delete(0, END)  #pour vider le champs de l'interprétation

   
 #------------------------Algoritheme de bissection---------------------------#
    def Bissection(self):
            self.clearChamp() #appel la coction pour vider les chams avant d'appliquer l'algorithme une autre fois
            #-----------recuperer les valeurs enter par l'uteliateur----------#
            val1 = self.txtValeur_A.get() #la valeur de a (extrimité de lintervale[a, b])
            val2 = self.txtValeur_B.get() # la valeur de b extrimité de lintervale[a, b])
            delTTa1 = self.txtdelta1.get() # la tolérence delta
            fonction22t = self.txt_fonction.get() #la fonction f(x)
            if(val1 =="" or val2 =="" or delTTa1 =="" or fonction22t ==""): #message d'erreur si l'un des entrer n'est pas sisais 
                MessageBox.showerror("Error"," Remplir tout les champs SVP !!", parent=self.fenetre1)
           
            else: 
                try:                   
                     A = float(val1)#convirtir les valeurs saisis en des float
                     B = float(val2)
                     delta1 = float(delTTa1)
                     if(A > B): #pour verifier que l'interval saisie est valide
                          MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre1)
                     else:
                         #----------evaluation de la fonction22tion --------------#
                         def f(x):
                             y = eval(fonction22t)
                             return y 
                         #----------le graphe de f--------------------------------#
                         plt.clf()
                         y = np.linspace(A, B, 1000)
                         plt.plot(y, f(y), label = "La courbe de f(x) ")
                         plt.title(" Bissection ")
                         plt.xlabel("Abscisses")
                         plt.ylabel("Ordonnees")   
                         
                         #-----------la calcule de dirivée de f en point a et b---# 
                         fprim_a = misc.derivative(f, A, dx=1.0, n=1, args=(), order=3) -1    
                         fprim_b = misc.derivative(f, B, dx=1.0, n=1, args=(), order=3) - 1
                         #----initialisation de deux var pour calculer le nomber des itiration 
                         j = 1243
                         k=1101
                         #----------------la condition de vérification------------#
                         if( fprim_a < 0 and fprim_b > 0):
                             plt.plot(A , f(A), 'r.')
                             plt.plot(B , f(B), 'r.')
                             #---------indice de nomber d'incrémentation ---------#
                             i=1
                             
                             
                             while( abs(A - B) > delta1):
                                 #-------- la valeur de c ----------------------------#
                                 C = (B + A)/2 #la calcule de c
                                 aprim = misc.derivative(f, A, dx=1.0, n=1, args=(), order=3) -1 #la diriver premier en a
                                 bprim = misc.derivative(f, B, dx=1.0, n=1, args=(), order=3) -1 #la deriver premier en b
                                 if( aprim < 0 and bprim > 0): #vérifier que f prime de  A < 0 et f prim de B > 0 : c-a-d f est convexe
                                     #-----------------la dérivé au point c :--------------------------------#
                                     fprimDec = misc.derivative(f, C, dx=1.0, n=1, args=(), order=3) -1
                                     if(fprimDec <= 0): #---si f prime en c est < 0 c-a-d f est decroissante en c
                                           if(fprimDec == 0):#---si f prime en c est null danc ona un minimum locale
                                               #----------------------- la calcule de f seconde de f en poit c -------------#
                                                 fseconfDec = misc.derivative(f, C, dx=1.0, n=2, args=(), order=3)
                                                 if(fseconfDec > 0): #si f seconde est > 0 alor ona un minimum locale
                                                     self.varsolBissect.set(C) #affichade de valeur de c
                                                     self.varbissecitir.set(i) #affichage de nbr d'itiration
                                                     Texte = StringVar() #--ifichage d'une petit interpretation
                                                     mylabel = Label(self.frame2, font=("Comic Sans MS", 15,"bold"), bg="lightgray",fg="green", textvariable=Texte).place(x=290,y=263,width=545)
                                                     Texte.set('la solution  '+ str(C) + ' est un minimum de la fonction f(x) ')
                                                     plt.plot(C, f(C), 'g+') #ploter la point de la solution
                                                     break #pour sorti dans la boucle  while
                                                 elif(fseconfDec < 0):#si f seconde est > 0 alor ona un maximum locale
                                                     self.varsolBissect.set(C) #affichade de valeur de c
                                                     self.varbissecitir.set(i)#affichage de nbr d'itiration i
                                                     Texte = StringVar()#--ifichage d'une petit interpretation
                                                     mylabel = Label(self.frame2, font=("Comic Sans MS", 15,"bold"), bg="lightgray",fg="green", textvariable=Texte).place(x=290,y=263,width=545)
                                                     Texte.set('la solution  '+ str(C) + '  est un maximum de la fonction f(x) ')
                                                     plt.plot(C, f(C), 'g+') #ploter la point de la solution
                                                     break    # pour sorti dans la boucle while
                                                 else : #si non c-a-d f seconde en c est null alors ona une point d'inflexion !
                                                     self.var_iterpreBissec.set("Ona une Point d inflexion dans le point : "+str(C)) #affichage de l'interpretation de cette situation
                                                     MessageBox.showinfo("Error"," Ona une Point d'inflexion !!", parent=self.fenetre1)
                                                     break
                                           else :
                                                    plt.plot(A, f(A), 'r.') #chaque itiration de l'algorithme en plote les point A  trouver par lalgorithme
                                                    A = C # mise a jour de A par C
                                                    j = A #une condition pour sorti dans le cas de la meme valeur trouver dans l'itiration k et k+1 sont egaux (pour avoir le nbr d'itiration fait l'algorithme exactement)
                                                    i+=1 #incrementer i 
                                     else : 
                                             plt.plot(B, f(B), 'r.')#chaque itiration de l'algorithme en plote les point B  trouver par lalgorithme
                                             B = C # mise a jour de B par C
                                             k = B #une condition pour sorti dans le cas de la meme valeur trouver dans l'itiration k et k+1 sont egaux (pour avoir le nbr d'itiration fait l'algorithme exactement)
                                             i+=1 #incrémentation de nbr d'itiration i 
                             
                                     
                                 #-- dans cette partie on traiter le cas ou la fonction f est concave 
                                 elif(aprim > 0 and bprim < 0): 
                                     C = (B + A)/2 #la calcule de c
                                     plt.plot(A , f(A), 'r.') #ploter A et B
                                     plt.plot(B , f(B), 'r.')
                                     i=1   #initialisation d'un compteur qui permet de calculer le nomber d'itiration
                                     if(fprimDec >= 0): #---le cas ou f prime en c est >= 0
                                           if(fprimDec == 0): #si f prim est nulle en c dan ona une maximum locale 
                                               #----------------------- la calcule de f seconde de f en poit c -------------#
                                                 fseconfDec = misc.derivative(f, C, dx=1.0, n=2, args=(), order=3)
                                                 if(fseconfDec > 0):#si f seconde > 0 danc onaune minimum
                                                     self.varsolBissect.set(C)#affichade de valeur de c
                                                     self.varbissecitir.set(i)#affichade de valeur de compteur i 
                                                     Texte = StringVar() #affichade de l'interprétation
                                                     mylabel = Label(self.frame2, font=("Comic Sans MS", 15,"bold"), bg="lightgray",fg="green", textvariable=Texte).place(x=290,y=263,width=545)
                                                     Texte.set('la solution  '+ str(C) + '  est un minimum de la fonction f(x) ')
                                                     plt.plot(C, f(C), 'g+') #ploter la solution dans le graphe
                                                     break #Alors stop
                                                 elif(fseconfDec < 0):#si f seconde < 0 danc onaune maximum locale
                                                     self.varsolBissect.set(C)#affichade de valeur de c
                                                     self.varbissecitir.set(i)#affichade de valeur de i
                                                     Texte = StringVar()#affichade de l'interprétation
                                                     mylabel = Label(self.frame2, font=("Comic Sans MS", 15,"bold"), bg="lightgray",fg="green", textvariable=Texte).place(x=290,y=263,width=545)
                                                     Texte.set('la solution  '+ str(C) + '  est un maximum de la fonction f(x)')
                                                     plt.plot(C, f(C), 'g+')  #ploter la solution dans le graphe
                                                     break   #stop
                                                 else :# si f seconde en C est null alors ona une point d'inflection 
                                                     self.var_iterpreBissec.set("Ona une Point d inflexion dans le point : "+str(C))
                                                     MessageBox.showinfo("Error"," Ona une Point d'inflexion !!", parent=self.fenetre1)
                                                     break #alors stop!
                                           else :
                                               if(j== A and k==B):
                                                    break
                                               else:
                                                    plt.plot(A, f(A), 'r.') #ploter dans le graphe les traces de l'algorithme valeur da A
                                                    A = C #mise a jour de A par C
                                                    j=A #une condition pour sorti dans le cas de la meme valeur trouver dans l'itiration k et k+1 sont egaux (pour avoir le nbr d'itiration fait l'algorithme exactement)
                                                    i+=1 #incrémentations de nbr d'itiration
                                     else :
                                         if(A==j and k == B): 
                                             break
                                         else:  
                                             plt.plot(B, f(B), 'r.') #ploter dans le graphe les trace de l'algorithme valeur de B
                                             B = C #mise a jour de B par C
                                             k= B #une condition pour sorti dans le cas de la meme valeur trouver dans l'itiration k et k+1 sont egaux (pour avoir le nbr d'itiration fait l'algorithme exactement)
                                             i+=1 #incrémentations de nbr d'itiration
                                         
                                 elif((aprim > 0 and bprim > 0)or(aprim < 0 and bprim < 0)) :
                                     quit()
                                     
                             #-Affichage des resultats final dans l'interface-#
                             self.varDeA.set(A) #la valeur de A
                             self.varDeBsol.set(B) #la valeur de B
                             self.varbissecitir.set(i) #le nbr d'itir 
                             self.var_iterpreBissec.set("la solution x* est dans l'intervale ["+str(A) +" , "+ str(B) +"]")
                             plt.plot(A, f(A), label="l'intervale [a, b] ")
                             plt.plot(A, f(A), 'g+') #ploter es dernier valeur de A et B 
                             plt.plot(B, f(B), 'g+') #trouver par l'algorithme
                             plt.legend()
                             plt.show()
                         else:
                             MessageBox.showwarning("Error","On ne peut pas Appliquer algorithme de Bissection sur cette fonction22tion dans ces deux points. par ce que ona f'(a)*f'(b) > 0 !!",parent=self.fenetre1)
                             self.var_iterpreBissec.set("Bissection ne fonction22tions pas car f'(a)*f'(b) > 0")
                             plt.clf()
                             
                except Exception as es:                  
                        MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre1)  
                
       

     #======================Le gghaphe de la fonction==========================#   
    def graphe_de_fonction(self):
            val1 = self.txtValeur_A.get()
            val2 = self.txtValeur_B.get()
            fonc = self.txt_fonction.get()
            
            if(val1 =="" or val2 ==""  or fonc =="" ):
                MessageBox.showerror("Error"," Remplir tout les champs svp!", parent=self.fenetre1)
            
            else :
                try:
                    a = float(val1)
                    b = float(val2)
                    if(a > b):
                        MessageBox.showerror("Error","Intervale invalide !! \n Sisair deux entier tel que a < b ", parent=self.fenetre1)
                   
                    else:
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
                    MessageBox.showerror("Error",f" Error Due to : {str(es)} ", parent=self.fenetre1) 
        
        

fenetre1=Tk()
obj=Bissection(fenetre1)
fenetre1.mainloop()  
        
        
        


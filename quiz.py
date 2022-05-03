from tkinter import *
from tkinter import messagebox as mb
import json

class Quiz:
    def __init__(self):

        self.nbr_Q =0 
         
        self.affich_titre()

        self.affich_quest()
         
        self.affich_quested=IntVar()
      
        self.opts=self.bouton_radio()

        self.affich_options()
         
        self.boutons()
         
        self.taille_données=len(question)
         
        self.correctes=0

    def affich_result(self):
         
        fausses_rep = self.taille_données - self.correctes
        correctes = f"correctes: {self.correctes}"
        fausses = f"fausses: {fausses_rep}"
         
        score = int(self.correctes / self.taille_données * 100)
        result = f"Score: {score}%"

        mb.showinfo("Résultat", f"{result}\n{correctes}\n{fausses}")
 
    def verif_rep(self,nbr_Q ):
         
        if self.affich_quested.get() == reponses[nbr_Q]:
            return True
 
    def suivant_btn(self):
         
        if self.verif_rep(self.nbr_Q):
            self.correctes += 1

        self.nbr_Q += 1

        if self.nbr_Q==self.taille_données:
            self.affich_result()
            gui.destroy()

        else:
            self.affich_quest()
            self.affich_options()
 
    def boutons(self):

        suiv_btn = Button(gui, text="Suivant",command=self.suivant_btn,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        suiv_btn.place(x=350,y=380)
 
    def affich_options(self):
        val=0
        self.affich_quested.set(0)

        for option in options[self.nbr_Q]:
            self.opts[val]['text']=option
            val+=1
  
    def affich_quest(self):
         
        nbr_Q = Label(gui, text=question[self.nbr_Q], width=60, fg="red",
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        nbr_Q.place(x=70, y=100)
 
    def affich_titre(self):
         
        title = Label(gui, text="A toi de deviner !",
        width=35, bg="black",fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=0)

    def bouton_radio(self):

        q_list = []
         
        y_pos = 150
         
        while len(q_list) < 4:
             
            radio_btn = Radiobutton(gui,text=" ",variable=self.affich_quested,
            value = len(q_list)+1,font = ("ariel",14))
             
            q_list.append(radio_btn)
             
            radio_btn.place(x = 100, y = y_pos)

            y_pos += 40
         
        return q_list
 
gui = Tk()
gui.geometry("600x450")
gui.title("Quiz_couleur")

f= open('data.json') 
data = json.load(f)

question = (data['question'])
options = (data['options'])
reponses = (data[ 'reponses'])
 
quiz = Quiz()
gui.mainloop()
 
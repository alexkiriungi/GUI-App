import customtkinter as ctk
import tkinter as tk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
appWidth, appHeight = 600, 700
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("GUIApp")
        self.geometry(f"{appWidth} x {appHeight}")
        self.nameLabel = ctk.CTkLabel(self, text ="Name")
        self.nameLabel.grid(row=0, column=0, padx=20, pady=20,sticky="ew")
        
        self.nameEntry = ctk.CTkEntry(self, placeholder_text="Your Name")
        self.nameEntry.grid(row=0, column=1, columnspan=3,padx=20,pady=20,sticky="ew")
        
        self.agelabel = ctk.CTkLabel(self, text="Age")
        self.agelabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        
        self.ageEntry = ctk.CTkEntry(self, placeholder_text="Your Age")
        self.ageEntry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
        
        self.genderLabel = ctk.CTkLabel(self, text="Gender")
        self.genderLabel.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        
        self.genderVar = tk.StringVar(value="Prefer\ not to say")
        self.maleRadioButton = ctk.CTkRadioButton(self, text="Male",
                                                  variable= self.genderVar,
                                                  value = "He is")
        self.maleRadioButton.grid(row=2,column=1,padx=20,pady=20, sticky="ew")
        
        self.femaleRadioButton = ctk.CTkRadioButton(self, text="Female",
                                                    variable= self.genderVar,
                                                    value = "She is")
        self.femaleRadioButton.grid(row=2, column=2,padx=20,pady=20, sticky="ew")
        
        self.noneRadioButton = ctk.CTkRadioButton(self, text="Prefer not to say",
                                                  variable=self.genderVar,
                                                  value="They are")
        self.noneRadioButton.grid(row=2, column=3, padx=20, pady=20, sticky="ew")
        
        self.choiceLabel = ctk.CTkLabel(self, text="Feed")
        self.choiceLabel.grid(row=3,column=0, padx=20, pady=20, sticky="ew")
        
        self.checkboxVar = tk.StringVar(value="Choice 1")
        
        self.choice1 = ctk.CTkCheckBox(self, text="Beef-eater",
                                       variable = self.checkboxVar,
                                       onvalue = "Beef-eater")
        
        self.choice1.grid(row=3,column=2,padx=20, pady=20, sticky="ew")
        
        self.choice2 = ctk.CTkCheckBox(self, text="Vegetarian",
                                       variable=self.checkboxVar,
                                       onvalue="Vegetarian")
        
        self.choice2.grid(row=3, column=3, padx=20, pady=20, sticky="ew")
        
        self.occupationLabel = ctk.CTkLabel(self, text="Occupation")
        self.occupationLabel.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
        
        self.occupationOptionMenu = ctk.CTkOptionMenu(self, values=["Students",
                                                                   "Working Professional"])
        self.occupationOptionMenu.grid(row=4, column=1, padx=20, pady=20, columnspan=2, sticky="ew")
        
        self.generateResultsButton = ctk.CTkButton(self, text="Generate Results", command= self.generateResults)
        self.generateResultsButton.grid(row=5, column=1, padx=20, pady=20, sticky="ew")
        
        self.displaybox = ctk.CTkTextbox(self, width=200, height=100)
        self.displaybox.grid(row=6, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")
        
    def generateResults(self):
        self.displaybox.delete("0.0", "200.0")
        text = self.createText()
        self.displaybox.insert("0.0", text)
            
            
    def createText(self):
        checkboxvalue = " "
            
        if self.choice1._check_state and self.choice2._check_state:
            checkboxvalue += self.choice1.get() + " and " + self.choice2.get()
        elif self.choice1._check_state:
            checkboxvalue += self.choice1.get()
        elif self.choice2._check_state:
            checkboxvalue += self.choice2.get()
        else:
            checkboxvalue = "none of the available options"
            
        text = f"{self.nameEntry.get()} : \n{self.genderVar.get()} {self.ageEntry.get()} years old and is a {checkboxvalue}\n"
        text += f"{self.genderVar.get()} currently a {self.occupationOptionMenu.get()}"
        return text
        
    
if __name__ == '__main__':
    app = App()
    app.mainloop()
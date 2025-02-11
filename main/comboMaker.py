import tkinter as tk
import json
import os

os.chdir(r"C:\Users\felix\Combo Maker")
q = open(r"main\sf6Moves.json")
sf6Moves = json.load(q)

class Application:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1920x1080") # TODO: Add support for resizing'
        self.master.after(100, self.gameSelect) # Ensures window is drawn before call

    def gameSelect(self):
        for child in self.master.winfo_children(): child.destroy() # Wipe elements from screen

        title = tk.Label(self.master, text="Combo Maker", anchor="center", bg="light gray", font=("Arial", 42, "bold"))
        title.pack(padx=20, pady=40)

        halfX = self.master.winfo_width() // 2  # Get window width, divide by 2
        halfY = self.master.winfo_height() // 2  # Get window width, divide by 2

        # Street Fighter 6 Button
        sf6But = tk.Button(self.master, text="Street Fighter 6", width=50, height=7, command=self.sf6CharSel)
        sf6But.place(x=halfX * 0.75, y=halfY, anchor="center")

        # Tekken 8 Button
        tekBut = tk.Button(self.master, text="Tekken 8", width=50, height=7, command=self.tekCharSel)
        tekBut.place(x=halfX * 1.25, y=halfY, anchor="center")

    def sf6CharSel(self):
        for child in self.master.winfo_children(): child.destroy() # Wipe elements from screen

        # "Go Back" button
        backButton = tk.Button(self.master, text="Go Back", width=10, height=3, command=self.gameSelect)
        backButton.place(x=10, y=10)
        
        title = tk.Label(self.master, text="Street Fighter 6", anchor="center", bg="light gray", font=("Arial", 42, "bold"))
        subTitle = tk.Label(self.master, text="Character Select", anchor="center", bg="light gray", font=("Arial", 22, "bold"))

        title.pack(padx=20, pady=20)
        subTitle.pack(padx=20, pady=10)
        
        buttonFrame = tk.Frame(self.master, background="")
        buttonFrame.pack(pady=20)

        # 25 total characters, listed in order of appearance on roster
        sf6_characters = [
            ["Luke", "Jamie"],
            ["Manon", "Kimberly", "Marisa", "Lily"],
            ["JP", "Juri", "Dee Jay", "Cammy"],
            ["Ryu", "E. Honda", "Blanka", "Guile"], 
            ["Ken", "Chun Li", "Zangief", "Dhalsim"],
            ["Rashid", "AKI", "Ed", "Akuma"], 
            ["M. Bison", "Terry", "Mai"]
        ]
        for rowIndex, row in enumerate(sf6_characters):
            numChars = len(row)
            startCol = (4 - numChars) // 2 # Center the row based upon 4 columns
            for colIndex, name in enumerate(row):
                btn = tk.Button(
                    buttonFrame, text=name, width=12, height=2,
                    command=lambda n=name: self.sf6ComboScreen(n) # Waits for button click, passes name to sf6ComboScreen function
                )
                btn.grid(row=rowIndex, column=startCol + colIndex, padx=5, pady=5)
    
    def sf6ComboScreen(self, name):
        for child in self.master.winfo_children(): child.destroy()
        
        backButton = tk.Button(self.master, text="Go Back", width=10, height=3, command=self.sf6CharSel)
        backButton.place(x=10, y=10)

        title = tk.Label(self.master, text=name, anchor="center", bg="light gray", font=("Arial", 42, "bold"))
        title.pack(padx=20, pady=20)

        buttonFrame = tk.Frame(self.master, width=self.master.winfo_width(), height=(self.master.winfo_height() // 3)) # TODO: Make transparent
        buttonFrame.pack(side="bottom")
        
        #   ↖7   ↑8   9↗
        #   ←4        6→   Directions will be in an 8 way pattern, named as such 
        #   ↙1   ↓2   3↘   Arrows will depict these on the User Interface

        directions = [
            ["7", "8", "9"],  # Top row
            ["4", "0", "6"],  # Middle row (0 is neutral)
            ["1", "2", "3"]   # Bottom row
        ]

        for row in range(2, -1, -1):
            for col in range(3):
                if directions[row][col] == 0: ## TODO: Fix this mess
                    continue
                else:
                    path = r"assets\dir" + directions[row][col] + ".png"
                    img = tk.PhotoImage(file=path)
                    img = img.subsample(4,4)
                    btn = tk.Button(buttonFrame, image=img, command=lambda direct=directions[row][col]: print(direct)) # TODO: Add functionality beyond testing
                    btn.grid(row=row, column=col)
        print(sf6Moves[name]["specials"]) # Test if reading

        # TODO: Finish .json list of special moves and supers



    def tekCharSel(self):
        for child in self.master.winfo_children(): child.destroy() # Wipe elements from screen

        backButton = tk.Button(self.master, text="Go Back", width=10, height=3, command=self.gameSelect)
        backButton.place(x=10, y=10)

        title = tk.Label(self.master, text="Tekken 8", anchor="center", bg="light gray", font=("Arial", 42, "bold"))
        subTitle = tk.Label(self.master, text="Character Select", anchor="center", bg="light gray", font=("Arial", 22, "bold"))

        title.pack(padx=20, pady=20)
        subTitle.pack(padx=20, pady=10)

        buttonFrame = tk.Frame(self.master, background="")
        buttonFrame.pack(pady=200) # pady might become an issue later

        # 36 total characters, listed in order of appearance on roster
        tek_characters = [
            ["Eddy", "Claudio", "Zafina", "Paul", "Raven", "Victor", "Reina", "Azucena", "Shaheen", "Law", "Leroy", "Leo", "Lidia"],
            ["Heihachi", "Panda", "Asuka", "Lee", "Xiaoyu", "Jin", "??", "Kazuya", "Nina", "Hwoarang", "Feng", "Yoshimitsu", "Clive"], # ?? resembles the random character option
            ["Kuma", "Lili", "Alisa", "Lars", "Jun", "Devil Jin", "Jack-8", "King", "Steve", "Dragunov", "Bryan"]
        ]

        for rowIndex, row in enumerate(tek_characters):
            numChars = len(row)
            startCol = (13 - numChars) // 2 # Center the row based upon 13 columns
            for colIndex, name in enumerate(row):
                if rowIndex == 1 and colIndex == 6: # Skip the second row, 7th column, the "??" element
                    continue
                btn = tk.Button(
                    buttonFrame, text=name, width=12, height=4,
                    command=lambda n=name: self.tekComboScreen(n) # Waits for button click, passes name to sf6ComboScreen function
                )
                btn.grid(row=rowIndex, column=startCol + colIndex, padx=5, pady=5)
    
    def tekComboScreen(self, name):
        for child in self.master.winfo_children(): child.destroy()

        backButton = tk.Button(self.master, text="Go Back", width=10, height=3, command=self.tekCharSel)
        backButton.place(x=10, y=10)

        title = tk.Label(self.master, text=name, anchor="center", bg="light gray", font=("Arial", 42, "bold"))
        title.pack(padx=20, pady=20)

        buttonFrame = tk.Frame(self.master, width=self.master.winfo_width(), height=(self.master.winfo_height() // 3)) # TODO: Make transparent
        buttonFrame.pack(side="bottom")
        
        #   ↖7   ↑8   9↗
        #   ←4        6→   Directions will be in an 8 way pattern, named as such 
        #   ↙1   ↓2   3↘   Arrows will depict these on the User Interface

        # TODO: Create list/database of moves and special moves

root = tk.Tk()
root.title("Combo Maker by Felix Silva")
root.configure(bg="light gray")
root.state('zoomed')
Application(root)
root.mainloop()
import tkinter as tk

class Application:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1920x1080") # TODO: Add support for resizing'
        self.master.after(100, self.gameSelect) # Ensures window is drawn before call

    def gameSelect(self):
        title = tk.Label(self.master, text="Combo Maker", anchor="center", font=("Arial", 42, "bold"))
        title.pack(padx=20, pady=40)

        halfX = self.master.winfo_width() // 2  # Get window width, divide by 2
        halfY = self.master.winfo_height() // 2  # Get window width, divide by 2

        # Street Fighter 6 Button
        sf6But = tk.Button(self.master, text="Street Fighter 6", width=50, height=7)
        sf6But.place(x=halfX * 0.75, y=halfY, anchor="center")

        # Tekken 8 Button
        tekBut = tk.Button(self.master, text="Tekken 8", width=50, height=7)
        tekBut.place(x=halfX * 1.25, y=halfY, anchor="center")

root = tk.Tk()
root.title("Combo Maker by Felix Silva")
Application(root)
root.mainloop()
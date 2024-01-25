import tkinter as tk
from tkinter import ttk
from game import Game


class MainWindow(tk.Tk):
    """

    Creating interface of the game, inheriting from
    the tkinter Tk class, which is standart GUI toolkit.

    """

    def __init__(self):
        """

        Call of the initializer of the parent class (tk.Tk)
        and creating window geometry, title, button styles.

        """
        super().__init__()
        self.attributes("-fullscreen", True)
        self.title("Set!")
        self.configure(bg="darkseagreen3")
        btn_style = ttk.Style(self)
        btn_style.configure(
            "FancyButton.TButton",
            font=("Times New Roman", 36, "bold"),
            foreground="black",
            background="green",
            padding=(10, 10),
        )
        self.create_widgets()

    def create_widgets(self):
        """

        Creating all buttons, labels and placing them.

        """
        self.game = Game(self)
        self.play_btn = ttk.Button(
            self,
            text="Play",
            command=self.play_button_pressed,
            style="FancyButton.TButton",
        )
        self.play_btn.place(relx=0.5, rely=0.6, anchor="center", width=300, height=150)

        self.quit_btn = ttk.Button(
            self, text="Quit", command=self.game.quit_game, style="FancyButton.TButton"
        )
        self.quit_btn.place(relx=0.5, rely=0.75, anchor="center", width=300, height=150)

        label_text = "SET"
        self.set_label = ttk.Label(
            self,
            text=label_text,
            font=("Times New Roman", 72, "bold"),
            foreground="black",
            background="darkseagreen3",
        )
        self.set_label.place(relx=0.5, rely=0.2, anchor="center")

    def play_button_pressed(self):
        """

        After click on the button Play,
        redrawing all buttons, starting game
        from file game.py

        """
        self.set_label.destroy()
        self.quit_btn.destroy()
        self.play_btn.destroy()
        self.new_quit = ttk.Button(
            self, text="Quit", command=self.game.quit_game, style="FancyButton.TButton"
        )
        self.new_quit.place(relx=0.9, rely=0.9, anchor="center", width=300, height=150)
        self.game.start_game()

    def quit_game(self):
        self.destroy()

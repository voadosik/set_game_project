from card import Card, is_set
from random import sample
from tkinter import messagebox, ttk
import os
from PIL import ImageTk, Image


class Game:
    def __init__(self, root):
        """

        Initializing game, creating root window,
        list of all possible combinations of cards,
        empty list of cards on the board, picked cards and score.

        """
        self.root = root
        self.cards = [
            Card(color, number, shape, shading)
            for color in Card.colors
            for number in Card.number_of_objects
            for shape in Card.shape
            for shading in Card.shading
        ]
        self.cards_on_board = []
        self.picked_cards = []
        self.score = 0
        self.play_btn = None

    def shuffle(self):
        """

        Randomly picking 12 cards from the deck
        using sample() from random library, shuffling
        till it has at least one set.

        """
        while True:
            self.picked_cards = []
            self.cards_on_board = sample(self.cards, 12)
            if self.has_set():
                break

    def has_set(self):
        """

        Checking all the possible combinations of cards,
        if there is no set on the table, returning False, and
        True otherwise.

        """
        for i in range(len(self.cards_on_board) - 2):
            for j in range(i + 1, len(self.cards_on_board) - 1):
                for k in range(j + 1, len(self.cards_on_board)):
                    if is_set(
                        self.cards_on_board[i],
                        self.cards_on_board[j],
                        self.cards_on_board[k],
                    ):
                        return True
        return False

    def start_game(self):
        """

        Creating in-game labels, such as score,
        creating skip button.

        """
        label_text = "Score:"
        label = ttk.Label(
            text=label_text,
            font=("Times New Roman", 72, "bold"),
            foreground="black",
            background="darkseagreen3",
        )
        label.place(relx=0.5, rely=0.9, anchor="center")

        score_label = ttk.Label(
            text=str(self.score),
            font=("Times New Roman", 72, "bold"),
            foreground="black",
            background="darkseagreen3",
        )
        score_label.place(relx=0.6, rely=0.9, anchor="center")

        self.shuffle()
        self.show_cards()

        self.play_btn = ttk.Button(
            self.root, text="Skip", command=self.start_game, style="FancyButton.TButton"
        )

        self.play_btn.place(relx=0.1, rely=0.9, anchor="center", width=300, height=150)

    def play_game(self):
        """

        Checking if the 3 cards that player picked is set,
        messages if it is set and if not.

        """
        if is_set(*self.picked_cards):
            messagebox.showinfo("Set!", "Set!")
            self.score += 1
            if self.score == 10:
                messagebox.showinfo(
                    "That`s it",
                    "Your score is 10, you can continue if you want, but you don't",
                )
                self.start_game()
            else:
                self.start_game()
        else:
            messagebox.showinfo("No", "That`s not a set!")
            self.shuffle()
            self.show_cards()

    def show_cards(self):
        """

        Showing cards in the root window, root is divided
        into rows(12) and columns(4), then using label.grid
        set a distinct row and column for every card.

        Displaying an image of card is done by searching for an
        image path using os.path.join() and concatenating 3 strings:
        os.getcwd() - working directory
        "images_of_cards" - folder with images
        card.image_path - function that concatenates attributes of card
        that needs to be displayed into a string

        Pick of card is performed by tkinter event handler .bind()
        which starting a function select_card(card) if player clicked
        on the image of card with mouse <Button-1>

        """

        for col in range(4):
            self.root.columnconfigure(col, weight=1)
        for row in range(12):
            self.root.rowconfigure(row, weight=1)

        for i, card in enumerate(self.cards_on_board):
            image_path = os.path.join(os.getcwd(), "images_of_cards", card.image_path)
            image = Image.open(image_path)
            image = image.resize((240, 160), Image.LANCZOS)  # Adjust the size as needed
            card_image = ImageTk.PhotoImage(image)

            label = ttk.Label(
                self.root,
                image=card_image,
            )
            label.image = card_image
            label.grid(row=i // 4, column=i % 4, padx=20, pady=20)
            label.bind("<Button-1>", lambda event, c=card: self.select_card(c))

    def select_card(self, card):
        """

        Function that adds card that was picked by player using
        tkinter event handler to the list of picked cards.

        """
        if card in self.picked_cards:
            self.picked_cards.remove(card)
        else:
            self.picked_cards.append(card)

        if len(self.picked_cards) == 3:
            self.play_game()

    def quit_game(self):
        self.root.destroy()

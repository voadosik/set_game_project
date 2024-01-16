from card import Card, is_set
from random import sample
from tkinter import messagebox, ttk
import os
from PIL import ImageTk, Image

class Game:
    def __init__(self, root):
        self.root = root #reference to root window
        self.cards = [Card(color, number, shape, shading) for color in Card.colors
                      for number in Card.number_of_objects for shape in Card.shape 
                      for shading in Card.shading] #all possible cards
        self.cards_on_board = []
        self.picked_cards = []
        self.score = 0
        self.play_btn = None
        
    def shuffle(self): #Pick 12 cards from the deck
        while True:
            self.picked_cards = []
            self.cards_on_board = sample(self.cards, 12)
            if self.cards_on_board:
                break

    def has_set(self):
        for i in range(len(self.cards_on_board) - 2):
            for j in range(i + 1, len(self.cards_on_board) - 1):
                for k in range(j + 1, len(self.cards_on_board)):
                    if is_set(self.cards_on_board[i], self.cards_on_board[j], self.cards_on_board[k]):
                        return True
        return False

    def start_game(self):  # Start
        label_text = "Score:"
        label = ttk.Label(
            text=label_text,
            font=("Times New Roman", 72, "bold"),
            foreground="black",
            background="darkseagreen3"
        )
        label.place(relx=0.5, rely=0.9, anchor="center")

        score_label = ttk.Label(
            text=str(self.score),
            font=("Times New Roman", 72, 'bold'),
            foreground="black",
            background="darkseagreen3"
        )
        score_label.place(relx=0.6, rely=0.9, anchor="center")

        self.shuffle()
        self.show_cards()

        if self.play_btn:
            self.play_btn.destroy()
        self.play_btn = ttk.Button(
            self.root, text="Skip", command=self.start_game, style='FancyButton.TButton'
        )

        self.play_btn.place(relx=0.1, rely=0.9, anchor="center", width=300, height=150)

    def play_game(self): #Checking pick of player
        if is_set(*self.picked_cards):
            messagebox.showinfo("Set!", "Set!")
            self.score += 1
            if self.score == 10:
                messagebox.showinfo("That`s it", "Your score is 10, you can continue if you want, but you don't")
                self.start_game()
            else:
                self.start_game()
        else:
            messagebox.showinfo("No", "That`s not a set!")
            self.shuffle()
            self.show_cards()

    def show_cards(self):
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
            label.grid(row=i//4, column=i % 4, padx=20, pady=20)
            label.bind("<Button-1>", lambda event, c=card: self.select_card(c))#When user click on the card with Button-1,
                                                                                #lambda event(tkinter info about event)
                                                                                #card c is added to the selected cards
                                                                                #when the number of cards == 3, check if set.

            
    def select_card(self, card): #Picking the cards
        if card in self.picked_cards:
            self.picked_cards.remove(card)
        else:
            self.picked_cards.append(card)

        if len(self.picked_cards) == 3:
            self.play_game()

    def quit_game(self):
        self.root.destroy()
        
def to_path(card):
    path = ''
    path += card.color
    path += card.shape
    path += card.shading
    path += str(card.number)
    path += '.png'
    return path

class Card:
    colors = ["red", "green", "purple"]
    number_of_objects = [1, 2, 3]
    shape = ["diamond", "squiggle", "oval"]
    shading = ["filled", "shaded", "empty"]

    def __init__(self, color, number, shape, shading):
        self.color = color
        self.number = number
        self.shape = shape
        self.shading = shading
        self.image_path = to_path(self)

    def __eq__(self, card2):  # checks if cards are equal
        return (
            self.color == card2.color
            and self.number == card2.number
            and self.shape == card2.shape
            and self.shading == card2.shading
        )


def is_set(
    card1, card2, card3
):  # True if some of them and True if everything different
    color = check(card1.color, card2.color, card3.color)
    shape = check(card1.shape, card2.shape, card3.shape)
    number = check(card1.number, card2.number, card3.number)
    shading = check(card1.shading, card2.shading, card3.shading)
    return color and shape and number and shading

def check(prop1, prop2, prop3):
    if prop1 == prop2 and prop1 == prop3:
        return True
    elif prop1 != prop2 and prop1 != prop3 and prop2 != prop3:
        return True

    return False



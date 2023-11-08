class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self, num):
        if num == 1:
            # Add to beginning of face up list
            self.hand.face_up.insert(0, self.hand.stack[num - 1])
        else:
            self.hand.face_up += self.hand.stack[:num]
        return self.hand.face_up

    def has_cards(self):
        return len(self.hand.stack) > 0

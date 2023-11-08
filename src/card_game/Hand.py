class Hand:
    def __init__(self, stack):
        self.stack = stack

        self.face_up = []
        # self.face_down = []  # Not yet used

    def add(self, cards):
        for card in cards:
            self.stack.append(card)
        # Make an update so the card played is put in the "bottom" of the stack as well
        self.update()

    def remove(self):
        # Remove cards on "top" of stack
        del self.stack[: len(self.face_up)]

    def update(self):
        # Move cards to the bottom of stack
        for card in self.face_up:
            self.stack.append(card)
        self.remove()

from Deck import Deck
from Hand import Hand
from Player import Player


# Ranks that are letters have to be mapped to numbers if played
def map_ranks(rank1, rank2):
    rank_mapping = {"J": 11, "Q": 12, "K": 13, "A": 14}

    if rank1 in rank_mapping:
        rank1 = rank_mapping.get(rank1)
    if rank2 in rank_mapping:
        rank2 = rank_mapping.get(rank2)

    return int(rank1), int(rank2)


# The higher hand get cards won added to stack. The lower hand have cards lost removed from its stack
def update_stack(higher, lower):
    higher.hand.add(lower.hand.face_up)
    lower.hand.remove()


def compare_cards(tuple1, tuple2, player1, player2):
    # Last item in "card tuple" is the rank
    rank1, rank2 = map_ranks(tuple1[1], tuple2[1])

    if rank1 > rank2:
        update_stack(player1, player2)
    elif rank1 < rank2:
        update_stack(player2, player1)
    else:
        # If ranks are equal, the cards have to be moved to bottom of stack before war
        player1.hand.update()
        player2.hand.update()
        return True
    return False


def start_new_round(num_of_cards, player1, player2):
    # Start turning up cards
    player1_cards = player1.play_card(num_of_cards)
    player2_cards = player2.play_card(num_of_cards)

    print(f"--> {player1.name} plays: {player1_cards}")
    print(f"--> {player2.name} plays: {player2_cards}\n")

    # If card's ranks are equal, it is war
    is_war = compare_cards(player1_cards[0], player2_cards[0], player1, player2)

    return is_war


def main():
    print("#####################################")
    print("#  Let's play the 'War' card game!  #")
    print("#####################################")

    # Divide deck
    deck = Deck()
    deck.shuffle()
    stack1, stack2 = deck.split()

    # Create players
    player1 = Player(input("Name of 1st player: "), Hand(stack1))
    player2 = Player(input("Name of 2st player: "), Hand(stack2))

    is_war = False
    while player1.has_cards() and player2.has_cards():
        input("👽 Press Enter to play cards")
        if not is_war:
            is_war = start_new_round(1, player1, player2)

            player1.hand.face_up.clear()
            player2.hand.face_up.clear()
        else:
            print("😲 Same ranks! Press Enter to start the war of cards")

            is_war = start_new_round(3, player1, player2)
            while is_war:
                print("😲😲 The 'war' continues!")
                is_war = start_new_round(1, player1, player2)

            player1.hand.face_up.clear()
            player2.hand.face_up.clear()
            print("The war is over. Back to the regular game!")

        # Debug (or just helpful to see the players stacks)
        print(
            f"--> {player1.name}'s stack: {player1.hand.stack} --> {len(player1.hand.stack)} cards"
        )
        print(
            f"--> {player2.name}'s stack: {player2.hand.stack} --> {len(player2.hand.stack)} cards\n"
        )

        print("-------------------------\n")

    # One of the players is out of cards, game ends
    winner = player1.name if player1.has_cards() else player2.name
    print(f"{winner} wins!")


main()

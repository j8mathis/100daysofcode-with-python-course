import random

from playandroll import Roll, Player


def main():
    print_header()

    rolls = [
        Roll('rock', 'paper'),
        Roll('scissors', 'rock'),
        Roll('paper', 'scissors')
    ]

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)


def print_header():
    print('-------------------------')
    print(' Rock! Paper! Scissors!')
    print('-------------------------')
    print()


def get_players_name():
    name = input('What is you name: ')
    return name


def display_roll(player, roll):
    print(f"{player} rolls a {roll}")


def display_winner(player):
    print(f"{player} wins this round")
    print()


def is_tie(p1_roll, p2_roll):
    if p2_roll.name == p1_roll:
        print("Same roll try again!")
        print()
        return True
    else:
        return False


def game_loop(player1, player2, rolls):
    count = 0
    while count < 3:
        if player1.score == 2 or player2.score == 2:
            break
        p2_roll = random.choice(rolls)
        p1_roll = input('[R]ock, [P]aper, or [S]cissors?')
        p1_roll = p1_roll.lower()
        if p1_roll == 'r':
            p1_roll = 'rock'
            t = is_tie(p1_roll, p2_roll)
            if t:
                continue
            else:
                outcome = p2_roll.can_defeat(p1_roll)

        elif p1_roll == 'p':
            p1_roll = 'paper'
            t = is_tie(p1_roll, p2_roll)
            if t:
                continue
            else:
                outcome = p2_roll.can_defeat('paper')

        elif p1_roll == 's':
            p1_roll = 'scissors'
            t = is_tie(p1_roll, p2_roll)
            if t:
                continue
            else:
                outcome = p2_roll.can_defeat('scissors')
        else:
            print(f"We don't understand {p1_roll}")
            continue

        # display throws
        display_roll(player1.name, p1_roll)
        display_roll(player2.name, p2_roll.name)
        # display winner for this round
        if not outcome:
            display_winner(player2.name)
            player2.add_score()

        else:
            display_winner(player1.name)
            player1.add_score()

        count += 1

    print(f"Total scores are:")
    print(f"{player1.name}: {player1.score}")
    print(f"{player2.name}: {player2.score}")

    if player1.score > player2.score:
        print(f"{player1.name} wins the game!")
    else:
        print(f"{player2.name} wins the game!")


if __name__ == '__main__':
    main()

from ..projects import RAINY_DAY, HOGWARTS_HOUSES, WHO_IS_THE_MURDERER, MASTERMIND

def logic_games_test():
    print("Available Logic Games: ")
    
    print("[1] - Rainy Day")
    print("[2] - Hogwart's Houses")
    print("[3] - Who Is The Murderer?")
    print("[4] - Mastermind")
    
    game_index = input("\nWhich logic game do you want to play?: ")
    print()
    
    try:
        selected_index = int(game_index)
        if 0 < selected_index <= 4:
            if selected_index == 1:
                rainy_day_game = RAINY_DAY()
                rainy_day_game.play()
                
            elif selected_index == 2:
                hogwarts_houses_game = HOGWARTS_HOUSES()
                hogwarts_houses_game.play()

            elif selected_index == 3:
                who_is_the_murderer_game = WHO_IS_THE_MURDERER()
                who_is_the_murderer_game.play()
                
            elif selected_index == 4:
                mastermind_game = MASTERMIND()
                mastermind_game.play()
                
        else:
            print("Invalid index on logic game selection.")
            exit(2)
                
    except ValueError:
        print("Invalid input type on logic game selection.")
        exit(1)
        
    return 0


def main():
    return 0


if __name__ == '__main__':
    main()
    
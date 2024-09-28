import game_graphics as draw
import random, time, sys, os.path

class Duskers:

    def __init__(self, r_seed, a_min, a_max, location: str):
        random.seed(r_seed)
        self.is_running = True
        self.anim_min_duration = int(a_min)
        self.anim_max_duration = int(a_max)
        self.locations = location.replace("_", " ").split(",")
        self.titanium = 0
        self.user_name = 'John'
        self.robots = 3
        self.slot_list = ['empty', 'empty', 'empty']
        self.titanium_scan = False
        self.enemy_scan = False


    def show_help(self):
        print("\n\t\tStrategic game inspired by Misfits Attic 'Duskers'.\n\
        You're in charge of a squad of robots exploring mysterious locations\n\
        and looking for titanium.\n\
        To play the game, enter commands provided in square brackets (ex. [Back]).\n\
        Command are case-insensitive (back, Back, and bAcK all map to [Back]).\n\
        Keep an aye on your robot squad! When you lose all your robots, the game is over![Back]\n")


    def show_scores(self):
        separator, index = " " * 5, 1
        print()
        print("  HIGH SCORES\n")

        if os.path.exists('high_scores.txt'):
            with open('high_scores.txt', 'r') as score_file:
                for score in score_file:
                    print(f"({index})", score, end="")
                    index += 1
            print("\n  [Back]")
        else:
            print("\nNo scores to display.\n  [Back]")


    def upgrade_shop(self):
        upgrade_prices = (250, 500, 1000)

        while True:

            print(draw.upgrade_menu)

            user_input = input("Your command: ")

            if user_input == '1' and self.titanium >= upgrade_prices[0] and self.titanium_scan == False:
                self.titanium -= upgrade_prices[0]
                self.titanium_scan = True
                print("Purchase successful. You can now see how much titanium you can get from each found location.")
                break
            elif user_input == '2' and self.titanium >= upgrade_prices[1] and self.enemy_scan == False:
                self.titanium -= upgrade_prices[1]
                self.enemy_scan = True
                print(f"Purchase successful. "
                      f"You will now see how likely you will encounter an enemy at each found location.")
                break
            elif user_input == '3' and self.titanium >= upgrade_prices[2]:
                self.titanium -= upgrade_prices[2]
                self.robots += 1
                print("Purchase successful. You now have an additional robot")
                break
            elif user_input == 'back':
                break
            else:
                print("\nNot enough titanium!\n")


    def generate_hub(self):

        if self.robots > 0:
            separator = "|"
            robots = [draw.robot_graphic for _ in range(self.robots)]
            print("+==============================================================================+")
            for robot in zip(*(rt.splitlines() for rt in robots)):
                print(separator.join(robot))
            print("+==============================================================================+")
            print(f"| Titanium: {self.titanium}")
            print("+==============================================================================+")
            print("|                  [Ex]plore                          [Up]grade                |")
            print("|                  [Save]                             [M]enu                   |")
            print("+==============================================================================+")
        else:
            print("Deploying robots...\nEnemy encounter!!!\nMission aborted, the last robot lost...")
            print(draw.game_over)
            self.save_score()
            self.start_game()


    def save_score(self):
        if os.path.exists('high_scores.txt'):
            # store the whole file in a list
            scores_list = []
            with open('high_scores.txt', 'r') as scores_file:
                for line in scores_file:
                    scores_list.append(line.strip())

            if len(scores_list) == 10:
                # Before save, we analyze the top 10 scores and see if the new score fits in
                last_score = ''
                with open('high_scores.txt', 'r') as read_score:
                    for read in read_score:
                        last_score = read
                # Extract the score number and convert it to integer
                old_score = int(last_score[last_score.find(" ") + 1:])

                # If current score is greater than the top 10 score rewrite the whole file and save it
                if self.titanium > old_score:
                    line_counter = 0
                    with open('high_scores.txt', 'w') as new_scores:
                        for line in scores_list:
                            score = int(line[line.find(" ") + 1:])
                            if self.titanium == score:
                                print(line, file=new_scores)
                                print(f"{self.user_name} {self.titanium}", file=new_scores)
                                line_counter += 1
                                break
                            elif self.titanium > score:
                                print(f"{self.user_name} {self.titanium}", file=new_scores)
                                line_counter += 1
                                break
                            else:
                                print(line, file=new_scores)
                                line_counter += 1
                        # Continue writing leftovers scores
                        for line in range(line_counter, len(scores_list) - 1):
                            print(scores_list[line], file=new_scores)

            else:
                with open('high_scores.txt', 'a') as score_file:
                    print(f"{self.user_name} {self.titanium}", file=score_file)
        else:
            with open('high_scores.txt', 'a') as score_file:
                print(f"{self.user_name} {self.titanium}", file=score_file)


    def load_slots(self):
        slot_number = 1

        for _ in range(3):

            slot_path = f"save_file{slot_number}.txt"

            if os.path.isfile(slot_path):
                with open(slot_path) as slot_file:
                    save_record = str(slot_file.readline().strip())
                    if save_record:
                        self.slot_list[slot_number - 1] = save_record

            slot_number += 1

        print(f"\nSelect save slot:\n [1] "
              f"{self.slot_list[0]} \n [2] {self.slot_list[1]} \n [3] {self.slot_list[2]}\n")


    def load_game(self):

        self.load_slots()

        while True:

            user_slot = input("\nYour command:\n")

            if user_slot == 'back':
                break
            elif user_slot.isnumeric() and int(user_slot) in range(1, 4):
                file_path = f"save_file{user_slot}.txt"
                # loading the game if the slot is not empty
                if os.path.isfile(file_path):
                    with open(file_path) as load_file:
                        load_record = str(load_file.readline().strip())
                        if load_record:
                            # Using str find() method with indexes and string slicing to retrieve and assign the data
                            start_index = load_record.find("Titanium:") + 9
                            end_index = load_record.find("Robots:") - 1
                            titanium_amount = load_record[start_index:end_index]
                            self.titanium = int(titanium_amount)
                            self.user_name = load_record[:load_record.find("Titanium:") - 1]
                            robot_start = load_record.find("Robots:") + 8
                            robot_end = load_record.find("Last save:") - 1
                            self.robots = int(load_record[robot_start:robot_end])
                            enemy_info = load_record.find("enemy_info")
                            titanium_info = load_record.find("titanium_info")
                            self.titanium_scan = True if titanium_info >= 0 else False
                            self.enemy_scan = True if enemy_info >= 0 else False
                            print(draw.load_game)
                            print(f"Welcome back, commander {self.user_name}!")
                        else:
                            print("\nEmpty slot!")
                    break
                else:
                    print("\nEmpty slot!")

            self.load_slots()


    def save_game(self):

        self.load_slots()

        user_slot = input("\nYour command:\n")
        # writing the game state to a slot_file
        game_state = (f"{self.user_name} Titanium: {self.titanium} Robots: {self.robots} Last save: "
                      f"{time.strftime("%Y-%m-%d %H:%M", time.localtime())} "
                      f"Upgrades:{' titanium_info' if self.titanium_scan else ''}"
                      f"{' enemy_info' if self.enemy_scan else ''}")

        if user_slot.isnumeric() and int(user_slot) in range(1, 4):
            with open(f'save_file{user_slot}.txt', 'w') as save_file:
                save_file.write(game_state)
            print(draw.save_game)
        elif user_slot == 'back':
            pass
        else:
            print("\nInvalid input\n")


    def generate_animation(self):
        for _ in range((self.anim_min_duration + self.anim_max_duration) // 2):
            print(".", end="")
            time.sleep(1)
        print()


    def explore_location(self):
        max_loc_number = random.randint(1, 9)

        # Generate the first location record and save it to the location dictionary
        loc_counter = 1
        location_dict = {loc_counter: (random.choice(self.locations), random.randint(10, 100), random.random())}

        def search_locations():
            print(f"\nSearching", end="")
            self.generate_animation()

            for index, value in location_dict.items():
                # Determine if there are upgrades available and assign the information to loc_info variable
                loc_info = f"[{index}] {value[0]}"
                if self.titanium_scan and self.enemy_scan:
                    loc_info = (f"[{index}] {value[0]} Titanium: {value[1]} "
                                        f"Encounter rate: {round(value[2], 2) * 100:.0f}%")
                elif self.titanium_scan and not self.enemy_scan:
                    loc_info = f"[{index}] {value[0]} Titanium: {value[1]}"
                elif self.enemy_scan and not self.titanium_scan:
                    loc_info = f"[{index}] {value[0]} Encounter rate: {round(value[2], 2) * 100:.0f}%"

                print(loc_info)

            print("\n[S] to continue searching")

        search_locations()

        while True:

            user_option = input("\nYour command:\n").lower()

            if user_option == 's' and loc_counter == max_loc_number:
                print("\nNothing more in sight.\n       [Back]")

            elif user_option == 's':
                loc_counter += 1
                location_dict[loc_counter] = (random.choice(self.locations),
                                              random.randint(10, 100), random.random())

                search_locations()

            elif user_option.isnumeric() and int(user_option) in range(1, len(location_dict) + 1):
                loc_record = location_dict[int(user_option)]
                encounter_rate = loc_record[2]
                loc_rate = random.random()
                self.titanium += loc_record[1]

                # Enemy encounter, 1 robot lost.
                if loc_rate < encounter_rate:
                    self.robots -= 1

                    if self.robots <= 0:
                        self.titanium -= loc_record[1]
                        break

                    print(f"\nDeploying robots", end="")
                    self.generate_animation()
                    print("Enemy encounter")
                    print(f"{loc_record[0]} successfully, 1 robot lost..\n"
                            f"Acquired {loc_record[1]} lumps of titanium")

                # No encounter, no damage taken.
                else:
                    print(f"\nDeploying robots", end="")
                    self.generate_animation()
                    print(f"{loc_record[0]} successfully, with no damage taken.\n"
                            f"Acquired {loc_record[1]} lumps of titanium")

                break

            elif user_option == 'back':
                break

            else:
                print("\nInvalid input")


    def inside_play_menu(self):

        while self.is_running:

            print(draw.inside_play_menu)

            user_option = input("\nYour command:\n").lower()

            if user_option == 'back':
                break
            elif user_option == 'main':
                self.start_game()
            elif user_option == 'save':
                self.save_game()
                self.is_running = False
            elif user_option == 'exit':
                print("\nThanks for playing, bye!")
                self.is_running = False
            else:
                print("Invalid input")

    def play_game(self):

        while self.is_running:

            self.generate_hub()

            user_option = input("\nYour command:\n").lower()

            if user_option == 'ex':
                self.explore_location()
            elif user_option == 'up':
                self.upgrade_shop()
            elif user_option == 'save':
                self.save_game()
            elif user_option == 'm':
                self.inside_play_menu()
            elif user_option == 'back':
                break
            elif user_option == 'main':
                break
            elif user_option == 'exit':
                print("\nThanks for playing, bye!")
                self.is_running = False
            else:
                print("Invalid input")


    def welcome_screen(self):
        print(draw.main_menu)


    def start_game(self):

        while self.is_running:

            self.welcome_screen()

            user_option = input("\nYour command:\n").lower()

            if user_option == 'new':
                self.user_name = input("\nEnter your name:\n")
                print(f"\nGreetings, commander {self.user_name}!")
                print("Are you ready to begin? \n[Yes] [No] Return to Main[Menu]")

                while self.is_running:
                    user_answer = input()
                    if user_answer == 'yes':
                        self.play_game()
                    elif user_answer == 'menu':
                        break
                    elif user_answer == 'exit':
                        print("\nThanks for playing, bye!")
                        self.is_running = False
                    else:
                        print("\nHow about now.")
                        print("Are you ready to begin? \n   [Yes] [No]")

            elif user_option == 'load':
                self.load_game()
                self.play_game()
            elif user_option == 'exit':
                print("\nThanks for playing, bye!")
                self.is_running = False
            elif user_option == 'high':
                self.show_scores()
            elif user_option == 'back' or user_option == 'menu':
                continue
            elif user_option == 'help':
                self.show_help()
            else:
                print("\nInvalid input")


def main():
    args = sys.argv
    game = Duskers(None, 0, 0, "High_street,Green_park,Destroyed_Arch")

    if len(args) == 5:
        game = Duskers(args[1], args[2], args[3], args[4])

    game.start_game()


if __name__ == "__main__":
    main()

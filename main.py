class Menu:
    def __init__(self):
        self.choices = {
            '1': '1.py',
            '2': '2.py',
            '3': '3.py',
            '4': '4.py',
            '5': '5.py',
            '6': '6.py'
        }

    def show(self):
        while True:
            print("Choose an file:")
            print("1. 1")
            print("2. 2")
            print("3. 3")
            print("4. 4")
            print("5. 5")
            print("6. 6")
            print("Press any other key to exit")

            choice = input("> ")

            if choice in self.choices:
                filename = self.choices[choice]
                with open('output.txt', 'a') as f:
                    f.write(f"Output for option {choice}:\n")

                exec(open(filename).read())

                with open('output.txt', 'a') as f:
                    f.write("\n\n")
            else:
                print("Option does not exist")
                break

            continue_program = input("Do you want to continue? (y/n) ")
            if continue_program.lower() != 'y':
                break


menu = Menu()
menu.show()
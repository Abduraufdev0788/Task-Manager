import sys
from utils import print_main, print_satatus, print_menu
from manager import Manager

def main() -> None:
    manager = Manager()

    while True:
        print_main()
        op = input("> ")

        if op == '1':
            if manager.login():
                while manager.user:
                    print_satatus(f"{manager.user.name} sizni accounting.")
                    print_menu()

                    choice = input(">")
                    while True:
                        if choise =="1":
                            pass
                        elif choise = "2":
                            pass
                        elif choise == '3':
                            sys.exit(0)
                        else:
                            sys.exit(1)
                        
        elif op == '2':
            manager.register()
        elif op == '3':
            sys.exit(0)
        else:
            sys.exit(1)

if __name__ == "__main__":
    main()

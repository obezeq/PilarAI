# Dependencies
import os

def check_menu_option(choice: str) -> bool:
    if choice == "0" or choice == "exit":
        return False

# Menu
def menu():
    print("─────────────────────────────────")
    print("      Welcome to Pilar AI        ")
    print("─────────────────────────────────")

    print("Please, select the book topic.")
    print("[0] EXIT")
    print("[1] Ficción")
    print("[2] Misterio y Suspenso")
    print("[3] Romance")
    print("[4] Ciencia Ficción")
    print("[5] Fantasía")
    print("[6] Terror")
    print("[7] Aventura")
    print("[8] Poesía")

    choice = input("~> ").strip().replace(' ', '').lower()

    if not check_menu_option(choice):
        return False

# Main Function
def main():
    
    menu_option = menu()
    print("test123456789")

if __name__ == '__main__':
    main()
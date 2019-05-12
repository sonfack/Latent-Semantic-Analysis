import os, sys
from src.commons import createtfIdfModel, singularDecomposition,  wordImportance

listText = ""
N = 100
newListText = ""

# =======================
#     MENUS FUNCTIONS
# =======================
# Main menu
def main_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome,\n")
    print("Please choose the menu you want to start:")
    print("1. To create LSA modle")
    print("2. To analyze your data")
    print("3. To analyze sentiments of your data")
    print("\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)

    return


# Execute menu
def exec_menu(choice):
    os.system("cls" if os.name == "nt" else "clear")
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return


# Menu 1
def menu1():
    print("Menu --> To create LSA model !\n")
    print("Enter CSV data file \n")
    dataFile = input(">> ")
    dataFile = os.path.join("../data", dataFile)
    df = pd.read_csv(dataFile)
    newdf = df.iloc[:N]
    newListText = newdf['Text']
    print("\n Enter you frame column containing text \n")
    # dfColumn = "Text"
    dfColumn = input(">> ")
    if not dfColumn:
        dfColumn = "Text"
    listText = df[dfColumn]
    #Training our model: This should be done ones 
    createtfIdfModel(listText)
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return


# Menu 2
def menu2():
    print("Menu --> 2. To analyze your data !\n")
    if not listText:
        menu1()
    print("Enter the word you are looking for it importance \n")
    word = input(">> ")
    # example : wordImportance(listText,1, 'error')
    wordImportance(listText,1, word)
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Menu 3
def menu3():
    print("Menu --> 3. To analyze sentiments of your data !\n")
    if not listText:
        menu1()
    # Singular Value  Decomposition
    singularDecomposition(newListText)
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return


# Back to main menu
def back():
    menu_actions['main_menu']()


# Exit program
def exit():
    sys.exit()


# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '9': back,
    '0': exit,
}

import time
import tkinter as tk

root = tk.Tk()
root.title('candy clicker: return of the candy')

candy = 0
hat_modifier = 1
costume_level = 1


# Define a function to update the label and the clicks
def update():
    global candy, costume_level, hat_modifier

    # Increase the clicks by the multiplier
    candy += costume_level * hat_modifier
    # Update the label with the new number of clicks
    label.config(text=str(f'you have {candy} candy!'))

def costume_upgrade():
    global candy, costume_level, hat_modifier
    if candy >= 10:
        costume_level += 1
    label.config(text=str(f'costume level is now {costume_level}'))

# Create a label to display the number of clicks
label = tk.Label(root, text="you have 0 candy!", font=("Comic sans MS", 32))

label.pack()



# Create a button to increase the number of clicks
photo = tk.PhotoImage(file="gyatt.png")
button = tk.Button(root, image=photo, command=update)
upgrade_button = tk.Button(root, text='costume upgrade', command=costume_upgrade())
button.pack()

# Run the main loop
root.mainloop()


def load():
    return 0, 1


def play_game():
    candy, costume_level = load()
    playing = True
    already_bought = False
    hat_modifier = 1
    while playing:
        user_input = input()
        if user_input == "upgrade costume":
            if candy >= 10:
                candy -= 10
                costume_level += 1 * hat_modifier
                print("costume upgraded!")
            else:
                print('not enough candy')
        elif user_input == "buy hat" and not already_bought:
            if candy >= 10000:
                candy -= 10000
                hat_modifier = 5
                print('purchased hat!')
            else:
                print('you havent got enough candy brokie')
        elif user_input == "exit":
            exit()
        else:
            candy += costume_level * hat_modifier
        print(f'candy: {str(candy)}')


play_game()

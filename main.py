#import time

#user_data_file = open("userdata.txt")
#user_name = user_data_file.readline().strip()
#user_age = user_data_file.readline().strip()
#user_animal_preference = user_data_file.readline().strip()
#user_data_file.close()
#print(f'im gonna kill you {user_name}, you are a waste of {user_age} years and '
 #     f'i hope all {user_animal_preference} disappear, making you wildly upset')

# second example
#user_data_two = open("funny.txt")
#name = user_data_two.readline().strip()
#address = user_data_two.readline().strip()
#time_till_im_there = user_data_two.readline().strip()
#how_afraid_you_should_be = user_data_two.readline().strip()

#user_data_two.close()
#  for i in range(int(time_till_im_there)):
#     print(f"name: {name}\nlocation: {address}\n"
#     f"time till im there: {int(time_till_im_there) - i}\n"
#     f"how afraid you should be: {how_afraid_you_should_be}")
#     time.sleep(1)

# writing to a file

#user_name = input('name')
#user_money = input('money')

#letter_file = open(f'{user_name}_letter.txt', 'w')

#letter_file.write(f'CONGRATULATION {user_name}!!! you have won large money, £{user_money}!'
  #                f'TO redem your GRAND PRIZE please email credit card informations to this'
 #                 f'emails addres! we hope hear from you soon!!!')
#letter_file.close()

def save(candy, costume_level, hat_modifier, already_bought):
    save_file = open('data.txt', 'w')
    save_file.write(f'{candy}\n{costume_level}\n{hat_modifier}\n{already_bought}')
    save_file.close()


def load():
    try:
        save_file = open('data.txt')
        val1 = int(save_file.readline())
        val2 = int(save_file.readline())
        val3 = int(save_file.readline())
        val4 = int(save_file.readline())
        save_file.close()
        return val1, val2, val3, val4
    except ValueError or FileNotFoundError:
        print('save data corrupt! creating new file...')
        save(candy=0,costume_level=1,hat_modifier=1,already_bought=0)
        return 0, 1, 1, 0


def play_game():
    candy, costume_level, hat_modifier, already_bought = load()
    playing = True
    while playing:
        user_input = input()
        if user_input == "upgrade costume":
            if candy >= 10:
                candy -= 10
                costume_level += 1 * hat_modifier
                print("costume upgraded!")
            else:
                print('not enough candy')
        elif user_input == "buy hat":
            if already_bought == 1:
                print('you already have a hat!!')
            elif candy >= 10000:
                candy -= 10000
                hat_modifier = 5
                print('purchased hat!')
                already_bought = 1
            else:
                print('you havent got enough candy brokie')
        elif user_input == "save":
            save(candy, costume_level, hat_modifier, already_bought)
            print('file saved!')
        elif user_input == "new game":
            candy = 0
            costume_level = 1
            hat_modifier = 1
            already_bought = 0
            save(candy, costume_level, hat_modifier, already_bought)
        else:
            candy += costume_level * hat_modifier
        print(f'candy: {str(candy)}')


play_game()

# Create a dictionary that holds the name of the movie as a key and a list containing the necessary age and seats left. Anytime someone purchases a new ticket
# the seats counter goes down. 
# So, basically:
# Film_dictionary = {Name of the movie: [restriction age, seats left]}

film_dictionary = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }


print("We currently have the following movies available. Please select one:")
for film in film_dictionary: 
    print(film)

print( ) #Blank to look better
while True:
    choice = input("What film would you like to watch?: ").strip().title()

    if choice in film_dictionary:
        age = int(input("How old are you?: ").strip())
#remember, input always returns a string! You need to convert into int before using it

        #check user age

        if age >= film_dictionary[choice][0]:

        #check enough seats

            num_seats = film_dictionary[choice][1]

            if film_dictionary[choice][1] > 0:

                print("We currently have {} seats available".format(film_dictionary[choice][1]))
                print("Enjoy the film!")
                film_dictionary[choice][1] = film_dictionary[choice][1] - 1

            else:
                print("I'm sorry, but there are no more tickets left!")
        else:
            print("You are too young to see that film!")
    else:
        print("We don't have that film...")



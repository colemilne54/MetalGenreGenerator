from tkinter import *
import random
#import colorama
#from colorama import Fore, Back, Style

#colorama.init()

def generator():
    x = random.randint(2, 6)

    starters = ['New Wave of', 'Blackened', 'Christian', 'Melodic', 'Symphonic', ' Ambient']

    nationality = [' American', ' British', ' Norwegian']

    fillers = [' Technical', ' Progressive', ' Avant Garde', ' Brutal', ' Folk', ' Viking', ' Pirate', ' Stoner',
               ' Pagan', ' Power', ' Groove']

    enders = [' Death', ' Thrash', ' Doom', ' Sludge', ' Drone']

    if x == 2:
        a = (random.choice(fillers))
        b = (random.choice(fillers))

        genre = a + b

    if x == 3:
        a = (random.choice(fillers))
        b = (random.choice(fillers))
        c = (random.choice(enders))

        genre = a + b + c

    if x == 4:
        a = (random.choice(starters))
        b = (random.choice(fillers))
        c = (random.choice(fillers))
        d = (random.choice(enders))

        genre = a + b + c + d

    if x == 5:
        a = (random.choice(starters))
        b = (random.choice(fillers))
        c = (random.choice(fillers))
        d = (random.choice(fillers))
        e = (random.choice(enders))

        genre = genre = a + b + c + d + e

    if x == 6:
        y = random.randint(1, 2)
        if y == 1:
            a = (random.choice(starters))
            b = (random.choice(nationality))
            c = (random.choice(fillers))
            d = (random.choice(fillers))
            e = (random.choice(fillers))
            f = (random.choice(enders))
        else:
            a = (random.choice(starters))
            b = (random.choice(fillers))
            c = (random.choice(fillers))
            d = (random.choice(fillers))
            e = (random.choice(fillers))
            f = (random.choice(enders))

        genre = genre = a + b + c + d + e + f



    #print(genre + ' Metal')
    complete = (genre + ' Metal')

    print = Label(root, text = complete)
    print.grid()

root = Tk()

root.title("Metal Genre Generator")
root.geometry("1030x800")
root.configure(background='black')

app = Frame(root)
app.grid()

photo = PhotoImage(file = "C:/Users/Piraticus/Desktop/metal.png")
label = Label(root, image=photo, borderwidth = 0, highlightthickness = 0)
label.grid()

printButton = Button(app, text = "Generate", width = 10, height = 2, command = generator) #(x = 500, y = 100)
printButton.place(x = 500, y = 100)
printButton.grid()


#label = Label(app, text = "This is a label!") print goes here?
#label.grid()



root.mainloop()
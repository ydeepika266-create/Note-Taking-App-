notes=[]
def info():
    print('Task')
    print("1.Add a note")
    print("2.view all notes")
    print("3.clear all notes")
    print("4.Exit")

while True:
    info()
    n = int(input("Please choose from 1 to 4: "))

    if n == 1:
        note = input("Write your note: ")
        notes.append(note)
        print("Note added!")
    elif n == 2:
        print( notes)
    elif n == 3:
        notes.clear()
        print("All notes cleared")
    elif n == 4:
        print("Exit")
        break
    else:
        print("Invalid input.")
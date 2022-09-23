from email.charset import SHORTEST


while(True):
    buy= input("Welcome to muy shoes shop! You need something? (S/s => Yes) (N/n => No) ")
    if buy.upper() == "S":
        shoes= input("""What shoes do you want?
Tacones
Deportivas
Botas
""")
        if shoes.upper() == "TACONES":
            pass
        elif shoes.upper() == "DEPORTIVAS":
            pass
        elif shoes.upper() == "BOTAS":
            pass
        else:
            pass
        break

    elif buy.upper() == "N":
        print("Bye! See you next time")
        break

    else:
        print ("Error put again the information")
        

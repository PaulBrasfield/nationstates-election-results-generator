import random
import sys

def main():
    tuple = ('Conservative', 'Liberal', 'New Democratic', 'Green')

    winningParties = []
    x = 0
    y = int(input("\nEnter the number of states/constituencies: "))

    conInt = 0
    libInt = 0
    newDemInt = 0
    greenInt = 0

    conWeight = float(input("\nConservative Weight: "))
    libWeight = float(input("Liberal Weight: "))
    newDemWeight = float(input("New Democratic Weight: "))
    greenWeight = float(input("Green Weight: "))

    print("\n")
        
    while x < y:
        choice = random.choices(tuple, weights=(conWeight, libWeight, newDemWeight,
                                                greenWeight), k=1)
        winningParties.append(choice)

        print(choice)
        x+=1
        
    for i in range(len(winningParties)):
        if winningParties[i] == ['Conservative']:
            conInt+=1
        elif winningParties[i] == ['Liberal']:
            libInt+=1
        elif winningParties[i] == ['New Democratic']:
            newDemInt+=1
        elif winningParties[i] == ['Green']:
            greenInt+=1

    print("\nConservative Party has won " + str(conInt) + " states/constituencies")
    print("Liberal Party has won: " + str(libInt) + " states/constituencies")
    print("New Democratic Party has won: " + str(newDemInt) + " states/constituencies")
    print("Green Party has won: " + str(greenInt) + " states/constituencies")

    choice = input("\nWould you like to run the program again? (Y)es or (N)o: ")

    if (choice.upper() == "Y"):
        print("\n-----------------------------------------------------------")
        main()
    elif (choice.upper() == "N"):
        print("\nThe program will now close.")
        sys.exit()
    else:
        print("You did not enter a valid answer. The program will now close.")
        sys.exit()
main()

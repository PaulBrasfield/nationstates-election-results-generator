# NationStates Election Results Generator

This program was designed for the online nation simulation game NationStates. This program takes in the number of states/constituencies along with the
weights of each political party defined in a tuple. We then select a party from the tuple at random, based on the specified weight, and do so for as many 
states/constituencies as was specified. Each time a party is drawn, they are "awarded" a state/constituency and add to their overall counter. 
In the end, we output each party along with the number of states/constituencies they have been awarded. We then prompt the user to either run the 
generator again or exit.

## Getting Started

### Prerequisites

Python 3 is required to run this program.

### Installing

```
Click on 'Clone or Download' in the top right
```

```
Click 'Download ZIP'
```

```
Open the ZIP file and extract the folder onto your computer.
```

```
Open the folder and double-click on the 'Dropshipping Price Calculator.py' to run the program.
```

**Example of program:**
```
Enter the number of states/constituencies: 5

Conservative Weight: 5
Liberal Weight: 5
New Democratic Weight: 5
Green Weight: 5


['Conservative']
['New Democratic']
['Green']
['Liberal']
['Conservative']

Conservative Party has won 2 states/constituencies
Liberal Party has won: 1 states/constituencies
New Democratic Party has won: 1 states/constituencies
Green Party has won: 1 states/constituencies

Would you like to run the program again? (Y)es or (N)o: y

-----------------------------------------------------------

Enter the number of states/constituencies: 5

Conservative Weight: 5
Liberal Weight: 5
New Democratic Weight: 5
Green Weight: 5


['Green']
['Green']
['New Democratic']
['Liberal']
['Green']

Conservative Party has won 0 states/constituencies
Liberal Party has won: 1 states/constituencies
New Democratic Party has won: 1 states/constituencies
Green Party has won: 3 states/constituencies

Would you like to run the program again? (Y)es or (N)o: n

The program will now close.
```

## Built With

* [Python3](https://www.python.org/download/releases/3.0/) - Programming language and IDE used

## Authors

* **Paul Brasfield** - *Initial work* - [PaulBrasfield](https://github.com/PaulBrasfield)


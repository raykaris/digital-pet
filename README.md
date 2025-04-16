# This is a simple digital pet🐶 code in python

The pet has been created using object-oriented Programming concepts in python. <br>
It helps in the use of classes, attributes, methods, and constructors.

### Attributes:
- `name`: the name of your pet
- `hunger`: an integer representing hunger level (0 = full, 10 = very hungry)
- `energy`: an integer representing energy level (0 = tired, 10 = fully rested)
- `happiness`: an integer (0–10)

### Methods:
- `eat()`: reduces hunger by 3 points (but not below 0), and increases happiness by 1.
- `sleep()`: increases energy by 5 points (but not above 10).
- `play()`: decreases energy by 2, increases happiness by 2, and increases hunger by 1.
- `get_status()`: prints the current state of the pet.
- `train(trick_name)`: teaches the pet a new trick and stores it in a list.
- `show_tricks()`: prints all learned tricks.


## How to run the project
1. clone this repo to your local machine.
2. cd into the project folder and open your editor
3. on your terminal run: 

```bash
python main.py
```

## sample output
```bash
🐶 Oscar's Status 🐶
Hunger: 5/10
Energy: 5/10
Happiness: 5/10
Oscar ate some food. Hunger decreased from 5 to 2.     
Oscar's happiness increased to 6.
Oscar played! Energy is now at 3.
Oscar's happiness increased to 8.
Oscar took a nap. Energy increased from 3 to 8.        
Oscar learned a new trick: roll over!
Oscar learned a new trick: paly dead!
Oscar knows the following tricks: roll over, paly dead.
🐶 Oscar's Status 🐶
Hunger: 3/10
Energy: 8/10
Happiness: 8/10
```
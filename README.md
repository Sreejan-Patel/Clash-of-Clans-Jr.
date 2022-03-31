# Clash of Clans Jr.

Oh yeah! This is a Jr. version of Clash of Clans. Although not as Graphical as the original , this is a terminal game to provide the best experience to novice's.

Checkout the instruction manual and functionalities of the game below -

---
## Village
- The village consists of the base of the defender.
- The color of the buildings change according to the health they are in 
    - 100% - 50% -> Green Color
    - 50% - 20% -> Yellow Color
    - 20% - 0% -> Red Color
    - 0 - Dead -> LightBlack 
- **TownHall** 
    - 4x3 tiles is the central and most important building in the base
- **Cannons** 
    - 2 Cannons of 2x3 are the weapons of the defender which targets the enemy's barbarians
    - The range of the cannons are 5 tiles from the centre of the building
    - Shoots once per second

- **Huts** 
    - 5 huts of 1x1 tile consists of the builders who maintain the base.

- **Walls**
    - They defend the base from the outside forming a parameter.
    - 1x1 tile each
    - Black Color

- **Spawning Points**
    - the enemy barbarians spawn at these points in the village
    - Barbarians have 3 spawning points defined which activates by passing the key's - i , j , k
    - King has a separate spawning point defined which activates by passing the key - b

## King
- The King is the main troop of the enemy
- The king's movement is handles by the user
    - w -> move up
    - s -> move down
    - d -> move right
    - a -> move left
- the king moves 1 tile per movement and 2 tiles when rage is activated
- 'SPACE' is used for attack 
    - Sword of the King attacks one building at a time which is in the 1 tiles range of the king
    - Leviathan axe of the King attacks all the buildings in the 4 tile radius of the king
- damage and health of the king are predefined , and heal and rage spells effect as required
- Red Color

## Barbarians
- These are the foot soldiers of the enemy - 10
- Barbarians move once per 1 sec and once per 0.5 sec when the rage spell is activated
- The movement speed is 1 tile per move and the health is predefined
- The color of the barbarians change when the health of the barbarian reduces below 50%
- The movement of the barbarians is automated
    - first they check if there is any broken wall. if there is any broken wall they move towards it. After they reach the broken wall they move towards the nearest non-destroyed building.
    - if there is no wall broken , they move towards the nearest building and destroy any wall in between the shortest path
- Blue Color

## Spells
- **Heal**
    - Increases the health of every alive troop on the village with 150% of the current health to the max
    - Yellow Color
- **Rage**
    - Doubles the movement speed and damage of every troop alive on the base 
    - The effect longs for 4 seconds
    - Magenta - color

## Game endings
- **Victory**
    - The enemy's win when the whole base is destroyed (except the walls)
- **Loss** 
    - the enemy's lose when all their barbarians are dead and they haven't destroyed the whole base
## Replay
- Each game played is stored in the replays folder for the user to look at later
- Running the replay.py and specifying the game number allows the user to look at the replay of that game

---

# Bonus

## Leviathan Axe
- This is a feature of the king which allows the king to attack buildings in a range of 4 tiles (AoE)
- Passing the key - l activates the leviathan axe of the king.

## Sound Effects
- Sound effects increase the pleasure of playing a game
- Few sound effects are added to increase the playing experience
    - king_attack
    - king_die
    - cannon_attack
    - barb_attack
    - heal
    - rage

---
# Machine Specifications
- OS - OSX
- Terminal - ZSH
- Processor - M1

--- 
# Libraries Used
- colorama
- math
- os
- numpy
- sys
- tty
- termios
- signal
- time




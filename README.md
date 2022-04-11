# Clash of Clans Jr.

Oh yeah! This is a Jr. version of Clash of Clans. Although not as Graphical as the original , this is a terminal game to provide the best experience to novice's.

Checkout the instruction manual and functionalities of the game below -

---

## Levels
- There are 3 levels in this game
- Each level has different layout as per the requirements
- the player passes to the next level is he wins the current level and loses the game if he loses any game
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
    - LEVEL+1 Cannons of 2x3 are the weapons of the defender which targets the enemy's ground troops
    - The range of the cannons are 6 tiles from the centre of the building
    - Shoots once per second
- **Wizard Towers**
    - LEVEL+1 wizard towers of 3x3 are the weapons of the defender which targets the enemy's troops both ground and air
    - the range of the wizard tower is 6 tiles from the centre of the building
    - it has an area of effect attack which reduces the health of all the troops which lie at a distance 3x3 tiles around the selected target , both ground and air
    - Attacks once per second

- **Huts** 
    - 5 huts of 1x1 tile consists of the builders who maintain the base.

- **Walls**
    - They defend the base from the outside forming a parameter.
    - 1x1 tile each
    - Black Color

- **Spawning Points**
    - Barbarians
        - the enemy barbarians spawn at these points in the village
        - Barbarians have 3 spawning points defined which activates by passing the key's - i , j , k
    - King
        - King has a separate spawning point defined which activates by passing the key - b
    - Queen
        - Queen has a separate spawning point defined which activates by passing the key - q
    - Archers 
        - the enemy archers spawn at these points in the village
        - loons have 3 spawning points defined which activates by passing the key's - m , n , o
    - Loons
        - the enemy loons spawn at these points in the village
        - loons have 3 spawning points defined which activates by passing the key's - x , y , z

## Heros
- Only one of the two heroes can be selected per game
- King and Queen
## King
- The King is a troop of the enemy
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

## Queen 
- The Queen is a troop of the enemy
- The queen's movement is handles by the user
    - w -> move up
    - s -> move down
    - d -> move right
    - a -> move left
- the queen moves 1 tile per movement and 2 tiles when rage is activated
- 'SPACE' is used for attack 
    - Bow of the queen targets one building at a time which is in the range of 8 tiles away in the last moved direction of the queen and the arrows attack an area of effect of tiles 5x5. All the buildings present around the target building in the range of 5x5 tiles gets attacked 
    - Eagle artillery of the queen is similar to that of the bow but the range is 16 tiles and the area of effect is 9x9 tiles. the queen launces the arrows high above and the arrows reach the destined target 1 secoud after the attack is initiated.


## Barbarians
- These are the foot soldiers of the enemy - 10
- Barbarians move once per 2 sec and once per 1 sec when the rage spell is activated
- The movement speed is 1 tile per move and the health is predefined
- The color of the barbarians change when the health of the barbarian reduces below 50%
- The movement of the barbarians is automated
    - first they check if there is any broken wall. if there is any broken wall they move towards it. After they reach the broken wall they move towards the nearest non-destroyed building.
    - if there is no wall broken , they move towards the nearest building and destroy any wall in between the shortest path
- Blue Color

## Archers
- These are the foot soldiers of the enemy - 5
- Archers move once per 1 sec and once per 0.5 sec when the rage spell is activated
- The movement speed is 1 tile per move and the health is predefined
- The color of the archers change when the health of the barbarian reduces below 50%
- The movement of the archers is automated
    - first they check if there is any broken wall. if there is any broken wall they move towards it. While moving towards the broken wall if there is any building which comes in it's range it attack the building. After they reach the broken wall they move towards the nearest non-destroyed building.
    - if there is no wall broken , they move towards the nearest building and if they fall in the range before encountering any wall them attack the building, whereas if the wall is encountered before any building falls in its range they destroy any wall in between the shortest path
- Cyan Color

## Loons
- these are the aerial forces of the enemy - 2
- Loons move once per 1 sec and once per 0.5 sec when the rage is activated
- The movement speed is 1 tile per move and the health is predefined
- The color of the loons change when the health of the barbarian reduces below 50%
- The movement of the archers is automated
    - first they check if there are any defenses left i.e cannons and wizard towers. if there are any defenses left they attack the nearest non-destroyed defense
    - If there are no defenses left , they choose the nearest non-destroyed building and attack it
- Yellow Color

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
    - the enemy's lose when all their troops are dead and they haven't destroyed the whole base
## Replay
- Each game played is stored in the replays folder for the user to look at later
- Running the replay.py and specifying the game number allows the user to look at the replay of that game

---

# Bonus

## Leviathan Axe
- This is a feature of the king which allows the king to attack buildings in a range of 4 tiles (AoE)
- Passing the key - l activates the leviathan axe of the king.

## Eagle Arrow
- this is a feature of the queen which allows the queen launch arrows in the air and attack a target 16 tiles away from the queen in the last moved direction with an area od effect with 9x9 tiles
- Passing the key - e activates the eagle arrow of the queen

## Sound Effects
- Sound effects increase the pleasure of playing a game
- Few sound effects are added to increase the playing experience
    - intro
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




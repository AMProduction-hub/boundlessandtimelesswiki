---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/humanoid/burrowling
statblock: inline
aliases: ["Burrowling"]
---
# [Burrowling](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/burrowling-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 47*  

*These light brown, furred creatures inquisitively survey their surroundings, each comforted by the presence of the others.*

## Friendly Farmers

Burrowlings work together at every task: digging tunnels, foraging, and rearing their young. They are omnivorous, eating roots, berries, insects, and reptiles—and they consider snakes a particular delicacy. The most advanced burrowling towns set up rudimentary farms, where they grow the fruits and vegetables they usually find in the wild.

## Safe Warrens

Some towns have domesticated prairie dogs, which burrowlings train to stand watch alongside their masters. Pairs of adults stand watch around the town perimeter and sound a warning when they spot a foe. An alerted town retreats to the safety of its warrens, while the strongest creatures add more tunnels if necessary, and close access from the surface until the threat has passed. In combat, burrowlings stand together in defense of the helpless young and fight with crude slings or their sharp teeth and claws.

## Die of Loneliness

If separated from its coterie, a burrowling becomes despondent, crying for others of its kind. A lone burrowling usually dies of loneliness within a week, unless it can find its way back to its town or discover another burrowling town. Rarely, a solitary creature makes its way to a non-burrowling settlement where it attempts to assist its new community. This frustrates the creature and those it interacts with as it tries to anticipate what its companions want. It may join an adventuring party in the hope of returning to a settlement. After spending at least six months with a party, the burrowling can use its Burrow Awareness with its new allies. Burrowlings live up to 15 years and can have a litter of pups up to twice a year. A burrowling pup reaches adulthood in a year.

> [!note] Burrowlings in Midgard
> 
> Burrowling towns are found in the Western Wastes, where their greatest enemies are dust goblins. They seem to thrive in the badlands and magically scant territories of former human settlements.
^burrowlings-in-midgard

```statblock
"name": "Burrowling (ToB1-2023)"
"size": "Small"
"type": "humanoid"
"subtype": "burrowling"
"alignment": "Lawful Neutral"
"ac": !!int "13"
"hp": !!int "27"
"hit_dice": "6d6 + 6"
"stats":
- !!int "10"
- !!int "16"
- !!int "12"
- !!int "9"
- !!int "12"
- !!int "13"
"speed": "30 ft., burrow 10 ft."
"skillsaves":
  "Perception": !!int "3"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Common"
"cr": "1/2"
"traits":
- "desc": "A burrowling has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks if at least one other burrowling within 10 feet of it isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Burrow Awareness"
- "desc": "The burrowling has advantage on attack rolls against a creature if at least\
    \ one of the burrowling's allies is within 5 feet of the creature and the ally\
    \ isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Pack Tactics"
"actions":
- "desc": "The burrowling makes one Bite attack and one Claw attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4\
    \ + 3) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4\
    \ + 3) slashing damage."
  "name": "Claw"
- "desc": "Ranged Weapon Attack: +5 to hit, range 30/120 ft., one target. Hit:\
    \ 5 (1d4 + 3) bludgeoning damage."
  "name": "Sling"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/burrowling-tob1-2023.webp"
```
^statblock

## Environment

farmland, forest
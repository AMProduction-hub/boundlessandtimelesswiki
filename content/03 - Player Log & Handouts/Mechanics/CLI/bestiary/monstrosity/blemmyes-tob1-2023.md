---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Blemmyes"]
---
# [Blemmyes](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/blemmyes-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 37*  

*This headless giant has a large mouth in its chest with eyes bulging out on either side of it.*

## Always Hungry

Blemmyes are brutes that savor humanoid flesh, and they see all humanoids as potential meals. Some even have the patience to tend groups of humans, goblins, or halflings like unruly herds, farming them for food and fattening them up for maximum succulence.

## Cannibals

So great is their hideous hunger that blemmyes are not above eating their own kind; they cull and consume the weakest specimens of their people when other food is scarce. The most terrible habit of these monsters is that they seldom wait for their food to die, or even for a battle to conclude, before launching into a grisly feast.

```statblock
"name": "Blemmyes (ToB1-2023)"
"size": "Large"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "168"
"hit_dice": "16d10 + 80"
"stats":
- !!int "20"
- !!int "13"
- !!int "20"
- !!int "7"
- !!int "12"
- !!int "5"
"speed": "40 ft."
"skillsaves":
  "Intimidation": !!int "3"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Giant"
"cr": "8"
"traits":
- "desc": "At the start of each of its turns, if the blemmyes can see an [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ creature, the blemmyes must succeed on a DC 11 Wisdom saving throw or spend\
    \ its next turn moving toward and attacking that creature."
  "name": "Carnivorous Compulsion"
"actions":
- "desc": "The blemmyes makes one Bite attack and two Slam attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 19\
    \ (4d6 + 5) piercing damage. If the target is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ and a Medium or smaller creature, the target is swallowed. A swallowed creature\
    \ is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ and [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ it has total cover against attacks and other effects outside the blemmyes, and\
    \ it takes 14 (4d6) acid damage at the start of each of the blemmyes' turns.\
    \ The blemmyes can have only one target swallowed at a time.\n\nIf the blemmyes\
    \ takes 20 damage or more on a single turn from the swallowed creature, the blemmyes\
    \ must succeed on a DC 15 Constitution saving throw at the end of that turn or\
    \ regurgitate the creature, which falls [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ in a space within 5 feet of the blemmyes. If the blemmyes dies, a swallowed\
    \ creature is no longer [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by it and can escape from the corpse using 5 feet of movement, exiting [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 14\
    \ (2d8 + 5) bludgeoning damage. If the target is a creature, it must succeed\
    \ on a DC 16 Wisdom saving throw or be [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the end of its next turn."
  "name": "Slam"
- "desc": "Ranged Weapon Attack: +8 to hit, range 30/120 ft., one target. Hit:\
    \ 27 (4d10 + 5) bludgeoning damage. If the target is a creature, it must succeed\
    \ on a DC 16 Wisdom saving throw or be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ until the end of its next turn."
  "name": "Rock"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/blemmyes-tob1-2023.webp"
```
^statblock

## Environment

farmland, forest, hill
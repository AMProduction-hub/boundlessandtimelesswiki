---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Water Leaper"]
---
# [Water Leaper](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/water-leaper-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 394*  

*The frogheaded, legless creature with wide, batlike wings opens its gaping maw and shrieks. Its long, sinuous tail whips around it, tipped in a barb dripping with poison.*

## Gliding Wings

The creature has no legs or arms, but it sports a pair of wide, membranous wings. It uses its wings to glide beneath the water and to soar through the air.

## Scourge of Waterways

Water leapers plague fresh lakes and rivers. They prey on animals that come to the water's edge to drink, as well as on fishermen that ply their trade in the water leaper's territory. Stories circulate among fishers of waterways known for broken lines and missing bait. Fishers give these areas a wide berth for fear of water leapers. Desperate or unwary fishers who ignore the warnings are never seen again; drifting, empty boats are the signs of their passing.

```statblock
"name": "Water Leaper (ToB1-2023)"
"size": "Large"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "97"
"hit_dice": "13d10 + 26"
"stats":
- !!int "16"
- !!int "14"
- !!int "15"
- !!int "4"
- !!int "12"
- !!int "5"
"speed": "5 ft., fly 50 ft., swim 40 ft."
"skillsaves":
  "Stealth": !!int "4"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": ""
"cr": "4"
"traits":
- "desc": "The water leaper can breathe air and water."
  "name": "Amphibious"
- "desc": "The water leaper has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made while underwater."
  "name": "Underwater Camouflage"
"actions":
- "desc": "The water leaper makes one Bite attack and one Stinger attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10\
    \ (2d6 + 3) piercing damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 13). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and the water leaper can't Bite another target."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d8 + 3) piercing damage, and the target must succeed on a DC 13 Constitution\
    \ saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. While [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way, the creature takes 5 (2d4) poison damage at the start of each\
    \ of its turns. A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Stinger"
- "desc": "The water leaper makes a Bite attack against a Medium or smaller creature\
    \ it is grappling. If the attack hits, the target is also swallowed, and the grapple\
    \ ends. While swallowed, the target is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ and [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ it has total cover against attacks and other effects outside the water leaper,\
    \ and it takes 7 (2d6) acid damage at the start of each of the water leaper's\
    \ turns. The water leaper can have only one creature swallowed at a time.\n\n\
    If the water leaper takes 15 damage or more on a single turn from the swallowed\
    \ creature, the leaper must succeed on a DC 12 Constitution saving throw at the\
    \ end of that turn or regurgitate the creature, which falls [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ in a space within 5 feet of the leaper. If the leaper dies, a swallowed creature\
    \ is no longer [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by it and can escape from the corpse by using 10 feet of movement, exiting [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Swallow"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/water-leaper-tob1-2023.webp"
```
^statblock

## Environment

underwater
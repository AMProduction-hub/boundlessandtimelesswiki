---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/giant
statblock: inline
aliases: ["Zimwi"]
---
# [Zimwi](03 - Player Log & Handouts\Mechanics\CLI\bestiary\giant/zimwi-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 402*  

*This swift-moving, lanky humanoid has long arms ending in wicked claws and jaws that open impossibly wide.*

## Swift as Horses

Distantly related to trolls, the swift and nimble zimwi are a plague upon grasslands. They are constantly hungry, ill-tempered and capable of running down horses, leading many zimwi to attack large caravans for food.

## Always Starving

Most zimwi attacks are driven by hunger. The stomach of a zimwi is larger than its body, extending extra-dimensionally and driving the zimwi nearly insane with constant hunger, leaving the zimwi always feeling as if it is starving to death. Because of their endless hunger and low intelligence, zimwi have little awareness of the course of a battle. Losing means only that they have not eaten. As long as they continue to feast, they fight on, feeling victorious until death comes to them or all of their prey.

## Stomachs of Holding

The extradimensional pouch within a zimwi's stomach makes the stomach serviceable as a bag of holding if treated and enchanted properly. The harder part is relieving the zimwi of its prize.

```statblock
"name": "Zimwi (ToB1-2023)"
"size": "Medium"
"type": "giant"
"alignment": "Chaotic Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "119"
"hit_dice": "13d8 + 52"
"stats":
- !!int "13"
- !!int "18"
- !!int "19"
- !!int "6"
- !!int "9"
- !!int "7"
"speed": "60 ft."
"skillsaves":
  "Perception": !!int "2"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": "Giant"
"cr": "5"
"traits":
- "desc": "When the zimwi is below half its hp maximum, it has advantage on melee\
    \ attack rolls against creatures that aren't Constructs."
  "name": "Desperate Hunger"
"actions":
- "desc": "The zimwi makes one Bite attack and one Claw attack. It can replace its\
    \ Bite attack with a use of Swallow."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) slashing damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 12) if it is a Medium or smaller creature. The zimwi has two claws,\
    \ each of which can grapple only one target."
  "name": "Claws"
- "desc": "The zimwi makes one Bite attack against a Medium or smaller creature it\
    \ is grappling. If the attack hits, the target is also swallowed, and the grapple\
    \ ends. While swallowed, the target is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ and [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ it has total cover against attacks and other effects outside the zimwi, and\
    \ it takes 10 (3d6) acid damage at the start of each of the zimwi's turns. A\
    \ zimwi can have up to two creatures swallowed at a time.\n\nIf the zimwi takes\
    \ 20 damage or more on a single turn from a swallowed creature, the zimwi must\
    \ succeed on a DC 14 Constitution saving throw at the end of that turn or regurgitate\
    \ all swallowed creatures, which fall [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ in a space within 5 feet of the zimwi. If the zimwi dies, a swallowed creature\
    \ is no longer [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by it and can escape from the corpse by using 5 feet of movement, exiting [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Swallow"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/giant/token/zimwi-tob1-2023.webp"
```
^statblock

## Environment

grassland
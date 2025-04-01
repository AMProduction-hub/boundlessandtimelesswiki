---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Ngobou Dinosaur"]
---
# [Ngobou Dinosaur](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/ngobou-dinosaur-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 102*  

*This ill-tempered, six-horned creature resembles a triceratops the size of an ox, with pairs of horns atop its nose and brows, as well as great tusks jutting from each side of its mouth.*

## Hatred of Elephants

Ngobous are ox-sized dinosaurs often at war with elephants over territory. Ngobous are irascible and suspicious by nature, prone to chasing after any creature that stays too long inside its territory. They also become aggressive when they can see or smell elephants. Even old traces of elephant scent are sufficient to trigger an ngobou's rage.

## Poor Beasts of War

Grasslands tribes sometimes try to train ngobous as beasts of burden or war, but most have given up on the ill-tempered animals. Most believe the ngobou's behavior is too erratic, especially if elephants are nearby or have been in the area recently.

## Trample Crops

Stampeding ngobou herds can smash fields of crops flat in minutes, and their horns can tear through a herd of goats or cattle in little time.

```statblock
"name": "Ngobou Dinosaur (ToB1-2023)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "102"
"hit_dice": "12d10 + 36"
"stats":
- !!int "20"
- !!int "9"
- !!int "16"
- !!int "2"
- !!int "12"
- !!int "6"
"speed": "40 ft."
"skillsaves":
  "Perception": !!int "4"
"senses": "passive Perception 14"
"languages": ""
"cr": "5"
"traits":
- "desc": "The ngobou has advantage on attack rolls against elephants. It can pinpoint,\
    \ by scent, the location of any elephant or elephant material no older than 48\
    \ hours within 120 feet of it."
  "name": "Elephants' Bane"
- "desc": "At the start of each of its turns, the ngobou deals 4 (1d8) piercing\
    \ damage to any creature grappling it."
  "name": "Jagged Hide"
- "desc": "At the start of its turn, the ngobou can gain advantage on all melee weapon\
    \ attack rolls it makes during that turn, but attack rolls against it have advantage\
    \ until the start of its next turn. If the ngobou detects an elephant within 120\
    \ feet of it, this trait is always active, and the ngobou can't choose to end\
    \ it until it starts its turn more than 120 feet from an elephant."
  "name": "Reckless"
- "desc": "If the ngobou moves at least 20 feet straight toward a creature and then\
    \ hits it with a Gore attack on the same turn, that target must succeed on a DC\
    \ 14 Strength saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ If the target is [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
    \ the ngobou can make one Stomp attack against it as a bonus action."
  "name": "Trampling Charge"
"actions":
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 27\
    \ (4d10 + 5) piercing damage."
  "name": "Gore"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ creature. Hit: 18 (3d8 + 5) bludgeoning damage."
  "name": "Stomp"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/ngobou-dinosaur-tob1-2023.webp"
```
^statblock

## Environment

farmland, forest, grassland
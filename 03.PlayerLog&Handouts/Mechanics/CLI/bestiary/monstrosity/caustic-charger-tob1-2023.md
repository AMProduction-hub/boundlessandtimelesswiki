---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/badlands
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Caustic Charger"]
---
# [Caustic Charger](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/caustic-charger-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 51*  

*This massive hexapod trundles along, the dangling tentacles festooning its squat body barely clearing the ground. A bony brow ridge set over beady eyes dominates its head.*

Caustic chargers are large, squat creatures that dwell in inhospitable locations, making such lands even more dangerous.

## Unusual Feeder

A caustic charger's odd, toothless snout makes it difficult to hunt and devour prey, but the creature has adapted by secreting a paralytic acid from its tentacles. To make the best use of its stubby tentacles, it charges its prey, striking with its powerful brow ridge to knock over the victim. Then, the charger stands over and dissolves the creature with its tentacles, slurping up the liquefied remains with its snout.

## Solitary Hunters

Caustic chargers are belligerent horrors that attack anything that opposes them, including others of their own kind. Once a year, two chargers become tolerant enough of each other to produce young, resulting in a score of gray eggs with hard shells.

## Ornery Steeds

While not very smart and exceedingly violent, caustic chargers can be persuaded to partner with smaller creatures that might not provide much nourishment but can offer a bounty of prey. Dust goblins are the most common creatures that partner with caustic chargers, with varying degrees of success.

```statblock
"name": "Caustic Charger (ToB1-2023)"
"size": "Huge"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "133"
"hit_dice": "14d12 + 42"
"stats":
- !!int "19"
- !!int "11"
- !!int "16"
- !!int "4"
- !!int "10"
- !!int "6"
"speed": "30 ft., burrow 10 ft."
"damage_immunities": "acid"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": ""
"cr": "7"
"traits":
- "desc": "The caustic charger can end its move in the space of a [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ Large or smaller creature. A creature standing up from [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ in the same space as the charger can move to a space within 5 feet of the charger\
    \ as part of standing up."
  "name": "Straddler"
- "desc": "Difficult terrain composed of rocks or sand doesn't cost the caustic charger\
    \ extra movement."
  "name": "Wastes Walk"
"actions":
- "desc": "The caustic charger makes two Ram attacks. It can replace one Ram attack\
    \ with a Tentacles attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 22\
    \ (4d8 + 4) bludgeoning damage, and if the target is a Large or smaller creature,\
    \ it must succeed on a DC 15 Strength saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ If the charger moved at least 10 feet straight toward the target immediately\
    \ before the hit, the target has disadvantage on the saving throw."
  "name": "Ram"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 7 (1d6\
    \ + 4) bludgeoning damage plus 14 (4d6) acid damage. If the target is a creature,\
    \ it must succeed on a DC 15 Constitution saving throw or be [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ for 1 minute. The [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success. If the caustic charger attacks a target that\
    \ is not in the charger's space, the target takes half the acid damage and has\
    \ advantage on the saving throw."
  "name": "Tentacles"
"bonus_actions":
- "desc": "The caustic charger feeds on a creature [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ by its Tentacles attack. The target must succeed on a DC 15 Constitution saving\
    \ throw or its hp maximum is reduced by half the amount of acid damage dealt by\
    \ the Tentacles attack that caused the paralysis, and the charger regains hp equal\
    \ to that amount. This reduction lasts until the target finishes a long rest.\
    \ The target dies if this effect reduces its hp maximum to 0."
  "name": "Slurp"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/caustic-charger-tob1-2023.webp"
```
^statblock

## Environment

badlands, grassland
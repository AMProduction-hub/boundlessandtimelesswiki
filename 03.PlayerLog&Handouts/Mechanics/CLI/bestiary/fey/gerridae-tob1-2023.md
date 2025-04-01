---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Gerridae"]
---
# [Gerridae](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/gerridae-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 198*  

*This large water-striding insect resembles a strange cross between a camel and a wingless, long-legged locust. A large hollow in the small of its back holds enough space for a rider.*

## Elvish Water Steeds

Known by their Elvish name, these large fey water striders were enchanted and bred by the elves in ages past, when their explorers roamed the world. Elven mages started with normal water striders and—through elaborate magical procedures and complex cross-breeding programs—transformed the mundane water striders into large, docile mounts. They can cross large bodies of water quickly while carrying a humanoid rider, even in windy conditions.

## Fond of Sweet Scents

Gerridae can sometimes be distracted by appealing scents, such as from apple blossoms or fresh hay. They are also fond of raw duck and swan.

> [!note] Gerridae in Midgard
> 
> Since the elven retreat from Midgard almost 500 years ago, many of the gerridae have gone feral, and while normally shy and docile, they can attack in furious swarms if hunted or surprised in their claimed territories. Some enterprising elfmarked Barsellan pirates have domesticated them and use the water striders as chasers and boarding craft when taking on Bemmean and Septime ships.
^gerridae-in-midgard

```statblock
"name": "Gerridae (ToB1-2023)"
"size": "Large"
"type": "fey"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "76"
"hit_dice": "9d10 + 27"
"stats":
- !!int "16"
- !!int "15"
- !!int "17"
- !!int "2"
- !!int "13"
- !!int "7"
"speed": "40 ft., swim 80 ft. (20 ft. when walking on land)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": ""
"cr": "1"
"traits":
- "desc": "The gerridae can't be [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ or [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ while it has a rider."
  "name": "Bred to the Saddle"
- "desc": "For every hour the gerridae spends on dry land, its hp maximum is reduced\
    \ by 2 (1d4)."
  "name": "Water Bound"
- "desc": "The gerridae can move across the surface of water as if it were harmless,\
    \ solid ground. This trait works like the [water walk](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/water-walk.md)\
    \ spell."
  "name": "Water Walker"
"actions":
- "desc": "The gerridae makes one Bite attack and one Claw attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6\
    \ + 3) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4\
    \ + 3) slashing damage."
  "name": "Claw"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/gerridae-tob1-2023.webp"
```
^statblock

## Environment

coastal, forest, underwater
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Asanbosam"]
---
# [Asanbosam](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/asanbosam-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 27*  

*A hirsute hulk with bulging, bloodshot eyes perches high in a tree, ready to seize unwary passersby with its rusty, hook-like talons.*

## Iron Hooks and Fangs

Asanbosam resemble hairy ogres from the waist up, but with muscular, flexible legs much longer than those of an ogre. These odd appendages end in feet with hook-like talons, and both the creature's hooks and its fangs are composed of iron rather than bone or other organic material. These iron fangs and claws mark an asanbosam's age, not just by their size but also by their color. The youngest specimens have shiny gray hooks and fangs, while those of the older asanbosams are discolored and rusty.

## Iron Eaters

The asanbosam diet includes iron in red meat, poultry, fish, and leaf vegetables, and—in times of desperation—grinding iron filings off their own hooks to slake their cravings. The asanbosams' taste for fresh blood and humanoid flesh led to the folklore that they are vampiric (not true).

## Tree Lairs

Asanbosams spend most of their lives in trees, where they build nestlike houses or platforms of rope and rough planks. They don't fear magic; most tribes count at least one spellcaster among its members.

```statblock
"name": "Asanbosam (ToB1-2023)"
"size": "Large"
"type": "aberration"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "102"
"hit_dice": "12d10 + 36"
"stats":
- !!int "18"
- !!int "13"
- !!int "17"
- !!int "11"
- !!int "10"
- !!int "5"
"speed": "40 ft., climb 15 ft."
"skillsaves":
  "Stealth": !!int "4"
  "Perception": !!int "3"
  "Acrobatics": !!int "4"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Giant"
"cr": "5"
"traits":
- "desc": "The asanbosam can climb difficult surfaces, including upside down on ceilings,\
    \ without needing to make an ability check."
  "name": "Spider Climb"
"actions":
- "desc": "The asanbosam makes one Bite attack and one Claws attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 15\
    \ (2d10 + 4) piercing damage. If the target is a creature, it must succeed on\
    \ a DC 14 Constitution saving throw or take 11 (2d10) poison damage and contract\
    \ a disease. Until the disease ends, the creature is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ Every 24 hours that elapse, the infected creature must repeat the saving throw.\
    \ On a success, the disease ends. On a failure, the creature's hp maximum is reduced\
    \ by 5 (1d10). This reduction lasts until the disease ends. The target dies\
    \ if its hp maximum is reduced to 0."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 20\
    \ (3d10 + 4) piercing damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 14). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and the asanbosam can't use its Claws on another target. If the target is a\
    \ creature, it must succeed on a DC 14 Constitution saving throw or contract the\
    \ disease described in the Bite attack."
  "name": "Claws"
"bonus_actions":
- "desc": "While in a tree, the asanbosam takes the Disengage or Hide action."
  "name": "Arboreal Escape"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/asanbosam-tob1-2023.webp"
```
^statblock

## Environment

forest, hill
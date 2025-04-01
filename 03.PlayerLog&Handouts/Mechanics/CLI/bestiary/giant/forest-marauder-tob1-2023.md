---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/giant
statblock: inline
aliases: ["Forest Marauder"]
---
# [Forest Marauder](03 - Player Log & Handouts\Mechanics\CLI\bestiary\giant/forest-marauder-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 191*  

*A relatively diminutive giant stalks beneath the forest's dark canopy, large spear in hand.*

## Painted Skin

Roughly the size and shape of an ogre, the forest marauder is covered in paint or colored mud. An exaggerated brow ridge juts out over close-set eyes, and corded muscle stands out all over the giant.

## Keep to the Wilderness

Cruel and savage when encountered, the forest marauders' demeanor has worked against them, and they have nearly been driven to extinction in places where they can be easily tracked. They have since learned to raid far from their hidden homes, leading to sightings in unexpected places.

## Orc Friends

Forest marauders get along well with orcs and goblins, who appreciate their brute strength and their skill at night raids.

```statblock
"name": "Forest Marauder (ToB1-2023)"
"size": "Large"
"type": "giant"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "114"
"hit_dice": "12d10 + 48"
"stats":
- !!int "21"
- !!int "10"
- !!int "18"
- !!int "6"
- !!int "10"
- !!int "7"
"speed": "40 ft., climb 20 ft."
"saves":
  "Constitution": !!int "6"
"skillsaves":
  "Stealth": !!int "4"
"senses": "darkvision 120 ft., passive Perception 10"
"languages": "Giant, Orc, Sylvan"
"cr": "4"
"traits":
- "desc": "The giant has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in forested terrain."
  "name": "Forest Camouflage"
- "desc": "While in sunlight, the forest marauder has disadvantage on attack rolls,\
    \ as well as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
"actions":
- "desc": "The forest marauder makes two Boar Spear attacks. If both attacks hit one\
    \ creature, the target must succeed on a DC 15 Strength saving throw or be pushed\
    \ up to 10 feet away from the marauder. The marauder can choose not to push a\
    \ creature."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 16\
    \ (2d10 + 5) piercing damage."
  "name": "Boar Spear"
- "desc": "Ranged Weapon Attack: +7 to hit, range 30/120 ft., one target. Hit:\
    \ 21 (3d10 + 5) bludgeoning damage."
  "name": "Rock"
"bonus_actions":
- "desc": "While in a forest, the forest marauder can take the Hide action."
  "name": "Forest Ambusher"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/giant/token/forest-marauder-tob1-2023.webp"
```
^statblock

## Environment

forest
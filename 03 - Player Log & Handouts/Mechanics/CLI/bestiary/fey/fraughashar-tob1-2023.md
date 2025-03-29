---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Fraughashar"]
---
# [Fraughashar](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/fraughashar-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 192*  

*This slight creature resembles a goblin, but its blue skin and the icicles hanging from the tip of its long nose speak to the chilling truth.*

The fraughashar are a race of short, tricky, cruel fey who inhabit cold mountainous regions. Fraughashar have light blue skin, short pointed ears, and needlelike teeth. Delighting in mayhem, they always seem to have devilish grins on their faces.

## Sacred Rivers

The fraughashar view cold rivers and river gorges as sacred places in which their wicked god Fraugh dwells, and they likewise revere the snowy peaks where the Snow Queen holds sway. They are fiercely protective of their territory, and their easy mobility over frozen and rocky terrain lets them make short work of intruders.

## Chilling Tales

The origin of the strange and deadly fraughashar is unclear. Some druidic legends claim the fraughashar were born out of a winter so cold and cruel that the spirits of the river itself froze. Bardic tales claim that the fraughashar are a tribe of corrupted goblins, and that they were permanently disfigured during a botched attempt at summoning an ice devil. Whatever the truth of their beginnings, the fraughashar are cruel and merciless. They kill anyone who enters their land.

```statblock
"name": "Fraughashar (ToB1-2023)"
"size": "Small"
"type": "fey"
"alignment": "Neutral Evil"
"ac": !!int "15"
"ac_class": "[leather armor](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/leather-armor.md),\
  \ [shield](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/shield.md)"
"hp": !!int "22"
"hit_dice": "5d6 + 5"
"stats":
- !!int "8"
- !!int "14"
- !!int "12"
- !!int "10"
- !!int "14"
- !!int "7"
"speed": "25 ft."
"skillsaves":
  "Stealth": !!int "4"
"damage_immunities": "cold"
"senses": "passive Perception 10"
"languages": "Sylvan"
"cr": "1/2"
"traits":
- "desc": "The fraughashar can move across icy surfaces without needing to make an\
    \ ability check, and difficult terrain composed of ice and snow doesn't cost it\
    \ extra movement. In addition, the fraughashar has advantage on Strength and Dexterity\
    \ saving throws made against effects that would knock it [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ while in icy or snowy terrain."
  "name": "Deft Snow Walk"
"actions":
- "desc": "The fraughashar makes one Bite attack and one Dagger attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4\
    \ + 2) piercing damage."
  "name": "Bite"
- "desc": "Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 4 (1d4 + 2) piercing damage."
  "name": "Dagger"
- "desc": "Ranged Spell Attack: +4 to hit, range 60 ft., one target. Hit: 7\
    \ (2d4 + 2) cold damage."
  "name": "Frost Bolt"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/fraughashar-tob1-2023.webp"
```
^statblock

## Environment

arctic
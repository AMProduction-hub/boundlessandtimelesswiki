---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Shadow Beast"]
---
# [Shadow Beast](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/shadow-beast-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 324*  

*A mass of shadows and cloudstuff, never touching the ground, extends clawed hands as it reveals a glint of jagged teeth.*

## Called from the Void

Shadow beasts are thought to be the result of shadow fey dabbling in the magic of the Void, transforming the shadow fey into something wholly different. Almost shapeless and largely incorporeal, through an act of will they can form rough semblances of their old bodies when needed.

## Hate the Past

The motivations of these creatures are inscrutable. They despise light and anything that reminds them of light or of their former existence. Beyond that, little is understood about them.

## Cryptic Messages

Shadow beasts are seldom found in groups, but when they are, they seem to have no difficulty or reluctance about operating and fighting together. They have been known to deliver cryptic and threatening messages, but speaking is difficult for them. At times, they perform arcane rituals with the aid of evil humanoids and the use of dark materials. In these rituals, they sacrifice magical energies and life blood as well as the tears of innocents and the souls of the damned.

```statblock
"name": "Shadow Beast (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"hp": !!int "112"
"hit_dice": "15d8 + 45"
"stats":
- !!int "6"
- !!int "20"
- !!int "17"
- !!int "14"
- !!int "14"
- !!int "19"
"speed": "0 ft., fly 40 ft. (hover)"
"saves":
  "Wisdom": !!int "5"
  "Constitution": !!int "6"
"skillsaves":
  "Stealth": !!int "8"
"damage_resistances": "acid; cold; lightning; thunder; bludgeoning, piercing, slashing\
  \ from nonmagical attacks"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": "Common, Elvish, Umbral, Void Speech"
"cr": "7"
"traits":
- "desc": "The shadow beast can move through other creatures and objects as if they\
    \ were difficult terrain. It takes 5 (1d10) force damage if it ends its turn\
    \ inside an object."
  "name": "Incorporeal Movement"
- "desc": "The shadow beast has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
- "desc": "The shadow beast's weapon attacks are magical. When the shadow beast hits\
    \ with any weapon, the weapon deals an extra 2d6 necrotic damage (included in\
    \ the attack)."
  "name": "Shadow Weapons"
- "desc": "While in sunlight, the shadow beast has disadvantage on attack rolls, as\
    \ well as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
"actions":
- "desc": "The shadow beast makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (1d8\
    \ + 5) piercing damage plus 7 (2d6) necrotic damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 8 (1d6\
    \ + 5) slashing damage plus 7 (2d6) necrotic damage."
  "name": "Claw"
- "desc": "The shadow beast releases a wave of shadows filled with frightening images\
    \ of eyes, fangs, and other barely seen and terrifying beasts in a 30-foot cone.\
    \ Each creature in the area must make a DC 15 Wisdom saving throw. On a failure,\
    \ a creature takes 42 (12d6) necrotic damage and is [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened).\
    \ A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ creature must take the Dash action and move away from the shadow beast by the\
    \ safest available route on each of its turns, unless there is nowhere to move.\
    \ A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Frightful Shadows (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/shadow-beast-tob1-2023.webp"
```
^statblock

## Environment

planar
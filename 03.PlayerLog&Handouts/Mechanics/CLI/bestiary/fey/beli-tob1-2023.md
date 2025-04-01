---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Beli"]
---
# [Beli](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/beli-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 35*  

*With their pale skin and translucent wings, these winter fairies blend perfectly into their snowy environment. Only their beady black eyes stand out against the snow and ice.*

These malevolent ice-sprites are a plague upon the people of snowy climates, ambushing unwary prey with icy arrows and freezing powers.

## Servants of the North Wind

Known as*patzinaki*in some dialects of Dwarvish, the beli are the servants of winter gods and venerate the north wind as Boreas and other gods of darker aspects. They are frequent allies with the fraughashar.

## Feast Crashers

Beli especially delight in disrupting feasts and making off with the holiday cakes—the least deadly of their malicious pranks.

## Fear of Druids

They have an irrational fear of northern druids and their snow bear companions.

```statblock
"name": "Beli (ToB1-2023)"
"size": "Small"
"type": "fey"
"alignment": "Neutral Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "45"
"hit_dice": "10d6 + 10"
"stats":
- !!int "11"
- !!int "16"
- !!int "12"
- !!int "8"
- !!int "11"
- !!int "14"
"speed": "30 ft., fly 30 ft."
"saves":
  "Dexterity": !!int "5"
"skillsaves":
  "Stealth": !!int "5"
  "Perception": !!int "4"
"damage_vulnerabilities": "fire"
"damage_immunities": "cold"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Common, Dwarvish, Giant"
"cr": "2"
"traits":
- "desc": "The beli has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in snowy terrain. In addition, it has advantage on Wisdom\
    \ ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight in snowy terrain."
  "name": "Arctic Hunter"
- "desc": "If it starts its turn in an area with below freezing temperature, the beli\
    \ regains 3 hp. If the beli takes fire damage, this trait doesn't function at\
    \ the start of the beli's next turn. The beli dies only if it starts its turn\
    \ with 0 hp and it doesn't regenerate."
  "name": "Cold Regeneration"
- "desc": "The beli doesn't provoke opportunity attacks when it flies out of an enemy's\
    \ reach."
  "name": "Flyby"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4\
    \ + 3) piercing damage plus 5 (2d4) cold damage."
  "name": "Ice Dagger"
- "desc": "Ranged Weapon Attack: +5 to hit, range 80/320 ft., one target. Hit:\
    \ 6 (1d6 + 3) piercing damage plus 5 (2d4) cold damage, and the target must\
    \ succeed on a DC 13 Constitution saving throw or suffer one level of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)\
    \ from the arrow's icy chill. On a success, the target can't suffer further levels\
    \ of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)\
    \ from any beli's Icy Shortbow for 24 hours. If a creature would suffer a sixth\
    \ level of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)\
    \ from this attack, it is reduced to 0 hp instead and must make death saving throws\
    \ as normal. A creature reduced to 0 hp in this way can't suffer further levels\
    \ of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)\
    \ from any beli's Icy Shortbow for 24 hours."
  "name": "Icy Shortbow"
- "desc": "The beli magically turns [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ until it attacks or until its [concentration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ ends (as if [concentrating](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ on a spell). Any equipment the beli wears or carries is [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ with it."
  "name": "Invisibility"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/beli-tob1-2023.webp"
```
^statblock

## Environment

arctic
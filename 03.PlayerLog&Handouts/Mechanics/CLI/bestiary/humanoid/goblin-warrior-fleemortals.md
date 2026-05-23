---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/fleemortals
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/humanoid/goblin
- ttrpg-cli/monster/type/humanoid/skirmisher
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Goblin Warrior"
---
# [Goblin Warrior](03.PlayerLog&Handouts/Mechanics/CLI/bestiary/humanoid/goblin-warrior-fleemortals.md)
*Source: Flee, Mortals! p. 129*  

```statblock
"name": "Goblin Warrior (FleeMortals)"
"size": "Small"
"type": "humanoid"
"subtype": "goblin, Skirmisher"
"alignment": "Any alignment"
"ac": !!int "15"
"ac_class": "[leather armor](03.PlayerLog&Handouts/Mechanics/CLI/items/leather-armor.md),\
  \ [shield](03.PlayerLog&Handouts/Mechanics/CLI/items/shield.md)"
"hp": !!int "9"
"hit_dice": "2d6 + 2"
"modifier": !!int "2"
"stats":
  - !!int "8"
  - !!int "14"
  - !!int "12"
  - !!int "10"
  - !!int "10"
  - !!int "8"
"speed": "30 ft., climb 20 ft."
"skillsaves":
  - "name": "[Acrobatics](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Acrobatics)"
    "desc": "+4"
  - "name": "[Stealth](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Stealth)"
    "desc": "+4"
"gear":
  - "[shortbow](03.PlayerLog&Handouts/Mechanics/CLI/items/shortbow.md)"
  - "[shortsword](03.PlayerLog&Handouts/Mechanics/CLI/items/shortsword.md)"
"senses": "[darkvision](03.PlayerLog&Handouts/Mechanics/CLI/rules/senses.md#Darkvision)\
  \ 60 ft., passive Perception 10"
"languages": "Common, Goblin"
"cr": "1/4"
"traits":
  - "desc": "The warrior doesn't provoke opportunity attacks when they move out of\
      \ an enemy's reach."
    "name": "Crafty"
"actions":
  - "desc": "*Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 5\
      \ (1d6 + 2) piercing damage."
    "name": "Shortsword"
  - "desc": "*Ranged Weapon Attack:* +4 to hit, range 80/320 ft., one target. *Hit:*\
      \ 5 (1d6 + 2) piercing damage."
    "name": "Shortbow"
"reactions":
  - "desc": "When a creature within 5 feet of the warrior misses them with a melee\
      \ attack, the warrior can move up to half their speed."
    "name": "Fleet Foot"
"source":
  - "FleeMortals"
```
^statblock
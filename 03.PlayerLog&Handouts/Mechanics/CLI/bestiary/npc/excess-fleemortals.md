---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/fleemortals
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/monstrosity/ambusher
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Excess"
---
# [Excess](03.PlayerLog&Handouts/Mechanics/CLI/bestiary/npc/excess-fleemortals.md)
*Source: Flee, Mortals! p. 358*  

```statblock
"name": "Excess (FleeMortals)"
"size": "Medium"
"type": "monstrosity"
"subtype": "Ambusher"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"hp": !!int "45"
"hit_dice": "6d8 + 18"
"modifier": !!int "4"
"stats":
  - !!int "14"
  - !!int "18"
  - !!int "16"
  - !!int "10"
  - !!int "15"
  - !!int "11"
"speed": "30 ft., climb 30 ft."
"saves":
  - "dexterity": !!int "6"
  - "constitution": !!int "5"
"skillsaves":
  - "name": "[Acrobatics](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Acrobatics)"
    "desc": "+6"
  - "name": "[Perception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Perception)"
    "desc": "+4"
  - "name": "[Stealth](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Stealth)"
    "desc": "+8"
"senses": "[darkvision](03.PlayerLog&Handouts/Mechanics/CLI/rules/senses.md#Darkvision)\
  \ 60 ft., passive Perception 14"
"languages": "Common"
"cr": "2"
"traits":
  - "desc": "Excess can climb difficult surfaces, including upside down on ceilings,\
      \ without needing to make an ability check."
    "name": "Spider Climb"
"actions":
  - "desc": "Excess makes one Bite attack and one Sting attack."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 8\
      \ (1d8 + 4) piercing damage. If the target is a Medium or smaller creature,\
      \ they are [grappled](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
      \ (escape DC 14). While [grappled](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
      \ a target takes 2 (1d4) poison damage at the start of each of Excess's turns,\
      \ and Excess can't make a Bite attack against another target."
    "name": "Bite"
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 10 ft., one target. *Hit:*\
      \ 7 (1d6 + 4) piercing damage, and the target must succeed on a DC 13 Constitution\
      \ saving throw or be [poisoned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
      \ for 1 minute (save ends at end of turn)."
    "name": "Sting"
  - "desc": "Excess makes a Bite attack against a Medium or smaller creature who they\
      \ are grappling or hidden from.\n\nIf the attack hits, the target is swallowed\
      \ as Excess enlarges their head and stomach. The swallowed target is no longer\
      \ [grappled](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
      \ but they are [blinded](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
      \ and [restrained](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
      \ have total cover against attacks and other effects outside Excess, and take\
      \ 10 (3d6) acid damage at the start of each of Excess's turns. Excess can\
      \ have only one target swallowed at a time.\n\nIf Excess dies, a swallowed creature\
      \ is no longer [restrained](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
      \ by them and can escape from the corpse by using 5 feet of movement, exiting\
      \ [prone](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
    "name": "Swallow"
"bonus_actions":
  - "desc": "Excess takes the Dash, Disengage, or Hide action."
    "name": "Cunning Action"
"source":
  - "FleeMortals"
```
^statblock
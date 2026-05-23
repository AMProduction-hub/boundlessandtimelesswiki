---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/fleemortals
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead/incorporeal
- ttrpg-cli/monster/type/undead/skirmisher
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Specter"
---
# [Specter](03.PlayerLog&Handouts/Mechanics/CLI/bestiary/undead/specter-fleemortals.md)
*Source: Flee, Mortals! p. 247*  

```statblock
"name": "Specter (FleeMortals)"
"size": "Medium"
"type": "undead"
"subtype": "incorporeal, Skirmisher"
"alignment": "typically  Chaotic Evil"
"ac": !!int "11"
"hp": !!int "19"
"hit_dice": "3d8 + 6"
"modifier": !!int "1"
"stats":
  - !!int "1"
  - !!int "13"
  - !!int "14"
  - !!int "10"
  - !!int "10"
  - !!int "15"
"speed": "0 ft., fly 50 ft. (hover)"
"damage_resistances": "acid; cold; fire; lightning; thunder; bludgeoning, piercing,\
  \ slashing from mundane attacks"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[charmed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [dazed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Dazed), [exhaustion](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [grappled](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Prone), [restrained](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [unconscious](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "[darkvision](03.PlayerLog&Handouts/Mechanics/CLI/rules/senses.md#Darkvision)\
  \ 60 ft., passive Perception 10"
"languages": "the languages they knew in life"
"cr": "1"
"traits":
  - "desc": "The specter can move through other creatures and objects as if they were\
      \ difficult terrain. The specter takes 5 (1d10) force damage if they end their\
      \ turn inside an object. A creature takes 2 (1d4) necrotic damage the first\
      \ time a specter passes through them on a turn."
    "name": "Corrupting Phasing"
"actions":
  - "desc": "*Melee Spell Attack:* +4 to hit, reach 5 ft., one creature. *Hit:*\
      \ 7 (2d6) necrotic damage, and the target must succeed on a DC 12 Constitution\
      \ saving throw or spend 1 Hit Die without any benefit. If the target has no\
      \ Hit Dice to spend, they drop to 0 hit points instead.\n\nIf a Humanoid dies\
      \ within 1 minute of being hit by this attack, their spirit rises as a specter\
      \ under the GM's control in an unoccupied space nearest to where that Humanoid\
      \ died."
    "name": "Decaying Touch"
"bonus_actions":
  - "desc": "The specter turns [invisible](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
      \ and then moves up to their speed. At the end of this movement, the invisibility\
      \ ends."
    "name": "Hidden Movement (Recharge 5-6)"
"source":
  - "FleeMortals"
```
^statblock
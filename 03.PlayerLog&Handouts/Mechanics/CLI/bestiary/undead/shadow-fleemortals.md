---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/fleemortals
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead/ambusher
- ttrpg-cli/monster/type/undead/incorporeal
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Shadow"
---
# [Shadow](03.PlayerLog&Handouts/Mechanics/CLI/bestiary/undead/shadow-fleemortals.md)
*Source: Flee, Mortals! p. 247*  

```statblock
"name": "Shadow (FleeMortals)"
"size": "Medium"
"type": "undead"
"subtype": "incorporeal, Ambusher"
"alignment": "typically  Chaotic Evil"
"ac": !!int "12"
"hp": !!int "13"
"hit_dice": "3d8"
"modifier": !!int "2"
"stats":
  - !!int "6"
  - !!int "14"
  - !!int "11"
  - !!int "10"
  - !!int "10"
  - !!int "14"
"speed": "40 ft."
"skillsaves":
  - "name": "[Stealth](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Stealth)"
    "desc": "+4"
"damage_resistances": "acid; lightning; necrotic; thunder; bludgeoning, piercing,\
  \ slashing from mundane attacks"
"damage_immunities": "cold, poison"
"condition_immunities": "[dazed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Dazed),\
  \ [exhaustion](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [grappled](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Prone), [restrained](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Restrained)"
"senses": "[darkvision](03.PlayerLog&Handouts/Mechanics/CLI/rules/senses.md#Darkvision)\
  \ 60 ft., passive Perception 10"
"languages": "the languages they knew in life"
"cr": "1/2"
"traits":
  - "desc": "The shadow can move through other creatures and objects as if they were\
      \ difficult terrain. The shadow takes 5 (1d10) force damage if they end their\
      \ turn inside an object. A creature takes 1 cold damage the first time a shadow\
      \ passes through them on a turn."
    "name": "Chilling Phasing"
  - "desc": "While in dim light or darkness, the shadow has advantage on Dexterity\
      \ ([Stealth](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Stealth)) checks."
    "name": "Dark Stalker"
"actions":
  - "desc": "*Melee Spell Attack:* +4 to hit, reach 5 ft., one creature. *Hit:*\
      \ 6 (1d8 + 2) cold damage, and the target's Dexterity score is reduced by\
      \ 2. The target dies if this reduces its Dexterity to 0. Otherwise, the reduction\
      \ lasts until the target finishes a short or long rest."
    "name": "Chilling Grasp"
  - "desc": "The shadow pours magical darkness out of their hand in a 15-foot cone.\
      \ A creature with darkvision who isn't an incorporeal Undead can't see through\
      \ this darkness, and light can't illuminate it. Each creature in this darkness\
      \ when it first appears must succeed on a DC 12 Constitution saving throw or\
      \ take 7 (2d6) cold damage. The darkness remains in that area for 1 minute\
      \ or until the shadow is destroyed."
    "name": "Freezing Dark (1/Day)"
"bonus_actions":
  - "desc": "The shadow targets one creature they can see within 15 feet of them who\
      \ is in bright or dim light. The target must succeed on a DC 12 Strength saving\
      \ throw or be [grappled](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
      \ by their own shadow (escape DC 12). The grapple ends if the target is no longer\
      \ in bright or dim light, or if the shadow who used this bonus action is destroyed."
    "name": "Shadow Bind"
"source":
  - "FleeMortals"
```
^statblock
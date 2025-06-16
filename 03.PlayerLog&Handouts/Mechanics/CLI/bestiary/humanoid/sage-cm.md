---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/cm
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
statblock-link: "#^statblock"
aliases:
- Sage
---
# [Sage](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\humanoid/sage-cm.md)
*Source: Candlekeep Mysteries p. 9*  

Candlekeep's resident lore experts are master sages and sages who dedicate themselves to scholarship above all.

```statblock
"name": "Sage (CM)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Unaligned"
"ac": !!int "10"
"hp": !!int "22"
"hit_dice": "5d8"
"modifier": !!int "0"
"stats":
  - !!int "8"
  - !!int "10"
  - !!int "10"
  - !!int "18"
  - !!int "15"
  - !!int "11"
"speed": "30 ft."
"skillsaves":
  - "name": "[Arcana](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Arcana)"
    "desc": "+8"
  - "name": "[History](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#History)"
    "desc": "+8"
  - "name": "[Insight](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Insight)"
    "desc": "+4"
  - "name": "[Investigation](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Investigation)"
    "desc": "+8"
  - "name": "[Medicine](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Medicine)"
    "desc": "+6"
  - "name": "[Nature](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Nature)"
    "desc": "+8"
  - "name": "[Religion](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Religion)"
    "desc": "+8"
"senses": "passive Perception 12"
"languages": "Common plus any four languages"
"cr": "1/2"
"actions":
  - "desc": "Melee Spell Attack: +6 to hit (with advantage if the target is wearing\
      \ armor made of metal), reach 5 ft., one creature. Hit: 9 (2d8) lightning\
      \ damage, and the target can't take reactions until the start of its next turn."
    "name": "Shocking Grasp (Cantrip)"
  - "desc": "The sage casts one of the following spells, using Intelligence as the\
      \ spellcasting ability (save DC 14, +6 to hit with spell attacks):\n\nAt\
      \ will: [light](03.PlayerLog&Handouts/Mechanics/CLI/spells/light.md), [mage\
      \ hand](03.PlayerLog&Handouts/Mechanics/CLI/spells/mage-hand.md), [mending](03.PlayerLog&Handouts/Mechanics/CLI/spells/mending.md)\n\
      \n3/day each: [comprehend languages](03.PlayerLog&Handouts/Mechanics/CLI/spells/comprehend-languages.md),\
      \ [detect magic](03.PlayerLog&Handouts/Mechanics/CLI/spells/detect-magic.md),\
      \ [identify](03.PlayerLog&Handouts/Mechanics/CLI/spells/identify.md)\n\n1/day\
      \ each: [dispel magic](03.PlayerLog&Handouts/Mechanics/CLI/spells/dispel-magic.md),\
      \ [levitate](03.PlayerLog&Handouts/Mechanics/CLI/spells/levitate.md), [locate\
      \ object](03.PlayerLog&Handouts/Mechanics/CLI/spells/locate-object.md), [see\
      \ invisibility](03.PlayerLog&Handouts/Mechanics/CLI/spells/see-invisibility.md),\
      \ [sending](03.PlayerLog&Handouts/Mechanics/CLI/spells/sending.md), [tongues](03.PlayerLog&Handouts/Mechanics/CLI/spells/tongues.md),\
      \ [unseen servant](03.PlayerLog&Handouts/Mechanics/CLI/spells/unseen-servant.md)"
    "name": "Spellcasting"
"reactions":
  - "desc": "When the sage is hit by an attack or targeted by a [magic missile](03.PlayerLog&Handouts/Mechanics/CLI/spells/magic-missile.md)\
      \ spell, it calls forth an [invisible](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
      \ barrier of magical force that protects it. Until the start of its next turn,\
      \ the sage has a +5 bonus to AC, including against the triggering attack, and\
      \ it takes no damage from magic missile."
    "name": "Shield (1st-Level Spell; 3/Day)"
"source":
  - "CM"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/humanoid/token/sage-cm.webp"
```
^statblock
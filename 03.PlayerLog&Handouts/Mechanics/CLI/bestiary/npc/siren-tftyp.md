---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tftyp
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
statblock-link: "#^statblock"
aliases:
- Siren
---
# [Siren](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\npc/siren-tftyp.md)
*Source: Tales from the Yawning Portal p. 243, Mythic Odysseys of Theros*  

Imprisoned inside a mist-filled chamber in the Tomb of Horrors, Siren serves as evidence of Acererak's heartless sense of humor. This mysterious fey creature yearns to be released, but an enchantment laid on her by the demilich prevents her from telling visitors how to accomplish that task. If anyone succeeds in freeing her, she vows to be a lifelong friend.

```statblock
"name": "Siren (TftYP)"
"size": "Medium"
"type": "fey"
"alignment": "Chaotic Good"
"ac": !!int "14"
"hp": !!int "38"
"hit_dice": "7d8 + 7"
"modifier": !!int "4"
"stats":
  - !!int "10"
  - !!int "18"
  - !!int "12"
  - !!int "13"
  - !!int "14"
  - !!int "16"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  - "name": "[Medicine](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Medicine)"
    "desc": "+4"
  - "name": "[Nature](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Nature)"
    "desc": "+3"
  - "name": "[Stealth](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Stealth)"
    "desc": "+6"
  - "name": "[Survival](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Survival)"
    "desc": "+4"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": "Common, Elvish, Sylvan"
"cr": "3"
"traits":
  - "desc": "Siren's innate spellcasting ability is Charisma (spell save DC 13). She\
      \ can innately cast the following spells, requiring no material components:\n\
      \n1/day each: [charm person](03.PlayerLog&Handouts/Mechanics/CLI/spells/charm-person.md),\
      \ [fog cloud](03.PlayerLog&Handouts/Mechanics/CLI/spells/fog-cloud.md), [greater\
      \ invisibility](03.PlayerLog&Handouts/Mechanics/CLI/spells/greater-invisibility.md),\
      \ [polymorph](03.PlayerLog&Handouts/Mechanics/CLI/spells/polymorph.md) (self\
      \ only)"
    "name": "Innate Spellcasting"
  - "desc": "Siren can breathe air and water."
    "name": "Amphibious"
  - "desc": "Siren has advantage on saving throws against spells and other magical\
      \ effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7\
      \ (1d6 + 4) piercing damage."
    "name": "Shortsword"
  - "desc": "Siren touches one creature she can see within 5 feet of her. The creature\
      \ must succeed on a DC 13 Intelligence saving throw or take 13 (3d6 + 3) psychic\
      \ damage and be [stunned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
      \ until the start of Siren's next turn."
    "name": "Stupefying Touch"
"source":
  - "TftYP"
  - "MOT"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/npc/token/siren-tftyp.webp"
```
^statblock
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/scc
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid/bard
statblock: inline
statblock-link: "#^statblock"
aliases:
- Silverquill Professor of Radiance
---
# [Silverquill Professor of Radiance](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\humanoid/silverquill-professor-of-radiance-scc.md)
*Source: Strixhaven: A Curriculum of Chaos p. 215*  

Professors of radiance call up magic through spoken words and glyphs formed of magically shaped ink and light. The professors channel radiance to illuminate their allies, bolstering them with encouragement and inspiring any who witness their orations. Professors of radiance can turn their words into potent assets in battle or strike at their foes with searing radiance.

These Silverquill teachers seek to inspire greatness in all that they do, pushing their students to look for the good in all things and bring that into the light.

## Silverquill Scholars

The scholars of Silverquill College study the power of magic shaped through spoken and written words. They use that power either to illuminate and guide or to obscure and demoralize.

```statblock
"name": "Silverquill Professor of Radiance (SCC)"
"size": "Small or Medium"
"type": "humanoid"
"subtype": "bard"
"alignment": "Any alignment"
"ac": !!int "12"
"hp": !!int "97"
"hit_dice": "15d8 + 30"
"modifier": !!int "2"
"stats":
  - !!int "11"
  - !!int "14"
  - !!int "14"
  - !!int "16"
  - !!int "13"
  - !!int "19"
"speed": "30 ft."
"saves":
  - "dexterity": "+5"
  - "intelligence": "+6"
  - "wisdom": "+4"
  - "charisma": "+7"
"skillsaves":
  - "name": "[Arcana](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Arcana)"
    "desc": "+6"
  - "name": "[Deception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Deception)"
    "desc": "+7"
  - "name": "[Performance](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Performance)"
    "desc": "+10"
  - "name": "[Persuasion](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Persuasion)"
    "desc": "+10"
"damage_resistances": "radiant"
"senses": "passive Perception 11"
"languages": "Common plus any four languages"
"cr": "7"
"actions":
  - "desc": "The professor makes two Radiant Strike attacks. The professor can replace\
      \ one of the attacks with a use of Spellcasting."
    "name": "Multiattack"
  - "desc": "Melee  or Ranged Spell Attack: +7 to hit, reach 5 ft. or range 120\
      \ ft., one target. Hit: 17 (3d8 + 4) radiant damage. If the target is a\
      \ creature, it must succeed on a DC 15 Constitution saving throw be [blinded](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
      \ until the end of its next turn."
    "name": "Radiant Strike"
  - "desc": "The professor casts one of the following spells, requiring no material\
      \ components and using Charisma as the spellcasting ability (spell save DC 15):\n\
      \nAt will: [dancing lights](03.PlayerLog&Handouts/Mechanics/CLI/spells/dancing-lights.md),\
      \ [friends](03.PlayerLog&Handouts/Mechanics/CLI/spells/friends.md)\n\n2/day\
      \ each: [bless](03.PlayerLog&Handouts/Mechanics/CLI/spells/bless.md), [command](03.PlayerLog&Handouts/Mechanics/CLI/spells/command.md),\
      \ [cure wounds](03.PlayerLog&Handouts/Mechanics/CLI/spells/cure-wounds.md),\
      \ [daylight](03.PlayerLog&Handouts/Mechanics/CLI/spells/daylight.md), [mage\
      \ armor](03.PlayerLog&Handouts/Mechanics/CLI/spells/mage-armor.md)\n\n1/day\
      \ each: [hypnotic pattern](03.PlayerLog&Handouts/Mechanics/CLI/spells/hypnotic-pattern.md),\
      \ [tongues](03.PlayerLog&Handouts/Mechanics/CLI/spells/tongues.md)"
    "name": "Spellcasting"
"source":
  - "SCC"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/humanoid/token/silverquill-professor-of-radiance-scc.webp"
```
^statblock
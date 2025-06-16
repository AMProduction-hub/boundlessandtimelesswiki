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
- Silverquill Professor of Shadow
---
# [Silverquill Professor of Shadow](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\humanoid/silverquill-professor-of-shadow-scc.md)
*Source: Strixhaven: A Curriculum of Chaos p. 215*  

Professors of shadow wield the linguistic magic of Silverquill College through slicing wit and debilitating inky shadow. Whether weaving their magic through spoken incantations and scathing insults or through shadows, these teachers break down the resolve of their foes.

The professors strive to carry themselves as immaculately as possible, seeking to overawe and wrong-foot anyone who would stand against them in debate or in battle. In teaching their students, professors of shadow focus on words that find the tiniest, most invisible cracks in an opponent's defenses and break them.

## Silverquill Scholars

The scholars of Silverquill College study the power of magic shaped through spoken and written words. They use that power either to illuminate and guide or to obscure and demoralize.

```statblock
"name": "Silverquill Professor of Shadow (SCC)"
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
    "desc": "+10"
  - "name": "[Persuasion](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Persuasion)"
    "desc": "+7"
  - "name": "[Stealth](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Stealth)"
    "desc": "+5"
"damage_resistances": "necrotic"
"senses": "darkvision 300 ft., passive Perception 11"
"languages": "Common plus any four languages"
"cr": "7"
"traits":
  - "desc": "Magical darkness doesn't impede the professor's darkvision."
    "name": "Devil's Sight"
"actions":
  - "desc": "The professor makes two Ink Lance attacks. The professor can replace\
      \ one of the attacks with a use of Spellcasting."
    "name": "Multiattack"
  - "desc": "Melee  or Ranged Spell Attack: +7 to hit, reach 5 ft. or range 120\
      \ ft., one target. Hit: 17 (3d8 + 4) necrotic damage. If the target is a\
      \ creature, it must succeed on a DC 15 Constitution saving throw be [blinded](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
      \ until the end of its next turn."
    "name": "Ink Lance"
  - "desc": "The professor casts one of the following spells, requiring no material\
      \ components and using Charisma as the spellcasting ability (spell save DC 15):\n\
      \nAt will: [dancing lights](03.PlayerLog&Handouts/Mechanics/CLI/spells/dancing-lights.md),\
      \ [friends](03.PlayerLog&Handouts/Mechanics/CLI/spells/friends.md)\n\n2/day\
      \ each: [bane](03.PlayerLog&Handouts/Mechanics/CLI/spells/bane.md), [command](03.PlayerLog&Handouts/Mechanics/CLI/spells/command.md),\
      \ [darkness](03.PlayerLog&Handouts/Mechanics/CLI/spells/darkness.md), [mage\
      \ armor](03.PlayerLog&Handouts/Mechanics/CLI/spells/mage-armor.md)\n\n1/day\
      \ each: [tongues](03.PlayerLog&Handouts/Mechanics/CLI/spells/tongues.md)"
    "name": "Spellcasting"
"source":
  - "SCC"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/humanoid/token/silverquill-professor-of-shadow-scc.webp"
```
^statblock
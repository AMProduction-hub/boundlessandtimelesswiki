---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/fleemortals
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/human
- ttrpg-cli/monster/type/humanoid/skirmisher
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Victory Graves"
---
# [Victory Graves](03.PlayerLog&Handouts/Mechanics/CLI/bestiary/npc/victory-graves-fleemortals.md)
*Source: Flee, Mortals! p. 377*  

```statblock
"name": "Victory Graves (FleeMortals)"
"size": "Medium"
"type": "humanoid"
"subtype": "human, Skirmisher"
"alignment": "Neutral Evil"
"ac": !!int "18"
"ac_class": "[studded leather](03.PlayerLog&Handouts/Mechanics/CLI/items/studded-leather-armor.md)"
"hp": !!int "88"
"hit_dice": "16d8 + 16"
"modifier": !!int "6"
"stats":
  - !!int "16"
  - !!int "22"
  - !!int "12"
  - !!int "14"
  - !!int "13"
  - !!int "13"
"speed": "40 ft."
"saves":
  - "dexterity": !!int "9"
  - "intelligence": !!int "5"
"skillsaves":
  - "name": "[Acrobatics](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Acrobatics)"
    "desc": "+9"
  - "name": "[Athletics](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Athletics)"
    "desc": "+6"
  - "name": "[Deception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Deception)"
    "desc": "+4"
  - "name": "[Intimidation](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Intimidation)"
    "desc": "+4"
  - "name": "[Stealth](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Stealth)"
    "desc": "+9"
"senses": "passive Perception 11"
"languages": "Common, thieves' cant, telepathy 120 ft."
"cr": "5"
"traits":
  - "desc": "When Victory makes an attack, she has advantage on the attack roll."
    "name": "Exploit Opening (3/Day)"
  - "desc": "Victory can communicate telepathically with any Amethyst Knife boss regardless\
      \ of distance, provided they are on the same plane of existence."
    "name": "Mind Link"
  - "desc": "When Victory hits a creature with a melee weapon attack, her speed increases\
      \ by a cumulative 5 feet and she gains one additional reaction until the start\
      \ of her next turn."
    "name": "Kinetic Buildup"
  - "desc": "When Victory hits a creature with a Mindrazor attack, she can attempt\
      \ to inflict a psionic wound (no action required). The target must succeed on\
      \ a DC 17 Intelligence saving throw or become vulnerable to psychic damage for\
      \ 1 minute (save ends at end of turn)."
    "name": "Psionic Wound (3/Day)"
"actions":
  - "desc": "Victory makes three Mindrazor attacks and one Cheap Shot attack."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +10 to hit, reach 5 ft., one target. *Hit:*\
      \ 11 (1d8 + 7) piercing damage."
    "name": "Mindrazor"
  - "desc": "*Melee Weapon Attack:* +9 to hit, reach 5 ft., one target. *Hit:* 8\
      \ (1d4 + 6) bludgeoning damage, and the target must make a DC 17 Dexterity\
      \ saving throw. On a failed save, Victory can choose for the target to either\
      \ be knocked [prone](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
      \ or gain one of the following conditions until the end of the target's next\
      \ turn: [blinded](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
      \ [dazed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Dazed), or\
      \ [deafened](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Deafened)."
    "name": "Cheap Shot"
"reactions":
  - "desc": "When Victory is [blinded](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
      \ [charmed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
      \ [dazed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Dazed), [deafened](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
      \ [frightened](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
      \ [paralyzed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
      \ or [stunned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Stunned),\
      \ she chooses a willing Amethyst Knife boss within 60 feet of her who doesn't\
      \ already have the condition or is immune to it. The chosen creature then gains\
      \ the condition for the duration, and Victory loses the condition. She can use\
      \ this reaction even while [incapacitated](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
    "name": "Shared Condition"
"source":
  - "FleeMortals"
```
^statblock
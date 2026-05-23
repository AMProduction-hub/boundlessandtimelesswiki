---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/fleemortals
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/elemental/skirmisher
- ttrpg-cli/monster/type/elemental/water
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Essence of Tides"
---
# [Essence of Tides](03.PlayerLog&Handouts/Mechanics/CLI/bestiary/elemental/essence-of-tides-fleemortals.md)
*Source: Flee, Mortals! p. 93*  

```statblock
"name": "Essence of Tides (FleeMortals)"
"size": "Medium"
"type": "elemental"
"subtype": "water, Skirmisher"
"alignment": "Any alignment"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "84"
"hit_dice": "13d8 + 26"
"modifier": !!int "4"
"stats":
  - !!int "12"
  - !!int "18"
  - !!int "14"
  - !!int "9"
  - !!int "16"
  - !!int "10"
"speed": "15 ft., swim 50 ft."
"skillsaves":
  - "name": "[Acrobatics](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Acrobatics)"
    "desc": "+7"
  - "name": "[Medicine](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Medicine)"
    "desc": "+6"
"damage_resistances": "acid, fire, poison"
"condition_immunities": "[grappled](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [poisoned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [restrained](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Restrained)"
"senses": "[darkvision](03.PlayerLog&Handouts/Mechanics/CLI/rules/senses.md#Darkvision)\
  \ 60 ft., passive Perception 13"
"languages": "Aquan, Common"
"cr": "5"
"traits":
  - "desc": "While within 5 feet of a liquid or solid surface, the essence gains a\
      \ flying speed equal to their swimming speed. While flying, the essence doesn't\
      \ provoke opportunity attacks."
    "name": "Water Glide"
"actions":
  - "desc": "The essence makes two Water Wing attacks and one Lightning Tail Whip\
      \ attack."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 7\
      \ (1d6 + 4) bludgeoning damage. If the same creature is hit twice with this\
      \ attack on a turn, they are vulnerable to lightning damage until the end of\
      \ the essence's turn."
    "name": "Water Wing"
  - "desc": "*Melee Spell Attack:* +6 to hit, reach 15 ft., one target. *Hit:* 7\
      \ (2d6) lightning damage, and the target is pushed up to 10 feet away from\
      \ the essence."
    "name": "Lightning Tail Whip"
"bonus_actions":
  - "desc": "The essence imbues the power of water in themself or another Elemental\
      \ they can see within 30 feet, granting one of the following effects of that\
      \ Elemental's choice:\n\n- **Scalding Steam.** The Elemental spouts blistering\
      \ steam. Each non-Elemental creature within 15 feet of them must make a DC 15\
      \ Constitution saving throw. On a failed save, a target takes 18 (4d8) fire\
      \ damage and is [blinded](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
      \ until the end of their next turn. On a successful save, a target takes half\
      \ as much damage and isn't [blinded](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Blinded).\
      \  \n- **Waters of Vitality.** The Elemental regains 25 hit points and can end\
      \ one of the following conditions affecting them: [blinded](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
      \ [charmed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
      \ [dazed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Dazed), [deafened](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
      \ [paralyzed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
      \ [poisoned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
      \ or [stunned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Stunned).\
      \  "
    "name": "Convocation of Water (1/Day)"
"source":
  - "FleeMortals"
```
^statblock
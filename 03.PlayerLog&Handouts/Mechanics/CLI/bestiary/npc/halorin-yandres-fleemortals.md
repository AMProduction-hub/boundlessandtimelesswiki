---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/fleemortals
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead/soldier
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Halorin Yandres"
---
# [Halorin Yandres](03.PlayerLog&Handouts/Mechanics/CLI/bestiary/npc/halorin-yandres-fleemortals.md)
*Source: Flee, Mortals! p. 351*  

```statblock
"name": "Halorin Yandres (FleeMortals)"
"size": "Medium"
"type": "undead"
"subtype": "Soldier"
"alignment": "Lawful Evil"
"ac": !!int "17"
"ac_class": "[breastplate](03.PlayerLog&Handouts/Mechanics/CLI/items/breastplate.md),\
  \ [shield](03.PlayerLog&Handouts/Mechanics/CLI/items/shield.md)"
"hp": !!int "32"
"hit_dice": "5d8 + 10"
"modifier": !!int "1"
"stats":
  - !!int "16"
  - !!int "13"
  - !!int "14"
  - !!int "10"
  - !!int "12"
  - !!int "10"
"speed": "30 ft."
"saves":
  - "strength": !!int "5"
  - "constitution": !!int "4"
"skillsaves":
  - "name": "[Athletics](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Athletics)"
    "desc": "+5"
  - "name": "[Intimidation](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Intimidation)"
    "desc": "+2"
  - "name": "[Perception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Perception)"
    "desc": "+3"
"gear":
  - "[mace](03.PlayerLog&Handouts/Mechanics/CLI/items/mace.md)"
"senses": "[darkvision](03.PlayerLog&Handouts/Mechanics/CLI/rules/senses.md#Darkvision)\
  \ 60 ft., passive Perception 13"
"languages": "Common, Elvish"
"cr": "1"
"traits":
  - "desc": "Halorin and any Undead within 30 feet of him have advantage on saving\
      \ throws against effects that turn Undead."
    "name": "Aura of Command"
  - "desc": "Halorin regains 5 hit points at the start of his turn if he has at least\
      \ 1 hit point."
    "name": "Pendant of Grave Regeneration"
"actions":
  - "desc": "Halorin makes one Shield Slam attack and one Mace attack. If he hits\
      \ the same creature with both attacks, the target has disadvantage on attack\
      \ rolls against creatures other than Halorin until the end of their next turn."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 6\
      \ (1d6 + 3) bludgeoning damage."
    "name": "Mace"
  - "desc": "*Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 5\
      \ (1d4 + 3) bludgeoning damage, and the target must succeed on a DC 13 Strength\
      \ saving throw or be knocked [prone](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
    "name": "Shield Slam"
"reactions":
  - "desc": "When a willing ally within 5 feet of Halorin is hit by an attack, he\
      \ swaps places with that creature without provoking opportunity attacks and\
      \ is hit by the attack instead. To use this reaction, Halorin must be able to\
      \ see the ally and the attacker."
    "name": "Unyielding Protection"
"source":
  - "FleeMortals"
```
^statblock
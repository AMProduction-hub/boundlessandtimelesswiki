---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/toa
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/half-elf
statblock: inline
statblock-link: "#^statblock"
aliases:
- Xandala
---
# [Xandala](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\npc/xandala-toa.md)
*Source: Tomb of Annihilation p. 236*  

The half-elf sorcerer Xandala has come to Chult in search of the Ring of Winter, an artifact in Artus Cimber's possession. Xandala knows that the ring has kept Artus alive for over a century, and she craves its power. If she meets the characters, Xandala pretends to be Artus's daughter and tries to convince them to help her find him. Her plan is to cast [dominate person](03.PlayerLog&Handouts/Mechanics/CLI/spells/dominate-person.md) on Artus and force him to give her the ring, then escape using her [fly](03.PlayerLog&Handouts/Mechanics/CLI/spells/fly.md) spell.

Xandala's magic traces back to a draconic bloodline, and parts of her skin are covered by a thin sheen of protective scales. She has befriended a pseudodragon named Summerwise, who thinks that Xandala's quest for the ring is dangerous but has given up trying to talk the sorcerer out of it. Summerwise can be turned against Xandala by good-aligned characters.

## Xandala's Traits

### Ideal

"I have the blood of dragons flowing through my veins. I am destined for greatness."

### Bond

"The Ring of Winter will bring me power and immortality."

### Flaw

"I'm surrounded by fools."

```statblock
"name": "Xandala (ToA)"
"size": "Medium"
"type": "humanoid"
"subtype": "half-elf"
"alignment": "Neutral Evil"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "71"
"hit_dice": "11d8 + 22"
"modifier": !!int "0"
"stats":
  - !!int "10"
  - !!int "11"
  - !!int "14"
  - !!int "18"
  - !!int "16"
  - !!int "18"
"speed": "30 ft."
"saves":
  - "intelligence": "+7"
  - "wisdom": "+6"
"skillsaves":
  - "name": "[Arcana](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Arcana)"
    "desc": "+7"
  - "name": "[Deception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Deception)"
    "desc": "+10"
  - "name": "[History](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#History)"
    "desc": "+7"
  - "name": "[Insight](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Insight)"
    "desc": "+6"
  - "name": "[Survival](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Survival)"
    "desc": "+6"
"senses": "passive Perception 13"
"languages": "Common, Draconic, Dwarvish, Elvish, Halfling"
"cr": "7"
"traits":
  - "desc": "Xandala is a 9th-level spellcaster. Her spellcasting ability is Charisma\
      \ (spell save DC 15, +7 to hit with spell attacks). Xandala has the following\
      \ sorcerer spells prepared:\n\nCantrips (at will): [acid splash](03.PlayerLog&Handouts/Mechanics/CLI/spells/acid-splash.md),\
      \ [fire bolt](03.PlayerLog&Handouts/Mechanics/CLI/spells/fire-bolt.md), [light](03.PlayerLog&Handouts/Mechanics/CLI/spells/light.md),\
      \ [mage hand](03.PlayerLog&Handouts/Mechanics/CLI/spells/mage-hand.md), [ray\
      \ of frost](03.PlayerLog&Handouts/Mechanics/CLI/spells/ray-of-frost.md)\n\n\
      1st level (4 slots): [chromatic orb](03.PlayerLog&Handouts/Mechanics/CLI/spells/chromatic-orb.md),\
      \ [feather fall](03.PlayerLog&Handouts/Mechanics/CLI/spells/feather-fall.md),\
      \ [shield](03.PlayerLog&Handouts/Mechanics/CLI/spells/shield.md)\n\n2nd level\
      \ (4 slots): [invisibility](03.PlayerLog&Handouts/Mechanics/CLI/spells/invisibility.md),\
      \ [misty step](03.PlayerLog&Handouts/Mechanics/CLI/spells/misty-step.md)\n\n\
      3rd level (3 slots): [fireball](03.PlayerLog&Handouts/Mechanics/CLI/spells/fireball.md),\
      \ [fly](03.PlayerLog&Handouts/Mechanics/CLI/spells/fly.md)\n\n4th level (3\
      \ slots): [ice storm](03.PlayerLog&Handouts/Mechanics/CLI/spells/ice-storm.md),\
      \ [polymorph](03.PlayerLog&Handouts/Mechanics/CLI/spells/polymorph.md)\n\n5th\
      \ level (1 slots): [dominate person](03.PlayerLog&Handouts/Mechanics/CLI/spells/dominate-person.md)"
    "name": "Spellcasting"
  - "desc": "When she casts a spell that has a casting time of 1 action, Xandala changes\
      \ the casting time to 1 bonus action for that casting."
    "name": "Quickened Spell (3/Day)"
"actions":
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3\
      \ (d6) bludgeoning damage, or 4 (d8) bludgeoning damage when used with two\
      \ hands."
    "name": "Quarterstaff"
"source":
  - "ToA"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/npc/token/xandala-toa.webp"
```
^statblock
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Fellforged"]
---
# [Fellforged](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/fellforged-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 170*  

*A darkly foreboding intelligence glows behind this automaton's eyes, and its joints seep hissing green vapors.*

## Spectral Constructs

Fellforged are the castoffs of gearforged and clockworks production, given foul sentience when the construct bodies attract specters yearning to feel the corporeal world. The clockwork bodies trap the specters, but it gives them physical form. The specters twist the bodies to their own use, sometimes going so far as to destroy the body to harm the living. On rare occasions, other ghostly undead choose to inhabit such constructs, using the constructs as tools to enact their will in the living world at the cost of many of their natural abilities and defenses.

## Soldiers for Vampires

Fellforged often seek out greater undead as their masters. Vampires and liches are favorite leaders, but mummies and darakhul also make suitable commanders.

## Grave Speech

The fellforged's voice is echoing and sepulchral, unnerving most living creatures.

> [!note] Fellforged in Midgard
> 
> Dwarves of Grisal canton create fellforged to fight against undead haunts and spirits and melt them down afterwards, destroying wraiths, ghosts, and other incorporeal undead. The fellforged are also sometimes created by the Emerald Order and other cults seeking to give their evil masters a body and a shape with which to rule.
^fellforged-in-midgard

```statblock
"name": "Fellforged (ToB1-2023)"
"size": "Medium"
"type": "construct"
"alignment": "Lawful Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "135"
"hit_dice": "18d8 + 54"
"stats":
- !!int "14"
- !!int "12"
- !!int "17"
- !!int "12"
- !!int "14"
- !!int "15"
"speed": "30 ft."
"saves":
  "Wisdom": !!int "5"
  "Strength": !!int "5"
"damage_resistances": "acid, cold, fire, lightning"
"damage_immunities": "necrotic, poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": "the languages it knew in life"
"cr": "5"
"traits":
- "desc": "The fellforged doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The fellforged is inhabited and animated by a specter. If the fellforged\
    \ fails a saving throw against an effect that turns undead, the specter is expelled\
    \ into an unoccupied space within 5 feet of the fellforged with the hp total it\
    \ had before it was expelled. The specter otherwise uses the statistics of a specter.\n\
    \nWithout its animating specter, the fellforged becomes dormant for 1 minute then\
    \ crumbles to pieces and is destroyed. The expelled specter can reinhabit the\
    \ dormant fellforged as a bonus action while within 5 feet of the fellforged,\
    \ making it active again and using the specter's current hp as the fellforged's\
    \ hp total."
  "name": "Inhabiting Spirit"
- "desc": "While in sunlight, the fellforged has disadvantage on attack rolls, as\
    \ well as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
"actions":
- "desc": "The fellforged makes two Necrotic Slam attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 9 (2d6\
    \ + 2) bludgeoning damage plus 9 (2d8) necrotic damage. If the target is a\
    \ creature, it must succeed on a DC 14 Constitution saving throw or its hp maximum\
    \ is reduced by an amount equal to the necrotic damage taken. This reduction lasts\
    \ until the target finishes a long rest. The target dies if this effect reduces\
    \ its hp maximum to 0."
  "name": "Necrotic Slam"
"bonus_actions":
- "desc": "The specter within the fellforged strains the construct's body, sending\
    \ broken springs and gears flying. Each creature within 5 feet of the fellforged\
    \ must make a DC 14 Dexterity saving throw, taking 7 (2d6) piercing damage on\
    \ a failed save, or half as much damage on a successful one. Each time the fellforged\
    \ uses this bonus action, its speed is reduced by 5 feet, and it can't use this\
    \ bonus action if its speed is 0. Its speed returns to normal when it finishes\
    \ a long rest."
  "name": "Burst Gears"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/fellforged-tob1-2023.webp"
```
^statblock

## Environment

urban
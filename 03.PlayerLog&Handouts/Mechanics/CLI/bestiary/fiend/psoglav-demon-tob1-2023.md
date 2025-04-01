---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend/demon
statblock: inline
aliases: ["Psoglav Demon"]
---
# [Psoglav Demon](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/psoglav-demon-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 86*  

*An immense creature sniffs at the air, its singular eye glowing with malice.*

## Paid in Souls and Memories

These demonic creations are bred for protection, which they provide for a select few. The price for their guardianship is always high and never in coin. They demand everything from memories to souls in exchange for their services.

## Fond of Trophies

Psoglav demons carry recent kills along with them as grisly toys, and they often wear strings of scalps or ears as trophies. They do not mind the stench, and enjoy gnawing bones as a pastime, the larger and more durable the better.

## Shadow Stealers

The psoglav has a single, menacing eye that is capable of commanding a creature's shadow to separate from its owner and follow the psoglav. The psoglav's command of the shadow is tenuous, however, and the shadow returns to its owner within a few days. Psoglav demons sometimes use this to sow further fear, allowing the shadow to return and letting the victim believe the psoglav has moved on, only for the psoglav to show up days later to finish the kill.

```statblock
"name": "Psoglav Demon (ToB1-2023)"
"size": "Large"
"type": "fiend"
"subtype": "demon"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "115"
"hit_dice": "11d10 + 55"
"stats":
- !!int "21"
- !!int "23"
- !!int "20"
- !!int "16"
- !!int "19"
- !!int "18"
"speed": "40 ft., fly 60 ft."
"saves":
  "Charisma": !!int "7"
  "Dexterity": !!int "9"
  "Wisdom": !!int "7"
  "Constitution": !!int "8"
"skillsaves":
  "Intimidation": !!int "7"
  "Stealth": !!int "9"
  "Perception": !!int "7"
  "Acrobatics": !!int "9"
"damage_resistances": "cold, fire, lightning"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 30 ft., darkvision 60 ft., passive Perception 17"
"languages": "Abyssal, Common, telepathy 60 ft."
"cr": "7"
"traits":
- "desc": "The psoglav has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The psoglav's weapon attacks are magical."
  "name": "Magic Weapons"
"actions":
- "desc": "The psoglav makes three Bite attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 18\
    \ (2d12 + 5) piercing damage."
  "name": "Bite"
- "desc": "The psoglav magically turns [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ until it attacks or uses Shadow-Stealing Ray, or until its [concentration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ ends (as if [concentrating](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ on a spell). Any equipment the psoglav wears or carries is [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ with it."
  "name": "Invisibility"
- "desc": "The psoglav emits a beam from its single eye at one creature it can see\
    \ within 60 feet of it. The target must make a DC 15 Constitution saving throw.\
    \ On a failure, the target is pushed up to 20 feet away from the psoglav, and\
    \ its shadow becomes a creature under the psoglav's control for 24 hours or until\
    \ the shadow is reduced to 0 hp. On a success, the target is pushed up to 10 feet\
    \ away from the psoglav and its shadow isn't stolen. Each controlled shadow uses\
    \ the statistics of a shadow, except it can't create shadows from killing Humanoids.\
    \ The psoglav can have no more than five shadows under its control at a time.\
    \ The shadow becomes permanently under the psoglav's control if the shadow's original\
    \ owner dies.\n\nIf a shadow's original owner died within the past minute, the\
    \ psoglav can command (no action required) the shadow to inhabit and control the\
    \ body, using the owner's statistics, proficiencies, and class features. A shadow\
    \ inhabiting a body in this way can't cast spells or activate magic items the\
    \ owner possessed, and it loses its Amorphous, Shadow [Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth),\
    \ and Sunlight Weakness traits while inhabiting the body. The shadow can inhabit\
    \ or exit the body as a bonus action. The shadow can inhabit the body for up to\
    \ 24 hours after the creature died, after which time it is ejected and can't inhabit\
    \ the body again.\n\nIf a creature's saving throw is successful or its shadow\
    \ is returned to it, the creature is immune to the Shadow-Stealing Ray of all\
    \ psoglav demons for the next 24 hours."
  "name": "Shadow-Stealing Ray (Recharge 5-6)"
"bonus_actions":
- "desc": "While in shadows, dim light, or darkness, the psoglav disappears into the\
    \ darkness and reappears in an unoccupied space it can see within 60 feet."
  "name": "Shadow Jump (3/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/psoglav-demon-tob1-2023.webp"
```
^statblock

## Environment

planar
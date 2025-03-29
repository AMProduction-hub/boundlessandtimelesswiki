---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Ghostwalk Spider"]
---
# [Ghostwalk Spider](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/ghostwalk-spider-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 343*  

*A pasty-white spider the size of a horse slinks through the shadows. It fades from sight with a ghostly blue shimmer.*

Ghostwalk spiders are malevolent hunters that sprang from misguided experiments on phase spiders. They are spindly, emaciated things all but devoid of color. The spider is 8 feet in diameter (including legs) and weighs 500 pounds.

## Phantom Webs

Ghostwalk spiders spin ephemeral webs in secluded areas. They spend most of their time stalking prey to paralyze and drag back to their phantom web. As long as these remains lie tangled in ghostly webs, they go unnoticed by most creatures, but the spiders eventually cast old kills aside. Adventurers are wise to fear empty caves containing unexplained, desiccated remains.

```statblock
"name": "Ghostwalk Spider (ToB1-2023)"
"size": "Large"
"type": "monstrosity"
"alignment": "Neutral Evil"
"ac": !!int "15"
"hp": !!int "119"
"hit_dice": "14d10 + 42"
"stats":
- !!int "15"
- !!int "20"
- !!int "17"
- !!int "9"
- !!int "14"
- !!int "8"
"speed": "50 ft., climb 50 ft."
"saves":
  "Charisma": !!int "3"
  "Dexterity": !!int "9"
"skillsaves":
  "Stealth": !!int "9"
  "Perception": !!int "6"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "truesight 60 ft., passive Perception 16"
"languages": "understands Undercommon but can't speak"
"cr": "9"
"traits":
- "desc": "The ghostwalk spider has resistance to acid, cold, fire, lightning, and\
    \ thunder damage and to bludgeoning, piercing, and slashing damage from nonmagical\
    \ attacks, and it has immunity to the [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
    \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
    \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
    \ and [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ conditions."
  "name": "Ghostly Body (Ghostwalk Form Only)"
- "desc": "The ghostwalk spider can move through other creatures and objects as if\
    \ they were difficult terrain. It takes 5 (1d10) force damage if it ends its\
    \ turn inside an object."
  "name": "Incorporeal Movement (Ghostwalk Form Only)"
- "desc": "The spider can climb difficult surfaces, including upside down on ceilings,\
    \ without needing to make an ability check."
  "name": "Spider Climb"
- "desc": "The spider ignores movement restrictions caused by webbing."
  "name": "Web Walker"
"actions":
- "desc": "The ghostwalk spider makes one Bite attack and one Ghostly Snare attack,\
    \ or it makes two Bite attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 21\
    \ (3d10 + 5) piercing damage. If the ghostwalk spider is in its true form, the\
    \ target must make a DC 15 Constitution saving throw, taking 13 (3d8) poison\
    \ damage on a failed save, or half as much damage on a successful one. If the\
    \ poison damage reduces the target to 0 hp, the target is stable but [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 hour, even after regaining hp, and is [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ while [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way."
  "name": "Bite"
- "desc": "Ranged Weapon Attack: +9 to hit, range 30/60 ft., one target. Hit:\
    \ The target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ webbing. While [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ in this way, the target is [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible).\
    \ As an action, the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ target can make a DC 15 Strength check, bursting the webbing on a success. The\
    \ webbing can also be attacked and destroyed (AC 12; hp 15; immunity to bludgeoning,\
    \ poison, and psychic damage)."
  "name": "Ghostly Snare (Ghostwalk Form Only, Recharge 4-6)"
"bonus_actions":
- "desc": "The ghostwalk spider magically takes on a ghostly form or returns to its\
    \ true, tangible form. Its statistics are the same in each form. Any equipment\
    \ it is wearing or carrying becomes ghostly with it. It reverts to its true form\
    \ if it dies."
  "name": "Ghostwalk"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/ghostwalk-spider-tob1-2023.webp"
```
^statblock

## Environment

underdark
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Monolith Champion"]
---
# [Monolith Champion](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/monolith-champion-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 274*  

*This suit of armor stands motionless, its visor raised to reveal a black skull with eyes cold as a winter moon. A cloak of owl feathers hangs from its shoulders, and a greatsword sits across its back.*

## Beautiful Constructs

Monolithic servitors are constructs designed to serve the courts of the shadow fey. As constructs go, these are uncommonly beautiful; they are meant to be as pleasing to the eyes as they are functional. Beauty, of course, is in the eye of the beholder, and what's beautiful in the eyes of the shadow fey might be considered strange, disturbing, or even alarming to mortal folk.

## Expensive Armor

Regardless of a viewer's aesthetic opinion, it's obvious that a monolith champion incorporates amazing workmanship. Every fitting is perfect, and every surface is burnished and etched with detail almost invisible to the naked eye or else decorated with macabre inlays and precious chasing. The skull in the helmet is mere decoration, meant to frighten the weak of heart and mislead opponents into thinking the champion is some form of undead rather than a pure construct.

## Keeping Out the Rabble

As its name implies, the monolith champion serves as a guardian, warrior, or sentry. In those roles, it never tires, never becomes distracted or bored, never questions its loyalty, and never swerves from its duty. It delights in throwing non-fey visitors out of fey settlements and buildings.

```statblock
"name": "Monolith Champion (ToB1-2023)"
"size": "Large"
"type": "construct"
"alignment": "Neutral"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "102"
"hit_dice": "12d10 + 36"
"stats":
- !!int "19"
- !!int "12"
- !!int "16"
- !!int "10"
- !!int "10"
- !!int "10"
"speed": "40 ft."
"damage_immunities": "poison; psychic; bludgeoning, piercing, slashing from nonmagical\
  \ attacks that aren't adamantine"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Elvish, Umbral"
"cr": "8"
"traits":
- "desc": "The monolith champion's weapon attacks are imbued with blue fey fire and\
    \ magical. When the champion hits with any weapon, the weapon deals an extra 3d8\
    \ cold damage or fire damage (included in the attack), the champion's choice."
  "name": "Coldfire Weapons"
- "desc": "The monolith champion doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
"actions":
- "desc": "The monolith champion makes one Greatsword attack and one Slam attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 18\
    \ (4d6 + 4) slashing damage plus 13 (3d8) cold damage or fire damage (the\
    \ champion's choice). If the target is within a fey court or castle, the target\
    \ must succeed on a DC 14 Charisma saving throw or become [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible),\
    \ silent, and [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ for 1 minute, while an illusory version of the target under the champion's control\
    \ remains visible and audible. The illusion shouts to the target's allies for\
    \ a retreat or similar action. The target can repeat the saving throw at the end\
    \ of each of its turns, ending the effect on itself and destroying the illusory\
    \ double on a success."
  "name": "Greatsword"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) bludgeoning damage plus 13 (3d8) cold damage or fire damage (the\
    \ champion's choice)."
  "name": "Slam"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/monolith-champion-tob1-2023.webp"
```
^statblock

## Environment

planar, urban
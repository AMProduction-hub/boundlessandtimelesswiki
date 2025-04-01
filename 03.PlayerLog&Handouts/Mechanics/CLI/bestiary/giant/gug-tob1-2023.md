---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/giant
statblock: inline
aliases: ["Gug"]
---
# [Gug](03 - Player Log & Handouts\Mechanics\CLI\bestiary\giant/gug-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 225*  

*The giant, four-armed, two-legged creature steps forward, long claws extended. A large toothy mouth splits its torso from shoulders to navel.*

## Underworld Godlings

Gugs are giants of the underworld that enjoy smashing and devouring lesser creatures. Their burbling and grunting speech displays a surprising and malign intelligence to those who can understand it. Gugs are occasionally worshipped by tribes of derro, and their strange underworld cities are filled with esoteric monoliths and constructs.

## Nocturnal Raiders

While gugs were banished into the underworld by forgotten gods long ago, they regularly flout this prohibition by raiding the surface by night. They also spend much time in the Ethereal Plane, and some gug spellcasters travel the planes with entourages of fext or noctiny.

## Prey on Ghouls

Gugs devour ghouls and darakhul as their preferred food. When these are not available, they seem to prefer carrion and particular varieties of psychotropic mushrooms, as well as something that is best described as candied bats.

```statblock
"name": "Gug (ToB1-2023)"
"size": "Huge"
"type": "giant"
"alignment": "Neutral Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "230"
"hit_dice": "20d12 + 100"
"stats":
- !!int "24"
- !!int "10"
- !!int "21"
- !!int "10"
- !!int "8"
- !!int "14"
"speed": "40 ft."
"saves":
  "Charisma": !!int "6"
  "Dexterity": !!int "4"
  "Strength": !!int "11"
  "Constitution": !!int "9"
"skillsaves":
  "Athletics": !!int "11"
  "Stealth": !!int "4"
  "Perception": !!int "3"
"damage_immunities": "poison"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 240 ft., passive Perception 13"
"languages": "Deep Speech, Giant, Undercommon"
"cr": "12"
"traits":
- "desc": "The gug is considered to be a Gargantuan giant for the purpose of determining\
    \ its carrying capacity."
  "name": "Towering Strength"
"actions":
- "desc": "The gug makes two four Grasping Claw attacks, or it makes two Grasping\
    \ Claw attacks and two Stomp attacks. It can replace one Grasping Claw attack\
    \ with a use of Fling or Swallow."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 18\
    \ (2d10 + 7) bludgeoning damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 17) if it is a Large or smaller creature. The gug has four Grasping\
    \ Claws, each of which can grapple only one target."
  "name": "Grasping Claw"
- "desc": "Melee Weapon Attack: +11 to hit, reach 10 ft. Hit: 20 (2d12 + 7)\
    \ bludgeoning damage, and the target must succeed on a DC 17 Strength saving throw\
    \ or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Stomp"
- "desc": "One Large or smaller object held or creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by the gug is thrown up to 60 feet in a random direction and knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ If a thrown target strikes a solid surface, the target takes 3 (1d6) bludgeoning\
    \ damage for every 10 feet it was thrown. If the target is thrown at another creature,\
    \ that creature must succeed on a DC 17 Dexterity saving throw or take the same\
    \ damage and be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Fling"
- "desc": "The gug makes one Grasping Claw attack against a Large or smaller creature\
    \ it is grappling. If the attack hits, the target is also swallowed, and the grapple\
    \ ends. While swallowed, the target is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ and [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ it has total cover against attacks and other effects outside the gug, and it\
    \ takes 14 (4d6) acid damage at the start of each of the gug's turns. A gug\
    \ can have only one creature swallowed at a time.\n\nIf the gug takes 30 damage\
    \ or more on a single turn from the swallowed creature, the gug must succeed on\
    \ a DC 19 Constitution saving throw at the end of that turn or regurgitate the\
    \ creature, which falls [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ in a space within 10 feet of the gug. If the gug dies, a swallowed creature\
    \ is no longer [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by it and can escape from the corpse by using 10 feet of movement, exiting [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Swallow"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/giant/token/gug-tob1-2023.webp"
```
^statblock

## Environment

planar, underdark
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/17
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Urochar"]
---
# [Urochar](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/urochar-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 374*  

*This gigantic crimson leech slithers upright on four muscular tentacles. At the top of its writhing trunk, a great lidless eye glows with baleful orange light, surrounded by quivering, feathered antennae.*

## Underworld Wanderers

Sometimes fearfully called "strangling watchers," the urochar are among the most dreaded monsters of the underworld. They have long plagued the drow, grimlocks, and other humanoids of the deep paths. They seek out death and the dying all the way to the banks of the River Styx.

## Devour the Dying

Urochars feast on the final moments of those caught in their crushing tentacles. Though powerful, urochars are quite passive. They watch the life and death struggles of other creatures and take action only to drink in a dying being's final moments from a nearby crevice or overhang.

## Immortal

Strangling watchers are effectively immortal. Gargantuan specimens in the deepest reaches of the underworld are several millennia old.

```statblock
"name": "Urochar (ToB1-2023)"
"size": "Huge"
"type": "aberration"
"alignment": "Chaotic Evil"
"ac": !!int "19"
"ac_class": "natural armor"
"hp": !!int "256"
"hit_dice": "19d12 + 133"
"stats":
- !!int "24"
- !!int "15"
- !!int "24"
- !!int "14"
- !!int "14"
- !!int "20"
"speed": "40 ft., climb 40 ft."
"saves":
  "Charisma": !!int "11"
  "Dexterity": !!int "8"
  "Wisdom": !!int "8"
  "Constitution": !!int "13"
"skillsaves":
  "Stealth": !!int "8"
  "Perception": !!int "8"
"damage_resistances": "cold; lightning; bludgeoning, piercing, slashing from nonmagical\
  \ attacks that aren't silvered"
"damage_immunities": "thunder"
"condition_immunities": "[frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "truesight 120 ft., passive Perception 18"
"languages": "understands Darakhul and Void Speech but can't speak"
"cr": "17"
"traits":
- "desc": "When the urochar dies, it releases all the fear it consumed in its lifetime\
    \ in a single, mind-rending wave. Each creature within 30 feet of it must succeed\
    \ on a DC 19 Charisma saving throw or be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ creature takes 14 (4d6) psychic damage at the start of each of its turns.\
    \ A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Mind-Rending Death"
- "desc": "The urochar's body is rubbery with few bones, allowing it to easily move\
    \ through any opening large enough for a Medium creature. It can squeeze through\
    \ any opening large enough for a Small creature. The urochar's destination must\
    \ still have suitable room to accommodate its volume."
  "name": "Rubbery Body"
- "desc": "The urochar can climb difficult surfaces, including upside down on ceilings,\
    \ without needing to make an ability check."
  "name": "Spider Climb"
"actions":
- "desc": "The urochar can use its Paralyzing Gaze. It then makes four Tentacle attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +13 to hit, reach 20 ft., one target. Hit: 25\
    \ (4d8 + 7) bludgeoning damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 19) if it is a Large or smaller creature. Until this grapple ends,\
    \ the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ The urochar has four tentacles, each can grapple only one target."
  "name": "Tentacle"
- "desc": "The urochar turns its eerie gaze upon one creature it can see within 60\
    \ feet of it. The target must succeed on a DC 19 Wisdom saving throw or be [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ for 1 minute. The target can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success. If a target's saving throw\
    \ is successful or the effect ends for it, the target is immune to the urochar's\
    \ Paralyzing Gaze for the next 24 hours."
  "name": "Paralyzing Gaze"
- "desc": "Each creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by the urochar must make a DC 19 Strength saving throw. On a failure, a creature\
    \ takes 36 (8d8) bludgeoning damage and can't breathe until the grapple ends.\
    \ On a success, a creature takes half the damage and can still breathe."
  "name": "Strangling Grasp"
"reactions":
- "desc": "The urochar magically teleports, along with any equipment it is wearing\
    \ or carrying, up to 30 feet to an unoccupied space it can see and takes the Hide\
    \ action. Grappled creatures are no longer [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ and don't teleport with it."
  "name": "Hidden Step"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/urochar-tob1-2023.webp"
```
^statblock

## Environment

underdark
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/giant
statblock: inline
aliases: ["Flab Giant"]
---
# [Flab Giant](03 - Player Log & Handouts\Mechanics\CLI\bestiary\giant/flab-giant-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 206*  

*This obese, bell-shaped giant is blemished by ulcers, enlarged veins, and fungal rashes. Though it stumbles about on a pair of short, calloused legs, it moves its weight with dangerous potential.*

## Great Girth

Whether as a result of a centuries-past curse or a gradual adaptation to an easygoing existence, the flab giant is gigantic in width rather than height and almost comical in its simple life. Too obese to effectively grasp weapons in its chubby fingers, a flab giant uses its great mass to deadly effect, overrunning or grabbing opponents and then sitting on them to crush them to death. Its bulk and hardiness allow it to tolerate the blows of struggling victims until they are fully crushed.

## Efficient Foragers

Flab giants are the least active of giant types, spending most of their waking hours resting, napping, and sleeping, and only devote a short period each day to listlessly shuffling about, scrounging for food. Because a flab giant can eat practically anything, it doesn't have to roam far to find enough food to sustain its bulk, and only devote a short period each day to listlessly shuffling about, scrounging for food. Because a flab giant can eat practically anything, it doesn't have to roam far to find enough food to sustain its bulk, and it is rarely found far from its crude lair

## Knotted Skins

Flab giants wear only scraps of clothing made of loosely knotted skins, leaving most of their stretch-marked and discolored skin exposed. Favored pelts include bear and human. A flab giant stands eight to ten feet tall and weighs 2,000 to 2,500 pounds.

```statblock
"name": "Flab Giant (ToB1-2023)"
"size": "Large"
"type": "giant"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "110"
"hit_dice": "13d10 + 39"
"stats":
- !!int "20"
- !!int "6"
- !!int "16"
- !!int "9"
- !!int "13"
- !!int "8"
"speed": "20 ft."
"saves":
  "Constitution": !!int "5"
"skillsaves":
  "Perception": !!int "3"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "passive Perception 13"
"languages": "Common, Dwarvish, Giant"
"cr": "4"
"traits":
- "desc": "A flab giant can't take the Dash action. In addition, a creature attempting\
    \ to grapple, push, or knock the giant [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ has disadvantage on attack rolls and ability checks to do so."
  "name": "Massive Bulk"
"actions":
- "desc": "The giant makes two Slam attacks. If both attacks hit a Medium or smaller\
    \ creature, the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 15)."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d6 + 5) bludgeoning damage."
  "name": "Slam"
- "desc": "One creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by the flab giant must make a DC 15 Strength saving throw. On a failure, a creature\
    \ takes 22 (5d6 + 5) bludgeoning damage and is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ until the grapple ends. On a success, a creature takes half the damage and isn't\
    \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ but it remains [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ until it escapes. While [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ a creature takes 8 (1d6 + 5) bludgeoning damage at the start of each of the\
    \ giant's turns. If the flab giant moves, the target is no longer [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ or [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)."
  "name": "Squatting Pin"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/giant/token/flab-giant-tob1-2023.webp"
```
^statblock

## Environment

forest
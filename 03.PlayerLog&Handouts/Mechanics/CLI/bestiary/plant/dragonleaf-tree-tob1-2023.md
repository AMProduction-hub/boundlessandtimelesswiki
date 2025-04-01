---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/plant
statblock: inline
aliases: ["Dragonleaf Tree"]
---
# [Dragonleaf Tree](03 - Player Log & Handouts\Mechanics\CLI\bestiary\plant/dragonleaf-tree-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 137*  

*The dragon-headed leaves of these oak trees sometimes rustle despite a lack of wind, betraying a hint that they're more than they seem.*

## Gifts among Dragons

These magnificent trees are imbued with some characteristics of their draconic masters. While most groves consist of only one type of dragonleaf tree, dragons sometimes make gifts of them to cement a pact or as a show of fealty. The dragon giving the tree relinquishes command of the plant as part of the deal. This accounts for mixed groves belonging to especially powerful dragon lords.

## Silent Guardians

Dragonleaf trees use fairly simple tactics to deter potential intruders into their masters' lairs. They remain motionless or allow the breeze to jostle their leaves to appear inconspicuous. Once enough intruders enter the grove, the trees fire razor sharp leaves or rain elemental energies upon the intruders, adjusting their position to make better use of their weapons.

## Long Memories

Dragonleaf trees live up to 1,000 years. They stand 15 feet tall and weigh 3,000 pounds, but ancient specimens can reach heights of 45 feet. Growing a new dragonleaf tree requires a cutting from an existing tree at least 50 years old, which the tree's draconic master imbues with power, sacrificing the use of its breath weapon for a month. While this time barely registers on a dragon's whole lifespan, it still carefully considers the creation of a new tree, for fear that others might discover its temporary weakness.

> [!note] Dragonleaf Trees in Midgard
> 
> The finest druidic minds in the Mharoti Empire created these trees for the draconic lords of the land. Once the druids had shown the dragons the secret of the tree's creation, they were slain so that the secret would not spread. A handful of human and kobold gardeners know how to tend them and make them thrive, but little more.
^dragonleaf-trees-in-midgard

```statblock
"name": "Dragonleaf Tree (ToB1-2023)"
"size": "Large"
"type": "plant"
"alignment": "Unaligned"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "152"
"hit_dice": "16d10 + 64"
"stats":
- !!int "16"
- !!int "14"
- !!int "19"
- !!int "5"
- !!int "12"
- !!int "17"
"speed": "15 ft."
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened)"
"senses": "blindsight 120 ft., passive Perception 11"
"languages": "understands Draconic but can't speak"
"cr": "8"
"traits":
- "desc": "The dragonleaf tree has immunity to a type of damage based on the type\
    \ of dragon that grew it: acid (black, copper), cold (silver, white), fire (brass,\
    \ gold, red), lightning (blue, bronze), or poison (green)."
  "name": "Elemental Affinity"
- "desc": "The dragonleaf tree has advantage on ability checks and saving throws against\
    \ influence or effects that would encourage it or force it to act against its\
    \ draconic master. If [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ or controlled and directed to act against its master, the tree can immediately\
    \ repeat the effect's saving throw, ending the effect on itself on a success."
  "name": "Eternally Loyal"
"actions":
- "desc": "The dragon leaf tree makes three Slam or Throw Leaves attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 12\
    \ (2d8 + 3) bludgeoning damage plus 7 (2d6) damage of the type noted in the\
    \ Elemental Affinity trait."
  "name": "Slam"
- "desc": "Ranged Weapon Attack: +5 to hit, range 30/120 ft., one target. Hit:\
    \ 12 (4d4 + 2) slashing damage plus 7 (2d6) damage of the type noted in the\
    \ Elemental Affinity trait."
  "name": "Throw Leaves"
- "desc": "The dragonleaf tree's leaves rain acid, shed bolts of lightning, shake\
    \ loose icicles, or similarly emit the elemental energies of the dragon that grew\
    \ the tree. Each creature within 20 feet of the dragonleaf tree must make a DC\
    \ 15 Dexterity saving throw, taking 42 12d6 damage of the type noted in the\
    \ Elemental Affinity trait."
  "name": "Elemental Leaves (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/plant/token/dragonleaf-tree-tob1-2023.webp"
```
^statblock

## Environment

any
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/monstrosity/shapechanger
statblock: inline
aliases: ["Map Mimic"]
---
# [Map Mimic](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/map-mimic-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 269*  

*A treasure map flaps as if caught in a strong wind. It suddenly splits open, revealing a fanged mouth and face.*

## Mimic Spawn

Mimic adhesive is not just a powerful means of trapping prey, it also contains millions of microscopic larvae that feed on flesh. Most of the larvae are consumed by the mimic when it eats. Mimics are either unaware of this, or they're indifferent to the fact that they routinely cannibalize their own offspring. A few larvae survive by adhering to the clothing or equipment of someone who escaped from a full-grown mimic's attack. These larvae hitch a ride, their host taking them far from the dungeon, cavern, or ruin of their birth. There, they drop off and grow into wormlike mimic young called map mimics. In time, map mimics grow into typical mimics.

## Smaller than a Dinner Plate

Map mimics are too small to mimic the types of objects their parent does, but they still deceive prey by altering their forms. They can assume the shape, texture, and coloration of anything up to the size of a dinner plate.

## Paper Scrolls

Their preferred form is parchment paper. They can display the path they've followed on their hide, complete with important landmarks. In this form, they curl up and wait inside bottles, or in the clutches of a corpse in plain view, until an unsuspecting adventurer discovers them. If the mimic is hungry, it attacks and attaches to the finder's face. Otherwise, it continues its charade as a map, eventually leading the reader back to the parent mimic.

```statblock
"name": "Map Mimic (ToB1-2023)"
"size": "Tiny"
"type": "monstrosity"
"subtype": "shapechanger"
"alignment": "Neutral"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "22"
"hit_dice": "5d4 + 10"
"stats":
- !!int "7"
- !!int "15"
- !!int "14"
- !!int "5"
- !!int "13"
- !!int "16"
"speed": "30 ft., fly 15 ft."
"damage_immunities": "acid"
"condition_immunities": "[prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": ""
"cr": "1/4"
"traits":
- "desc": "While the mimic remains motionless, it is indistinguishable from an ordinary\
    \ object."
  "name": "False Appearance (Object Form Only)"
- "desc": "Regardless of the form it takes, the map mimic can make a map on its surface\
    \ (no action required) that shows the route it has traveled since it left its\
    \ parent mimic. The map shows terrain features and landmarks of where it has been,\
    \ but doesn't show the names of those places."
  "name": "Life Path"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6\
    \ + 2) bludgeoning damage, and it attaches to the target. While attached, the\
    \ mimic can't attack, the target is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
    \ and at the start of each of the mimic's turns, the target takes 5 (1d6 + 2)\
    \ bludgeoning damage.\n\nThe attached mimic moves with the target whenever the\
    \ target moves, requiring none of the mimic's movement. It can detach itself by\
    \ spending 5 feet of its movement on its turn. A creature, including the target,\
    \ can use its action to detach the mimic by succeeding on a DC 8 Strength check."
  "name": "Pseudopod"
"bonus_actions":
- "desc": "The mimic transforms into a Tiny object or back into its true, amorphous\
    \ form. Its statistics are the same in each form. Any equipment it is wearing\
    \ or carrying isn't transformed. It reverts to its true form if it dies."
  "name": "Change Shape"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/map-mimic-tob1-2023.webp"
```
^statblock

## Environment

underdark, urban
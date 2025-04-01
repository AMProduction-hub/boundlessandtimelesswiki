---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/monstrosity/shapechanger
statblock: inline
aliases: ["Dune Mimic"]
---
# [Dune Mimic](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/dune-mimic-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 268*  

*The sand surges and shifts, a sinkhole opens, and sandy tendrils reach out.*

## Enormous Forms

Though most commonly seen as dunes, a dune mimic can take the form of a date palm grove, a riverbank, an enormous boulder, or other large shapes in the landscape.

## A King's Guardians

Dune mimics were created by a forgotten king as guardians for his desert tomb. Somewhere, dozens of them guard vast wealth.

## Spread by Spores

Although not intended to reproduce, they began producing spores spontaneously and replicating themselves. Now they are spread across the deserts. Luckily for the other inhabitants, dune mimics reproduce just once per century

```statblock
"name": "Dune Mimic (ToB1-2023)"
"size": "Huge"
"type": "monstrosity"
"subtype": "shapechanger"
"alignment": "Neutral"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "168"
"hit_dice": "16d12 + 64"
"stats":
- !!int "20"
- !!int "8"
- !!int "18"
- !!int "9"
- !!int "13"
- !!int "10"
"speed": "15 ft."
"skillsaves":
  "Perception": !!int "4"
"damage_immunities": "acid, fire"
"condition_immunities": "[prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "darkvision 60 ft., tremorsense 30 ft., passive Perception 14"
"languages": ""
"cr": "8"
"traits":
- "desc": "The dune mimic adheres to anything that touches it. A creature adhered\
    \ to the dune mimic is also [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by it (escape DC 15). Ability checks made to escape this grapple have disadvantage.\
    \ The dune mimic can harden its outer surface, so only the creatures it chooses\
    \ are affected by this trait."
  "name": "Adhesive (Object or Terrain Form Only)"
- "desc": "While the dune mimic remains motionless, it is indistinguishable from an\
    \ ordinary sandy object or terrain feature."
  "name": "False Appearance (Object or Terrain Form Only)"
- "desc": "The dune mimic has advantage on attack rolls against any creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by it."
  "name": "Grappler"
"actions":
- "desc": "The dune mimic makes three Pseudopod attacks. It can replace one attack\
    \ with a use of Engulf."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 15 ft., one target. Hit: 18\
    \ (3d8 + 5) bludgeoning damage. If the dune mimic is in object or terrain form,\
    \ the target is subjected to the mimic's Adhesive trait."
  "name": "Pseudopod"
- "desc": "The dune mimic engulfs a Large or smaller creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by it. The engulfed target is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
    \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and unable to breathe, and it must succeed on a DC 15 Constitution saving throw\
    \ at the start of each of the mimic's turns or take 10 (3d6) slashing damage,\
    \ as the creature is lacerated by the mimic's sand-coated form. If the mimic moves,\
    \ any engulfed creatures move with it. The mimic can have no more than two creatures\
    \ engulfed at a time."
  "name": "Engulf"
"bonus_actions":
- "desc": "The dune mimic transforms into a Huge sand- or gravel-covered object, shapes\
    \ itself into a sandy or rocky terrain feature no larger than a 20-foot cube or\
    \ transforms back into its true, amorphous form. Its statistics are the same in\
    \ each form. Any equipment it is wearing or carrying isn't transformed. It reverts\
    \ to its true form if it dies."
  "name": "Change Shape"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/dune-mimic-tob1-2023.webp"
```
^statblock

## Environment

desert
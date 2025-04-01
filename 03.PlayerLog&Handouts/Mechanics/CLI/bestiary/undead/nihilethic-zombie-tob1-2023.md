---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Nihilethic Zombie"]
---
# [Nihilethic Zombie](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/nihilethic-zombie-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 9*  

*Eons ago, a group of aboleth left the Material Plane to wander through distant planes—seeing them through magical scrying was not enough, so these aboleth used astral magic and bodily travel to see far beyond normal realms*.

## A Forgotten Tribe

As ages passed, memories of those who departed slowly faded from the minds of those aboleth who remained behind. Those few aboleth who did remember that long ago some of their kin had gone plane-wandering assumed that the wanderers died in distant hells or paradises.

## Changed by Planar Wandering

The plane-wanderers hadn't died. Instead, their eons-long exposure to alien realms and the space between changed them, restructuring their life force, making them into something even more nightmarish—but better able to withstand both strange hells and golden realms of eldritch delight. They returned even more corrupt and powerful than when left, and these wandering nihileths returned to the mortal world intent on spreading the influence of the Void and the utter evil they found in the vast darkness between worlds.

## Undead Servitors

Humanoids, giants, and monstrosities that succumb to the nihileth's disease transform into servitors for the twisted aboleths. Most humanoids transform into nihilethic zombies, while the larger giants and monstrosities transform into nihilethic dominators. While the creatures retain much of the general shape they had in life, these servitors have translucent and slimy skin, and are adept swimmers, able to function in water or on land in service to their nihileth masters.

```statblock
"name": "Nihilethic Zombie (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "8"
"hp": !!int "37"
"hit_dice": "5d8 + 15"
"stats":
- !!int "13"
- !!int "6"
- !!int "16"
- !!int "3"
- !!int "6"
- !!int "5"
"speed": "20 ft., swim 30 ft."
"saves":
  "Wisdom": !!int "0"
"damage_immunities": "cold, necrotic, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 8"
"languages": "understands Void Speech and the languages it knew in life but can't\
  \ speak"
"cr": "1"
"traits":
- "desc": "The nihilethic zombie has resistance to bludgeoning, piercing, and slashing\
    \ damage from nonmagical attacks. In addition, the zombie can move through other\
    \ creatures and objects as if they were difficult terrain. It takes 5 (1d10)\
    \ force damage if it ends its turn inside an object."
  "name": "Ghostly Body (Void Ghost Form Only)"
- "desc": "If damage reduces the nihilethic zombie to 0 hp, it must make a Constitution\
    \ saving throw with a DC of 5 + the damage taken, unless the damage is radiant\
    \ or from a critical hit. On a success, the zombie drops to 1 hp instead."
  "name": "Undead Fortitude"
- "desc": "The nihilethic zombie doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6\
    \ + 1) bludgeoning damage plus 7 (2d6) necrotic damage."
  "name": "Slam (Undead Form Only)"
- "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 8 (2d6\
    \ + 1) necrotic damage."
  "name": "Withering Touch (Void Ghost Form Only)"
"bonus_actions":
- "desc": "The nihilethic zombie magically transforms into a dark purple, Void ghost\
    \ form or back into its Undead form. Its statistics, other than its speed and\
    \ resistances, are the same in each form. Any equipment it is wearing or carrying\
    \ changes with it. It reverts to its Undead form of it dies."
  "name": "Void Shape"
"reactions":
- "desc": "When the nihilethic zombie's controlling nihileth takes damage while within\
    \ 30 feet of the zombie, the zombie can send its life force to the nihileth. The\
    \ zombie's hp is reduced by up to the amount of damage the nihileth took, preventing\
    \ that amount of damage to the nihileth. If this damage reduces the zombie to\
    \ 0 hp, it is immediately destroyed. A nihileth can benefit from only one zombie's\
    \ Sacrifice Life for each source of damage it takes."
  "name": "Sacrifice Life"
- "desc": "When the nihilethic zombie takes damage that isn't radiant, it can reduce\
    \ the damage by 1d12."
  "name": "Void Body"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/nihilethic-zombie-tob1-2023.webp"
```
^statblock

## Environment

coastal, underdark, underwater
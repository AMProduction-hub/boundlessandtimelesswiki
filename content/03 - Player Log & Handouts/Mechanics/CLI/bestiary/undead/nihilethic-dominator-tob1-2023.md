---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Nihilethic Dominator"]
---
# [Nihilethic Dominator](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/nihilethic-dominator-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 10*  

*Eons ago, a group of aboleth left the Material Plane to wander through distant planes—seeing them through magical scrying was not enough, so these aboleth used astral magic and bodily travel to see far beyond normal realms*.

## A Forgotten Tribe

As ages passed, memories of those who departed slowly faded from the minds of those aboleth who remained behind. Those few aboleth who did remember that long ago some of their kin had gone plane-wandering assumed that the wanderers died in distant hells or paradises.

## Changed by Planar Wandering

The plane-wanderers hadn't died. Instead, their eons-long exposure to alien realms and the space between changed them, restructuring their life force, making them into something even more nightmarish—but better able to withstand both strange hells and golden realms of eldritch delight. They returned even more corrupt and powerful than when left, and these wandering nihileths returned to the mortal world intent on spreading the influence of the Void and the utter evil they found in the vast darkness between worlds.

## Undead Servitors

Humanoids, giants, and monstrosities that succumb to the nihileth's disease transform into servitors for the twisted aboleths. Most humanoids transform into nihilethic zombies, while the larger giants and monstrosities transform into nihilethic dominators. While the creatures retain much of the general shape they had in life, these servitors have translucent and slimy skin, and are adept swimmers, able to function in water or on land in service to their nihileth masters.

```statblock
"name": "Nihilethic Dominator (ToB1-2023)"
"size": "Large"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "82"
"hit_dice": "11d8 + 33"
"stats":
- !!int "16"
- !!int "8"
- !!int "16"
- !!int "3"
- !!int "6"
- !!int "7"
"speed": "30 ft., swim 30 ft."
"damage_immunities": "cold, necrotic, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 8"
"languages": "understands Void Speech and the languages it knew in life but can't\
  \ speak"
"cr": "5"
"traits":
- "desc": "The nihilethic dominator has resistance to bludgeoning, piercing, and slashing\
    \ damage from nonmagical attacks. In addition, the dominator can move through\
    \ other creatures and objects as if they were difficult terrain. It takes 5 (1d10)\
    \ force damage if it ends its turn inside an object."
  "name": "Ghostly Body (Void Ghost Form Only)"
- "desc": "If damage reduces the nihilethic dominator to 0 hp, it must make a Constitution\
    \ saving throw with a DC of 5 + the damage taken, unless the damage is radiant\
    \ or from a critical hit. On a success, the dominator drops to 1 hp instead."
  "name": "Undead Fortitude"
- "desc": "The nihilethic dominator doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The nihilethic dominator makes three Claw attacks, or it makes two Tendril\
    \ of the Void attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d8 + 3) slashing damage. If the target is a creature, it must succeed on\
    \ a DC 14 Strength saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Claw (Undead Form Only)"
- "desc": "Melee Weapon Attack: +6 to hit, reach 10 ft., one creature. Hit:\
    \ 7 (1d8 + 3) cold damage plus 7 (2d6) necrotic damage."
  "name": "Tendril of the Void (Void Ghost Form Only)"
"bonus_actions":
- "desc": "The nihilethic dominator magically transforms into a dark purple, Void\
    \ ghost form or back into its Undead form. Its statistics, other than its speed\
    \ and resistances, are the same in each form. Any equipment it is wearing or carrying\
    \ changes with it. It reverts to its Undead form of it dies."
  "name": "Void Shape"
"reactions":
- "desc": "When the nihilethic dominator takes damage that isn't radiant, it can reduce\
    \ the damage by 1d12."
  "name": "Void Body"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/nihilethic-dominator-tob1-2023.webp"
```
^statblock

## Environment

coastal, underdark, underwater
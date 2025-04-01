---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/fiend
statblock: inline
aliases: ["Herald of Blood"]
---
# [Herald of Blood](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/herald-of-blood-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 232*  

*The giant has bruised, purple skin and wart-like blood blisters that deform its features. It wears cowled robes, and its staff is ebony and mithral embedded with precious stones.*

As powerful sorcerers and blood mages, heralds of blood are without peer. They enjoy enslaving ogres and giants whenever possible, though they make do with lesser slaves when they must.

## Dark Prophets

Their stirring speeches proclaim that the end times are fast approaching and that all must prepare for a bloody reckoning. Their charismatic preaching serves various elder earthly gods, who demand blood sacrifices, and dark druid orders devoted to hunting and murdering innocents. They have the power to grant strength, lust, and vitality—or to wither those who cross them.

## Blood Magic Vortexes

Beneath their giant-like veneer, heralds of blood are swirling vortexes of blood, bone, and raw magical power. They feed on ley line magic and the black blood of the earth as much as on flesh and blood.

```statblock
"name": "Herald of Blood (ToB1-2023)"
"size": "Huge"
"type": "fiend"
"alignment": "Neutral Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "184"
"hit_dice": "16d12 + 80"
"stats":
- !!int "22"
- !!int "12"
- !!int "20"
- !!int "14"
- !!int "17"
- !!int "16"
"speed": "30 ft., fly 50 ft., swim 30 ft."
"saves":
  "Wisdom": !!int "7"
  "Strength": !!int "10"
  "Constitution": !!int "9"
"skillsaves":
  "Perception": !!int "7"
  "Arcana": !!int "10"
"damage_resistances": "cold, fire, lightning"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 240 ft., passive Perception 17"
"languages": "Common, Draconic, Infernal, Void Speech"
"cr": "12"
"traits":
- "desc": "Each time a creature with blood hits the herald with a melee attack while\
    \ within 10 feet of the herald, the creature takes 4 (1d8) necrotic damage,\
    \ and the herald's AC increases by 1 until the end of its next turn. The herald's\
    \ AC can't be increased to more than 20 from this trait."
  "name": "Blood Armor"
"actions":
- "desc": "The herald makes three Herald's Staff or Blood Bolt attacks, or it makes\
    \ two Herald's Staff attacks and one Grasping Slam attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 13\
    \ (2d6 + 6) bludgeoning damage plus 13 (3d8) necrotic damage."
  "name": "Herald's Staff"
- "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 17\
    \ (2d10 + 6) bludgeoning damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 17) if it is a Large or smaller creature. Until this grapple ends,\
    \ the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ and takes 9 (2d8) necrotic damage at the start of each of its turns, and the\
    \ herald can't use its Grasping Slam on another target."
  "name": "Grasping Slam"
- "desc": "Ranged Spell Attack: +7 to hit, range 120 ft., one target. Hit: 25\
    \ (5d8 + 3) necrotic damage. If the target is a creature with blood, it must\
    \ succeed on a DC 17 Constitution saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn."
  "name": "Blood Bolt"
- "desc": "Each creature with blood within 10 feet of the herald must make a DC 17\
    \ Constitution saving throw, taking 45 (10d8) necrotic damage on a failed save,\
    \ or half as much damage on a successful one. The herald then gains temporary\
    \ hp equal to the single highest amount of necrotic damage dealt. A creature that\
    \ fails the saving throw by 5 or more also suffers one level of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)."
  "name": "Call Blood (Recharge 5-6)"
"bonus_actions":
- "desc": "The herald of blood infuses reckless rage in one creature it can see within\
    \ 60 feet of it that isn't a Construct or Undead. The target must succeed on a\
    \ DC 17 Constitution saving throw or be enraged for a number of rounds equal to\
    \ the target's Constitution modifier. While enraged, the target has advantage\
    \ on all melee attack rolls, and attack rolls against it have advantage. When\
    \ the rage ends, the target takes 13 (3d8) necrotic damage and suffers one level\
    \ of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion).\
    \ A creature with any levels of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)\
    \ automatically succeeds on this saving throw."
  "name": "Grant Blood Rage"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/herald-of-blood-tob1-2023.webp"
```
^statblock

## Environment

any
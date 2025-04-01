---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Deep Drake"]
---
# [Deep Drake](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/deep-drake-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 142*  

*This large, unnerving drake's glassy black scales have purple undertones. Its features are elongated and almost alien. Black, expressionless eyes stare ahead, and a barbed stinger sits at the end of a long tail*.

## Friend to Ghouls

The deep drake has made a niche for itself in subterranean realms, establishing trade with the darakhul and with other races of the underworld. The drakes' poison ensures the ghouls have replacements when their population dwindles. In return, those underlings who fail their rulers become food for the drake.

## Love Darkness

Deep drakes are 12 feet long, plus a three-foot long tail, and weigh up to 1,500 pounds. Their coloration makes them ideal predators in the subterranean dark. They love life underground, and they feel a kinship with the aberrations and undead residing there. They avoid sunlight and are strictly nocturnal when on the surface.

## Few in Number

A deep drake mates for life with another deep drake when two of these rare creatures meet. A hermaphroditic creature, the drake assumes a gender until it finds a mate, at which time it may change. Once every 10–20 years, the drakes reproduce, resulting in three or four threefoot long, rubbery eggs. Occasionally, subterranean undead or aberrations take these eggs to their cities to train the young drakes. A "household drake" is a great status symbol in some deep places, and surface necromancers who have heard of them are often eager to acquire one.

```statblock
"name": "Deep Drake (ToB1-2023)"
"size": "Large"
"type": "dragon"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "150"
"hit_dice": "20d10 + 40"
"stats":
- !!int "21"
- !!int "19"
- !!int "14"
- !!int "11"
- !!int "14"
- !!int "12"
"speed": "40 ft., climb 30 ft., fly 80 ft."
"saves":
  "Dexterity": !!int "8"
  "Constitution": !!int "6"
"skillsaves":
  "Athletics": !!int "9"
  "Insight": !!int "6"
  "Perception": !!int "6"
"damage_immunities": "necrotic"
"condition_immunities": "[paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)"
"senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 16"
"languages": "Common, Darakhul, Draconic, Undercommon"
"cr": "9"
"traits":
- "desc": "The drake has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "While in sunlight, the drake has disadvantage on attack rolls, as well\
    \ as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
"actions":
- "desc": "The drake makes one Bite attack, two Claw attacks, and one Stinger attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 16\
    \ (2d10 + 5) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft, one target. Hit: 12 (2d6\
    \ + 5) slashing damage."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 16\
    \ (2d10 + 5) piercing damage plus 7 (2d6) poison damage, and the target must\
    \ succeed on a DC 16 Constitution saving throw or become [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature must repeat the saving throw at the end of each of its turns. On a\
    \ failure, the creature takes 7 (2d6) poison damage. On a success, the condition\
    \ ends. When animate dead is cast on one or more creatures killed by this poison,\
    \ the spellcaster requires no material components and can cast the spell as an\
    \ action."
  "name": "Stinger"
- "desc": "The deep drake exhales pain-inducing, purple-black energy in a 90-foot\
    \ line that is 5 feet wide. Each creature in the line must make a DC 16 Dexterity\
    \ saving throw. On a failure, a creature takes 35 (10d6) necrotic damage and\
    \ is [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the end of its next turn. On a success, a creature takes half the damage\
    \ and isn't [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)."
  "name": "Enervating Breath (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/deep-drake-tob1-2023.webp"
```
^statblock

## Environment

underdark
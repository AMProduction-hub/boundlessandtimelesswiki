---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Sarcophagus Slime"]
---
# [Sarcophagus Slime](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/sarcophagus-slime-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 316*  

*The sarcophagus opens to reveal an eerie, scintillating light. Wisps of gelid amber ectoplasm undulate outward from a quivering mass with a blackened skull at its center.*

## Vigilant Slime

Sarcophagus slimes are amorphous undead guardians placed in the tombs of the powerful to guard them and to wreak terrible vengeance on would-be defilers of the ancient crypts. The slimes seethe with baleful energy, and their blackened skulls retain a simple watchfulness.

## Muddled Origins

Many sages speculate that the first sarcophagus slime was spawned accidentally, in a mummy creation ritual that gave life to the congealed contents of canopic jars rather than the intended, mummified body. Others maintain sarcophagus slime was created by a powerful necromancer-pharaoh bent on formulating the perfect alchemical sentry to guard his crypt.

## Death to Tomb Robbers

These ectoplasmic slimes are the bane of burglars and a constant danger for excavators and antiquarians exploring ruins or tombs. The rituals for their creation have not been entirely lost; modern necromancers still create these undead abominations for their own fell purposes, and tomb robbers are turned into slimes if they lack proper caution.

```statblock
"name": "Sarcophagus Slime (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "11"
"hp": !!int "102"
"hit_dice": "12d8 + 48"
"stats":
- !!int "14"
- !!int "12"
- !!int "18"
- !!int "3"
- !!int "12"
- !!int "12"
"speed": "20 ft."
"saves":
  "Charisma": !!int "4"
  "Wisdom": !!int "4"
"damage_resistances": "acid, necrotic"
"damage_immunities": "poison"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 11"
"languages": ""
"cr": "5"
"traits":
- "desc": "The sarcophagus slime can move through a space as narrow as 1 inch wide\
    \ without squeezing."
  "name": "Amorphous"
- "desc": "The sarcophagus slime doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The sarcophagus slime can use its Frightful Presence. It then makes two\
    \ Slam attacks. It can replace one Slam attack with a use of Corrupting Gaze."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 9 (2d6\
    \ + 2) bludgeoning damage plus 9 (2d8) acid damage."
  "name": "Slam"
- "desc": "One creature the sarcophagus slime can see within 30 feet of it must make\
    \ a DC 15 Constitution saving throw, taking 18 (4d8) necrotic damage on a failed\
    \ save, or half as much damage on a successful one. The target's hp maximum is\
    \ reduced by an amount equal to the damage taken. This reduction lasts until the\
    \ target finishes a long rest. The target dies if this effect reduces its hp maximum\
    \ to 0. A Humanoid slain by this effect rises 24 hours later as a sarcophagus\
    \ slime, unless the Humanoid is restored to life or its body is destroyed."
  "name": "Corrupting Gaze"
- "desc": "Each creature of the sarcophagus slime's choice that is within 60 feet\
    \ of the sarcophagus slime and aware of it must succeed on a DC 15 Wisdom saving\
    \ throw or become [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. A creature can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success. If a creature's saving throw\
    \ is successful or the effect ends for it, the creature is immune to the sarcophagus\
    \ slime's Frightful Presence for the next 24 hours."
  "name": "Frightful Presence"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/sarcophagus-slime-tob1-2023.webp"
```
^statblock

## Environment

underdark, urban
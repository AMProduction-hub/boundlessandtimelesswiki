---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/badlands
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Qwyllion"]
---
# [Qwyllion](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/qwyllion-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 298*  

*The reeking creature resembles a toothless, cadaverous hag. Its large eyes glow with unearthly green light, and ragged claws extend from its fingers.*

## Twisted Nymphs

Qwyllion (the name means "polluter" in Old Elvish) are fey who have been twisted by the corrupted magic of magical wastelands or warped by alchemical experiments into baleful versions of their former selves.

## Frighten Animals

Besides making them hideously ugly, the transformation leaves them with a deadly gaze and the ability to control a living creature with a mere glance. Most animals can sense the corruption within the fey and refuse to approach it.

## Goblin Mercenaries

Qwyllion are sometimes engaged by goblin sorcerers and evil mages to guard desecrated temples and despoiled gardens. The terms and payments for these arrangements vary wildly from one qwyllion to the next. Anyone who dares to employ a qwyllion must be constantly vigilant, because these creatures are prone to renege on any agreement eventually.

```statblock
"name": "Qwyllion (ToB1-2023)"
"size": "Medium"
"type": "aberration"
"alignment": "Neutral Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "110"
"hit_dice": "13d8 + 52"
"stats":
- !!int "12"
- !!int "20"
- !!int "19"
- !!int "12"
- !!int "13"
- !!int "16"
"speed": "30 ft."
"saves":
  "Charisma": !!int "6"
  "Dexterity": !!int "8"
"skillsaves":
  "Perception": !!int "4"
  "Acrobatics": !!int "11"
"damage_resistances": "acid; fire; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Common, Goblin, Infernal, Sylvan, Void Speech"
"cr": "8"
"traits":
- "desc": "A creature that starts its turn within 20 feet of the qwyllion must succeed\
    \ on a DC 15 Constitution saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature that fails this saving throw is also [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ while [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way. A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success. If a creature's saving throw is successful\
    \ or the effect ends for it, the creature is immune to the qwyllion's Nauseating\
    \ Stench for the next 24 hours."
  "name": "Nauseating Stench"
"actions":
- "desc": "The qwyllion makes three Claw or Deadly Gaze attacks. If two Deadly Gaze\
    \ attacks hit one creature, the target must succeed on a DC 15 Constitution saving\
    \ throw or be [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ until the end of its next turn."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 18\
    \ (3d8 + 5) slashing damage."
  "name": "Claw"
- "desc": "Ranged Spell Attack: +6 to hit, range 60 ft., one target. Hit: 17\
    \ (4d6 + 3) psychic damage. A Humanoid slain by this attack rises 8 hours later\
    \ as a specter under the qwyllion's control, unless the Humanoid is restored to\
    \ life. The qwyllion can have no more than ten specters under its control at one\
    \ time."
  "name": "Deadly Gaze"
- "desc": "One Humanoid or Beast the qwyllion can see within 30 feet of it must succeed\
    \ on a DC 15 Wisdom saving throw or be magically [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ for 1 day. The [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ target obeys the qwyllion's verbal commands. If the target suffers any harm\
    \ or receives a suicidal command, it can repeat the saving throw, ending the effect\
    \ on a success. If the target successfully saves against the effect, or if the\
    \ effect on it ends, the target is immune to the qwyllion's Charm for the next\
    \ 24 hours.\n\nThe qwyllion can have no more than one Humanoid and up to three\
    \ Beasts [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ at a time. If it charms another Humanoid or a fourth Beast, the oldest effect\
    \ on a previous target ends."
  "name": "Charm"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/qwyllion-tob1-2023.webp"
```
^statblock

## Environment

badlands
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Son of Fenris"]
---
# [Son of Fenris](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/son-of-fenris-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 335*  

*The massive wolf lumbers forward, malice gleaming in its black eyes. Two snake-like tongues slither in its jaws, and green scales peek from beneath its black fur.*

## Demonic Wolves

Demonic black eyes, two snakelike tongues, and green-black scales beneath their black fur betray the sons of Fenris's unnatural origins.

## Hibernate Until Ravenous

Sons of Fenris slumber beneath the snow for months, waking when they grow ravenous or when prey approaches. When hunting, they revel in wanton savagery and destruction, killing entire herds to delight in blood.

## Desperate Worshipers

Despite their fierce nature, all the sons of Fenris are divine offspring and wise in divine lore, attracting desperate souls who offer them worship and sacrifice in exchange for aid. The sons of Fenris enjoy this adulation, and they provide protection and wisdom to their followers. Sometimes, they gather enormous war bands and go reaving.

```statblock
"name": "Son of Fenris (ToB1-2023)"
"size": "Huge"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "175"
"hit_dice": "14d12 + 84"
"stats":
- !!int "26"
- !!int "16"
- !!int "23"
- !!int "16"
- !!int "18"
- !!int "14"
"speed": "60 ft., burrow 30 ft."
"saves":
  "Dexterity": !!int "7"
  "Wisdom": !!int "8"
  "Constitution": !!int "10"
"skillsaves":
  "Intimidation": !!int "6"
  "Religion": !!int "11"
  "Arcana": !!int "7"
"damage_resistances": "necrotic; radiant; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"damage_immunities": "cold, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "passive Perception 14"
"languages": "Celestial, Common, Giant, telepathy 60 ft."
"cr": "12"
"traits":
- "desc": "The son of Fenris has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on hearing or smell."
  "name": "Keen Hearing and Smell"
- "desc": "The son of Fenris's weapon attacks are magical. When the son hits with\
    \ any weapon, the weapon deals an extra 3d6 necrotic damage or 3d6 radiant\
    \ damage (included in the attack), the son's choice."
  "name": "Divine Weapons"
"actions":
- "desc": "The son of Fenris makes one Bite attack and two Slam attacks, or it makes\
    \ four Divine Bolt attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 19\
    \ (2d10 + 8) piercing damage plus 10 (3d6) necrotic damage or (3d6) radiant\
    \ damage (the son's choice). If the target is a Large or smaller creature, it\
    \ must succeed on a DC 18 Dexterity saving throw or be swallowed by the son of\
    \ Fenris. A swallowed creature is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ and [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ it has total cover against attacks and other effects outside the son, and it\
    \ takes 21 (6d6) acid damage at the start of each of the son's turns. The son\
    \ can have only one creature swallowed at a time.\n\nIf the son takes 30 damage\
    \ or more on a single turn from a creature inside it, the son must succeed on\
    \ a DC 20 Constitution saving throw at the end of that turn or regurgitate the\
    \ swallowed creature, which falls [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ in a space within 10 feet of the son. If the son dies, the swallowed creature\
    \ is no longer [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by it and can escape from the corpse by using 10 feet of movement, exiting [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 13\
    \ (1d10 + 8) bludgeoning damage plus 10 (3d6) necrotic damage or (3d6) radiant\
    \ damage (the son's choice)."
  "name": "Slam"
- "desc": "Ranged Spell Attack: +8 to hit, range 60 ft., one target. Hit: 18\
    \ (4d6 + 4) necrotic damage or (4d6 + 4) radiant damage (the son's choice)."
  "name": "Divine Bolt"
- "desc": "The two snake tongues of the son of Fenris each exhale poison in a 30-foot\
    \ line that is 5 feet wide, resulting in two lines. Each creature in a line must\
    \ make a DC 18 Dexterity saving throw, taking 45 (10d8) poison damage on a failed\
    \ save, or half as much damage on a successful one. If the lines overlap, each\
    \ creature in the overlapping lines must make one saving throw with disadvantage\
    \ against only one of the lines rather than one saving throw for each line."
  "name": "Snake Breath (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/son-of-fenris-tob1-2023.webp"
```
^statblock

## Environment

arctic
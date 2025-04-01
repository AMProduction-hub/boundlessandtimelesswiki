---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/gargantuan
- ttrpg-cli/monster/type/ooze
statblock: inline
aliases: ["Oozasis"]
---
# [Oozasis](03 - Player Log & Handouts\Mechanics\CLI\bestiary\ooze/oozasis-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 290*  

*The oasis appears as an idyllic desert respite, offering water, shade, and even edible fruit and nuts in the trees above.*

## Mockmire

The oozasis, or oasis ooze, is also known as a mockmire in other climates. It mimics a peaceful, pristine watering hole to draw in unsuspecting prey. An oozasis cycles seemingly at random between activity and dormancy.

## Quest Givers

Within its odd physiology stirs an ancient mind with an inscrutable purpose. Far from being a mindless sludge, its fractured intelligence occasionally reads the thoughts of visitors. At these times, it tries to coerce them into undertaking quests for cryptic reasons.

## Ancient Minds

Some tales claim these creatures preserve the memories of mad wizards from dead empires, or that they have unimaginably ancient, inhuman origins.

```statblock
"name": "Oozasis (ToB1-2023)"
"size": "Gargantuan"
"type": "ooze"
"alignment": "Unaligned"
"ac": !!int "7"
"hp": !!int "217"
"hit_dice": "14d20 + 70"
"stats":
- !!int "18"
- !!int "5"
- !!int "20"
- !!int "8"
- !!int "20"
- !!int "13"
"speed": "20 ft., burrow 20 ft., swim 20 ft."
"saves":
  "Charisma": !!int "5"
  "Wisdom": !!int "9"
  "Intelligence": !!int "3"
"skillsaves":
  "Deception": !!int "5"
  "Insight": !!int "9"
  "Perception": !!int "9"
  "History": !!int "3"
"damage_vulnerabilities": "cold"
"damage_resistances": "fire; bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "acid"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "blindsight 120 ft. (blind beyond this radius), passive Perception 19"
"languages": "telepathy 120 ft. understands all languages but can't speak"
"cr": "9"
"traits":
- "desc": "The oozasis can move through a space as narrow as 1 foot wide without squeezing."
  "name": "Amorphous"
- "desc": "While the oozasis remains motionless and partially submerged on the surface\
    \ of sand or soil, it is indistinguishable from a small oasis or pond. The oozasis's\
    \ body provides enough water for plants to grow around it, provided the oozasis\
    \ remains in the area for an extended period of time. A creature that eats a fruit\
    \ from a plant growing in the oozasis's water is affected by the Waters of Unfathomable\
    \ Compulsion trait as if it drank the water."
  "name": "Oasis Appearance"
- "desc": "The oozasis doesn't require sleep."
  "name": "Ooze Nature"
- "desc": "A creature that drinks the water of an oozasis experiences a cryptic dream\
    \ the next time it sleeps. When it wakes, it must succeed on a DC 16 Wisdom saving\
    \ throw or be affected by the [geas](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/geas.md)\
    \ spell for 30 days. While under the geas, the affected creature must perform\
    \ a specific, seemingly minor task that furthers the decades-long goals of the\
    \ oozasis. Such a task could be planting a white rose in a specific garden, rescuing\
    \ the next endangered young animal the target encounters, or standing in a specific\
    \ spot at a certain time each day for three days."
  "name": "Waters of Unfathomable Compulsion"
"actions":
- "desc": "The oozasis makes three Pseudopod attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 15 ft., one target. Hit: 13\
    \ (2d8 + 4) bludgeoning damage plus 7 (2d6) acid damage. If the target is\
    \ a Large or smaller creature, it is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 16). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ The oozasis can have up to two creatures [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ at a time."
  "name": "Pseudopod"
- "desc": "The oozasis emits mind-altering vapors. Each creature within 20 feet of\
    \ the oozasis must make a DC 16 Constitution saving throw. On a failure, a creature\
    \ takes 45 (10d8) psychic damage and suffers either tranquility or turmoil for\
    \ minute. On a success, a creature takes half the damage and doesn't suffer tranquility\
    \ or turmoil. A creature suffering tranquility is [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ and can't attack. A creature suffering turmoil is unable to distinguish friend\
    \ from foe and must move to and attack the nearest creature other than the oozasis\
    \ on each of its turns, stalking off in a random direction if no creature is in\
    \ range. A creature suffering tranquility or turmoil can repeat the saving throw\
    \ at the end of each of its turns, ending the effect on itself on a success."
  "name": "Compelling Vapors (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/ooze/token/oozasis-tob1-2023.webp"
```
^statblock

## Environment

desert
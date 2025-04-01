---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/13
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Haugbui"]
---
# [Haugbui](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/haugbui-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 231*  

*A thick swirl of dust rises, settles, and forms the vague outline of a human—two points of yellow light shine where its eyes should be, staring malevolently.*

## Mound Haunter

A haugbui is an undead spirit tied to its burial mound or barrow. It serves as a familiar, protective spirit to nearby farmsteads or villages, so long as tribute is regularly paid to the haugbui. Traditional offerings may include pouring the first beer from a barrel, leaving portions of meals out overnight, sacrificing blood or livestock, or burying a portion of any income in the mound. A freshly-woken haugbui devours the remains of creatures it was buried with, such as a hawk, hound, or horse.

## Milder Spirits

Haugbuis are similar to vættir but much older. They are more humble and less prone to taking umbrage, and indeed, a great many haugbui have long since forgotten their own names. They are not quick to spill blood when irritated and thus are viewed with greater tolerance by the living.

## Scrye and Watch

Haugbuis prefer to watch over their people from within their mound, and only come forth over the most grievous insults or injuries. They can do a great deal from within their mounds thanks to their scrying ability.

```statblock
"name": "Haugbui (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Lawful Neutral"
"ac": !!int "15"
"hp": !!int "153"
"hit_dice": "18d8 + 72"
"stats":
- !!int "18"
- !!int "20"
- !!int "18"
- !!int "15"
- !!int "20"
- !!int "16"
"speed": "0 ft., fly 40 ft. (hover)"
"saves":
  "Dexterity": !!int "10"
  "Wisdom": !!int "10"
  "Constitution": !!int "9"
"skillsaves":
  "Intimidation": !!int "8"
  "Religion": !!int "12"
  "Perception": !!int "10"
  "History": !!int "7"
  "Arcana": !!int "7"
"damage_resistances": "acid, cold, fire, lightning, necrotic, thunder"
"damage_immunities": "poison; bludgeoning, piercing, slashing from nonmagical attacks"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)"
"senses": "truesight 60 ft., passive Perception 20"
"languages": "telepathy 120 ft. all the languages it knew in life"
"cr": "13"
"traits":
- "desc": "The haugbui casts one of the following spells, requiring no components\
    \ and using Wisdom as the spellcasting ability (spell save DC 18):\n\nAt will:\
    \ [dancing lights](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dancing-lights.md),\
    \ [mending](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mending.md),\
    \ [purify food and drink](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/purify-food-and-drink.md),\
    \ [spare the dying](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/spare-the-dying.md)\n\
    \n1/day each: [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md),\
    \ [remove curse](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/remove-curse.md)\n\
    \n3/day each: [gust of wind](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/gust-of-wind.md),\
    \ [telekinesis](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/telekinesis.md)"
  "name": "Spellcasting"
- "desc": "The haugbui can move through other creatures and objects as if they were\
    \ difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside\
    \ an object."
  "name": "Incorporeal Movement"
- "desc": "While in sunlight, the haugbui has disadvantage on attack rolls, as well\
    \ as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
- "desc": "The haugbui has advantage on saving throws against any effect that turns\
    \ undead."
  "name": "Turn Resistance"
- "desc": "The hangbui doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The haugbui makes three Psychic Blast attacks. It can replace one attack\
    \ with a use of Spellcasting."
  "name": "Multiattack"
- "desc": "Melee or Ranged Spell Attack: +10 to hit, range 120 ft., one target.\
    \ Hit: 27 (5d8 + 5) psychic damage."
  "name": "Psychic Blast"
- "desc": "The haugbui magically turns [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ until it attacks or casts a spell, or until its [concentration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ ends (as if [concentrating](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ on a spell). Any equipment the haugbui wears or carries is [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ with it."
  "name": "Invisibility"
"bonus_actions":
- "desc": "While within 1 mile of its burial mound, the haugbui creates an [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ sensor within 5 miles of the mound for 1 minute. When it uses this bonus action\
    \ and as a bonus action on each of its turns for the duration, the haugbui can\
    \ switch between using its own senses and projecting its senses through the sensor.\
    \ While projecting its senses through the sensor, it can see, hear, telepathically\
    \ communicate, and cast spells as if it was in the sensor's space, and it is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ and [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened)\
    \ with regard to its own senses. The sensor can be dispelled (DC 14)."
  "name": "Sepulchral Scrying (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/haugbui-tob1-2023.webp"
```
^statblock

## Environment

farmland, hill
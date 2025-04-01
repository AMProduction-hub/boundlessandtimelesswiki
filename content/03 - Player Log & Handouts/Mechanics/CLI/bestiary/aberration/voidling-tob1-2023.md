---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/11
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Voidling"]
---
# [Voidling](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/voidling-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 390*  

*Writhing black tendrils stretch from this indistinct orb of pure shadow. The faintest flicker of something green, like an eye, appears for a moment in the center of the globe and then fades to black again.*

## Called from Darkness

Voidlings are creatures of the darkest part of the Void, the cold space between the stars. They are drawn to mortal realms by practitioners of foul, corrupting magic known to break the minds of those who wield it. They frequently are summoned servants to Void dragons, and they have been seen as wardens of the temples on the Plateau of Leng.

## Sustained by Darkness

Voidlings are said to devour life and knowledge, and they subsist on darkness. The places they inhabit are known for their dank chill and obscurity. Voidlings are summoned by those hungry for power at any cost, and—despite their dark reputation—they serve well for years or even decades, until one day they turn on their summoners. If they slay their summoner, they grow in strength and return to the Void. Exactly what voidlings seek when they have not been summoned—and what triggers their betrayals—is a mystery.

## Cold Tendrils

Creatures of utter darkness, they can barely be said to have a shape. They consist largely of lashing tendrils of solid shadow. The tendrils meet at a central point and form a rough sphere in which something like an eye appears intermittently. Though their tentacles stretch ten feet long, the core of a voiding is no more than four feet across, and it weighs nothing, darting through either air or Void with impressive speed.

```statblock
"name": "Voidling (ToB1-2023)"
"size": "Large"
"type": "aberration"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"hp": !!int "180"
"hit_dice": "24d10 + 48"
"stats":
- !!int "15"
- !!int "21"
- !!int "15"
- !!int "14"
- !!int "16"
- !!int "10"
"speed": "0 ft., fly 50 ft. (hover)"
"saves":
  "Charisma": !!int "4"
  "Wisdom": !!int "7"
  "Intelligence": !!int "6"
  "Constitution": !!int "6"
"skillsaves":
  "Stealth": !!int "9"
"damage_vulnerabilities": "radiant"
"damage_immunities": "necrotic"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "truesight 60 ft., passive Perception 13"
"languages": "telepathy 60 ft., Void Speech"
"cr": "11"
"traits":
- "desc": "While in an area of dim light or darkness, the voidling regains 5 hp at\
    \ the start of its turn if it has at least 1 hp."
  "name": "Darkness Regeneration"
- "desc": "The voidling has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The voidling doesn't require air, food, drink, sleep, or ambient pressure."
  "name": "Void Traveler"
"actions":
- "desc": "The voidling makes four Shadow Tendril or Necrotic Bolt attacks. If two\
    \ Necrotic Bolt attacks hit one creature, the target must succeed on a DC 17 Wisdom\
    \ saving throw or be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ until the end of its next turn."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 8\
    \ (1d6 + 5) bludgeoning damage plus 10 (3d6) necrotic damage."
  "name": "Shadow Tendril"
- "desc": "Ranged Spell Attack: +7 to hit, range 120 ft., one target. Hit: 17\
    \ (4d6 + 3) necrotic damage."
  "name": "Necrotic Bolt"
- "desc": "The voidling releases a wave of small, grasping tendrils of shadow. Each\
    \ creature within 20 feet of it must make a DC 17 Dexterity saving throw. On a\
    \ failure, a creature takes 49 (14d6) necrotic damage and is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by tendrils of shadow for 1 minute. On a success, a creature takes half the\
    \ damage and isn't [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ A creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Shadow's Grasp (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/voidling-tob1-2023.webp"
```
^statblock

## Environment

planar
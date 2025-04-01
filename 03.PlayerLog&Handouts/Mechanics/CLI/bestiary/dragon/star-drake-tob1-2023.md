---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/15
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Star Drake"]
---
# [Star Drake](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/star-drake-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 146*  

*Twinkling motes of light move around the mottled, metallic scales of this dragon's body. Light reflections twinkle like starlight across its metallic scales.*

## Returned Travelers

A drake's curiosity sometimes drives it to seek experiences beyond its plane, and it finds companions with which it travels the multiverse. Such drakes return clearly changed in appearance, demeanor, and ability. Regardless of which type of drake embarked on the journey, the creature always returns as a star drake.

## Mortal Protectors

Star drakes consider themselves protectors of the Material Plane. They view those from other planes as meddlers in the affairs of humanoid races, regarding fiends and celestials as equally threatening. Star drakes might negotiate with, drive off, or destroy such meddlers.

## Unlikely Allies

Inexplicably, planewatchers can recognize when a drake that is exploring the planes is in the process of becoming a star drake, and they typically leave these drakes to their exploring. After a drake's metamorphosis, planewatchers often aid the drake, seeing it as a sort of kindred spirit.

```statblock
"name": "Star Drake (ToB1-2023)"
"size": "Large"
"type": "dragon"
"alignment": "Neutral"
"ac": !!int "19"
"ac_class": "natural armor"
"hp": !!int "189"
"hit_dice": "18d10 + 90"
"stats":
- !!int "20"
- !!int "17"
- !!int "21"
- !!int "16"
- !!int "24"
- !!int "20"
"speed": "40 ft., fly 100 ft."
"saves":
  "Charisma": !!int "10"
  "Dexterity": !!int "8"
  "Wisdom": !!int "12"
  "Constitution": !!int "10"
"skillsaves":
  "Religion": !!int "8"
  "Insight": !!int "12"
  "Perception": !!int "12"
  "History": !!int "8"
  "Arcana": !!int "8"
"damage_immunities": "cold; fire; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)"
"senses": "truesight 120 ft., passive Perception 22"
"languages": "Abyssal, Celestial, Common, Draconic, Infernal, Primordial"
"cr": "15"
"traits":
- "desc": "The drake has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "At the start of each of the drake's turns, each creature within 10 feet\
    \ of it and that can see it must succeed on a DC 18 Constitution saving throw\
    \ or be [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ until the end of its next turn."
  "name": "Nimbus of Swirling Stars"
- "desc": "The drake's weapon attacks are magical. When it hits with any weapon, the\
    \ weapon deals an extra 4d8 force damage (included in the attack)."
  "name": "Planar Weapons"
"actions":
- "desc": "The drake makes one Bite attack and two Claw attacks, or it makes four\
    \ Searing Star attacks. If two Searing Star attacks hit one creature, that creature\
    \ must succeed on a DC 18 Constitution saving throw or be [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the end of its next turn."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 16\
    \ (2d10 + 5) piercing damage plus 18 (4d8) force damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d6 + 5) slashing damage plus 18 (4d8) force damage."
  "name": "Claw"
- "desc": "Ranged Spell Attack: +12 to hit, range 120 ft., one target. Hit:\
    \ 14 (2d6 + 7) radiant damage plus 9 (2d8) force damage."
  "name": "Searing Star"
- "desc": "The star drake can transport itself to a different plane of existence.\
    \ This works like the [plane shift](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/plane-shift.md)\
    \ spell, except the drake can affect only itself and can't use this action to\
    \ banish an unwilling creature to another plane."
  "name": "Planar Traveler"
- "desc": "The drake exhales raw magic in a 60-foot cone. Each creature in that area\
    \ must make a DC 18 Dexterity saving throw, taking 55 (10d10) force damage on\
    \ a failed save, or half as much damage on a successful one."
  "name": "Plane-Altered Breath (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/star-drake-tob1-2023.webp"
```
^statblock

## Environment

any, planar
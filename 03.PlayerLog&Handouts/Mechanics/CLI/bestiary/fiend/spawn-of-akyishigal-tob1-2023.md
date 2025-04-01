---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fiend/demon
statblock: inline
aliases: ["Spawn of Akyishigal"]
---
# [Spawn of Akyishigal](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/spawn-of-akyishigal-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 75*  

*This human-sized insectoid has a tail that splits near the end curling over its back. Both ends bear needle-stingers dripping with poison.*

Spawn of Akyishigal are found in abundance wherever the demon lord abides. He has also been known to send them to his followers if their need is great and the spawn's presence somehow benefits Akyishigal.

## Lords of Vermin

Vermin of all types instinctively obey mental commands from a spawn of Akyishigal. What's more, these repulsive beings can vomit thousands of roaches that also do the spawn's bidding. They take particular delight in belching roaches directly onto their foes, but they've also been known to use roaches and vermin as a means of cutting off an enemy's retreat or of hindering pursuit when the spawn itself wants to escape.

```statblock
"name": "Spawn of Akyishigal (ToB1-2023)"
"size": "Medium"
"type": "fiend"
"subtype": "demon"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "119"
"hit_dice": "14d8 + 56"
"stats":
- !!int "15"
- !!int "13"
- !!int "19"
- !!int "10"
- !!int "11"
- !!int "12"
"speed": "30 ft., climb 30 ft."
"saves":
  "Dexterity": !!int "4"
"damage_resistances": "cold, fire, lightning"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Abyssal"
"cr": "5"
"traits":
- "desc": "The spawn of Akyishigal can command any Beast with an Intelligence of 2\
    \ or lower within 30 feet of it that isn't under the magical control of another\
    \ creature, provided the Beast is insectoid and doesn't have a Challenge Rating\
    \ higher than the spawn's. The Beast obeys the spawn's commands to the best of\
    \ its ability, heedless of its own safety."
  "name": "Command Vermin"
- "desc": "The spawn of Akyishigal has advantage on saving throws against spells and\
    \ other magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The spawn makes one Bite attack and two Sting attacks. It can replace its\
    \ Bite attack with a use of Swarming Cough, if available."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d10\
    \ + 2) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d8 + 2) piercing damage plus 3 (1d6) poison damage, and the target must\
    \ succeed on a DC 15 Constitution saving throw or become [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn."
  "name": "Sting"
- "desc": "The spawn belches forth a swarm of insects. The swarm is an ally of the\
    \ spawn, obeys its spoken commands, and takes its turn immediately after the spawn's.\
    \ The swarm remains for 1 minute, until the spawn dies, or until the spawn dismisses\
    \ it as a bonus action. The spawn can have no more than two swarms under its control\
    \ at a time."
  "name": "Swarming Cough (3/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/spawn-of-akyishigal-tob1-2023.webp"
```
^statblock

## Environment

urban
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Fext"]
---
# [Fext](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/fext-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 171*  

*Taut dead skin, adorned entirely with tattooed fish scales, covers this woman's face and hands. She wears scaled armor, sea green like verdigris on copper, and wields a sword swirling with arcane energies. Her pale eyes stare, unblinking*.

## Undead Warlock Vassals

Ancient and powerful beings across the multiverse grant magical knowledge to mortals through dangerous pacts. Those bound to these pacts become warlocks, but the will and force of their patron is borne by more than just those who strike bargains for sorcerous power. A fext is a former warlock who has become wholly dedicated to their patron—mind, body, and soul—and functions as enforcer, bodyguard, and assassin. They are powerful undead slaves to the will of their otherworldly patron.

## Linked to a Master

Each fext is a unique servant of their patron and exhibits the physical traits of its master. The eyes of every fext are tied directly to their patron's mind, who can see what the fext sees at any time. The fext also possesses a telepathic link to its patron. The process a warlock undergoes to become a fext is horrendous. The warlock is emptied of whatever morality and humanity he or she had as wine from a jug, and the patron imbues the empty vessel with its corruption and unearthly will. Whatever life the fext led before is completely gone. They exist only to serve.

## Outdoing Rivals

Scholars have debated about how many fext a patron can command. The more powerful and well-established have at least 100, while others have only a handful. Where there is more than one fext, however, they maneuver amongst themselves to curry favor with their powerful patron. Each fext is bound to obey commands, but they attempt to carry out the commands to the detriment of their competitors. Scheming is common and rampant among them, and each fext tries to work without the aid of other fext as much as possible.

```statblock
"name": "Fext (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Any alignment"
"ac": !!int "17"
"ac_class": "patron's blessing"
"hp": !!int "77"
"hit_dice": "14d8 + 14"
"stats":
- !!int "14"
- !!int "16"
- !!int "12"
- !!int "14"
- !!int "12"
- !!int "18"
"speed": "30 ft."
"saves":
  "Dexterity": !!int "6"
  "Wisdom": !!int "4"
"skillsaves":
  "Perception": !!int "4"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., truesight 20 ft., passive Perception 14"
"languages": "the languages it knew in life"
"cr": "6"
"traits":
- "desc": "The fext's weapon attacks are magical. When the fext hits with any weapon,\
    \ the weapon deals an extra 2d8 force damage (included in the attack)."
  "name": "Eldritch Weapons"
- "desc": "The fext has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "While the fext is conscious and wearing no armor and wielding no shield,\
    \ it adds its Charisma modifier to its AC (included above)."
  "name": "Patron's Blessing"
- "desc": "The fext doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The fext makes two Eldritch Blade or Eldritch Fury attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d8 + 3) slashing damage plus 9 (2d8) force damage."
  "name": "Eldritch Blade"
- "desc": "Ranged Spell Attack: +7 to hit, range 120 ft., one target. Hit: 17\
    \ (3d8 + 4) force damage."
  "name": "Eldritch Fury"
- "desc": "The fext channels its patron's awe‑inspiring presence, terrifying those\
    \ nearby. Each creature within 10 feet of the fext must make a DC 15 Wisdom saving\
    \ throw. On a failure, a creature takes 35 (10d6) psychic damage and is [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened).\
    \ A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Patron's Might (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/fext-tob1-2023.webp"
```
^statblock

## Environment

any
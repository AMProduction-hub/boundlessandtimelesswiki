---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Amphiptere"]
---
# [Amphiptere](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/amphiptere-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 16*  

*A flight of gold-crested, bat-winged serpents bursts from the foliage.*

## Tiny Wyverns

An amphiptere has batlike wings and a stinger similar to a wyvern's at the end of its tail. Their reptilian bodies are scaly, but their wings sprout greenish-yellow feathers.

## Swooping and Swift

They are surprisingly maneuverable in spite of their size, able to change direction suddenly and make deadly hit-and-run strikes. They swoop in and out of combat, snapping at targets with their needlelike teeth and striking with their envenomed stingers. Once a foe is poisoned and injured, they hover closer in a tightly packed, flapping mass of fangs, battering wings, and jabbing stingers.

## Strength in Flocks

Despite their fighting ability, amphipteres are not particularly brave. Most often, they lurk in small flocks in dense foliage, where they can burst forth in a flurry of wings when prey comes within view. They display surprising cunning and tenacity in large groups; they may harass foes for minutes or hours before closing in for the kill.

```statblock
"name": "Amphiptere (ToB1-2023)"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "60"
"hit_dice": "8d8 + 24"
"stats":
- !!int "11"
- !!int "18"
- !!int "17"
- !!int "2"
- !!int "16"
- !!int "6"
"speed": "20 ft., climb 20 ft., fly 60 ft., swim 20 ft."
"skillsaves":
  "Perception": !!int "5"
"senses": "blindsight 10 ft., passive Perception 15"
"languages": ""
"cr": "3"
"traits":
- "desc": "The amphiptere doesn't provoke opportunity attacks when it flies out of\
    \ an enemy's reach."
  "name": "Flyby"
- "desc": "Up to two amphipteres can share the same space at the same time. The amphiptere\
    \ has advantage on melee attack rolls if it is sharing its space with another\
    \ amphiptere that isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Swarming"
"actions":
- "desc": "The amphiptere makes one Bite attack and one Stinger attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 7\
    \ (1d6 + 4) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 7\
    \ (1d6 + 4) piercing damage plus 10 (3d6) poison damage, and the target must\
    \ succeed on a DC 13 Constitution saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 hour."
  "name": "Stinger"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/amphiptere-tob1-2023.webp"
```
^statblock

## Environment

forest, hill
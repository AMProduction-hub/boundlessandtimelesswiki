---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/humanoid/ratfolk
statblock: inline
aliases: ["Ratfolk Rogue"]
---
# [Ratfolk Rogue](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/ratfolk-rogue-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 302*  

*The halfling-sized, furred creature has a twitching snout, bony feet, and a long, pink tail.*

The ratfolk are canny survivors, rogues, and tricksters. Their strong family ties make it easy for them to found or join criminal societies—though others serve as expert scouts and saboteurs, able to infiltrate army camps, city sewers, and even castle dungeons with equal ease. Ratfolk leaders are often spellcasters and rogues.

## Adaptable

Ratfolk swim well and can survive on little. Some groups are endemic to tropical and subtropical islands. Others inhabit forests, sewers, labyrinths, and ancient, ruined cities.

## Fast Fighters

Ratfolk prefer light weapons and armor, fighting with speed and using numbers to bring down a foe. They have been known to ally themselves with goblins, darakhul, and kobolds on occasion, but more often prefer to serve a "Rat King" who may or may not be a rat of any kind. Such rat rulers might include a wererat, a rat king, an ogre, a minor demon, or an intelligent undead.

```statblock
"name": "Ratfolk Rogue (ToB1-2023)"
"size": "Small"
"type": "humanoid"
"subtype": "ratfolk"
"alignment": "Neutral"
"ac": !!int "15"
"ac_class": "[studded leather](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/studded-leather-armor.md)"
"hp": !!int "31"
"hit_dice": "7d6 + 7"
"stats":
- !!int "7"
- !!int "16"
- !!int "12"
- !!int "14"
- !!int "10"
- !!int "10"
"speed": "25 ft., swim 10 ft."
"skillsaves":
  "Stealth": !!int "7"
  "Perception": !!int "2"
  "Acrobatics": !!int "5"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": "Common, Thieves' cant"
"cr": "1"
"traits":
- "desc": "The ratfolk rogue can move through the space of any Medium or larger hostile\
    \ creature, and such a space isn't difficult terrain for the ratfolk rogue."
  "name": "Nimbleness"
- "desc": "The ratfolk rogue has advantage on attack rolls against a creature if at\
    \ least one of the ratfolk rogue's allies is within 5 feet of the creature and\
    \ the ally isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Pack Tactics"
"actions":
- "desc": "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 5 (1d4 + 3) piercing damage plus 7 (2d6) poison\
    \ damage."
  "name": "Dagger"
- "desc": "Ranged Weapon Attack: +5 to hit, range 80/320 ft., one target. Hit:\
    \ 7 (1d8 + 3) piercing damage plus 7 (2d6) poison damage."
  "name": "Light Crossbow"
"bonus_actions":
- "desc": "The ratfolk rogue takes the Dash, Disengage, or Hide action."
  "name": "Cunning Action"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/ratfolk-rogue-tob1-2023.webp"
```
^statblock

## Environment

urban
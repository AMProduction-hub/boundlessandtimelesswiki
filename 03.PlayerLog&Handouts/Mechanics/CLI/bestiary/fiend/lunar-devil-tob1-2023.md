---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend/devil
statblock: inline
aliases: ["Lunar Devil"]
---
# [Lunar Devil](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/lunar-devil-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 98*  

*A hulking figure floats in the air, a winged horror painted in mist and moonlight.*

## Corruptors of the Moon

Lunar devils can be found subverting druidical orders or leading packs of werewolves. They are a lazy breed of devil and prefer lounging in the light of the moon over more vigorous activity. The only exception is an opportunity to corrupt druids and moon-worshippers, pitting them against followers of sun gods.

## Vain and Boastful

Lunar devils are as vain as they are indolent. Tales the fey tell involve thwarting them by appealing to their vanity. Lunar devils frequently befriend the dark fey.

## Flying in Darkness

In combat, lunar devils sometimes bring allies along, bestowing magical flight on them. The devils stay in areas of moonlight whenever they can. Lunar devils have excellent vision in total darkness, though, and are happy to use that against foes. They prefer attacking from range, allowing allies to take the brunt of any opposition.

```statblock
"name": "Lunar Devil (ToB1-2023)"
"size": "Large"
"type": "fiend"
"subtype": "devil"
"alignment": "Lawful Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "94"
"hit_dice": "9d10 + 45"
"stats":
- !!int "21"
- !!int "21"
- !!int "20"
- !!int "16"
- !!int "15"
- !!int "18"
"speed": "40 ft., fly 60 ft. (hover)"
"saves":
  "Dexterity": !!int "8"
  "Wisdom": !!int "5"
  "Strength": !!int "8"
  "Constitution": !!int "8"
"skillsaves":
  "Perception": !!int "5"
"damage_resistances": "cold; bludgeoning, piercing, slashing from nonmagical attacks\
  \ that aren't silvered"
"damage_immunities": "fire, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., passive Perception 15"
"languages": "Celestial, Draconic, Elvish, Infernal, Sylvan, telepathy 120 ft."
"cr": "8"
"traits":
- "desc": "The lunar devil casts one of the following spells, requiring no material\
    \ components and using Charisma as the spellcasting ability (spell save DC 15):\n\
    \nAt will: [fly](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fly.md),\
    \ [major image](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/major-image.md)\n\
    \n1/day: [wall of ice](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/wall-of-ice.md)\n\
    \n3/day: [greater invisibility](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-invisibility.md)"
  "name": "Spellcasting"
- "desc": "Magical darkness doesn't impede the lunar devil's darkvision."
  "name": "Devil's Sight"
- "desc": "The lunar devil is translucent when standing in moonlight and is immune\
    \ to damage from all nonmagical weapons in such conditions."
  "name": "Light Incorporeality"
- "desc": "Once on its turn, the lunar devil can use half its movement to step magically\
    \ into one area of moonlight within its reach and emerge from a second area of\
    \ moonlight within 80 feet of the first, appearing in an unoccupied space within\
    \ that second area."
  "name": "Lightwalking"
- "desc": "The lunar devil has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The lunar devil makes one Bite attack, one Claw attack, and one Tail attack,\
    \ or it makes three Hurl Moonlight attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 16\
    \ (2d10 + 5) piercing damage plus 9 (2d8) cold damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 12\
    \ (2d6 + 5) slashing damage."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 14\
    \ (2d8 + 5) bludgeoning damage."
  "name": "Tail"
- "desc": "Ranged Spell Attack: +7 to hit, range 150 ft., one target. Hit: 17\
    \ (3d8 + 4) cold damage, and the target must succeed on a DC 15 Constitution\
    \ saving throw or become [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the end of its next turn."
  "name": "Hurl Moonlight"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/lunar-devil-tob1-2023.webp"
```
^statblock

## Environment

forest
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/badlands
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Mamura"]
---
# [Mamura](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/mamura-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 263*  

*This atrocity combines the worst elements of a dead frog and a rotting fish. Its slimy, scaly, vaguely humanoid form has eyes and three clawed arms arranged radially about its body. Its green, bat-like wings seem too small to work, yet it flies well*.

## Twisted Field Sprites

Mamuras are the twisted faeries of magical wastelands and barren plains. They were once good-aligned, pixie-like fey called "polevoi," or "field sprites." At some point, they swore their souls to a dark goddess and were corrupted by her foul magic. Now they are twisted, alien things.

## Cross-Dimensional

The mamura is one degree out of phase with reality. It appears blurry and indistinct even in bright light, and it seems translucent in dim light. They babble constantly, but their talk is mostly nonsense. Their minds operate in multiple dimensions in time as well as space, and this allows them to talk to and understand creatures of the Void. Because of this, their babble may be prophetic for the few who can decipher it.

## Prophetic Followers

They occasionally align themselves with powerful goblin tribes or evil wasteland sorcerers for their own unknowable purposes.

> [!note] Mamuras in Midgard
> 
> The mamura are servants of the Black Goat of the Woods, and they live in the Wasted West and various fetid swamps and badlands. They seem friendly with the selang, and they arrange strange and orgiastic rites with them at the equinoxes.
^mamuras-in-midgard

```statblock
"name": "Mamura (ToB1-2023)"
"size": "Small"
"type": "aberration"
"alignment": "Neutral Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "112"
"hit_dice": "15d6 + 60"
"stats":
- !!int "8"
- !!int "18"
- !!int "19"
- !!int "17"
- !!int "11"
- !!int "16"
"speed": "20 ft., fly 30 ft."
"saves":
  "Charisma": !!int "6"
  "Dexterity": !!int "7"
  "Constitution": !!int "7"
"skillsaves":
  "Stealth": !!int "7"
  "Perception": !!int "6"
  "Acrobatics": !!int "7"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"senses": "darkvision 60 ft., passive Perception 16"
"languages": "Common, Goblin, Sylvan, Void Speech"
"cr": "6"
"traits":
- "desc": "When a spellcaster that is [concentrating](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ on a spell starts its turn within 20 feet of the mamura, the spellcaster must\
    \ succeed on a DC 15 Constitution saving throw or lose [concentration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ on the spell. In addition, if a spellcaster within 20 feet of the mamura casts\
    \ a spell, it must succeed on a DC 15 Constitution saving throw or the spell fails\
    \ to cast, using the action, bonus action, or reaction to cast the spell but not\
    \ expending the spell slot."
  "name": "Distracting Babble"
- "desc": "The mamura doesn't provoke opportunity attacks when it flies out of an\
    \ enemy's reach."
  "name": "Flyby"
- "desc": "The mamura has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The mamura has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight and on saving throws against being [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded).\
    \ In addition, if the mamura isn't [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
    \ creatures attacking it can't benefit from traits and features that rely on a\
    \ creature's allies distracting or surrounding the mamura, such as the Pack Tactics\
    \ trait or Sneak Attack class feature."
  "name": "Radial Eyes"
"actions":
- "desc": "The mamura makes three Claw attacks and one Whiptail Stinger attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, range 5 ft., one target. Hit: 8 (1d8\
    \ + 4) slashing damage."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +7 to hit, range 10 ft., one target. Hit: 8\
    \ (1d8 + 4) piercing damage, and the target must succeed on a DC 15 Constitution\
    \ saving throw or take 7 (2d6) poison damage and be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. While [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
    \ the creature takes 3 (1d6) poison damage at the start of each of its turns.\
    \ The target can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Whiptail Stinger"
"bonus_actions":
- "desc": "While in dim light or darkness, the mamura takes the Hide action."
  "name": "Shadow Stealth"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/mamura-tob1-2023.webp"
```
^statblock

## Environment

badlands, grassland
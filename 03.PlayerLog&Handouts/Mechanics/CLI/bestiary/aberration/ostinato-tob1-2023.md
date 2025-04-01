---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Ostinato"]
---
# [Ostinato](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/ostinato-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 292*  

*A bit of catchy, repetitive music emanates from nowhere, drifting and moving as if dancing in the empty air.*

## Born from Drama

Incredibly moving arias, passionate performances, and ditties that drive a person mad are often the product of ostinatos. These creatures of living music are born from overwrought emotions, and they feed off the vitality and personality of mortals.

## Song Searchers

Ostinatos wander the mortal world as repetitive snippets of song, searching for hosts and rich feeding grounds. They enter hosts secretly, remaining undetected to prolong their voracious feasting.

```statblock
"name": "Ostinato (ToB1-2023)"
"size": "Medium"
"type": "aberration"
"alignment": "Chaotic Neutral"
"ac": !!int "15"
"hp": !!int "39"
"hit_dice": "6d8 + 12"
"stats":
- !!int "1"
- !!int "20"
- !!int "15"
- !!int "5"
- !!int "12"
- !!int "17"
"speed": "0 ft., fly 50 ft. (hover)"
"skillsaves":
  "Perception": !!int "3"
"damage_vulnerabilities": "thunder"
"damage_resistances": "acid; cold; fire; lightning; bludgeoning, piercing, slashing\
  \ from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "telepathy 120 ft. understands Common but can't speak"
"cr": "4"
"traits":
- "desc": "The ostinato can move through other creatures and objects as if they were\
    \ difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside\
    \ an object."
  "name": "Incorporeal Movement"
- "desc": "The ostinato is [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)."
  "name": "Invisibility"
- "desc": "The ostinato has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The ostinato makes two Cacophony Burst attacks."
  "name": "Multiattack"
- "desc": "Melee or Ranged Spell Attack: +7 to hit, range 60 ft., one target.\
    \ Hit: 16 (3d8 + 3) thunder damage."
  "name": "Cacophony Burst"
- "desc": "One Humanoid that the ostinato can see within 5 feet of it must succeed\
    \ on a DC 13 Charisma saving throw or the ostinato merges with the target, becoming\
    \ an enjoyable, repetitive tune in its host's mind. The ostinato can't be targeted\
    \ by any attack, spell, or other effect, and it can't attack. The host retains\
    \ control of its body and is aware of the ostinato's presence only as a melody,\
    \ not as a living entity. The host no longer needs to eat or drink, gains the\
    \ ostinato's Magic Resistance trait, and has advantage on Charisma checks. In\
    \ addition, the host has disadvantage on Wisdom saving throws, and it can't maintain\
    \ [concentration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ on spells or other effects. At the end of each long rest, the host can make\
    \ a DC 13 Wisdom ([Insight](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Insight))\
    \ check, realizing that the music it hears comes from an external entity on a\
    \ success.\n\nThe Aural Symbiosis lasts until the host drops to 0 hp, the ostinato\
    \ ends it as a bonus action, or the ostinato is forced out by an effect like the\
    \ [dispel evil and good](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-evil-and-good.md)\
    \ spell. When the Aural Symbiosis ends, the ostinato bursts out from the host's\
    \ mind in a thunderous explosion of sound, reappearing in an unoccupied space\
    \ within 5 feet of the host. Each creature within 15 feet of the ostinato when\
    \ it exits, including the host, must make a DC 13 Constitution saving throw, taking\
    \ 18 (4d8) thunder damage on a failed save, or half as much damage on a successful\
    \ one. The host is immune to this ostinato's Aural Symbiosis for 24 hours after\
    \ succeeding on the saving throw or after the Aural Symbiosis ends."
  "name": "Aural Symbiosis (Recharge 6)"
- "desc": "While merged with a Humanoid host, the ostinato fills the minds of nearby\
    \ creatures with the same catchy tune playing in its host's mind. Each creature\
    \ within 30 feet of the ostinato's host must make a DC 13 Charisma saving throw,\
    \ taking 21 (6d6) psychic damage on a failed save, or half as much damage on\
    \ a successful one. The ostinato then gains temporary hp equal to the single highest\
    \ amount of psychic damage dealt. A [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened)\
    \ creature is immune to Contagious Tune."
  "name": "Contagious Tune (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/ostinato-tob1-2023.webp"
```
^statblock

## Environment

any
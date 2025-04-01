---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Crimson Drake"]
---
# [Crimson Drake](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/crimson-drake-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 141*  

*Crimson drakes are easy to spot, with scales the color of dried blood, a deadly scorpion stinger, and a mischievous gleam in their eyes.*

## Fiery Raiders

Crimson drakes lair in woodlands near small settlements, making nighttime forays to set fires and hunt those who flee the flames—traits that make humanoid tribes prize them as raiding partners. Goblins gleefully adopt a crimson drake as a mascot to burn things down while they get on with slaughtering people. Red dragons and flame dragons regard a crimson drake as a pet, at best, but this rarely works out. When it is inevitably insulted by its larger cousins, a malicious crimson drake may intentionally set fires to blaze a trail for hunters to find the dragon's lair.

## Mistaken for Pseudodragons

A crimson drake's scales and features are quite similar to those of a pseudodragon, and they can imitate a pseudodragon's hunting cry or song to trick victims into approaching. Once their prey gets close enough, they immolate it. As with pseudodragons, they resemble a red dragon in all but size and the presence of the drake's scorpion-like stinger. On average, a crimson drake weighs 12 pounds, its body measures about 18 inches long, and its tail adds another 18 inches.

> [!note] Crimson Drake Familiars
> 
> A crimson drake occasionally chooses to serve an evil spellcaster as a familiar. They are too mischievous to be especially loyal or trustworthy, but they are ferocious in defense of their master, feeling as possessive toward the master as other dragons might a piece of a hoard. Such crimson drakes have the following trait.
> 
> **Familiar.** The drake can serve another creature as a familiar, forming a magic, telepathic bond with that willing companion. While the two are bonded, the companion can sense what the drake senses as long as they are within 1 mile of each other. While the drake is within 10 feet of its companion, the companion shares the drake's Magic Resistance trait. At any time and for any reason, the drake can end its service as a familiar, ending the telepathic bond.
^crimson-drake-familiars

```statblock
"name": "Crimson Drake (ToB1-2023)"
"size": "Tiny"
"type": "dragon"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "45"
"hit_dice": "10d4 + 20"
"stats":
- !!int "10"
- !!int "14"
- !!int "14"
- !!int "8"
- !!int "9"
- !!int "14"
"speed": "15 ft., fly 80 ft."
"saves":
  "Dexterity": !!int "4"
"skillsaves":
  "Perception": !!int "1"
  "Acrobatics": !!int "4"
"damage_immunities": "fire"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Common, Draconic"
"cr": "1"
"traits":
- "desc": "The drake has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The crimson drake makes one Bite attack and one Stinger attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6\
    \ + 2) piercing damage plus 3 (1d6) fire damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4\
    \ + 2) piercing damage, and the target must succeed on a DC 12 Constitution saving\
    \ throw or become [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. If the saving throw fails by 5 or more, the target takes 2 (1d4)\
    \ poison damage at the start of each of its turns while [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Stinger"
- "desc": "The drake exhales fire in a 15-foot cone. Each creature in that area must\
    \ make a DC 12 Dexterity saving throw, taking 10 (3d6) fire damage on a failed\
    \ save, or half as much damage on a successful one."
  "name": "Fire Breath (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/crimson-drake-tob1-2023.webp"
```
^statblock

## Environment

farmland, forest
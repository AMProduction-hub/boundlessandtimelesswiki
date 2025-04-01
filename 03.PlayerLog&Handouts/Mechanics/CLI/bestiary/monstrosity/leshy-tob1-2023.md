---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Leshy"]
---
# [Leshy](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/leshy-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 251*  

*This strange man is covered in bark and root-like growths and wears loose scraps of clothing. The hair and beard that frame his piercing green eyes writhe like living vines.*

## Expanding the Wild

Solitary leshy tend plants and animals in groves around great forests, and they are the self-proclaimed protectors of the forest outskirts. Leshy have little patience for interlopers and often kill, abduct, or frighten off trailblazers and guides. They sabotage cultivated land, wipe out trails, and cultivate weed walls and thickets to keep civilization at bay. They transplant dangerous plant creatures to discourage new settlements, and some wrangle rabid animals to the same purpose.

## Ax Thieves

Leshy prefer trickery to combat, leading intruders astray by mimicking animal and humanoid sounds. If challenged, they do everything in their power to scare intruders away, but they never hesitate to fight to the death in service to the forest if necessary. Leshy hate metal, especially axes, and they go out of their way to steal metal items and lead those who use them astray.

## Accept Bribes

With careful courting and appropriate gifts, it is possible to gain a leshy's capricious assistance. This can be risky, because leshy love mischief. Still, a leshy's help is sometimes essential to a group traversing ancient woodlands.

```statblock
"name": "Leshy (ToB1-2023)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Chaotic Neutral"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "45"
"hit_dice": "7d8 + 14"
"stats":
- !!int "16"
- !!int "12"
- !!int "14"
- !!int "14"
- !!int "15"
- !!int "16"
"speed": "30 ft."
"skillsaves":
  "Deception": !!int "5"
  "Stealth": !!int "3"
  "Perception": !!int "4"
  "Survival": !!int "4"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Common, Elvish, Sylvan"
"cr": "1"
"traits":
- "desc": "The leshy can mimic animal sounds and Humanoid voices. A creature that\
    \ hears the sounds can tell they are imitations with a successful DC 15 Wisdom\
    \ ([Insight](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Insight))\
    \ check."
  "name": "Mimicry"
- "desc": "The leshy has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks it makes in any terrain with ample obscuring plant life."
  "name": "Plant Camouflage"
- "desc": "The leshy can communicate with Beasts and Plants as if they shared a language."
  "name": "Speak with Beasts and Plants"
- "desc": "The poisonous vines growing from the leshy entwine around its weapon. When\
    \ the leshy hits with any weapon, the weapon deals an extra 2d4 poison damage\
    \ (included in the attack)."
  "name": "Vine-Wrapped Weapons"
- "desc": "Difficult terrain composed of magical or nonmagical plants doesn't cost\
    \ the leshy extra movement."
  "name": "Woodland Stride"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4\
    \ + 3) bludgeoning damage plus 5 (2d4) poison damage."
  "name": "Club"
- "desc": "The leshy briefly appears to grow to an enormous size, taking on a malicious\
    \ mien before returning to normal. Each creature within 15 feet of the leshy and\
    \ that can see it must succeed on a DC 13 Wisdom saving throw or be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success. A creature is immune to Frightening Mien\
    \ if it can see through illusions."
  "name": "Frightening Mien (Recharge 5-6)"
- "desc": "The leshy whispers magical words of growth to nonmagical plants on a point\
    \ it can see within 30 feet of it. The plants burst with life and spread rapidly.\
    \ The area within 20 feet of that point becomes difficult terrain for 24 hours."
  "name": "Encourage Growth (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/leshy-tob1-2023.webp"
```
^statblock

## Environment

forest
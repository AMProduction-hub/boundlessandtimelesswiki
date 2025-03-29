---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/nkosi
- ttrpg-cli/monster/type/humanoid/shapechanger
statblock: inline
aliases: ["Nkosi"]
---
# [Nkosi](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/nkosi-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 286*  

*With a thick mane of beaded locks, this leonine humanoid grins with a mouthful of pointed teeth.*

## Beads and Braids

The nkosi resemble bestial humans with cat's eyes, slender tails, and the fangs and fur of a lion. Most grow their hair long, braiding colorful beads into their locks to mark important events in their lives. Although the nkosi's true form is that of a feline humanoid with leonine features, the most striking feature of the nkosi is their ability to change their shape, taking the form of a lion.

## Pridelords

Nkosi pridelords are exceptionally tall and muscular leaders. They keep impressive manes, but they are known for their roar, which wakes the feral heart inside all nkosi.

```statblock
"name": "Nkosi (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"subtype": "nkosi, shapechanger"
"alignment": "Lawful Neutral"
"ac": !!int "15"
"ac_class": "[studded leather](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/studded-leather-armor.md)"
"hp": !!int "27"
"hit_dice": "5d8 + 5"
"stats":
- !!int "16"
- !!int "16"
- !!int "12"
- !!int "10"
- !!int "10"
- !!int "8"
"speed": "30 ft. (50 ft. in lion form)"
"skillsaves":
  "Survival": !!int "2"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Common (can't speak in lion form)"
"cr": "1/2"
"traits":
- "desc": "The nkosi has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on smell."
  "name": "Keen Smell"
- "desc": "If the nkosi moves at least 20 feet straight toward a creature and then\
    \ hits it with a Mambele attack on the same turn, that target must succeed on\
    \ a DC 13 Strength saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ If the target is [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
    \ the nkosi can make one Bite attack against it as a bonus action."
  "name": "Pounce"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6\
    \ + 3) piercing damage."
  "name": "Bite"
- "desc": "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 6 (1d6 + 3) piercing damage."
  "name": "Mambele (Humanoid Form Only)"
"bonus_actions":
- "desc": "The nkosi transforms into a Large lion or back into its true form, which\
    \ is Humanoid. Its statistics, other than its size, speed, and AC, are the same\
    \ in each form. Any equipment it is wearing or carrying isn't transformed. It\
    \ reverts to its true form if it dies."
  "name": "Change Shape"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/nkosi-tob1-2023.webp"
```
^statblock

## Environment

forest, grassland
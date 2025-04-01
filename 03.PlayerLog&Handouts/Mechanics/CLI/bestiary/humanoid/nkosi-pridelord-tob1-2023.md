---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/nkosi
- ttrpg-cli/monster/type/humanoid/shapechanger
statblock: inline
aliases: ["Nkosi Pridelord"]
---
# [Nkosi Pridelord](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/nkosi-pridelord-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 286*  

*With a thick mane of beaded locks, this leonine humanoid grins with a mouthful of pointed teeth.*

## Beads and Braids

The nkosi resemble bestial humans with cat's eyes, slender tails, and the fangs and fur of a lion. Most grow their hair long, braiding colorful beads into their locks to mark important events in their lives. Although the nkosi's true form is that of a feline humanoid with leonine features, the most striking feature of the nkosi is their ability to change their shape, taking the form of a lion.

## Pridelords

Nkosi pridelords are exceptionally tall and muscular leaders. They keep impressive manes, but they are known for their roar, which wakes the feral heart inside all nkosi.

```statblock
"name": "Nkosi Pridelord (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"subtype": "nkosi, shapechanger"
"alignment": "Lawful Neutral"
"ac": !!int "16"
"ac_class": "[studded leather](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/studded-leather-armor.md)"
"hp": !!int "82"
"hit_dice": "15d8 + 15"
"stats":
- !!int "18"
- !!int "18"
- !!int "12"
- !!int "10"
- !!int "10"
- !!int "14"
"speed": "30 ft. (50 ft. in lion form)"
"skillsaves":
  "Survival": !!int "2"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Common (can't speak in lion form)"
"cr": "4"
"traits":
- "desc": "A melee weapon deals one extra die of its damage when the pridelord hits\
    \ with it (included in the attack)."
  "name": "Brute"
- "desc": "The pridelord has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on smell."
  "name": "Keen Smell"
- "desc": "If the pridelord moves at least 20 feet straight toward a creature and\
    \ then hits it with a Mambele attack on the same turn, that target must succeed\
    \ on a DC 14 Strength saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ If the target is [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
    \ the pridelord can make one Bite attack against it as a bonus action."
  "name": "Pounce"
"actions":
- "desc": "The pridelord makes three Bite or Mambele attacks. It can replace one attack\
    \ with a use of Pridelord's Roar, if available."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) piercing damage."
  "name": "Bite"
- "desc": "Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 7 (1d6 + 4) piercing damage or 11 (2d6 + 4) piercing\
    \ damage if used to make a melee attack."
  "name": "Mambele (Humanoid Form Only)"
- "desc": "Each nkosi of the pridelord's choice within 30 feet of it that can hear\
    \ it has advantage on the next attack roll it makes before the start of the pridelord's\
    \ next turn."
  "name": "Pridelord's Roar (Recharge 4-6)"
"bonus_actions":
- "desc": "The pridelord transforms into a Large lion or back into its true form,\
    \ which is Humanoid. Its statistics, other than its size, speed, and AC, are the\
    \ same in each form. Any equipment it is wearing or carrying isn't transformed.\
    \ It reverts to its true form if it dies."
  "name": "Change Shape"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/nkosi-pridelord-tob1-2023.webp"
```
^statblock

## Environment

forest, grassland
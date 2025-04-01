---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fiend/devil
statblock: inline
aliases: ["Spawn of Arbeyach"]
---
# [Spawn of Arbeyach](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/spawn-of-arbeyach-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 91*  

*This insectile humanoid's mouth stretches over dripping mandibles that are poorly concealed behind an ill-fitting mask of flesh. Its eyes have compound irises, and barbed stingers sprout between the fingers at the ends of its long, segmented limbs.*

Spawn of Arbeyach are extensions of the will of Hell's Prince of Swarms, Arbeyach, and often serve him in the mortal world as the arch-devil carries out their master's wishes. To this end, they often inhabit hives of tosculi that worship Arbeyach.

## Skin and Carapace

Spawn of Arbeyach are roughly humanoid, with many insectoid qualities, including a hardened carapace and oddly-jointed limbs. Their faces, arms, and legs are covered with a largely decorative skin which stretches and tears to reveal insectile traits.

## Hive Dwellers

They dwell in hive structures comprised of natural growth and rigid architecture. The hives are built in isolated, easily-defensible locales, and visitors often must climb or fly to reach them.

```statblock
"name": "Spawn of Arbeyach (ToB1-2023)"
"size": "Medium"
"type": "fiend"
"subtype": "devil"
"alignment": "Lawful Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "78"
"hit_dice": "12d8 + 24"
"stats":
- !!int "18"
- !!int "15"
- !!int "15"
- !!int "10"
- !!int "13"
- !!int "12"
"speed": "40 ft., climb 20 ft."
"saves":
  "Wisdom": !!int "4"
"skillsaves":
  "Stealth": !!int "5"
  "Perception": !!int "4"
"damage_resistances": "cold; bludgeoning, piercing, slashing from nonmagical attacks\
  \ that aren't silvered"
"damage_immunities": "fire, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., tremorsense 60 ft., passive Perception 14"
"languages": "Infernal"
"cr": "5"
"traits":
- "desc": "Magical darkness doesn't impede the spawn's darkvision."
  "name": "Devil's Sight"
- "desc": "While the spawn is within 60 feet of at least one member of its hive, it\
    \ has advantage on initiative rolls and on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks. The spawn can't be surprised if at least one other member is aware of\
    \ the danger and within 300 feet of it."
  "name": "Hive Bond"
- "desc": "The spawn has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The spawn can communicate with insects as if they shared a language."
  "name": "Speak with Insects"
"actions":
- "desc": "The spawn of Arbeyach makes one Bite attack and one Stinger attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) piercing damage plus 4 (1d8) poison damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 6 (1d4\
    \ + 4) piercing damage plus 13 (3d8) poison damage. If the target is a creature,\
    \ it must succeed on a DC 13 Constitution saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Stinger"
- "desc": "The spawn of Arbeyach magically calls 1d4 swarms of insects. The called\
    \ creatures arrive in 1d4 rounds, acting as allies of the spawn and obeying\
    \ its spoken commands. The insects remain for 1 hour, until the spawn dies, or\
    \ until the spawn dismisses them as a bonus action."
  "name": "Children of Arbeyach (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/spawn-of-arbeyach-tob1-2023.webp"
```
^statblock

## Environment

forest, hill
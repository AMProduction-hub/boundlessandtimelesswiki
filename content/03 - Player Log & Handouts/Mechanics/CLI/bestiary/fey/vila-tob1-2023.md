---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Vila"]
---
# [Vila](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/vila-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 386*  

*A woman with hair the color of spring grass, skin like polished wood, and eyes as gray as a storm rides through the forest on the back of a large deer.*

## Dryad Cousins

The vila are kin to the dryads, and like their cousins, they serve as protectors of the deepest forests.

## Demand Oaths

Where dryads beguile to accomplish their goals, the vila coerce and threaten. They demand oaths from interlopers and enforce the oaths fiercely. Vila delight in testing the virtue of travelers and in tormenting the uncharitable and cruel with misfortune.

## Hunt with a Pack

Vila rarely travel or fight alone; they are often seen in the company of alseid, wolves, wampus cats, or deer. In combat, they sometimes ride fleet-footed deer, the better to harry opponents or escape if events turn against them.

```statblock
"name": "Vila (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Lawful Neutral"
"ac": !!int "15"
"hp": !!int "77"
"hit_dice": "14d8 + 14"
"stats":
- !!int "12"
- !!int "20"
- !!int "13"
- !!int "11"
- !!int "14"
- !!int "16"
"speed": "30 ft."
"saves":
  "Charisma": !!int "6"
  "Wisdom": !!int "5"
  "Constitution": !!int "4"
"skillsaves":
  "Intimidation": !!int "6"
  "Animal Handling": !!int "8"
  "Stealth": !!int "8"
  "Insight": !!int "5"
  "Perception": !!int "8"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"senses": "darkvision 60 ft., passive Perception 18"
"languages": "Common, Sylvan"
"cr": "5"
"traits":
- "desc": "Difficult terrain composed of nonmagical plants doesn't cost the vila extra\
    \ movement, and it can pass through nonmagical plants without being slowed by\
    \ them and without taking damage from them if they have thorns, spines, or a similar\
    \ hazard. In addition, while in forested terrain, the vila has advantage on initiative\
    \ rolls."
  "name": "Forest's Defender"
- "desc": "The vila's weapons are coated with a magical poison harvest from the forest.\
    \ When the vila hits with any weapon, the weapon deals an extra 2d6 poison damage\
    \ (included in the attack)."
  "name": "Poisoned Weapons"
- "desc": "The vila can communicate with Beasts as if they shared a language."
  "name": "Speak with Beasts"
"actions":
- "desc": "The vila can use its Song of the Forest. It then makes two Shortsword or\
    \ Shortbow attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 8 (1d6\
    \ + 5) piercing damage plus 7 (2d6) poison damage."
  "name": "Shortsword"
- "desc": "Ranged Weapon Attack: +8 to hit, range 80/320 ft., one target. Hit:\
    \ 8 (1d6 + 5) piercing damage plus 7 (2d6) poison damage."
  "name": "Shortbow"
- "desc": "The vila sings one of the following songs at up to three creatures it can\
    \ see within 30 feet of it. Each target that can hear the song must succeed on\
    \ a DC 14 Wisdom saving throw or suffer the song's effect.\n\n- Ancient Lullaby.\
    \ Each creature that fails the saving throw falls [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ for 1 minute. The [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ creature wakes up if it takes damage or if another creature takes an action\
    \ to shake it awake.  \n- Fascinating Melody. Each creature that fails the\
    \ saving throw is [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the end of its next turn.  \n- Luckless Tune. Each creature that fails\
    \ the saving throw has disadvantage on attack rolls and ability checks until the\
    \ end of its next turn.  "
  "name": "Song of the Forest"
- "desc": "The vila magically calls 1d4 wolves or 1 wampus cat. The called creatures\
    \ arrive in 1d4 rounds, acting as allies of the vila and obeying its spoken\
    \ commands. The creatures remain for 1 hour, until the vila dies, or until the\
    \ vila dismisses them as a bonus action."
  "name": "Denizens of the Wilds (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/vila-tob1-2023.webp"
```
^statblock

## Environment

forest
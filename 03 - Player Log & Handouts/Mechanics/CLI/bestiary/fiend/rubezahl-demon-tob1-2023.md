---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fiend/demon
statblock: inline
aliases: ["Rubezahl Demon"]
---
# [Rubezahl Demon](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/rubezahl-demon-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 87*  

*A pair of immense, branching antlers arches above this man's coldly gleaming eyes, and wicked claws tip his long fingers.*

## Assume Mortal Form

Rubezahls are capricious creatures with an affinity for weather, particularly lightning. Like the ever-changing weather, they are driven by constantly shifting motivations and mannerisms. They are consummate tricksters who delight in taking the form of innocuous mortals, like traveling monks, tinkers, or lost merchants. They love to play the friend with their nearly undetectable lies, slipping into the confidence of unsuspecting mortals before murdering them.

## Counting Demons

Rubezahls have a weakness, however. They are known as counting demons, and a savvy mortal who knows its nature can confound one with groups of objects: a handful of coins, a basket of apples, even a bed of flowers. If the objects are clearly pointed out to the rubezahl, the creature becomes distracted until it counts each item in the group. Unfortunately for mortals, rebezahls can count startlingly fast; even a mound of gravel takes no more than a few moments for a rubezahl to assess. Rubezahl loathe being compelled this way, and they are driven to annihilate any mortal bold enough to exploit this weakness.

```statblock
"name": "Rubezahl Demon (ToB1-2023)"
"size": "Medium"
"type": "fiend"
"subtype": "demon"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "136"
"hit_dice": "21d8 + 42"
"stats":
- !!int "20"
- !!int "15"
- !!int "14"
- !!int "11"
- !!int "12"
- !!int "18"
"speed": "50 ft."
"saves":
  "Dexterity": !!int "6"
  "Wisdom": !!int "5"
  "Constitution": !!int "6"
"skillsaves":
  "Deception": !!int "8"
  "Perception": !!int "5"
  "Survival": !!int "5"
"damage_resistances": "cold; fire; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"damage_immunities": "lightning, poison, thunder"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)"
"senses": "blindsight 10 ft., darkvision 120 ft., passive Perception 15"
"languages": "Abyssal, Common, telepathy 120 ft."
"cr": "10"
"traits":
- "desc": "The rubezahl casts one of the following spells, requiring no material components\
    \ and using Charisma as the spellcasting ability (spell save DC 16):\n\nAt will:\
    \ [disguise self](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/disguise-self.md),\
    \ [fog cloud](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fog-cloud.md)\n\
    \n1/day: [control weather](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/control-weather.md)\
    \ (as an action)\n\n3/day each: [gust of wind](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/gust-of-wind.md),\
    \ [sleet storm](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/sleet-storm.md)"
  "name": "Spellcasting"
- "desc": "If a creature uses an action to point out an ordered group of objects that\
    \ the rubezahl can see, such as a pile of gravel, the demon is compelled to count\
    \ the entire group. Until the end of its next turn, the rubezahl has disadvantage\
    \ on attack rolls and ability checks, and it can't take reactions. Once it has\
    \ counted a given group of objects, it can't be compelled to count those objects\
    \ again."
  "name": "Counting Compulsion"
- "desc": "The rubezahl has advantage on Charisma ([Deception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Deception))\
    \ checks. In addition, magical attempts to discern lies always report that the\
    \ rubezahl's words are true, and it can't be magically forced to tell the truth."
  "name": "False Tongue"
- "desc": "The rubezahl has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The rubezahl makes one Gore attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 15\
    \ (3d6 + 5) slashing damage plus 7 (2d6) lightning damage."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 18\
    \ (3d8 + 5) piercing damage, and the target creature must succeed on a DC 16\
    \ Strength saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Gore"
- "desc": "The rubezahl calls a sizzling bolt of lightning out of the sky, or from\
    \ the air if underground or indoors, to strike a point the rubezahl can see within\
    \ 150 feet of it. Each creature within 20 feet of that point must make a DC 16\
    \ Dexterity saving throw. On a failure, the creature takes 36 (8d8) lightning\
    \ damage and is [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the end of its next turn. On a success, the creature takes half the damage\
    \ and isn't [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)."
  "name": "Thunderstrike (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/rubezahl-demon-tob1-2023.webp"
```
^statblock

## Environment

farmland, urban
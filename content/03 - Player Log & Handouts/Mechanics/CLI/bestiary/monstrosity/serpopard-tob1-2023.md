---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Serpopard"]
---
# [Serpopard](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/serpopard-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 322*  

*The spotted and scaly quadruped runs on hairless leonine paws, while its draconic head perches atop a sinuous, serpentine neck.*

## Swaying, Snakelike Cats

Serpopards are 13 feet long and weigh 600 pounds, with little gender dimorphism. They have feline bodies but long, serpentine necks topped by vaguely draconic heads. Their hairless paws have wickedly curved, retractable talons. A serpopard's neck is in constant motion, swaying like a cobra, allowing it to track foes on all sides and to strike in unexpected directions.

## Easily Distracted

Serpopards are foul-tempered predators and scavengers, and they are known to occasionally cannibalize their weakest pack mate. They actively hunt humanoids when possible and also attack other predators to steal their kills—or to kill and eat the predators, then take their kills. Serpopards are not tenacious hunters, however. They can be distracted from a pursuit by the appearance of an easier meal.

## Musk Glands

In some culture, serpopard pelts and musk glands are prized for use in fashion and perfumes. Images of these odd animals appear regularly in ancient tomb iconography and temple decoration.

```statblock
"name": "Serpopard (ToB1-2023)"
"size": "Large"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "85"
"hit_dice": "10d10 + 30"
"stats":
- !!int "17"
- !!int "16"
- !!int "16"
- !!int "2"
- !!int "12"
- !!int "6"
"speed": "40 ft., swim 30 ft."
"skillsaves":
  "Stealth": !!int "5"
  "Perception": !!int "3"
"damage_resistances": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": ""
"cr": "4"
"traits":
- "desc": "The serpopard has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in sandy, muddy, or swampy terrain."
  "name": "Coastal Camouflage"
- "desc": "The serpopard gets two extra reactions that can be used only for opportunity\
    \ attacks."
  "name": "Sinuous Strikeback"
"actions":
- "desc": "The serpopard makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 12\
    \ (2d8 + 3) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10\
    \ (2d6 + 3) slashing damage."
  "name": "Claw"
- "desc": "The serpopard releases foul-smelling musk in a 15-foot cone. Each creature\
    \ in that area must make a DC 13 Dexterity saving throw. On a failure, a creature\
    \ takes 21 (6d6) poison damage and is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 hour or until it spends 10 minutes washing off the musk. On a success,\
    \ a creature takes half the damage and isn't [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ While a creature is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way, any creature that starts its turn within 5 feet of the [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature must succeed on a DC 13 Dexterity saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its turn."
  "name": "Musk (Recharges after a Short or Long Rest)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/serpopard-tob1-2023.webp"
```
^statblock

## Environment

coastal, swamp
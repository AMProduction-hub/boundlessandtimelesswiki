---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Savager"]
---
# [Savager](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/savager-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 318*  

*A porcupine-quilled creature built like a grizzly bear with claws and fangs like scimitars rises on its hind legs. Its forelegs are mangled and scabbed, and its eyes shine with hatred and anticipation.*

## Driven by Dark Spirits

While many druids claim these bear-like animals are not cursed or enchanted, the savager's habit of killing any living creature on sight is not natural behavior. Hunger doesn't explain their attacks, since savagers eat only part of their kills before abandoning the meal and looking for other animals to attack. Some dark forest spirit drives them.

## Gnaws Itself

When there are no other creatures nearby to attack, a savager gnaws on its own forelimbs, resulting in scabs, scars, and calluses so thick and numb that they protect the savager from even the sharpest of swords.

## Rare Meetings

The only creature a savager won't attack on sight is another savager, giving each other a wide berth or meeting briefly to produce young. A savager litter contains anywhere from ten to twenty-five cubs, all of them born able to walk and fend for themselves.

```statblock
"name": "Savager (ToB1-2023)"
"size": "Large"
"type": "beast"
"alignment": "Neutral Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "105"
"hit_dice": "10d10 + 50"
"stats":
- !!int "22"
- !!int "14"
- !!int "21"
- !!int "2"
- !!int "10"
- !!int "13"
"speed": "40 ft., climb 20 ft."
"saves":
  "Dexterity": !!int "5"
  "Constitution": !!int "8"
"skillsaves":
  "Perception": !!int "3"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": ""
"cr": "8"
"traits":
- "desc": "If the savager doesn't move during its turn, it has advantage on the next\
    \ Claw attack it makes before the start of its next turn."
  "name": "Mighty Swing"
- "desc": "A creature that touches the savager or hits it with a melee attack while\
    \ within 5 feet of it takes 5 (2d4) piercing damage. In addition, a creature\
    \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by or grappling the savager takes 5 (2d4) piercing damage at the start of\
    \ the savager's turn."
  "name": "Spines"
"actions":
- "desc": "The savager makes one Bite attack and two Claw attacks. If both Claw attacks\
    \ hit one creature, the target must succeed on a DC 15 Strength saving throw or\
    \ take 9 (2d8) slashing damage as the savager rips into the target."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 19\
    \ (2d12 + 6) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 15\
    \ (2d8 + 6) slashing damage."
  "name": "Claw"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/savager-tob1-2023.webp"
```
^statblock

## Environment

forest
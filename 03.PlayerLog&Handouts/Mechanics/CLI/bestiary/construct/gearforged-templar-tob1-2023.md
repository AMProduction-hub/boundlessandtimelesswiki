---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Gearforged Templar"]
---
# [Gearforged Templar](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/gearforged-templar-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 196*  

*The bronze and mithral figure advances with heavy movements. Its eye lenses glare a golden hue, and gears click when it swings its greatsword.*

## Mechanical Champion

An intricate construction of bronze, steel, copper, and mithral, the gearforged templar is an imposing sight. A humanoid spirit contained in a soulgem animates the heavy body of gears and springs. Gearforged are relatively rare, and the templar is a paragon among them.

## Tireless Defender

The gearforged templar is relentless in pursuit of its duty. More so than other gearforged, the templar becomes fixed on its charge to the exclusion of distractions and even magical coercion. Gearforged templars serve as commanders of military or guard units, bodyguards for important individuals, or personal champions for nobility.

```statblock
"name": "Gearforged Templar (ToB1-2023)"
"size": "Medium"
"type": "construct"
"alignment": "Lawful Neutral"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "71"
"hit_dice": "11d8 + 22"
"stats":
- !!int "19"
- !!int "9"
- !!int "15"
- !!int "12"
- !!int "16"
- !!int "10"
"speed": "30 ft."
"saves":
  "Dexterity": !!int "2"
  "Constitution": !!int "5"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Common"
"cr": "6"
"traits":
- "desc": "The gearforged templar doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
"actions":
- "desc": "The gearforged templar makes four Greatsword or Javelin attacks. If two\
    \ Greatsword attacks hit one creature, the target must succeed on a DC 15 Strength\
    \ saving throw or be pushed up to 10 feet away from the templar. The templar can\
    \ choose not to push a creature."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) slashing damage."
  "name": "Greatsword"
- "desc": "Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 30/120\
    \ ft., one target. Hit: 7 (1d6 + 4) piercing damage."
  "name": "Javelin"
- "desc": "The gearforged templar whirls its greatsword in a great arc. Each creature\
    \ within 10 feet of the gearforged must make a DC 15 Dexterity saving throw, taking\
    \ 27 (5d10) slashing damage on a failed save, or half as much damage on a successful\
    \ one."
  "name": "Whirlwind (Recharge 5-6)"
"reactions":
- "desc": "When a creature enters the gearforged templar's reach, the templar makes\
    \ one Greatsword attack against the creature."
  "name": "Defensive Zone"
- "desc": "The gearforged templar adds 3 to its AC against one melee attack that would\
    \ hit it. To do so, the templar must be able to see the attacker and must be wielding\
    \ a melee weapon."
  "name": "Parry"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/gearforged-templar-tob1-2023.webp"
```
^statblock

## Environment

urban
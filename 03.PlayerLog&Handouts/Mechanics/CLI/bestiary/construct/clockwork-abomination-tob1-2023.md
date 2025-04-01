---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Clockwork Abomination"]
---
# [Clockwork Abomination](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/clockwork-abomination-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 59*  

*The pile of debris and scrap on the ground suddenly rises, revealing a large insectoid form with smoke rising between the plates of its hide. Its many orange-yellow eyes shine like dim lanterns and reveal no hint of expression or intent.*

## Bound Devils

Clockwork abominations result from ill-considered attempts to bind lesser devils into clockwork or steam-driven constructs. The disciplines of devil-binding and engineering seemingly do not mix well, and the results are typically disastrous. Every now and then, however, something goes right, and a clockwork abomination is created.

## Junk Collectors

Clockwork abominations are canny enough to collect bits of old wagons, tools, or machinery as camouflage. Motionless among such debris and with a deceptively long reach due to pistons in their limbs, they can surprise foes with a sudden attack.

## Sadistic Machines

Malevolent in the extreme, these fiendish automatons are frustrated by the limits of their forms, and they delight in inflicting suffering on others. Constantly seeking to break free of their creators' control, the most they can be entrusted to do is serve as a guardian or to attack something.

```statblock
"name": "Clockwork Abomination (ToB1-2023)"
"size": "Large"
"type": "construct"
"alignment": "Lawful Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "76"
"hit_dice": "8d10 + 32"
"stats":
- !!int "21"
- !!int "12"
- !!int "18"
- !!int "10"
- !!int "10"
- !!int "12"
"speed": "30 ft., climb 30 ft."
"saves":
  "Dexterity": !!int "4"
  "Constitution": !!int "7"
"skillsaves":
  "Athletics": !!int "8"
  "Stealth": !!int "4"
  "Perception": !!int "3"
"damage_resistances": "acid; cold; fire; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Common, Infernal"
"cr": "5"
"traits":
- "desc": "The clockwork abomination doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "When a clockwork abomination is destroyed, its infernal battery explodes.\
    \ Each creature within 10 feet of the abomination must make a DC 14 Dexterity\
    \ saving throw, taking 14 (4d6) fire damage on a failed save, or half as much\
    \ damage on a successful one. The explosion ignites flammable objects in the area\
    \ that aren't being worn or carried."
  "name": "Explosive Infernal Power Source"
- "desc": "The clockwork abomination is immune to any spell or effect that would alter\
    \ its form."
  "name": "Immutable Form"
- "desc": "The clockwork abomination has advantage on saving throws against spells\
    \ and other magical effects."
  "name": "Magic Resistance"
- "desc": "Moving through difficult terrain doesn't cost the clockwork abomination\
    \ extra movement, and its speed can't be reduced."
  "name": "Unstoppable"
"actions":
- "desc": "The clockwork abomination makes one Bite attack and one Slam attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 14\
    \ (2d8 + 5) piercing damage plus 7 (2d6) fire damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +8 to hit, reach 15 ft., one target. Hit: 12\
    \ (2d6 + 5) bludgeoning damage."
  "name": "Slam"
- "desc": "The clockwork abomination's infernal power source allows it to breathe\
    \ fire in a 30-foot cone. Each creature in the area must make a DC 14 Dexterity\
    \ saving throw, taking 21 (6d6) fire damage on a failed save, or half as much\
    \ damage on a successful one."
  "name": "Fire Breath (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/clockwork-abomination-tob1-2023.webp"
```
^statblock

## Environment

planar
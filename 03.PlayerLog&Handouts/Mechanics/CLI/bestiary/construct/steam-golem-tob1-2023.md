---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/13
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Steam Golem"]
---
# [Steam Golem](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/steam-golem-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 220*  

*With wicked axe blades fastened along its arms and bronze runes inlaid on its armored torso, this golem is a smooth-running machine of death.*

## Boilers and Hydraulics

A steam golem is built around a central boiler with clockwork gears and hydraulic cylinders powering its legs and arms. Most steam golems have axe blades welded onto each of their arms, and many have one arm extended in a single, long-hafted axe. They tower 10 feet tall, and their legs are often built with reversed knee joints for greater leverage when they move. The eyes of a steam golem glow orange or red from its internal fires.

## Steam Whistle

A steam golem has four to six vents for releasing steam. These whistles are mounted over the shoulders and can be heard at distances up to a mile in open terrain.

## Fuel Required

A steam golem's machinery consumes 30 pounds of coal and 100 gallons of water per day if it engages in more than brief combat. When resting or standing guard, a steam golem needs only one third of those amounts.

```statblock
"name": "Steam Golem (ToB1-2023)"
"size": "Large"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "171"
"hit_dice": "18d10 + 72"
"stats":
- !!int "26"
- !!int "12"
- !!int "18"
- !!int "3"
- !!int "10"
- !!int "1"
"speed": "40 ft."
"damage_immunities": "fire; poison; psychic; bludgeoning, piercing, slashing from\
  \ nonmagical attacks that aren't adamantine"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., passive Perception 10"
"languages": "understands the languages of its creator but can't speak"
"cr": "13"
"traits":
- "desc": "If the steam golem starts its turn immersed in water, or if it was soaked\
    \ with at least 20 gallons of water on its previous turn, it risks losing steam\
    \ pressure in its boiler. The steam golem must succeed on a DC 20 Constitution\
    \ saving throw or its internal fire is extinguished. Until its internal fire is\
    \ relit, the golem's speed is halved, its AC is reduced by 2, and it must repeat\
    \ the saving throw at the start of each of its turns. On a failure, it stops repeating\
    \ this saving throw and becomes dormant, effectively dead until the fire is relit.\
    \ A Medium or smaller creature within 5 feet of the golem can take an action to\
    \ relight the golem's internal fire, making it active again."
  "name": "Boiler Weakness"
- "desc": "The golem doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The steam golem's weapon attacks are magical. When the golem hits with\
    \ any weapon, the weapon deals an extra 4d8 fire damage (included in the attack)."
  "name": "Heated Weapons"
- "desc": "The golem is immune to any spell or effect that would alter its form."
  "name": "Immutable Form"
- "desc": "The golem has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The steam golem makes one Axe Arm attack and one Long Axe attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 22\
    \ (4d6 + 8) slashing damage plus 18 (4d8) fire damage."
  "name": "Axe Arm"
- "desc": "Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 26\
    \ (4d8 + 8) slashing damage plus 18 (4d8) fire damage."
  "name": "Long Axe"
- "desc": "The steam golem releases a blast of steam in a 30-foot cone or in a 10-foot-radius\
    \ cloud that extends from it, spreading around corners. Each creature in the area\
    \ must make a DC 17 Dexterity saving throw, taking 54 (12d8) fire damage on\
    \ a failed save, or half as much damage on a successful one."
  "name": "Steam Blast (Recharge 5-6)"
"reactions":
- "desc": "When a creature the steam golem can see within 30 feet of it casts a spell,\
    \ the steam golem emits a shriek from its twin steam whistles. The spellcaster\
    \ must succeed on a DC 17 Constitution saving throw or the spell fails and has\
    \ no effect."
  "name": "Whistle (Recharge 4-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/steam-golem-tob1-2023.webp"
```
^statblock

## Environment

urban
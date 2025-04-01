---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/badlands
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Gray Thirster"]
---
# [Gray Thirster](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/gray-thirster-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 221*  

*This dried-out body of a long dead traveler is still clad in the tattered remains of its clothes. Its skin, as dry as parchment, clings to its bones, and a hoarse moaning emanates from its dry, cracked lips.*

## Thirsting Undead

The greatest danger to people traversing badlands and deserts is thirst, and even the best prepared can find themselves without water. The lucky ones die quickly, while those less fortunate linger in sun-addled torment for days. These souls sometimes rise from the sand as gray thirsters, driven to inflict the torment they suffered upon other travelers.

## Destroy Wells and Oases

Gray thirsters destroy or foul sources of water and often lurk near such sources to ambush those seeking clean water.

## Thirsting Caravan

Though they hunt alone, in at least one case an entire caravan died of thirst and rose again as gray thirsters. Called the dust caravan, it prowls the deep desert accompanied by skin-changing gnolls, shrieking ghouls, and a mummy lord, building a strange, nomadic army.

```statblock
"name": "Gray Thirster (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "13"
"hp": !!int "52"
"hit_dice": "8d8 + 16"
"stats":
- !!int "12"
- !!int "16"
- !!int "15"
- !!int "6"
- !!int "12"
- !!int "14"
"speed": "30 ft."
"skillsaves":
  "Stealth": !!int "5"
"damage_resistances": "necrotic"
"damage_immunities": "fire, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "understands the languages it knew in life but can't speak"
"cr": "2"
"traits":
- "desc": "A creature that starts its turn within 30 feet of the gray thirster must\
    \ succeed on a DC 12 Constitution saving throw or suffer one level of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion).\
    \ On a successful saving throw, the creature is immune to the gray thirster's\
    \ Thirst Aura for the next 24 hours."
  "name": "Thirst Aura"
- "desc": "The gray thirster doesn't require air, food, or sleep."
  "name": "Thirsting Dead Nature"
"actions":
- "desc": "The gray thirster makes two Claw attacks, or it makes one Claw attack and\
    \ one Withering Turban attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4\
    \ + 3) slashing damage."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +5 to hit, reach 10 ft., one creature. Hit:\
    \ 7 (1d8 + 3) necrotic damage. The target must succeed on a DC 12 Constitution\
    \ saving throw or its hp maximum is reduced by an amount equal to the damage taken.\
    \ The target has disadvantage on this saving throw if it failed the saving throw\
    \ against the thirster's Thirst Aura. This reduction lasts until the target finishes\
    \ a long rest with no levels of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion).\
    \ The target dies if this effect reduces its hp maximum to 0."
  "name": "Withering Turban"
- "desc": "The gray thirster draws the moisture from containers and creatures around\
    \ it. Nonmagical water and other liquids within 20 feet of the thirster that aren't\
    \ being worn or carried turn to dust. Each creature within 20 feet of the thirster\
    \ that isn't a Construct or Undead must make a DC 12 Constitution saving throw.\
    \ On a failure, a creature takes 9 (2d8) necrotic damage and up to 5 gallons\
    \ of nonmagical liquid it is wearing or carrying turn to dust. On a success, a\
    \ creature takes half the damage, and nonmagical liquids it is wearing or carrying\
    \ don't turn to dust. Plants, Oozes, creatures with the Amphibious or Water Breathing\
    \ trait, and creatures made mostly of water, such as water elementals or steam\
    \ mephitis, have disadvantage on the saving throw."
  "name": "Drought (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/gray-thirster-tob1-2023.webp"
```
^statblock

## Environment

badlands, desert
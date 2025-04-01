---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/gnoll
statblock: inline
aliases: ["Gnoll Havoc Runner"]
---
# [Gnoll Havoc Runner](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/gnoll-havoc-runner-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 212*  

*A sprinting gnoll laughs as it runs, axe held high and flashing in the sun.*

With the bristly mane and spotted fur characteristic of all gnolls, havoc runners blend into their tribe. Only the canny glint in the eyes hints at the deadly difference before the havoc runner explodes into violence.

## Blinding Raids

Havoc runners are scouring storms across the trade routes that crisscross the tribe's territory. Like all gnolls, they are deadly in battle. Havoc runners incorporate another quality that makes them the envy of many raiders: they can tell at a glance which pieces of loot from a laden camel or wagon are the most valuable, without spending time rummaging, weighing, or evaluating. Their ability to strike into a caravan, seize the best items, and withdraw quickly is unparalleled.

```statblock
"name": "Gnoll Havoc Runner (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"subtype": "gnoll"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "[chain shirt](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/chain-shirt.md)"
"hp": !!int "58"
"hit_dice": "9d8 + 18"
"stats":
- !!int "16"
- !!int "14"
- !!int "14"
- !!int "8"
- !!int "12"
- !!int "9"
"speed": "30 ft."
"skillsaves":
  "Athletics": !!int "5"
  "Perception": !!int "5"
"senses": "darkvision 60 ft., passive Perception 15"
"languages": "Gnoll"
"cr": "3"
"traits":
- "desc": "If the gnoll attacks more than one creature in the same turn, the first\
    \ target has disadvantage on attack rolls until the end of its next turn."
  "name": "Harrying Attacks"
- "desc": "The gnoll has advantage on attack rolls against a creature if at least\
    \ one of the gnoll's allies is within 5 feet of the creature and the ally isn't\
    \ [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Pack Tactics"
"actions":
- "desc": "The gnoll makes one Bite attack and two Battleaxe attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8\
    \ + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands."
  "name": "Battleaxe"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6\
    \ + 3) piercing damage."
  "name": "Bite"
"bonus_actions":
- "desc": "The gnoll takes the Dash or Disengage action."
  "name": "Lightning Lope"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/gnoll-havoc-runner-tob1-2023.webp"
```
^statblock

## Environment

desert, grassland
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Putrid Haunt"]
---
# [Putrid Haunt](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/putrid-haunt-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 296*  

*This shambling corpse has twigs, branches, and other debris intertwined with its body. Its gaping maw crawls with scrabbling vermin.*

## Swamp Undead

Putrid haunts are walking corpses infused with moss, mud, and the detritus of the deep swamp. They are the shambling remains of individuals who, either through mishap or misdeed, died while lost in a vast swampland. Their desperate need to escape the marshland in life transforms into a hatred of all living beings in death. They often gather in places tainted by evil deeds.

## Mossy Islands

When no potential victims are nearby, putrid haunts sink into the water and muck, where moss and water plants grow over them and vermin inhabit their rotting flesh. When living creatures draw near, the dormant putrid haunt bursts from its watery hiding spot and attacks its prey, stomping foes deep into the muck. There's no planning and little cunning in their assault, but they move through the marshes more freely than most intruders, and they attack with a single-mindedness that's easily mistaken for purpose.

## Harbor Vermin

Putrid haunt corpses create favorable conditions for leeches, insects, and other swamp vermin. They are often hosts or hiding places for large gatherings of such creatures.

```statblock
"name": "Putrid Haunt (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "44"
"hit_dice": "8d8 + 8"
"stats":
- !!int "17"
- !!int "8"
- !!int "13"
- !!int "3"
- !!int "11"
- !!int "6"
"speed": "30 ft., swim 20 ft."
"damage_resistances": "bludgeoning, piercing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "understands the language it knew in life but can't speak"
"cr": "2"
"traits":
- "desc": "While the putrid haunt remains motionless and [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ in swampy terrain, it is indistinguishable from a pile of muck and moss."
  "name": "False Appearance"
- "desc": "Difficult terrain composed of mud, shallow water, and water plants doesn't\
    \ cost the putrid haunt extra movement."
  "name": "Swamp Walk"
- "desc": "The putrid haunt doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d8 + 3) bludgeoning damage plus 5 (2d4) poison damage."
  "name": "Slam"
- "desc": "The putrid haunt vomits forth the leeches, stinging insects, and other\
    \ swamp vermin infesting its innards in a 15-foot cone. Each creature in the area\
    \ must make a DC 13 Dexterity saving throw. On a failure, a creature takes 7 (2d6)\
    \ piercing damage and 7 (2d6) poison damage and is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Expel Vermin (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/putrid-haunt-tob1-2023.webp"
```
^statblock

## Environment

swamp
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/trollkin
statblock: inline
aliases: ["Trollkin Reaver"]
---
# [Trollkin Reaver](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/trollkin-reaver-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 371*  

*The humanoid's skin is thick and knobby, and it sports wicked talons and tusks.*

In the north, the masses huddle in fear at night, dreading the horns and howls of reavers come to slaughter and pillage.

## Fearsome Savages

Trollkin have a well-deserved reputation for savagery, and the reavers help reinforce that perception among their neighbors. With claws and fangs larger and sharper than their brethren, reavers are a sight to behold.

## War Leaders

Raiding is a staple industry among the trollkin, and the reavers lead the most savage raiding parties in search of wealth, slaves, and supplies. They often recruit other creatures or mercenaries into their bands. It is not uncommon to see bloodthirsty humans, gnolls, or hobgoblins in a reaver's band.

## Spirit Talkers

Trollkin reavers are quite fearful of spirits and ghosts, and they listen to their clan shaman and to the words of powerful fey or giants. They prefer to raid only in times of good omens.

```statblock
"name": "Trollkin Reaver (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"subtype": "trollkin"
"alignment": "Neutral"
"ac": !!int "14"
"ac_class": "[hide armor](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/hide-armor.md)"
"hp": !!int "82"
"hit_dice": "11d8 + 33"
"stats":
- !!int "19"
- !!int "13"
- !!int "16"
- !!int "11"
- !!int "12"
- !!int "13"
"speed": "30 ft."
"saves":
  "Constitution": !!int "5"
"skillsaves":
  "Intimidation": !!int "5"
  "Survival": !!int "3"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Common, Trollkin"
"cr": "4"
"traits":
- "desc": "The trollkin reaver regains 5 hp at the start of its turn. If the trollkin\
    \ takes acid or fire damage, this trait doesn't function at the start of the trollkin's\
    \ next turn. The trollkin dies if it starts its turn with 0 hp and doesn't regenerate."
  "name": "Regeneration"
- "desc": "The trollkin reaver's skin is thick and tough, granting it a +1 bonus to\
    \ Armor Class. This bonus is already factored into the trollkin's AC."
  "name": "Thick Hide"
"actions":
- "desc": "The trollkin raider makes one Bite attack and two Claw attacks, or it makes\
    \ three Handaxe attacks. It can replace one Claw attack with a Battleaxe attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4\
    \ + 4) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4\
    \ + 4) slashing damage."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8\
    \ + 4) slashing damage, or 9 (1d10 + 4) slashing damage if used with two hands."
  "name": "Battleaxe"
- "desc": "Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 7 (1d6 + 4) slashing damage."
  "name": "Handaxe"
- "desc": "The trollkin reaver howls a battle cry at up to three friendly creatures\
    \ it can see within 30 feet of it. Each target can make one weapon attack as a\
    \ reaction and has advantage on the attack roll."
  "name": "Howl of Battle (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/trollkin-reaver-tob1-2023.webp"
```
^statblock

## Environment

any
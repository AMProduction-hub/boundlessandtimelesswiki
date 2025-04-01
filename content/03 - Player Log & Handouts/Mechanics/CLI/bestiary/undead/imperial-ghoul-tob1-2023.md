---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Imperial Ghoul"]
---
# [Imperial Ghoul](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/imperial-ghoul-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 203*  

*An imperial ghoul stands tall and proud, its gray flesh robust and muscled, and its clothing strangely well kept. Its flickering red eyes have an intelligent, malicious gleam.*

## Shock Troops

Imperial ghouls are the shock troops of the ghoul empire, eager to expand its power and influence. Treated like auxiliaries, they get the most difficult tasks: to engage and hold foes while the darakhul, iron legionnaires, and others outflank them.

## Ambitious Strivers

Many believe that the hunger cults or the necrophagi know some secret of transforming imperial ghouls into iron ghouls. This rumor gives them hope of advancement. Their power over the lesser ghouls and slaves gives them a taste of tyranny. Because they are ambitious and always hungry for power, imperial ghouls are eager to prove themselves as hunters, as warriors, and as spies.

## Immune to Sun

Unlike a standard darakhul, an imperial ghoul does not suffer from sunlight and feels little need to disguise its true appearance.

> [!note] Darakhul Fever
> 
> Spread mainly through bite wounds, this disease makes itself known within 24 hours by swiftly debilitating the infected. An infected creature must make a DC 17 Constitution saving throw after every long rest. On a failed save, the victim takes 14 (`4d6`) necrotic damage, and its hp maximum is reduced by an amount equal to the damage taken. This reduction lasts until the victim finishes a long rest after the disease is cured. The victim recovers from the disease by making two consecutive successful saving throws. Greater restoration cures the disease, while lesser restoration gives the victim advantage on the next saving throw. Primarily spread among Humanoids, the disease can affect ogres, and therefore other Giants may be susceptible. If a creature dies while infected with darakhul fever, roll a `d20`, add the character's Constitution modifier, and find the result on the Adjustment Table below to determine what Undead form the victim's body rises in.
> 
> | Roll | Result |
> |------|--------|
> | 1-9 | None; victim is simply dead |
> | 10-16 | Ghoul |
> | 17-20 | Ghast |
> | 21+ | Darakhul |
> ^roll-result
^darakhul-fever

```statblock
"name": "Imperial Ghoul (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Lawful Evil"
"ac": !!int "16"
"ac_class": "[breastplate](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/breastplate.md)"
"hp": !!int "93"
"hit_dice": "17d8 + 17"
"stats":
- !!int "16"
- !!int "14"
- !!int "12"
- !!int "13"
- !!int "14"
- !!int "14"
"speed": "30 ft., burrow 15 ft."
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": "Common, Darakhul, Undercommon"
"cr": "4"
"traits":
- "desc": "The ghoul requires no air or sleep."
  "name": "Hungry Dead Nature"
- "desc": "The ghoul and any ghouls within 30 feet of it have advantage on saving\
    \ throws against effects that turn Undead."
  "name": "Turning Defiance"
"actions":
- "desc": "The imperial ghoul makes one Bite attack and one Claw attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d8 + 3) piercing damage, and, if the target is a Humanoid, it must succeed\
    \ on a DC 11 Constitution saving throw or contract the darakhul fever disease."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +5 to hit, reach, one target. Hit: 17 (4d6\
    \ + 3) slashing damage. If the target is a creature other than an elf or Undead,\
    \ it must succeed on a DC 11 Constitution saving throw or be [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ for 1 minute. The target can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success."
  "name": "Claw"
- "desc": "Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit:\
    \ 6 (1d8 + 2) piercing damage."
  "name": "Light Crossbow"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/imperial-ghoul-tob1-2023.webp"
```
^statblock

## Environment

underdark
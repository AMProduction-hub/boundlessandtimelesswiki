---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Iron Ghoul"]
---
# [Iron Ghoul](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/iron-ghoul-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 204*  

*A vicious-looking ghoul carries a cruel glaive, its forearms stained with dried blood. Its glowing, rust-colored eyes penetrate with a calculating stare of restrained hunger.*

## Backbone of the Legions

Iron ghouls and ghasts are the elite members of the imperial legions, acting as officers, non-commissioned officers, and standard-bearers. They feed from the slave pits and march on the orders of the darakhul nobility.

## Fond of Uniforms

Iron ghouls are proud of their status and uniforms. Their standard breastplates and open-faced helms are black iron with brass trim, and the helm's crest is often a ruby-dyed fan of bat wings or carrion beetle bristles to indicate their authority.

## Tooth and Bone Weaponry

Many items of an iron ghoul's gear are decorated with inlaid bone or set with teeth, much as pearls might be used for weapons crafted elsewhere.

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
"name": "Iron Ghoul (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Lawful Evil"
"ac": !!int "16"
"ac_class": "[breastplate](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/breastplate.md)"
"hp": !!int "143"
"hit_dice": "22d8 + 44"
"stats":
- !!int "18"
- !!int "16"
- !!int "14"
- !!int "14"
- !!int "14"
- !!int "14"
"speed": "30 ft., burrow 20 ft."
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": "Common, Darakhul, Undercommon"
"cr": "5"
"traits":
- "desc": "The ghoul requires no air or sleep."
  "name": "Hungry Dead Nature"
- "desc": "The iron ghoul and any ghouls within 30 feet of it have advantage on saving\
    \ throws against effects that turn Undead."
  "name": "Turning Defiance"
"actions":
- "desc": "The iron ghoul makes one Bite attack and one Claw attack, or it makes three\
    \ Glaive attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 17\
    \ (3d8 + 4) piercing damage. If the target is a Humanoid, it must succeed on\
    \ a DC 13 Constitution saving throw or contract the darakhul fever disease."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 18\
    \ (4d6 + 4) slashing damage. If the target is a creature other than an elf or\
    \ Undead, it must succeed on a DC 13 Constitution saving throw or be [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ for 1 minute. The target can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 9\
    \ (1d10 + 4) slashing damage."
  "name": "Glaive"
- "desc": "Ranged Weapon Attack: +6 to hit, range 100/400, one target. Hit:\
    \ 8 (1d10 + 3) piercing damage."
  "name": "Heavy Crossbow"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/iron-ghoul-tob1-2023.webp"
```
^statblock

## Environment

underdark
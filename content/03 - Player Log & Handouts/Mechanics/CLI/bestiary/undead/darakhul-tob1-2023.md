---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Darakhul"]
---
# [Darakhul](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/darakhul-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 202*  

*Intelligence gleams in the eyes of the well-dressed ghoul. It smiles a greeting, barely revealing sharp teeth.*

## Imperial Cunning

In the lightless depths, an empire of devouring ambition grows and plots and dreams. They call themselves the People, but the people of the surface world call them the Lords Subterranean, the Ghoul Imperium, or simply the Empire of the Ghouls. To them, if you are not a member of the People, you are food.

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
"name": "Darakhul (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "18"
"ac_class": "[scale mail](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/scale-mail.md),\
  \ [shield](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/shield.md)"
"hp": !!int "78"
"hit_dice": "12d8 + 24"
"stats":
- !!int "16"
- !!int "17"
- !!int "14"
- !!int "14"
- !!int "12"
- !!int "12"
"speed": "30 ft."
"skillsaves":
  "Deception": !!int "3"
  "Stealth": !!int "5"
"damage_resistances": "necrotic"
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Common, Darakhul"
"cr": "3"
"traits":
- "desc": "The darakhul requires no air or sleep."
  "name": "Hungry Dead Nature"
- "desc": "A darakhul in a prepared disguise has advantage on Charisma ([Deception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Deception))\
    \ checks made to pass as a living creature. While using this ability, it loses\
    \ its Stench."
  "name": "Master of Disguise"
- "desc": "Any creature that starts its turn within 5 feet of the darakhul must succeed\
    \ on a DC 12 Constitution saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the start of its next turn. If a creature's saving throw is successful\
    \ or the effect ends for it, the creature is immune to the darakhul's Stench for\
    \ the next 24 hours. A darakhul using this ability can't also benefit from Master\
    \ of Disguise."
  "name": "Stench"
- "desc": "While in sunlight, the darakhul has disadvantage on attack rolls, as well\
    \ as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
- "desc": "The darakhul and any ghouls within 30 feet of it have advantage on saving\
    \ throws against effects that turn Undead."
  "name": "Turning Defiance"
"actions":
- "desc": "The darakhul makes one Bite attack, one Claw attack, and one War Pick attack.\
    \ If the darakhul is using a shield, it instead makes one Bite attack and one\
    \ Claw or War Pick attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d8 + 3) piercing damage, and, if the target is a Humanoid, it must succeed\
    \ on a DC 11 Constitution saving throw or contract the darakhul fever disease."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10\
    \ (2d6 + 3) slashing damage. If the target is a creature other than an Undead,\
    \ it must succeed on a DC 12 Constitution saving throw or be [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ for 1 minute. A [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ target can repeat the saving throw at the end of each of its turns, ending the\
    \ effect on itself on a success. If a Humanoid is [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ for more than 2 rounds, it contracts darakhul fever."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8\
    \ + 3) piercing damage."
  "name": "War Pick"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/darakhul-tob1-2023.webp"
```
^statblock

## Environment

underdark, urban
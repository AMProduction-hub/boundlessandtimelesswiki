---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Lorelei"]
---
# [Lorelei](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/lorelei-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 258*  

*Lounging on a large river rock, this breathtaking fey calls plaintively to travelers.*

## Death to Men

A people born from an ancient oath to the River King, the loreleis' cruelty stems from whatever happened to their people long ago that brought about their transformation into loreleis. Now, these callous river sirens compete with one another in manipulating and destroying male travelers, using their deadly kisses to great effect.

## Beautiful Humanoids

Although legends describe the lorelei as golden-haired and fair-skinned, they come in all varieties, taking on the form of their most frequent prey. While most resemble sensual humans, a lorelei's form can include elf, dwarf, and, in some recorded cases, even orc or hobgoblin.

## Ignore Women

Women travelers are vexing for the lorelei. While the siren's powers affect women as readily as men, the lorelei lacks the urge to destroy them. Women traveling alone or in all-female groups may pass through a lorelei's territory safely, and they might even make peaceful contact.

```statblock
"name": "Lorelei (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"hp": !!int "93"
"hit_dice": "11d8 + 44"
"stats":
- !!int "10"
- !!int "21"
- !!int "18"
- !!int "16"
- !!int "16"
- !!int "21"
"speed": "30 ft., swim 30 ft."
"saves":
  "Charisma": !!int "8"
  "Dexterity": !!int "8"
"skillsaves":
  "Deception": !!int "8"
  "Performance": !!int "8"
  "Persuasion": !!int "8"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Common, Sylvan"
"cr": "5"
"traits":
- "desc": "When a Humanoid that can see the lorelei starts its turn within 30 feet\
    \ of the lorelei, the lorelei can force it to make a DC 15 Wisdom saving throw\
    \ if the lorelei isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ and can see the Humanoid. On a failed save, the Humanoid is [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ until the start if its next turn. While [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
    \ the target is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ and must move on its turn toward the lorelei by the most direct route, trying\
    \ to get within 5 feet of the lorelei for a kiss from her. The Humanoid doesn't\
    \ avoid opportunity attacks, but before moving into damaging terrain, such as\
    \ lava or a pit, and whenever it takes damage, the Humanoid can repeat the saving\
    \ throw. If the saving throw is successful, the effect ends for it, and it regains\
    \ its senses for the remainder of its turn.\n\nUnless surprised, a Humanoid can\
    \ avert its eyes to avoid the saving throw at the start of its turn. If the Humanoid\
    \ does so, it can't see the lorelei until the start of its next turn, when it\
    \ can avert its eyes again. If the Humanoid looks at the lorelei in the meantime,\
    \ it must immediately make the save."
  "name": "Alluring Presence"
- "desc": "The lorelei can breathe air and water."
  "name": "Amphibious"
- "desc": "While in contact with water, the lorelei ignores difficult terrain, and\
    \ magical effects can't reduce her speed or cause her to be [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ In addition, she can spend 5 feet of movement to escape from nonmagical restraints\
    \ or being [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)."
  "name": "Free Water Spirit"
"actions":
- "desc": "The lorelei can use her Stunning Glance. She then makes three Psychic Blast\
    \ attacks. She can replace one attack with a use of Corrupted Kiss."
  "name": "Multiattack"
- "desc": "Melee Spell Attack: +8 to hit, reach 5 ft., one willing creature, or\
    \ a creature that is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ or [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ Hit: 14 (2d8 + 5) necrotic damage, and the lorelei regains hp equal to that\
    \ amount."
  "name": "Corrupted Kiss"
- "desc": "Melee or Ranged Spell Attack: +8 to hit, reach 5 ft. or range 60 ft.,\
    \ one target. Hit: 12 (2d6 + 5) psychic damage."
  "name": "Psychic Blast"
- "desc": "The lorelei sends a seductive glance at a creature she can see within 30\
    \ feet of her. The target must succeed on a DC 15 Wisdom saving throw or be [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the end of its next turn. On a successful save, a creature is immune to\
    \ this lorelei's Stunning Glance for the next 24 hours."
  "name": "Stunning Glance"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/lorelei-tob1-2023.webp"
```
^statblock

## Environment

forest, underwater
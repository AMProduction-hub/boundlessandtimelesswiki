---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Skein Witch"]
---
# [Skein Witch](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/skein-witch-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 328*  

*The androgynous humanoid appears mummified in writhing, diamond thread. Its skin is translucent, and dozens of quivering hourglasses sit suspended inside its body in place of organs.*

## Shepherd Destiny

Skein witches are curators of destiny and enforcers of what must be. They voyage across the planes, weaving the strands of fate at the behest of their goddess-creator. Although they carry out their charge without regard to petty mortal concerns, they can be persuaded to bend fate for powerful petitioners whose interests align with those of their goddess.

## Surrounded by Guardians

Despite their supernatural abilities, a skein witch's physical body is frail. Because of that, they tend to surround themselves with undead, constructs, or other brutish, soulless guardians cut free from the thread of fate.

## Fear of Cards

If a deck of many things is brought close to a skein witch, the witch emits a psychic wail and disintegrates.

```statblock
"name": "Skein Witch (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "20"
"ac_class": "natural armor"
"hp": !!int "162"
"hit_dice": "25d8 + 50"
"stats":
- !!int "6"
- !!int "12"
- !!int "14"
- !!int "16"
- !!int "20"
- !!int "20"
"speed": "30 ft., fly 30 ft."
"saves":
  "Charisma": !!int "9"
  "Wisdom": !!int "9"
  "Intelligence": !!int "7"
"skillsaves":
  "Insight": !!int "13"
  "Perception": !!int "13"
  "History": !!int "7"
"damage_resistances": "radiant"
"damage_immunities": "fire, lightning, psychic"
"senses": "truesight 60 ft., passive Perception 23"
"languages": "Celestial, telepathy 120 ft."
"cr": "12"
"traits":
- "desc": "If the skein witch fails a saving throw, it can choose to succeed instead."
  "name": "Fate's Resistance (3/Day)"
- "desc": "The skein witch has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The skein witch makes three Inexorable Thread attacks. If two Inexorable\
    \ Thread attacks hit one creature, the target must succeed on a DC 17 Constitution\
    \ saving throw or have disadvantage on the next death saving throw it makes before\
    \ it finishes a short rest. If a creature fails this saving throw multiple times,\
    \ these effects are cumulative, affecting up to three of the creature's next death\
    \ saving throws before it finishes a short rest."
  "name": "Multiattack"
- "desc": "Melee or Ranged Spell Attack: +9 to hit, reach 5 ft. or range 60 ft.,\
    \ one creature. Hit: 27 (5d8 + 5) radiant damage."
  "name": "Inexorable Thread"
- "desc": "The skein witch frays the strands of fate in a 60-foot cone. Each creature\
    \ in the area must make a DC 17 Wisdom saving throw, taking 55 (10d10) force\
    \ damage on a failed save, or half as much damage on a successful one. If any\
    \ creature that failed the saving throw is affected by a condition, such as [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ or [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
    \ those conditions are randomly redistributed among all the creatures that failed\
    \ the saving throw."
  "name": "Destiny Distortion Wave (Recharge 5-6)"
- "desc": "One creature within 60 feet of the skein witch must succeed on a DC 17\
    \ Wisdom saving throw or the target's fate is bound to one of its ally's (chosen\
    \ at random). Any damage or condition the target suffers is inflicted on the individual\
    \ to which they are bound instead, and vice versa. A creature can be bound to\
    \ only one other creature at a time. This binding lasts until lifted by a heal\
    \ or [heroes' feast](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/heroes-feast.md)\
    \ spell or similar magic."
  "name": "Bind Fates (1/Day)"
"bonus_actions":
- "desc": "The skein witch teleports, along with any equipment it is wearing or carrying,\
    \ up to 30 feet to an unoccupied space it can see. A tiny hourglass shatters into\
    \ a swirl of sand at the origin and destination when it uses this bonus action."
  "name": "Fate's Step"
"reactions":
- "desc": "If the skein witch succeeds on a saving throw against a spell of 4th level\
    \ or lower that targets only the skein witch, the spell has no effect. If the\
    \ skein witch succeeds on the saving throw by 5 or more, the spell is reflected\
    \ back at the spellcaster, using the slot level, spell save DC, attack bonus,\
    \ and spellcasting ability of the caster."
  "name": "Parry Spell"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/skein-witch-tob1-2023.webp"
```
^statblock

## Environment

planar
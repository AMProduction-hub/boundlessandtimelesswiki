---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
aliases: ["Priest"]
---
# [Priest](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/priest.md)
*Source: Monster Manual p. 348, Baldur's Gate: Descent Into Avernus, Tasha's Cauldron of Everything, Sigil and the Outlands. Available in the <span title='Systems Reference Document (5.1)'>SRD</span> and the Basic Rules (2014)*  

Priests bring the teachings of their gods to the common folk. They are the spiritual leaders of temples and shrines and often hold positions of influence in their communities. Evil priests might work openly under a tyrant, or they might be the leaders of religious sects hidden in the shadows of good society, overseeing depraved rites. A priest typically has one or more acolytes to help with religious ceremonies and other sacred duties.

```statblock
"name": "Priest"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Any alignment"
"ac": !!int "13"
"ac_class": "[chain shirt](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/chain-shirt.md)"
"hp": !!int "27"
"hit_dice": "5d8 + 5"
"stats":
- !!int "10"
- !!int "10"
- !!int "12"
- !!int "13"
- !!int "16"
- !!int "13"
"speed": "30 ft."
"skillsaves":
  "Medicine": !!int "7"
  "Religion": !!int "5"
  "Persuasion": !!int "3"
"senses": "passive Perception 13"
"languages": "any two languages"
"cr": "2"
"traits":
- "desc": "The priest is a 5th-level spellcaster. Its spellcasting ability is Wisdom\
    \ (spell save DC 13, +5 to hit with spell attacks). The priest has the following\
    \ cleric spells prepared:\n\nCantrips (at will): [light](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/light.md),\
    \ [sacred flame](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/sacred-flame.md),\
    \ [thaumaturgy](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/thaumaturgy.md)\n\
    \n1st level (4 slots): [cure wounds](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/cure-wounds.md),\
    \ [guiding bolt](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/guiding-bolt.md),\
    \ [sanctuary](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/sanctuary.md)\n\
    \n2nd level (3 slots): [lesser restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/lesser-restoration.md),\
    \ [spiritual weapon](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/spiritual-weapon.md)\n\
    \n3rd level (2 slots): [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md),\
    \ [spirit guardians](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/spirit-guardians.md)"
  "name": "Spellcasting"
- "desc": "As a bonus action, the priest can expend a spell slot to cause its melee\
    \ weapon attacks to magically deal an extra 10 (3d6) radiant damage to a target\
    \ on a hit. This benefit lasts until the end of the turn. If the priest expends\
    \ a spell slot of 2nd level or higher, the extra damage increases by 1d6 for\
    \ each level above 1st."
  "name": "Divine Eminence"
"actions":
- "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6)\
    \ bludgeoning damage."
  "name": "Mace"
"source":
- "MM"
- "BGDIA"
- "TCE"
- "SatO"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/priest.webp"
```
^statblock

## Environment

urban
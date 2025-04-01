---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/11
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Dullahan"]
---
# [Dullahan](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/dullahan-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 151*  

*The black horse strides out of the shadows with its nostrils huffing steam. Its rider, swathed in black leather, raises its arm to reveal not a lantern but its own severed, grinning head.*

Though it appears to be a headless rider astride a black horse, the dullahan is a single creature. The fey spirit takes the shape of a horse rider holding its own head aloft like a lantern, or (more rarely) the form of an ogre cradling its head in one arm.

## Harbingers of Death

Hailing from the darkest of fey courts, the dullahan are macabre creatures that walk hand in hand with death. They sometimes serve powerful fey lords and ladies, riding far and wide in the capacity of a herald, bard, or ambassador. More often than not they carry doom to a wretch who roused their lord's ire.

```statblock
"name": "Dullahan (ToB1-2023)"
"size": "Large"
"type": "fey"
"alignment": "Lawful Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "178"
"hit_dice": "17d10 + 85"
"stats":
- !!int "19"
- !!int "18"
- !!int "20"
- !!int "13"
- !!int "15"
- !!int "17"
"speed": "60 ft."
"skillsaves":
  "Intimidation": !!int "7"
  "Perception": !!int "6"
  "Survival": !!int "6"
  "Persuasion": !!int "7"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "necrotic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "truesight 60 ft., passive Perception 16"
"languages": "Common, Elvish, Sylvan"
"cr": "11"
"traits":
- "desc": "When a creature that can see the eyes of the dullahan's severed head starts\
    \ its turn within 30 feet of the dullahan, the dullahan can force it to make a\
    \ DC 17 Wisdom saving throw if the dullahan isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ and can see the creature. On a failed save, the creature is [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ until the start of its next turn. While [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ in this way, the creature must take the Dash action and move away from the dullahan\
    \ by the safest available route. A doomed creature that fails this saving throw\
    \ is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ while [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ instead.\n\nUnless surprised, a creature can avert its eyes to avoid the saving\
    \ throw at the start of its turn. If the creature does so, it can't see the dullahan\
    \ until the start of its next turn, when it can avert its eyes again. If the creature\
    \ looks at the dullahan in the meantime, it must immediately make the save."
  "name": "Baleful Glare"
- "desc": "Moving through difficult terrain doesn't cost the dullahan extra movement,\
    \ and the dullahan can move across the surface of water as if it were harmless,\
    \ solid ground."
  "name": "Relentless Advance"
- "desc": "The dullahan doesn't require food, drink, or sleep."
  "name": "Relentless Nature"
"actions":
- "desc": "The dullahan makes three Spine Whip or Necrotic Bolt attacks. It can replace\
    \ one attack with a use of Seal the Doom."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 11\
    \ (2d6 + 4) slashing damage plus 10 (3d6) necrotic damage. If the target is\
    \ a creature, it must succeed on a DC 17 Constitution saving throw or fall [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ as it is wracked with pain."
  "name": "Spine Whip"
- "desc": "Ranged Spell Attack: +7 to hit, range 120 ft., one target. Hit: 21\
    \ (4d8 + 3) necrotic damage."
  "name": "Necrotic Bolt"
- "desc": "The dullahan points at a creature doomed by Deathly Doom within 40 feet\
    \ of it that it can see. The creature must make a DC 17 Constitution saving throw.\
    \ On a failure, the target immediately drops to 0 hp if it is below half its hp\
    \ maximum. On a success, the target is immune to the dullahan's Seal the Doom\
    \ for the next 24 hours."
  "name": "Seal the Doom"
"bonus_actions":
- "desc": "The dullahan magically dooms a creature for 1 hour. It can have only one\
    \ creature doomed at a time. If it dooms another, the effect on the previous target\
    \ ends. The dullahan knows the direction to the doomed creature as long as both\
    \ are on the same plane of existence."
  "name": "Deathly Doom"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/dullahan-tob1-2023.webp"
```
^statblock

## Environment

any, forest
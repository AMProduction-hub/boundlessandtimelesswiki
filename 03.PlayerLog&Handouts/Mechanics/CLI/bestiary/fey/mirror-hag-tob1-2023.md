---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Mirror Hag"]
---
# [Mirror Hag](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/mirror-hag-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 227*  

*This hunchbacked crone's sallow skin is covered with growths and lesions.*

## Hideous Hex

Until a creature can see past the hag's deformities, she curses it with the pain of a disfigured life. Some mirror hags do this for the betterment of all, but most do it because causing pain amuses them.

## Warped Features

Mirror hags are hunchbacked, with growths and lesions covering their skin. Their joints misalign, and the extremities of their bones press against their skin. However, it is their faces that inspire legends: the blackest moles sprouting long white hairs, noses resembling half-eaten carrots, and eyes mismatched in size, color, and alignment. If a creature recoils from a mirror hag's looks, she bestows her reconfiguring curse on it.

## Mirror Covens

Mirror hags can form a coven with two other hags. Generally, mirror hags only form covens with other mirror hags, but from time to time a mirror hag will join a coven of witches or green hags.

```statblock
"name": "Mirror Hag (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Chaotic Neutral"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "147"
"hit_dice": "14d8 + 84"
"stats":
- !!int "15"
- !!int "16"
- !!int "22"
- !!int "12"
- !!int "14"
- !!int "19"
"speed": "30 ft., fly 10 ft."
"damage_resistances": "thunder"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": "Common, Sylvan"
"cr": "6"
"traits":
- "desc": "The blood hag casts one of the following spells, requiring no material\
    \ components and using Charisma as the spellcasting ability (spell save DC 15):\n\
    \nAt will: [disguise self](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/disguise-self.md),\
    \ [ray of enfeeblement](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/ray-of-enfeeblement.md)\n\
    \n1/day each: [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md),\
    \ [locate creature](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/locate-creature.md)"
  "name": "Spellcasting"
- "desc": "Any Humanoid that starts its turn within 60 feet of the hag and can see\
    \ the hag's true form must succeed on a DC 15 Wisdom saving throw or be [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ until the start of its next turn. If the Humanoid's saving throw is successful,\
    \ it is immune to the hag's Confounding Ugliness for the next 24 hours.\n\nUnless\
    \ the target is surprised or the revelation of the hag's true form is sudden,\
    \ the target can avert its eyes to avoid the saving throw at the start of its\
    \ turn. If the Humanoid does so, it can't see the hag until the start of its next\
    \ turn, when it can avert its eyes again. If the Humanoid looks at the hag in\
    \ the meantime, it must immediately make the save."
  "name": "Confounding Ugliness"
"actions":
- "desc": "The mirror hag can use her Reconfiguring Curse. She then makes one Bite\
    \ attack and two Claw attacks. She can replace her Bite attack with a use of Spellcasting."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d8 + 3) piercing damage plus 5 (2d4) necrotic damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6\
    \ + 3) slashing damage plus 5 (2d4) necrotic damage."
  "name": "Claw"
- "desc": "The mirror hag curses one creature she can see within 60 feet of her, corrupting\
    \ its form. The target must make a DC 15 Constitution saving throw. On a success,\
    \ the target is immune to the hag's Reconfiguring Curse for the next 24 hours.\
    \ On a failure, the target is cursed, suffering one of the following effects of\
    \ the hag's choice:\n\n- Disfigured. The target's skin erupts with growths\
    \ and lesions, and it has disadvantage on all Charisma checks made to influence\
    \ Humanoids, except for [Intimidation](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Intimidation).\
    \  \n- Sickly. The target becomes frail and unhealthy, and it has disadvantage\
    \ on Constitution saving throws. It regains only half its lost hp at the end of\
    \ a long rest, and it halves the result of any Hit Dice rolled to restore hp during\
    \ a short rest.  \n- Twisted. The target's limbs and spine become bent and\
    \ clumsy. It has disadvantage on all Dexterity checks and Dexterity saving throws,\
    \ and its speed is reduced by 10 feet.  \n- Withered. The target's muscles\
    \ atrophy, and it has disadvantage on all Strength checks and Strength saving\
    \ throws.  "
  "name": "Reconfiguring Curse"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/mirror-hag-tob1-2023.webp"
```
^statblock

## Environment

forest, urban
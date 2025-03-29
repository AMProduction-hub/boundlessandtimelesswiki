---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Vile Barber"]
---
# [Vile Barber](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/vile-barber-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 387*  

*A pale, scrawny fellow clad in a black leather apron and slender ebon gloves grins from the shadows. A maw of needle-sharp teeth and a wicked straight razor at his side are clear warnings that his enemies should hasten their footsteps.*

Vile barbers are sadistic fey who move through the shadows to execute their bloody, malevolent wills. Known as barbers for both the use of wicked blades and their proclivity for slashing the necks of their victims, these insidious fey are found lurking in dark and harrowed places like back-alley streets or abandoned, deep-shaded cemeteries.

## Fey Punishers

Called the siabhra (pronounced she-uvh-ra) among the fey courts, vile barbers are fickle creatures. They are sent to punish those who have offended the fey lords and ladies (see Tome of Beasts), and their cruelty and cunning help them write messages in blood and skin. They scar those who have spoken ill of the fey, and they slowly bleed out those who have harmed or murdered the fey. Some of these deaths are made quite public to reinforce the power of the barber's lord.

## Slippery Fighters

Vile barbers can slip through shadows, catching foes off guard or escaping a foe that has the upper hand. They delight in close combat and in inflicting wounds that terrify onlookers.

## Assassins and Envoys

Vile barbers frequently consort with hags and prowl the places these wicked crones cannot go as emissaries and assassins. Information on the vile barbers is scant; most adventurers who meet them don't live to share the findings or to see the vile barber lick its bloody blade clean.

```statblock
"name": "Vile Barber (ToB1-2023)"
"size": "Small"
"type": "fey"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"hp": !!int "35"
"hit_dice": "10d6"
"stats":
- !!int "12"
- !!int "18"
- !!int "10"
- !!int "10"
- !!int "8"
- !!int "10"
"speed": "30 ft."
"skillsaves":
  "Stealth": !!int "6"
  "Acrobatics": !!int "3"
"condition_immunities": "[frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "darkvision 60 ft., passive Perception 9"
"languages": "Common, Goblin, Sylvan, Umbral"
"cr": "2"
"traits":
- "desc": "The vile barber has advantage on melee attack rolls against any creature\
    \ that doesn't have all its hp."
  "name": "Blood Frenzy"
"actions":
- "desc": "The vile barber makes two Straight Razor attacks. If both attacks hit one\
    \ creature, the target must succeed on a DC 14 Dexterity saving throw or lose\
    \ 3 1d6 hp at the start of each of its turns due to a bleeding wound. The creature\
    \ can repeat the saving throw at the end of each of its turns, ending the effect\
    \ on itself on a success. Any creature can take an action to stanch the wound\
    \ with a successful DC 12 Wisdom ([Medicine](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Medicine))\
    \ check. The wound also closes if the target receives magical healing."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6\
    \ + 4) slashing damage. Instead of dealing damage, the vile barber can steal\
    \ one item the target is wearing or carrying, provided the item weighs no more\
    \ than 10 pounds, isn't a weapon, and isn't wrapped around or firmly attached\
    \ to the target, such as a shirt or armor."
  "name": "Straight Razor"
- "desc": "The vile barber makes one Straight Razor attack against a creature it can\
    \ see within 5 feet of it. If the attack hits and deals damage, the target takes\
    \ an extra 7 (2d6) necrotic damage, and each creature that can see the attack\
    \ within 15 feet of the target must succeed on a DC 14 Wisdom saving throw or\
    \ be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Frightening Cut (Recharge 5-6)"
"bonus_actions":
- "desc": "The vile barber magically teleports, along with any equipment it is wearing\
    \ or carrying, up to 30 feet to an unoccupied space it can see and takes the Hide\
    \ action."
  "name": "Hidden Step"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/vile-barber-tob1-2023.webp"
```
^statblock

## Environment

planar, urban
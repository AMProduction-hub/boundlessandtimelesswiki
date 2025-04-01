---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/19
- ttrpg-cli/monster/environment/badlands
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Shoggoth"]
---
# [Shoggoth](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/shoggoth-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 326*  

*The giant, gelatinous blob of flesh releases whistles, trills, and chirps as it rolls forward, forming and reabsorbing mouths, eyes, and ears across its body.*

A shoggoth is an intelligent, gelatinous blob capable of manipulating and reshaping its body. Created by an elder race as servants, the shoggoths rebelled long ago and slew their masters without pity. Since that time, they've lived in isolated or desolate regions, devouring whatever they encounter and absorbing its flesh into their own amorphous, shifting forms.

## Constant Growth

Shoggoths continue growing throughout their lives, though the eldest among them grow very slowly indeed. Some shoggoths may shrink from starvation if they deplete a territory of resources.

## Mutable Form

A shoggoth can form any number of eyes, mouths, tentacles, or other appendages as needed, though it lacks the control to take and maintain the shape of another creature.

```statblock
"name": "Shoggoth (ToB1-2023)"
"size": "Huge"
"type": "aberration"
"alignment": "Chaotic Neutral"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "325"
"hit_dice": "21d12 + 189"
"stats":
- !!int "26"
- !!int "14"
- !!int "28"
- !!int "12"
- !!int "20"
- !!int "13"
"speed": "50 ft., climb 30 ft., swim 30 ft."
"skillsaves":
  "Perception": !!int "11"
"damage_resistances": "bludgeoning, fire, piercing"
"damage_immunities": "cold, slashing, thunder"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "darkvision 120 ft., tremorsense 60 ft., passive Perception 21"
"languages": "Void Speech"
"cr": "19"
"traits":
- "desc": "The shoggoth doesn't require air."
  "name": "Anaerobic Nature"
- "desc": "When the shoggoth kills a creature while within 15 feet of it, the creature's\
    \ body is absorbed into the shoggoth's. The creature can be restored to life only\
    \ by means of a true resurrection or a [wish](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/wish.md)\
    \ spell."
  "name": "Absorb Flesh"
- "desc": "The shoggoth can move through a space as narrow as 1 foot wide without\
    \ squeezing."
  "name": "Amorphous"
- "desc": "The shoggoth's many mouths constantly emit whistles, fluting, and other\
    \ high-pitched noises. It has disadvantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to be unheard. Each creature that starts its turn within 60 feet\
    \ of the shoggoth and that can hear it must make a DC 19 Wisdom saving throw or\
    \ be disoriented until the start of its next turn. A disoriented creature is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated),\
    \ and when it moves, it moves in a random direction.\n\nUnless surprised, a creature\
    \ can cover its ears to avoid the saving throw at the start of its turn. If the\
    \ creature does so, it can't hear until the start of its next turn, when it can\
    \ cover its ears again. If the creature uncovers its ears in the meantime while\
    \ within 60 feet of the shoggoth, it must immediately make the save. A creature\
    \ that is covering its ears and that has access to cloth, wax, or similar material\
    \ can stuff its ears with the material as a bonus action to free up its hands,\
    \ deafening itself while the material remains stuffed in its ears."
  "name": "Hideous Cacophony"
- "desc": "The shoggoth has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on hearing or smell."
  "name": "Keen Hearing and Smell"
- "desc": "Any spell or effect that would alter the shoggoth's form alters it for\
    \ only 1 round. Afterward, the shoggoth returns to its amorphous blob form."
  "name": "Limited Mutability"
"actions":
- "desc": "The shoggoth makes four Slam attacks. It can replace two Slam attacks with\
    \ a use of Crush."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +14 to hit, reach 15 ft., one target. Hit: 30\
    \ (4d10 + 8) bludgeoning damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 18) if it is a Large or smaller creature."
  "name": "Slam"
- "desc": "The shoggoth crushes up to two creatures it is grappling by rolling them\
    \ beneath its bulk. Each target must succeed on a DC 19 Strength saving throw\
    \ or take 30 (4d10 + 8) bludgeoning damage, be unable to breathe, and be [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ until the grapple ends. If the shoggoth moves, a creature beneath it is no longer\
    \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ and is able to breathe, but it remains [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)."
  "name": "Crush"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/shoggoth-tob1-2023.webp"
```
^statblock

## Environment

badlands, planar
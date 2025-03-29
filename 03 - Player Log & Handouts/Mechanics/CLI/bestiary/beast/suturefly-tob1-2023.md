---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Suturefly"]
---
# [Suturefly](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/suturefly-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 353*  

*This darting creature resembles a dragonfly, but with three pairs of gossamer wings and a body made from splintered wood. Flashes of bright colors run along its body.*

## Sew Mouths Shut

Forest folk rarely speak when sutureflies dart through the trees, because these creatures listen for lies and sew any offender's mouth, nose, and eyes shut. Some say the old woods hide nothing but liars, and that is why the deepest forest is shrouded in silence. Others say that the forest uses sutureflies to smother those who break its covenants or reveal its secrets. Adventurers see a suturefly's handiwork more often than they glimpse one of the creatures directly: corpses with mouths and noses stitched shut lie in the underbrush, mysterious people whose mouths are ringed with black puncture marks observe intruders from afar, and dryads step from trees, their eyes sewn shut against the evils of civilization.

## Seek Out Curses

Numerous suturefly varieties exist. Some attack based on verbal triggers other than lies. Black-banded sutureflies, for instance, detect curses and religious blasphemies. When attacking, sutureflies dart from hiding to surprise opponents. Once they sew someone's mouth closed, they target the same victim's nose, unless threatened by another opponent. Sutureflies attack until they have sewn all of their opponents' mouths, eyes and noses closed or until they're destroyed.

> [!note] Sutureflies in Midgard
> 
> In the Mistwallows of the deep Margreve, a green and gold variety of suturefly attacks briar folk, hags, and any others who allow magic to escape their lips. Sutureflies dart, hover, and strafe with perfect maneuverability. Most are six inches long, but rangers who've ventured deep into the Margreve claim to have discovered detached suturefly wings over 5 feet long, likely from a creature capable of sewing shut the eyes and mouths of giants.
> 
> Folk of the outer Margreve release sutureflies from wooden coffers at forest trials to encourage witnesses to tell the truth. In the heart of the woods, one of Baba Yaga's daughters polices her "flock" of stolen children with sutureflies.
^sutureflies-in-midgard

```statblock
"name": "Suturefly (ToB1-2023)"
"size": "Tiny"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "10"
"hit_dice": "4d4"
"stats":
- !!int "1"
- !!int "15"
- !!int "10"
- !!int "1"
- !!int "12"
- !!int "4"
"speed": "10 ft., fly 40 ft. (hover)"
"skillsaves":
  "Stealth": !!int "4"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": ""
"cr": "1/4"
"traits":
- "desc": "The suturefly knows if it hears a lie and can pinpoint the location of\
    \ a creature within 60 feet of it that lied within the last minute."
  "name": "Detect Lies"
- "desc": "The suturefly has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in forested terrain."
  "name": "Forest Camouflage"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4\
    \ + 2) piercing damage, and the target must succeed on a DC 12 Dexterity saving\
    \ throw or the suturefly sews the target's mouth, nose, or one of its eyes closed\
    \ (the suturefly's choice). With supernatural speed, the suturefly repeatedly\
    \ pierces the target's face, each time threading a loop of the target's own skin\
    \ through the previous hole. These skin loops rapidly blacken, shrink, and draw\
    \ the orifice tightly closed. If a target's mouth is sewn shut, it can't speak.\
    \ If its mouth and nose are sewn shut, it can't breathe, and if both eyes are\
    \ sewn shut, it is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded).\
    \ A creature, including the target, can take its action to cut open one of the\
    \ sewn orifices by succeeding on a DC 12 Dexterity check with an edged weapon\
    \ or tool."
  "name": "Sew"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/suturefly-tob1-2023.webp"
```
^statblock

## Environment

forest
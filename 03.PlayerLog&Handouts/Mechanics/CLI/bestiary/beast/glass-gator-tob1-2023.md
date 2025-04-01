---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Glass Gator"]
---
# [Glass Gator](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/glass-gator-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 211*  

*A near-transparent crocodilian creature leaps from the water, the remnants of its last meal still visible in its transparent gut.*

## Strange Anatomy

The body of a glass gator is most similar to a centipede, but with four oversized forelimbs and a more distinct head. Once the glass gator gets hold of prey, it wraps its body around the victim and squeezes, like a constrictor snake. Unlike a serpent, however, which uses powerful muscles to crush and suffocate its prey, the glass gator is only trying to bring its underbelly into contact with the prey. The glass gator's belly is lined with hundreds of stingers that deliver a virulent nerve toxin.

## Transparency

The glass gator's transparency isn't total. Its digestive tract usually is visible, especially for a few hours after it eats. The creature sometimes uses this limited visibility as bait, making itself appear as a wriggling snake or eel. It is most vulnerable just after eating, when it's lethargic.

## Larval Form

Subterranean variants—including some with bioluminescence—have been reported in caverns. It's been postulated that the glass gator may be the larval form of a larger creature, but what that larger creature might be is unknown.

```statblock
"name": "Glass Gator (ToB1-2023)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "45"
"hit_dice": "7d10 + 7"
"stats":
- !!int "15"
- !!int "14"
- !!int "12"
- !!int "4"
- !!int "10"
- !!int "5"
"speed": "30 ft., swim 50 ft."
"skillsaves":
  "Stealth": !!int "4"
  "Perception": !!int "2"
"senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 12"
"languages": ""
"cr": "1"
"traits":
- "desc": "The glass gator can breathe air and water."
  "name": "Amphibious"
- "desc": "If the glass gator jumps at least 10 feet straight toward a target and\
    \ then hits it with a Claw attack on the same turn, the target must succeed on\
    \ a DC 12 Strength saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ If the target is [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
    \ the gator can make one Constrict attack against it as a bonus action."
  "name": "Constricting Lunge"
- "desc": "The glass gator's long jump is up to 15 feet and its high jump is up to\
    \ 10 feet, with or without a running start."
  "name": "Standing Leap"
- "desc": "The glass gator has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide while underwater or in dim light."
  "name": "Transparent"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6\
    \ + 2) slashing damage."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5\
    \ (1d6 + 2) bludgeoning damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 12). Until the grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ and takes 5 (2d4) poison damage at the start of each of its turns, and the\
    \ glass gator can't use Constrict on another target."
  "name": "Constrict"
"reactions":
- "desc": "When it takes damage while underwater and within 5 feet of the bottom of\
    \ a body of water, the glass gator stirs up a 10-foot-radius sphere of silt centered\
    \ on it. The silt spreads around corners, and its area is heavily obscured. It\
    \ lasts for 1 minute or until a strong current disperses it. The glass gator can\
    \ then swim up to half its speed. The cloud of silt doesn't move with the glass\
    \ gator."
  "name": "Silt Cloud (Recharges after a Short or Long Rest)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/glass-gator-tob1-2023.webp"
```
^statblock

## Environment

desert, grassland, underwater
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Pombero"]
---
# [Pombero](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/pombero-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 294*  

*This squat little man has long limbs and skin the color of coal. The backs of its hands and tops of its feet are covered in thick hair. Its face seems a bit too wide for its head, and its eyes gleam a little too brightly in the pale light*.

Pomberos are strange tricksters, born of shadows in the wild. At rest, they tend to adopt a squatting posture, which accentuates their too-long limbs. They shun bright light, though it doesn't harm them, and seek out shadows and half-light. For this reason, many people call pomberos the Night People.

## Joy of Trespassing

Pomberos take delight from creeping into places where they don't belong and stealing interesting objects. A pombero's lair is littered with trinkets, both commonplace and valuable. The blame for all manner of misfortune is often laid at a pombero's hairy feet.

## Hatred of Hunters

In contrast to their larcenous ways, pomberos take great umbrage over the killing of animals and the destruction of trees in their forests. Birds are particularly beloved pets, and they enjoy mimicking bird songs and calls most of all. Villagers in areas near pombero territory are careful to treat the animals and trees with respect, and they have a strong taboo against killing birds.

```statblock
"name": "Pombero (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Chaotic Neutral"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "90"
"hit_dice": "12d8 + 36"
"stats":
- !!int "17"
- !!int "16"
- !!int "16"
- !!int "8"
- !!int "10"
- !!int "14"
"speed": "30 ft."
"skillsaves":
  "Athletics": !!int "5"
  "Sleight of Hand": !!int "5"
  "Stealth": !!int "5"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Sylvan"
"cr": "3"
"traits":
- "desc": "The pombero can contort its body into unnatural positions, allowing it\
    \ to easily move through any opening large enough for a Tiny creature. The pombero's\
    \ destination must still have suitable room to accommodate its volume."
  "name": "Contortionist"
- "desc": "The pombero has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in forested terrain."
  "name": "Forest Camouflage"
- "desc": "The pombero can communicate with Beasts as if they shared a language."
  "name": "Speak with Beasts"
"actions":
- "desc": "The pombero makes two Slam attacks. It can replace one attack with a use\
    \ of Charming Touch, if available."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d8 + 3) bludgeoning damage."
  "name": "Slam"
- "desc": "One creature the pombero can see within 5 feet of it must succeed on a\
    \ DC 12 Wisdom saving throw or be [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ for 10 minutes. If the target suffers any harm, the effect ends. Otherwise,\
    \ the target can repeat the saving throw at the end of every minute, ending the\
    \ effect on itself on a success. The pombero can have only one creature [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ at a time. If it charms another, the effect on the previous creature ends."
  "name": "Charming Touch (Recharge 5-6)"
- "desc": "The pombero magically turns [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ until it attacks or uses Charming Touch, or until its [concentration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ ends (as if [concentrating](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ on a spell). Any equipment the pombero wears or carries is [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ with it."
  "name": "Invisibility"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/pombero-tob1-2023.webp"
```
^statblock

## Environment

forest
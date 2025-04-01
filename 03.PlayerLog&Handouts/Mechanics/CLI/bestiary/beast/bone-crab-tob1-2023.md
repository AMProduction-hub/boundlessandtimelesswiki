---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Bone Crab"]
---
# [Bone Crab](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/bone-crab-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 40*  

*The cracked skull scurries forward on bone-white legs, crab claws raised.*

## Skull Shells

Much like an enormous hermit crab, bone crabs inhabit the remains of large fish, humanoids, and other creatures. A bone crab's spiny, ivory-white legs blend in perfectly with bones and pale driftwood. When lacking bones, these crabs gnaw cavities into chunks of driftwood or coral to make a shelter, cementing bits of shell and debris to their portable homes. They drag aquatic prey above the high tide line and leave it to fester in the hot sun. The crabs can pick corpses clean in a few hours, and their hunting grounds are littered with cracked and sun-bleached bones—the perfect hiding place for these littoral predators.

## Scavengers of Memory

Bone crabs are voracious scavengers. They live in seaside crags and coves, where they use their specialized chelae to crack open skulls and feast on the brains. Some crabs retain fragments of memory from those they devour, and these crabs recognize friends or attack the foes of those whose skulls they wear.

## Pack Hunters

Bone crabs hunt in packs, preying on seabirds and creatures stranded in tidal pools. Centuries of feeding on brains has left the crabs with a rudimentary intelligence and a psychic connection with fellow packmates. They use this to alert each other to danger, potential prey, or a threat to their territory. Although bone crabs cannot be domesticated, they can be convinced to nest in particular areas, attacking intruders while ignoring the area's regulars.

## White Ghost Shivers

Because they eat carrion, bone crabs carry a dangerous disease known as white ghost shivers. This disease wracks victims with fever and delirium. Sailors and others who eat a bone crab's unwholesome, diseased flesh rarely survive it.

```statblock
"name": "Bone Crab (ToB1-2023)"
"size": "Small"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "33"
"hit_dice": "6d6 + 12"
"stats":
- !!int "10"
- !!int "14"
- !!int "14"
- !!int "3"
- !!int "12"
- !!int "4"
"speed": "20 ft., swim 10 ft."
"skillsaves":
  "Stealth": !!int "4"
  "Perception": !!int "3"
"damage_resistances": "bludgeoning"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": ""
"cr": "1/2"
"traits":
- "desc": "The bone crab can breathe air and water."
  "name": "Amphibious"
- "desc": "The bone crab has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide among bones."
  "name": "Bone Camouflage"
- "desc": "The bone crab can magically communicate simple ideas, emotions, and images\
    \ telepathically with other bone crabs in its pack within 100 feet of it. While\
    \ within 30 feet of another bone crab, the bone crab can't be surprised and has\
    \ advantage on initiative rolls."
  "name": "Limited Telepathy"
- "desc": "The bone crab has advantage on attack rolls against a creature if at least\
    \ one of the crab's allies is within 5 feet of the creature and the ally isn't\
    \ [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Pack Tactics"
- "desc": "The bone crab's long jump is up to 20 feet and its high jump is up to 10\
    \ feet, with or without a running start."
  "name": "Standing Leap"
- "desc": "A creature that eats the meat of the bone crab or that is bitten by a creature\
    \ infected with the white ghost shivers disease must succeed on a DC 11 Constitution\
    \ saving throw or become infected with the disease. An infected creature develops\
    \ the first symptoms after 24 hours. Symptoms include a mild chill that escalates\
    \ to a fever and frightful hallucinations that give the disease its name. At the\
    \ end of each long rest, the infected creature must succeed on a DC 11 Constitution\
    \ saving throw or suffer one level of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion).\
    \ The [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)\
    \ lasts until the creature finishes a long rest after the disease is cured. A\
    \ creature that succeeds on two saving throws against the disease recovers from\
    \ it. Alternatively, the disease can be removed by the [lesser restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/lesser-restoration.md)\
    \ spell or similar magic."
  "name": "White Ghost Shivers"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4\
    \ + 2) slashing damage."
  "name": "Claw"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/bone-crab-tob1-2023.webp"
```
^statblock

## Environment

coastal
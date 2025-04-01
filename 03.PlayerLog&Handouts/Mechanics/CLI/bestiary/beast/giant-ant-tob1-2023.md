---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Ant"]
---
# [Giant Ant](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/giant-ant-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 22*  

*Several pony-sized ants swarm around an ant the size of a draft horse, clacking their serrated mandibles and threatening with their stingers.*

Giant ants look much like a normal ant with six legs, a waspish segmented body, and large antenna. Their hides are covered in thick chitin, and they have large, serrated mandibles flanking their mouths and stingers on their tails. These stingers are the size of a shortsword, and they're capable of stabbing and poisoning a human to death.

## Colony Defenders

Giant ants form colonies under the control of a queen much like their normal-sized cousins. Sterile females form castes with the workers building the nest and caring for larvae. Queens and male drones rarely leave the colony. Soldiers defend the colony and forage for food.

## Carry Prey Home

Giant ants are both predators and scavengers, working in organized groups to bring down large prey and carry it back to the nest. Giant ants tend to ignore animals away from the colony when not foraging for food, but they quickly move to overwhelm prey when hungry or threatened. A giant ant stands nearly four feet tall and weighs 400 pounds, while a giant ant queen is over five feet tall and weighs 900 pounds. Giant ants communicate with each other primarily with pheromones but also use sound and touch.

```statblock
"name": "Giant Ant (ToB1-2023)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "52"
"hit_dice": "7d10 + 14"
"stats":
- !!int "15"
- !!int "13"
- !!int "15"
- !!int "1"
- !!int "9"
- !!int "2"
"speed": "40 ft."
"senses": "blindsight 60 ft., passive Perception 9"
"languages": ""
"cr": "2"
"traits":
- "desc": "The giant ant has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on smell."
  "name": "Keen Smell"
"actions":
- "desc": "The giant ant makes one Bite attack and one Sting attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8\
    \ + 2) bludgeoning damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 12). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and the giant ant can't Bite a different target."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8\
    \ + 2) piercing damage. The target must make a DC 12 Constitution saving throw,\
    \ taking 11 (2d10) poison damage on a failed save, or half as much damage on\
    \ a successful one."
  "name": "Sting"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/giant-ant-tob1-2023.webp"
```
^statblock

## Environment

forest, underdark
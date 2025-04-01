---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Ant Queen"]
---
# [Giant Ant Queen](03 - Player Log & Handouts\Mechanics\CLI\bestiary\npc/giant-ant-queen-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 22*  

*Several pony-sized ants swarm around an ant the size of a draft horse, clacking their serrated mandibles and threatening with their stingers.*

Giant ants look much like a normal ant with six legs, a waspish segmented body, and large antenna. Their hides are covered in thick chitin, and they have large, serrated mandibles flanking their mouths and stingers on their tails. These stingers are the size of a shortsword, and they're capable of stabbing and poisoning a human to death.

## Colony Defenders

Giant ants form colonies under the control of a queen much like their normal-sized cousins. Sterile females form castes with the workers building the nest and caring for larvae. Queens and male drones rarely leave the colony. Soldiers defend the colony and forage for food.

## Carry Prey Home

Giant ants are both predators and scavengers, working in organized groups to bring down large prey and carry it back to the nest. Giant ants tend to ignore animals away from the colony when not foraging for food, but they quickly move to overwhelm prey when hungry or threatened. A giant ant stands nearly four feet tall and weighs 400 pounds, while a giant ant queen is over five feet tall and weighs 900 pounds. Giant ants communicate with each other primarily with pheromones but also use sound and touch.

```statblock
"name": "Giant Ant Queen (ToB1-2023)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "119"
"hit_dice": "14d10 + 42"
"stats":
- !!int "17"
- !!int "13"
- !!int "16"
- !!int "2"
- !!int "11"
- !!int "4"
"speed": "40 ft."
"senses": "blindsight 60 ft., passive Perception 10"
"languages": ""
"cr": "5"
"traits":
- "desc": "The giant ant queen has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on smell."
  "name": "Keen Smell"
- "desc": "Giant ants within 30 feet of the queen have advantage on attack rolls against\
    \ any creature that attacked the queen within the last minute."
  "name": "Queen's Scent"
"actions":
- "desc": "The giant ant queen makes two Bite attacks and one Sting attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d8\
    \ + 3) bludgeoning damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 13). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and the giant ant queen can't Bite a different target."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d8\
    \ + 3) piercing damage. The target must make a DC 13 Constitution saving throw,\
    \ taking 22 (4d10) poison damage on a failed save, or half as much damage on\
    \ a successful one."
  "name": "Sting"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/npc/token/giant-ant-queen-tob1-2023.webp"
```
^statblock

## Environment

forest, underdark
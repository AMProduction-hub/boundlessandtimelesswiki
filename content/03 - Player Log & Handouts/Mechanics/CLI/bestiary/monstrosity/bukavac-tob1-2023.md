---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Bukavac"]
---
# [Bukavac](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/bukavac-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 45*  

*Unleashing a bone-shattering roar, this toad-like monster bears two gnarled horns and wicked claws. It charges from its watery lair on six legs, eager for the kill.*

## Pond Lurkers

The placid surfaces of forest lakes and ponds hide many lethal threats, among them the bukavac. While not amphibious, the creature can hold its breath for minutes at a time as it lurks under the surface in wait for prey. A bukavac is 11 feet long, including its foot-long horns, stands four feet tall, and weighs 4,000 lb. The creature has a natural lifespan of 40 years, but its noise and proclivity to ambush intelligent prey attracts the attention of hunting parties, which considerably shortens the life expectancy of most bukavac.

## Enormous Roar

A ravenous bukavac lives to hunt and devour prey, preferring intelligent prey to animals, and usually ambushes its victims. Due to its size, the beast must find deep ponds or lakes to hide in, but it can flatten itself comfortably to rest in two feet of water. It leads with its wicked horns before grabbing hold of its target or another nearby foe and hanging on as it claws its victim to death. The creature relishes the feel of its victim's struggles to escape its embrace and reserves its roar, which sounds like a cross between a toad's croak and lion's roar emanating from a creature the size of a dragon, for organized foes or against overwhelming numbers. If a bukavac's devastating sonic attack routs its foes, it picks off remaining stragglers; otherwise, it retreats to its underwater hiding spot.

## Clamorous Mating

Solitary hunters by nature, bukavacs pair up briefly in the spring. Male bukavacs travel to a female's lair and demonstrate their prowess by unleashing their most powerful bellows. Villages ten miles away from the lair often hear these howls for a week and pray that the creatures don't attack. Later, the female finds a secluded, shallow lake in which to bury eggs. A bukavac reaches maturity in five years, during which time it and its siblings hunt together. After the bukavacs mature, each finds its own lair.

```statblock
"name": "Bukavac (ToB1-2023)"
"size": "Large"
"type": "monstrosity"
"alignment": "Neutral Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "199"
"hit_dice": "21d10 + 84"
"stats":
- !!int "20"
- !!int "17"
- !!int "18"
- !!int "7"
- !!int "15"
- !!int "12"
"speed": "40 ft., swim 20 ft."
"saves":
  "Dexterity": !!int "7"
  "Constitution": !!int "8"
"skillsaves":
  "Stealth": !!int "11"
  "Perception": !!int "10"
"damage_immunities": "thunder"
"senses": "darkvision 60 ft., passive Perception 20"
"languages": "Sylvan"
"cr": "9"
"traits":
- "desc": "The bukavac can hold its breath for 20 minutes."
  "name": "Hold Breath"
- "desc": "A bukavac's long jump is up to 20 feet and its high jump is up to 10 feet,\
    \ with or without a running start."
  "name": "Standing Leap"
"actions":
- "desc": "The bukavac makes one Bite attack, one Gore attack, and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 16\
    \ (2d10 + 5) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 11\
    \ (1d12 + 5) slashing damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 16) if it is a Medium or smaller creature. The bukavac can have no\
    \ more than two creatures [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ at a time."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 21\
    \ (3d10 + 5) piercing damage."
  "name": "Gore"
- "desc": "A bukavac can emit a howling thunderclap in a 15-foot radius. Each creature\
    \ in that area must make a DC 16 Constitution saving throw. On a failure, a creature\
    \ takes 36 (8d8) thunder damage and is [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened)\
    \ until cured by the [lesser restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/lesser-restoration.md)\
    \ spell or similar magic. On a success, a creature takes half the damage and isn't\
    \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened)."
  "name": "Croaking Blast (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/bukavac-tob1-2023.webp"
```
^statblock

## Environment

forest, underwater
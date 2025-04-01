---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Garroter Crab"]
---
# [Garroter Crab](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/garroter-crab-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 194*  

*This blue-black freshwater crab scuttles through the mud by the stream, searching for prey.*

## Strangling Claws

Garroter crabs are named for their abnormal right claws, which have evolved over time to strangle prey like a barbed whip. This long whip-claw is lined with powerful muscles and joints at the beginning, middle, and end that give it great flexibility.

## Clacking Hordes

During mating season, thousands of garroter crabs congregate in remote riverbanks and marshes, and the males whip their shells with a loud clacking sound to attract mates. Familiar with the sound, locals avoid the rivers and streams near their homes during such times.

## Tasty Predators

Garroter crabs prey on rodents, cats, and other small animals caught by the riverbank. Considered a delicacy by many, fishing communities near colonies of garroter crabs often have a few skilled fishers capable of bringing in the dangerous crabs.

## Unknowing Diviners

Garroter crabs are touched by minor divination power that typically triggers when the crabs attack humanoids, though some humanoids have found ways to prepare the crabs' remains to create the same effect. Because of this peculiar ability, scholars speculate the crabs were created long ago as tools of divination or were gifted by some longforgotten deity of fate to its followers.

> [!note] Garroter Crabs in Midgard
> 
> Common to the Argent upriver from the Free City of Zobeck, garroter crabs are used by the Kariv and crab diviners in their divinations. The Kariv treat the crabs as sacred creatures and never eat them. However, local Zobeckers hold no such notions and find them quite delectable. Much larger garroter crabs exist, and the Kariv believe these incredibly rare crabs can be used to shape the future, as well as divine it.
^garroter-crabs-in-midgard

```statblock
"name": "Garroter Crab (ToB1-2023)"
"size": "Tiny"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "18"
"hit_dice": "4d4 + 8"
"stats":
- !!int "14"
- !!int "10"
- !!int "14"
- !!int "1"
- !!int "10"
- !!int "2"
"speed": "30 ft., swim 20 ft."
"skillsaves":
  "Athletics": !!int "4"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": ""
"cr": "1/4"
"traits":
- "desc": "The garroter crab can breathe air and water."
  "name": "Amphibious"
- "desc": "A Humanoid reduced to 0 hp while [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by the garroter crab experiences a brief vision of the future. This effect works\
    \ like the divination spell, except the reply is only as a mental vision and it\
    \ can be about any specific goal, event, or activity to occur within 30 days.\
    \ Once a creature has received a vision in this way, it can't do so again for\
    \ 30 days."
  "name": "Strangling Divination"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 10 ft., one target. Hit: 5\
    \ (1d6 + 2) slashing damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 12). Until this grapple ends, the target can't speak or cast spells\
    \ with verbal components, and the crab can't use its Whip Claw on another target."
  "name": "Whip-Claw"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/garroter-crab-tob1-2023.webp"
```
^statblock

## Environment

forest, underwater
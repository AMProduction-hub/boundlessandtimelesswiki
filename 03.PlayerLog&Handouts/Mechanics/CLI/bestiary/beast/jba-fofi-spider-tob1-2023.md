---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["J'ba Fofi Spider"]
---
# [J'ba Fofi Spider](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/jba-fofi-spider-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 344*  

*A large, brown spider that resembles a tarantula with exaggeratedly long legs gracefully emerges from the bushes, followed by similar arachnids that are smaller and yellow in color.*

The j'ba fofi resembles an oversized tarantula with very long legs, although a flicker of intelligence indicates this species evolved above mere vermin.

## Spider Pack Leaders

The youngest are yellow in color, but their hairs turn brown as they age. Immature j'ba fofi pull ordinary spiders into their fellowship in teeming masses that follow along wherever they roam.

## Fond of Camouflage

The natural coloring of a j'ba fofi, along with its habit to cover its hair-like bristles in a layer of leaves makes it virtually invisible in its natural environment. They weave leaves and other forest litter into their webs to create well-hidden, enclosed lairs.

```statblock
"name": "J'ba Fofi Spider (ToB1-2023)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "75"
"hit_dice": "10d10 + 20"
"stats":
- !!int "17"
- !!int "17"
- !!int "15"
- !!int "4"
- !!int "13"
- !!int "6"
"speed": "40 ft., climb 40 ft."
"skillsaves":
  "Stealth": !!int "5"
"senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 11"
"languages": ""
"cr": "3"
"traits":
- "desc": "With 10 minutes of work, the j'ba fofi can create a camouflaged web in\
    \ a 10-foot cube. The web must be anchored between two solid mases or layered\
    \ across a floor, wall, or ceiling. A camouflaged web layered over a flat surface\
    \ has a depth of 5 feet. The web is camouflaged to match its surroundings, requiring\
    \ a successful DC 15 Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ check to notice them. Each creature that starts its turn in the camouflaged\
    \ web or that enters it during the creature's turn must succeed on a DC 13 Dexterity\
    \ saving throw or be [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ A creature, including the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature, can take its action to break the webbing and free the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature by succeeding on a DC 13 Strength check. The webbing can also be attacked\
    \ and destroyed (AC 10; hp 5; vulnerability to fire damage; immunity to bludgeoning,\
    \ poison, and psychic damage)."
  "name": "Camouflaged Webs"
- "desc": "The j'ba fofi has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in forested terrain."
  "name": "Forest Camouflage"
- "desc": "The j'ba fofi can climb difficult surfaces, including upside down on ceilings,\
    \ without needing to make an ability check."
  "name": "Spider Climb"
- "desc": "No spider can willingly attack the j'ba fofi, unless attacked first. A\
    \ spider can be forced to do so through magical means."
  "name": "Spider Passivism"
- "desc": "While in contact with a web, the j'ba fofi knows the exact location of\
    \ any other creature in contact with the same web."
  "name": "Web Sense"
- "desc": "The j'ba fofi ignores movement restrictions caused by webbing."
  "name": "Web Walker"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 8\
    \ (1d10 + 3) piercing damage, and the target must make a DC 12 Constitution\
    \ saving throw, taking 18 (4d8) poison damage on a failed save, or half as much\
    \ damage on a successful one. If the poison damage reduces the target to 0 hp,\
    \ the target is stable but [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 hour, even after regaining hp, and is [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ while [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way."
  "name": "Bite"
- "desc": "The j'ba fofi releases pheromones and calls 1 swarm of spiders. The spiders\
    \ arrive in 1d4 rounds, acting as allies of the j'ba fofi and obeying its pheromone\
    \ commands. The spiders remain for 1 hour, until the j'ba fofi dies, or until\
    \ the j'ba fofi dismisses them as a bonus action."
  "name": "Call Spiderlings (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/jba-fofi-spider-tob1-2023.webp"
```
^statblock

## Environment

forest
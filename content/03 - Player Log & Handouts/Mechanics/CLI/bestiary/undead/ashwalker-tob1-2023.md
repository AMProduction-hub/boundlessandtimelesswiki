---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Ashwalker"]
---
# [Ashwalker](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/ashwalker-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 28*  

*A winged shadow eclipsed the sun, and an inferno consumed the city. An ashen corpse rose from the dirt and walked the charred streets as if its world had not just been incinerated.*

Ashwalkers are the unfortunate result of humanoids who met their end from the breath of a dragon while in a place suffused with powerful magical energy. These undead creatures often emerge in hordes after a dragon's rage has leveled a city. Though burnt almost to ashes, many ashwalkers can rasp out a few words, typically words of hate for those who were spared the ashwalker's fate.

## The Last Breath

While the fire of a red dragon's breath is the most common source of ashwalkers, they can be created from any dragon's breath. The magical infusion of the dragon's breath that kills the individual leaves residual energy of a similar type in the remains. For example, an ashwalker killed by poison breath often exudes some of the noxious clouds as it walks the wastelands of its destroyed home.

## Unlived Dreams

Ashwalkers have no purpose in undeath and rarely serve a master. Sometimes they carry on a sad mimicry of their former life, acting out the final hours before their demise, not fully aware of what happened. Some ashwalkers even return to the site of their homes and lay down in the dirt to sleep, although sleep never comes. Adventurers who seek the riches of lost civilizations leveled by dragon fire have reported seeing smoldering corpses milling about marketplaces or theatre spaces until a living soul snaps them from their reverie, often driving them into maddened rages.

```statblock
"name": "Ashwalker (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "12"
"hp": !!int "31"
"hit_dice": "7d8"
"stats":
- !!int "13"
- !!int "15"
- !!int "10"
- !!int "7"
- !!int "10"
- !!int "6"
"speed": "30 ft."
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "understands all languages it knew in life but can't speak"
"cr": "1"
"traits":
- "desc": "The ashwalker has immunity to a type of damage based on the type of dragon\
    \ that killed it: acid (black, copper), cold (silver, white), fire (brass, gold,\
    \ red), lightning (blue, bronze), or poison (green)."
  "name": "Breath Born"
- "desc": "A creature that touches the ashwalker or hits it with a melee attack while\
    \ within 5 feet of it takes 3 (1d6) damage of the type noted in its Breath Born\
    \ trait."
  "name": "Burst of Breath"
- "desc": "The first time the ashwalker is reduced to 0 hp, it drops to 1 hp instead\
    \ and its Draconic Breath automatically recharges. The ashwalker transforms into\
    \ raw energy of the type noted in its Breath Born trait. While in this energy\
    \ form, it is immune to all damage and to being [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ or [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ At the end of the ashwalker's next turn, it is destroyed."
  "name": "Last Breath"
- "desc": "The ashwalker doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6\
    \ + 2) bludgeoning damage plus 3 (1d6) damage of the type noted in the ashwalker's\
    \ Breath Born trait."
  "name": "Slam"
- "desc": "The ashwalker exhales elemental energy in a 15-foot cone. Each creature\
    \ in the area must make a DC 12 Constitution saving throw, taking 14 (4d6) damage\
    \ of the type noted in its Breath Born trait on a failed save, or half as much\
    \ damage on a successful one."
  "name": "Draconic Breath (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/ashwalker-tob1-2023.webp"
```
^statblock

## Environment

any
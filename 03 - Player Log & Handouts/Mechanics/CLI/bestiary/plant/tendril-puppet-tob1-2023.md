---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/plant
statblock: inline
aliases: ["Tendril Puppet"]
---
# [Tendril Puppet](03 - Player Log & Handouts\Mechanics\CLI\bestiary\plant/tendril-puppet-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 389*  

*Vines crawl across the body and out of the eyes and mouth of this shambling human.*

## Plant Servants

Over time, a vine lord eventually commands a small army of plant creatures, fey, and even plant-based undead, such as vine troll skeletons, to enact its will. When no other allies present themselves, vine lords turn to creating tendril puppets by planting vine roots into humanoids. The vines eventually kill and animate the humanoids, which become mindless servants and expendable scouts. The puppets are connected to each other and the vine lord through a magical "root mind" that relays information almost instantaneously.

```statblock
"name": "Tendril Puppet (ToB1-2023)"
"size": "Medium"
"type": "plant"
"alignment": "Lawful Neutral"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "51"
"hit_dice": "6d8 + 24"
"stats":
- !!int "16"
- !!int "15"
- !!int "18"
- !!int "6"
- !!int "6"
- !!int "8"
"speed": "30 ft."
"damage_vulnerabilities": "fire"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened)"
"senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 8"
"languages": "understands the languages of its vine lord but can't speak"
"cr": "2"
"traits":
- "desc": "While in a forest, the tendril puppet regains 5 hp at the start of its\
    \ turn if it has at least 1 hp."
  "name": "Green Regeneration"
- "desc": "The vine lord and the tendril puppets it has created are connected via\
    \ a hive mind. The vine lord and its puppets can telepathically communicate with\
    \ each other, provided the communicating creatures are within 1 mile of each other.\
    \ In addition, while in a forest, the tendril puppet can't be surprised."
  "name": "Root Mind"
- "desc": "The tendril puppet has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
- "desc": "Difficult terrain composed of nonmagical plants doesn't cost the tendril\
    \ puppet extra movement, and it can pass through nonmagical plants without being\
    \ slowed by them and without taking damage from them if they have thorns, spines,\
    \ or a similar hazard."
  "name": "Woodland Walk"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d8 + 3) bludgeoning damage plus 5 (2d4) piercing damage."
  "name": "Thorned Slam"
- "desc": "Ranged Weapon Attack: +4 to hit, range 20/60 ft., one target. Hit:\
    \ 12 (4d4 + 2) piercing damage, and the ball bursts, scattering sharp thorns\
    \ around the target. Each creature within 5 feet of the target must succeed on\
    \ a DC 13 Dexterity saving throw or take 5 (2d4) piercing damage."
  "name": "Ball of Thorns"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/plant/token/tendril-puppet-tob1-2023.webp"
```
^statblock

## Environment

forest
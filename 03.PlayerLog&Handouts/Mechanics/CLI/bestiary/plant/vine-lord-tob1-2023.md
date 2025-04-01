---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/plant
statblock: inline
aliases: ["Vine Lord"]
---
# [Vine Lord](03 - Player Log & Handouts\Mechanics\CLI\bestiary\plant/vine-lord-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 388*  

*Covered with dark green bark and twining tendrils, this longlimbed humanoid exudes a palpable aura of horror.*

## Melding of Flesh and Vine

Vine lords are formed from the union of a vine-infested humanoid and the force-grown descendants of plantfolk. Their servants include most plant creatures, including the tendril puppets the vine lord creates.

## Walking Forests

Vine lords seek to expand and empower forests and jungles in the service of their patron gods and demons or simply to expand their own power. In many cases, they compel trees to walk into grasslands or plowed fields on moonless nights, claiming that territory for the trees.

## Plant Servants

Over time, a vine lord eventually commands a small army of plant creatures, fey, and even plant-based undead, such as vine troll skeletons, to enact its will. When no other allies present themselves, vine lords turn to creating tendril puppets by planting vine roots into humanoids. The vines eventually kill and animate the humanoids, which become mindless servants and expendable scouts. The puppets are connected to each other and the vine lord through a magical "root mind" that relays information almost instantaneously.

> [!note] Vine Lords in Midgard
> 
> Vine lords owe much of their parentage to the Kijani, the original inhabitants of Kush. They are agents of the Green Walker, working to spread the Living Jungle beyond its current borders. Vine lords marshal jungle denizens to fight for them as tendril puppets, and they often entice druid circles with promises of great power.
^vine-lords-in-midgard

```statblock
"name": "Vine Lord (ToB1-2023)"
"size": "Medium"
"type": "plant"
"alignment": "Lawful Neutral"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "105"
"hit_dice": "14d8 + 42"
"stats":
- !!int "12"
- !!int "20"
- !!int "16"
- !!int "14"
- !!int "16"
- !!int "18"
"speed": "30 ft., climb 30 ft."
"saves":
  "Charisma": !!int "8"
  "Wisdom": !!int "7"
  "Constitution": !!int "7"
"damage_vulnerabilities": "fire"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened)"
"senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 13"
"languages": "Common, Sylvan"
"cr": "9"
"traits":
- "desc": "While in a forest, the vine lord regains 10 hp at the start of its turn\
    \ if it hast at least 1 hp."
  "name": "Green Regeneration"
- "desc": "The vine lord has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The vine lord and the tendril puppets it has created are connected via\
    \ a hive mind. The vine lord and its puppets can telepathically communicate with\
    \ each other, provided the communicating creatures are within 1 mile of each other.\
    \ In addition, while in a forest, the vine lord can't be surprised."
  "name": "Root Mind"
- "desc": "A creature infected with a vine lord's vine seed suffers near-constant\
    \ pain as the seed takes root and spreads tendrils throughout its body. For the\
    \ first 24 hours after infection, the creature has disadvantage on attack rolls\
    \ and ability checks, as the pain from the spreading roots distracts it. Then,\
    \ the seed becomes a disease, devouring the creature from the inside as it grows\
    \ vines throughout the creature's body. Until the disease is cured, the infected\
    \ creature can't regain hp, and its hp maximum decreases by 7 (2d6) for every\
    \ 24 hours that elapse. This reduction lasts until the disease is cured. The creature\
    \ dies if this disease reduces its hp maximum to 0.\n\nThis potent disease can\
    \ be cured only by the [greater restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-restoration.md)\
    \ spell or similar magic. Alternatively, a creature can take 10 minutes and remove\
    \ the growing seed from the infected creature within the first 24 hours of infection\
    \ by succeeding on a DC 16 Wisdom ([Medicine](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Medicine))\
    \ check. A Humanoid slain by this disease rises 24 hours later as a tendril puppet\
    \ under the vine lord's control."
  "name": "Vine Seed"
- "desc": "Difficult terrain composed of plants doesn't cost the vine lord extra movement.\
    \ In addition, it can pass through plants without being slowed by them and without\
    \ taking damage from them if they have thorns, spines, or a similar hazard."
  "name": "Woodland Walk"
"actions":
- "desc": "The vine lord makes one Tendril attack and two Thorned Slam attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 7\
    \ (1d4 + 5) slashing damage plus 7 (2d6) poison damage, and the target must\
    \ succeed on a DC 16 Constitution saving throw or become infected with a vine\
    \ seed (see the Vine Seed trait)."
  "name": "Tendril"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 14\
    \ (2d8 + 5) bludgeoning damage plus 10 (4d4) piercing damage."
  "name": "Thorned Slam"
- "desc": "The vine lord magically calls 1d4 awakened trees or tendril puppets,\
    \ or it calls 1 Plant with a challenge rating of 4 or lower. The called creatures\
    \ arrive in 1d4 rounds, acting as allies of the vine lord and obeying its spoken\
    \ commands. The Plants remain for 1 hour, until the vine lord dies, or until the\
    \ vine lord dismisses them as a bonus action."
  "name": "Forest Protectors (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/plant/token/vine-lord-tob1-2023.webp"
```
^statblock

## Environment

forest
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Lantern Dragonette"]
---
# [Lantern Dragonette](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/lantern-dragonette-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 136*  

*This cat-sized drake with a waxy appearance and a glow emanating from its belly can hover in midair, filling a small area with a warm glow.*

The lantern dragonette is named for its belly, which glows with a warm light. The beast's yellow, waxy scales darken with age, though the dragonettes rarely live more than 50 years. They weigh from 5 to 10 pounds and are 18 inches long.

## Eat Candle Wax

The dragonette devours four ounces of candle wax each day, plus four more ounces if it has made its belly glow. A lantern dragonette's unusual diet leads it to lair in libraries, abbeys, and other places of study. Even though the dragonettes eat candles essential for study during dark hours, they still provide light and protect their adopted homes. Residents and caretakers consider them good luck and enjoy conversing with them.

## Telepathic Chatterbox

This gregarious dragonette prefers to speak with its companions but uses telepathy if necessary; the creature hisses when surprised or displeased. It loves nothing more than discussing magic and history with an intelligent and informed individual.

## Adventurous Companions

Occasionally, a dragonette wishing to learn more about the world finds a spellcaster or adventuring party to travel with, purely for the sake of learning or to acquire new sources of knowledge. Most parties enjoy the traveling light source and the abilities these companions bring to bear. A lantern dragonette avoids combat and uses its abilities only to escape or to defend its lair, family, and friends.

## Diligent Parents

A mated pair produces one clutch of two to five eggs every five years. One parent raises the young dragonettes until they mature, typically in a year, while the other scours the area for candle wax to feed the hungry hatchlings.

```statblock
"name": "Lantern Dragonette (ToB1-2023)"
"size": "Tiny"
"type": "dragon"
"alignment": "Lawful Neutral"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "28"
"hit_dice": "8d4 + 8"
"stats":
- !!int "7"
- !!int "15"
- !!int "13"
- !!int "16"
- !!int "13"
- !!int "12"
"speed": "15 ft., fly 40 ft. (hover)"
"saves":
  "Charisma": !!int "3"
  "Wisdom": !!int "3"
"skillsaves":
  "Nature": !!int "5"
  "Religion": !!int "5"
  "Perception": !!int "3"
  "History": !!int "5"
  "Arcana": !!int "5"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Common, Draconic, Primordial, telepathy 60 ft."
"cr": "1/2"
"traits":
- "desc": "While in an area of magical darkness, the lantern dragonette can't fly\
    \ or use Lantern Belly, and it takes 3 (1d6) necrotic damage each minute."
  "name": "Magical Darkness Hypersensitivity"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6\
    \ + 2) piercing damage."
  "name": "Bite"
- "desc": "The lantern dragonette breathes fire in a 15-foot cone. Each creature in\
    \ the area must make a DC 11 Dexterity saving throw, taking 10 (3d6) fire damage\
    \ on a failed save, or half the damage on a successful one."
  "name": "Fire Breath"
"bonus_actions":
- "desc": "The dragonette sheds bright light in a 20-foot radius and dim light for\
    \ an additional 20 feet or stops shedding light. To shed light, it must have eaten\
    \ at least 4 ounces of candle wax in the past 24 hours. It can shed light for\
    \ up to 1 hour for every 4 ounces of candle wax it has eaten in the past 24 hours,\
    \ to a maximum of 4 hours every 24 hours."
  "name": "Lantern Belly"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/lantern-dragonette-tob1-2023.webp"
```
^statblock

## Environment

urban
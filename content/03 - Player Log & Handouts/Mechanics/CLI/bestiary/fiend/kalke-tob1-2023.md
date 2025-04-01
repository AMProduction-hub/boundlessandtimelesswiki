---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/fiend
statblock: inline
aliases: ["Kalke"]
---
# [Kalke](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/kalke-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 242*  

*Combining the head of a goat and the body of a monkey, this creature exhibits the social grace of a baboon with the pretensions of a scholar.*

Fiendish pests that infest derelict wizards' towers and laboratories, the kalkes are either the by-product of botched gates into the lower realms or the personification of an evil deity's contempt for wizards. All kalkes act with the arrogance of magi while having the social characteristics of baboons. Being of fiendish blood, kalkes do not age. Though lacking any formal spellcasting ability, all kalkes can produce magical effects through the dramatic mumming of largely spontaneous and unstudied rituals.

## Hoard Magical Paraphernalia

The drive to produce ever more fanciful rituals gives a kalke the compulsion to accumulate spell components, magical foci, and other occult paraphernalia. Although these objects serve no purpose, the kalkes seek out spellcasters in their vicinity and steal any paraphernalia they can find. Because they have no ability to distinguish what's magically useful from what isn't, they grab any jewelry, pouches, sticks, or ornate objects they uncover.

## Perform Rituals

Troops of kalkes inhabit trees, caverns, and ruins around sites of significant magical activity. Twice a month, or more during major astrological and seasonal events, the kalkes gather to perform—by way of dance, chanting, and sacrifice—an imagined rite of great magic. The effort has an equal chance of achieving nothing whatsoever, causing dangerous but short-lived misfortunes (snakes raining on the countryside, creatures summoned from the lower planes), or triggering calamities (great fires or floods).

## Hagglers

The kalkes will return the goods they've taken, in exchange for a ransom or fee. These exchanges need to have the outward appearance of being impressively in the kalke's favor. A particularly generous (or devious) spellcaster may be able to reach an accommodation with a persistent local troop of kalkes.

```statblock
"name": "Kalke (ToB1-2023)"
"size": "Small"
"type": "fiend"
"alignment": "Neutral Evil"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "18"
"hit_dice": "4d6 + 4"
"stats":
- !!int "8"
- !!int "14"
- !!int "12"
- !!int "13"
- !!int "7"
- !!int "13"
"speed": "30 ft., climb 30 ft."
"skillsaves":
  "Sleight of Hand": !!int "4"
  "Stealth": !!int "4"
  "Perception": !!int "0"
"damage_resistances": "poison"
"senses": "darkvision 120 ft., passive Perception 10"
"languages": "Abyssal, Common, Infernal"
"cr": "1/4"
"traits":
- "desc": "The kalke has advantage on saving throws against spells and magical effects."
  "name": "Magic Resistance"
- "desc": "The kalke senses magic within 120 feet of it at will and can sense the\
    \ general direction of spells being cast within 1 mile of it. This trait otherwise\
    \ works like the [detect magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-magic.md)\
    \ spell but isn't itself magical."
  "name": "Sense Magic"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4\
    \ + 2) bludgeoning damage."
  "name": "Slam"
- "desc": "The kalke activates a magic item in its possession and can ignore all class,\
    \ race, and level requirements on the item. The kalke must make a DC 11 Intelligence\
    \ saving throw. On a success, the item activates normally. On a failure, the item\
    \ doesn't activate and can't be used again until the next dawn. If the kalke fails\
    \ the saving throw by 5 or more, it causes a magical backlash. Each creature within\
    \ 5 feet of the kalke, including the kalke, must make a DC 11 Dexterity saving\
    \ throw, taking 5 (2d4) force damage on a failed save, or half as much damage\
    \ on a successful one."
  "name": "Use Magic Item (Recharge 5-6)"
"bonus_actions":
- "desc": "The kalke takes the Disengage or Hide action."
  "name": "Nimble Escape"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/kalke-tob1-2023.webp"
```
^statblock

## Environment

urban
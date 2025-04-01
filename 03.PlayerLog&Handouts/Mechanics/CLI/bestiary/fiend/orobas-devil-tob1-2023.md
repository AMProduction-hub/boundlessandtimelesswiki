---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/14
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend/devil
statblock: inline
aliases: ["Orobas Devil"]
---
# [Orobas Devil](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/orobas-devil-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 99*  

*Tall and powerful, this creature resembles a strong man with well-chiseled muscles, save its equine head, flaring nostrils, and hoofed feet.*

Orobas devils thrive in Hell, selling their knowledge to those who have the coin or souls. The common phrase, "never trust a gift horse," stems from these corrupting devils.

## Horse-Headed but Wise

Orobas devils look like horrific horse-headed humans. Sulfuric smoke curls from their nostrils, and flames dance across their flails. This beast-like appearance belies their true strength; these devils possess an uncanny prescience and affinity for divination.

## Masters of Deceit

When bargaining with an orobas, one must speak truthfully—or possess an exceptionally quick tongue and the most charming smile.

## Surrounded by Lessers

Orobas devils gather lesser devils both as chattel and defense. Their analytical minds telepathically confer the strengths and weaknesses of foes to their allies. With surprising speed, the deceivers can assess a battlefield, weigh outcomes, and redirect forces.

```statblock
"name": "Orobas Devil (ToB1-2023)"
"size": "Large"
"type": "fiend"
"subtype": "devil"
"alignment": "Lawful Evil"
"ac": !!int "19"
"ac_class": "natural armor, [shield](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/shield.md)"
"hp": !!int "203"
"hit_dice": "14d10 + 126"
"stats":
- !!int "26"
- !!int "14"
- !!int "28"
- !!int "23"
- !!int "26"
- !!int "21"
"speed": "40 ft."
"saves":
  "Dexterity": !!int "7"
  "Wisdom": !!int "13"
  "Strength": !!int "13"
  "Constitution": !!int "14"
"skillsaves":
  "Deception": !!int "10"
  "Insight": !!int "13"
  "Perception": !!int "13"
  "History": !!int "11"
  "Persuasion": !!int "10"
"damage_resistances": "acid; cold; bludgeoning, piercing, slashing from nonmagical\
  \ attacks that aren't silvered"
"damage_immunities": "fire, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "truesight 90 ft., passive Perception 23"
"languages": "Celestial, Infernal, telepathy 100 ft."
"cr": "14"
"traits":
- "desc": "The orobas casts one of the following spells, requiring no material components\
    \ and using Charisma as the spellcasting ability (spell save DC 18):\n\nAt will:\
    \ [augury](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/augury.md),\
    \ [detect thoughts](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-thoughts.md),\
    \ [guidance](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/guidance.md)\n\
    \n1/day each: [contact other plane](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/contact-other-plane.md)\
    \ (as an action), [legend lore](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/legend-lore.md)\
    \ (as an action)\n\n3/day each: [locate creature](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/locate-creature.md),\
    \ [nondetection](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/nondetection.md)"
  "name": "Spellcasting"
- "desc": "When the orobas casts a spell of the divination school, it has advantage\
    \ on Charisma ([Deception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Deception))\
    \ checks for 1 minute."
  "name": "Deceptive Advice"
- "desc": "The orobas's weapon attacks are magical. When the orobas hits with any\
    \ weapon, the weapon deals an extra 3d8 fire damage (included in the attack)."
  "name": "Hellish Weapons"
- "desc": "The orobas has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The orobas can pinpoint the location of Celestials, consecrated places\
    \ or objects, and creatures wielding divine or celestial power, such as clerics,\
    \ paladins, or aasimars, within 60 feet of it."
  "name": "Sense Consecrated"
"actions":
- "desc": "The orobas makes one Bite attack, one Flail attack, and one Stomp attack,\
    \ or it makes four Hurl Flame attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 15\
    \ (2d6 + 8) piercing damage plus 13 (3d8) fire damage and 10 (3d6) poison\
    \ damage, and the target must succeed on a DC 18 Constitution saving throw or\
    \ become [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. The target can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 17\
    \ (2d8 + 8) bludgeoning damage plus 13 (3d8) fire damage."
  "name": "Flail"
- "desc": "Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 11\
    \ (1d6 + 8) bludgeoning damage plus 13 (3d8) fire damage."
  "name": "Stomp"
- "desc": "Ranged Spell Attack: +10 to hit, range 120 ft., one target. Hit:\
    \ 23 (4d8 + 5) fire damage."
  "name": "Hurl Flame"
- "desc": "The orobas magically teleports, along with any equipment, up to 120 feet\
    \ to an unoccupied space it can see."
  "name": "Teleport"
"reactions":
- "desc": "When the orobas makes an ability check or attack, it can choose to have\
    \ advantage on the roll."
  "name": "Prediction (3/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/orobas-devil-tob1-2023.webp"
```
^statblock

## Environment

planar
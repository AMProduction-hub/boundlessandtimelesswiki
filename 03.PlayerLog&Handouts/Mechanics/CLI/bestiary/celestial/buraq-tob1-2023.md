---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/11
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Buraq"]
---
# [Buraq](03 - Player Log & Handouts\Mechanics\CLI\bestiary\celestial/buraq-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 46*  

*An aura of holiness surrounds this handsome human-headed equine with short but strong feathered wings.*

## Only the Worthy

A buraq possesses astounding speed, determination, and resilience, among a host of noble qualities. Only pure-hearted humanoids can obtain a service from such a righteous and honorable creature.

## Angel Marked

Every buraq wears a gilded band around its head or neck. These are said to be angelic seals or wardings, each different. The hide of every buraq is white, though their beards, lashes, manes, and tails vary from silver and dusty tan to deep brown or glossy black.

## Heavenly Steeds

A buraq is smaller than a mule but bigger than a donkey, though their carrying capacity belies their size and apparent strength. Nevertheless, a buraq is the ultimate courier and a heavenly steed. Paladins and good-aligned clerics are the most likely candidates to ride a buraq, but other virtuous characters have had this privilege.

```statblock
"name": "Buraq (ToB1-2023)"
"size": "Medium"
"type": "celestial"
"alignment": "Lawful Good"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "152"
"hit_dice": "16d8 + 80"
"stats":
- !!int "15"
- !!int "18"
- !!int "20"
- !!int "18"
- !!int "18"
- !!int "20"
"speed": "60 ft., fly 90 ft."
"saves":
  "Charisma": !!int "9"
  "Wisdom": !!int "8"
  "Constitution": !!int "9"
"skillsaves":
  "Religion": !!int "8"
  "History": !!int "8"
"damage_resistances": "radiant; bludgeoning, piercing, slashing from nonmagical attacks"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "truesight 120 ft., passive Perception 14"
"languages": "Celestial, Common, Primordial, telepathy 120 ft."
"cr": "11"
"traits":
- "desc": "The buraq casts one of the following spells, requiring no components and\
    \ using Charisma as the spellcasting ability (spell save DC 17):\n\nAt will:\
    \ [comprehend languages](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/comprehend-languages.md),\
    \ [detect evil and good](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-evil-and-good.md),\
    \ [holy aura](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/holy-aura.md),\
    \ [pass without trace](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/pass-without-trace.md)\n\
    \n1/day each: [plane shift](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/plane-shift.md),\
    \ [wind walk](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/wind-walk.md)\n\
    \n3/day each: [haste](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/haste.md),\
    \ [longstrider](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/longstrider.md)"
  "name": "Spellcasting"
- "desc": "The buraq's attacks are magical. When the buraq hits with any weapon, the\
    \ weapon deals an extra 4d8 radiant damage (included in the attack)."
  "name": "Angelic Weapons"
- "desc": "The buraq has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "When outdoors at night, the distance of the buraq's vision is not limited\
    \ by nonmagical darkness. Once per month, the buraq can declare it is on a night\
    \ journey, and for the next 24 hours, it can Teleport as a bonus action. When\
    \ on a night journey, the buraq can teleport as often as it wants, and its destination\
    \ must always be in an area of nonmagical darkness within its line of sight. At\
    \ any point during the night journey, the buraq can use a bonus action to return\
    \ itself and its rider to the location where it began the night journey."
  "name": "Night Journey"
- "desc": "The buraq is considered to be a Large animal for the purpose of determining\
    \ its carrying capacity and its ability to carry a rider."
  "name": "Powerful Steed"
"actions":
- "desc": "The buraq makes two Hooves attacks. It can replace one attack with a use\
    \ of Spellcasting."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) bludgeoning damage plus 18 (4d8) radiant damage."
  "name": "Hooves"
- "desc": "The buraq magically teleports itself and its rider, along with any equipment\
    \ it is wearing or carrying, to a location the buraq is familiar with, up to 1\
    \ mile away."
  "name": "Teleport (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/celestial/token/buraq-tob1-2023.webp"
```
^statblock

## Environment

planar
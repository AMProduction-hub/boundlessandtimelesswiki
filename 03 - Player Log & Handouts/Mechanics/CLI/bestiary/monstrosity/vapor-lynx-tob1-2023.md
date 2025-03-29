---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Vapor Lynx"]
---
# [Vapor Lynx](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/vapor-lynx-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 383*  

*The great cat pads along noiselessly, while tendrils of smoke drift off its sleek, gray coat, leaving misty whorls in its wake. Its lips curl up into a fang-revealing smile as its body fades into fog.*

## Split the Herd

Vapor lynxes are capricious hunters. Devious, manipulative, and mischievous, they toy with their prey before killing it. They rarely enjoy a stand-up fight, instead coalescing in and out of the fog to harass victims and cut large groups into smaller, more manageable morsels.

## Dreary Marshlands

Their tactics have earned vapor lynxes a nasty reputation and the occasional bounty on their heads. Additionally, their magical nature makes them valuable to practitioners of the magical arts, and their beautiful, thick coats tempt many a furrier into hunts they may not be prepared to handle. For these reasons, vapor lynxes avoid civilization, fearing organized reprisal. Instead, they haunt marshes and swamps, where natural fog makes hunting easier. If an intelligent humanoid passes their way, they are happy for a change in diet.

## Chatty with Dinner

Although reclusive, vapor lynxes are intelligent, speaking both Common and Sylvan. They are particularly prideful and take joy in bantering with potential meals to belittle and frighten them. Survivors of vapor lynx encounters invariably mention their needling and self-aggrandizement.

```statblock
"name": "Vapor Lynx (ToB1-2023)"
"size": "Large"
"type": "monstrosity"
"alignment": "Chaotic Neutral"
"ac": !!int "14"
"hp": !!int "127"
"hit_dice": "15d10 + 45"
"stats":
- !!int "15"
- !!int "18"
- !!int "16"
- !!int "10"
- !!int "13"
- !!int "14"
"speed": "50 ft., climb 30 ft."
"skillsaves":
  "Stealth": !!int "7"
  "Perception": !!int "4"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Common, Sylvan"
"cr": "5"
"traits":
- "desc": "While in fog or mist, the vapor lynx can move through a space as narrow\
    \ at 1 inch wide without squeezing, provided the fog or mist is flowing through\
    \ the space."
  "name": "Fog Flow"
- "desc": "The vapor lynx can see through areas obscured by fog, mist, and steam without\
    \ penalty."
  "name": "Hazesight"
- "desc": "Difficult terrain composed of mud, shallow water, and water plants doesn't\
    \ cost the vapor lynx extra movement."
  "name": "Swamp Walk"
"actions":
- "desc": "The vapor lynx makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) slashing damage."
  "name": "Claw"
- "desc": "The vapor lynx exhales poisonous fog in a 20-foot radius centered on itself.\
    \ The fog spreads around corners, and its area is heavily obscured. Each creature\
    \ in the area must make a DC 14 Constitution saving throw. On a failure, a creature\
    \ takes 28 (8d6) poison damage and is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn. On a success, a creature takes half the damage\
    \ and isn't [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ The fog lasts for 1 minute. A creature that starts its turn in the fog or enters\
    \ the fog for the first time on a turn must succeed on a DC 14 Constitution saving\
    \ throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn."
  "name": "Poison Breath (Recharge 5-6)"
"bonus_actions":
- "desc": "The vapor lynx teleports, along with any equipment it is wearing or carrying,\
    \ up to 30 feet to an unoccupied space it can see. The origin and destination\
    \ spaces must contain fog."
  "name": "Fog Step"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/vapor-lynx-tob1-2023.webp"
```
^statblock

## Environment

swamp
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Ash Drake"]
---
# [Ash Drake](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/ash-drake-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 139*  

*A lean and dull-scaled drake perches on a chimney as if it just crawled out, its tail still hanging into the flue as smoke billows out.*

## Chimney Nesting

Ash drakes clog chimney flues and delight in dusting crowds with thick, choking ash and soot, while the drakes laugh with sneering, wheezing tones. To placate the creatures, owners of smelters and smithies leave large piles of ash for the drakes to play in, with the hope they leave the shop and workers alone. Anyone hunting ash drakes finds them difficult to attack in their cramped lairs because the creatures blend in with the surroundings. Ash drakes often befriend kobolds, who have little trouble appeasing the drakes and appreciate the added security they bring.

## Hunt Strays and Pets

Ash drakes eat rats and stray animals, although few can resist snatching an unattended pet. Contrary to popular opinion, this drake doesn't consume ash, but enjoys a pile of ash like a cat would catnip, rolling around in it and becoming wild-eyed. Anyone who disrupts such play becomes the target of the creature's intensely hot, sooty breath weapon.

## Slender Dragons

While an ash drake is three feet long with a four-foot-long tail that seems to trail off into smoke, it weighs less than one might expect—approximately ten pounds. Every third winter, when chimneys are active, a male drake leaves his lair to find a mate. The resulting eggs are left in a suitable chimney, and one of the parents protects the young until they leave the nest at two years of age.

## Volcanic Haunts

Ash drakes outside a city live in or near volcanic plateaus and mutter about the lack of neighbors to bully. In the wild, an ash drake may partner with a red dragon or flame dragon, since the dragon provides its lesser cousin with plenty of ash.

```statblock
"name": "Ash Drake (ToB1-2023)"
"size": "Small"
"type": "dragon"
"alignment": "Neutral Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "117"
"hit_dice": "18d6 + 54"
"stats":
- !!int "14"
- !!int "15"
- !!int "16"
- !!int "9"
- !!int "15"
- !!int "10"
"speed": "30 ft., fly 60 ft."
"saves":
  "Dexterity": !!int "4"
"skillsaves":
  "Stealth": !!int "4"
"damage_immunities": "fire"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": "Common, Draconic"
"cr": "4"
"traits":
- "desc": "The ash drake can see through areas obscured by fire, smoke, and fog without\
    \ penalty."
  "name": "Firesight"
"actions":
- "desc": "The drake makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6\
    \ + 2) piercing damage plus 3 (1d6) fire damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6\
    \ + 2) slashing damage."
  "name": "Claw"
- "desc": "The ash drake beats its wings, filling the area within 10 feet of it with\
    \ ash for 1 minute. The ash spreads around corners, and its area is heavily obscured.\
    \ Each creature that isn't an ash drake and that enters the cloud for the first\
    \ time on its turn or starts its turn there must succeed on a DC 13 Constitution\
    \ saving throw or become [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the end of its next turn. The ash moves with the drake, remaining centered\
    \ on it for the duration."
  "name": "Ash Cloud (Recharge 6)"
- "desc": "The ash drake spews blistering hot, choking ash in a 30-foot cone. Each\
    \ creature in the area must make a DC 13 Dexterity saving throw. On a failure,\
    \ a creature takes 14 (4d6) fire damage and is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Ash Breath (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/ash-drake-tob1-2023.webp"
```
^statblock

## Environment

mountain, urban
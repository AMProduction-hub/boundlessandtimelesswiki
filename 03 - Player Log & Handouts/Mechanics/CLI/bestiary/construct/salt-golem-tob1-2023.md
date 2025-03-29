---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Salt Golem"]
---
# [Salt Golem](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/salt-golem-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 218*  

*A crudely sculpted, roughly humanoid crystalline form shuffles about on wide, stump-like feet. Tiny salt crystals fall from its body in a glittering cloud with every step.*

## Coastal Druids

These unnatural creatures are created by druids and others living in coastal or desert regions, or by those who seek to wage war with creatures susceptible to the warding powers of salt. Stories tell of a druid who built a squad of nine salt golems to combat a rampaging zmey. The salt warriors waged a long hunt and eventually killed the powerful dragon in its lair while the creator druid and her wizard companion reaped the spoils of its hoard.

## Crystalline and Silent

A salt golem has a crudely formed humanoid body made of crystalline salts. It wears no clothing or armor and carries no weapons or other possessions. It cannot speak—the only sound it makes is the susurrus of sliding sand as it moves. A salt golem is incapable of strategy or tactics. It mindlessly fights until it destroys its opponents or until ordered to stop by its creator.

## Valuable Remains

A salt golem stands about eight feet tall and weighs around 1,000 pounds. A salt golem's body is formed from a composite of 1,000 pounds of rare salts and minerals worth at least 2,500 gp.

```statblock
"name": "Salt Golem (ToB1-2023)"
"size": "Large"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "115"
"hit_dice": "11d10 + 55"
"stats":
- !!int "20"
- !!int "9"
- !!int "20"
- !!int "3"
- !!int "11"
- !!int "1"
"speed": "20 ft."
"skillsaves":
  "Athletics": !!int "9"
"damage_immunities": "fire; poison; psychic; bludgeoning, piercing, slashing from\
  \ nonmagical attacks that aren't adamantine"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., passive Perception 10"
"languages": "understands the languages of its creator but can't speak"
"cr": "10"
"traits":
- "desc": "When the salt golem takes damage, thousands of tiny salt crystals erupt\
    \ from the golem's body, and each creature within 5 feet of the golem must succeed\
    \ on a DC 17 Dexterity saving throw or be [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the end of its next turn."
  "name": "Blinding Salt Spray"
- "desc": "The golem doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The salt golem's Slam attacks are magical. When the golem hits with a Slam\
    \ attack, the attack deals an extra 4d8 necrotic damage (included in the attack)."
  "name": "Dehydrating Fists"
- "desc": "The golem is immune to any spell or effect that would alter its form."
  "name": "Immutable Form"
- "desc": "The golem has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The salt golem makes two Slam attacks. If both attacks hit one creature,\
    \ the target must succeed on a DC 17 Constitution saving throw or suffer one level\
    \ of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 16\
    \ (2d10 + 5) bludgeoning damage plus 18 (4d8) necrotic damage."
  "name": "Slam"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/salt-golem-tob1-2023.webp"
```
^statblock

## Environment

coastal, desert
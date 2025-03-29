---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Hoard Golem"]
---
# [Hoard Golem](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/hoard-golem-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 217*  

*A pile of gold, jewelry, and weapons rises on its own like a tidal wave of riches, with a cold and determined face.*

## Dragon Fears Made Real

Hoard golems were born from the paranoia of dragons. Despite their great physical and intellectual power, dragons are always suspicious of any creature willing to work for them. The first hoard golem was created when a dragon realized that there could be no guardian more trustworthy with its hoard than the hoard itself. Since then, the secret of hoard golem construction has emerged, and rich nobles have followed suit, enchanting their wealth to defend itself from thieves.

## Patient Homebodies

As constructs, hoard golems are mindless, lying in wait for anyone other than their creator to come within striking distance. In the case of evil dragons, this may include the wyrmlings of dragon parents looking to establish dominance in the family. Hoard golems fight to the death, but they rarely leave the rooms they inhabit for fear that clever treasure hunters might trick the hoard into walking itself right out of the owner's den.

## Silent and Wealthy

Hoard golems cannot speak. A hoard golem is 25 feet tall and weighs 20,000 pounds. A hoard golem's body is composed of items—copper, silver, gold, works of art, armor, weapons, and magical items—worth at least 5,000 gp

```statblock
"name": "Hoard Golem (ToB1-2023)"
"size": "Huge"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "161"
"hit_dice": "14d12 + 70"
"stats":
- !!int "22"
- !!int "15"
- !!int "20"
- !!int "3"
- !!int "11"
- !!int "1"
"speed": "40 ft."
"saves":
  "Constitution": !!int "9"
"skillsaves":
  "Athletics": !!int "10"
  "Perception": !!int "4"
"damage_immunities": "poison; psychic; bludgeoning, piercing, slashing from nonmagical\
  \ attacks that aren't adamantine"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., passive Perception 14"
"languages": "understands the languages of its creator but can't speak"
"cr": "12"
"traits":
- "desc": "The golem doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The golem's weapon attacks are magical. When the golem hits with any weapon,\
    \ the weapon deals an extra 4d8 force damage (included in the attack)."
  "name": "Enchanted Weapons"
- "desc": "The golem is immune to any spell or effect that would alter its form."
  "name": "Immutable Form"
- "desc": "The golem has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "A creature that enters a space within 120 feet of the hoard golem or starts\
    \ its turn there must succeed on a DC 17 Wisdom saving throw or have disadvantage\
    \ on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks while it remains within 120 feet of the golem."
  "name": "Strike with Awe"
"actions":
- "desc": "The hoard golem makes two Slam attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 22\
    \ (3d10 + 6) bludgeoning damage plus 18 (4d8) force damage."
  "name": "Slam"
- "desc": "The hoard golem partially disperses into a whirlwind of coins, gemstones,\
    \ and other valuables then recoalesces. Each creature within 20 feet of the golem\
    \ must make a DC 17 Dexterity saving throw. On a failure, a creature takes 44\
    \ (8d10) bludgeoning damage and loses one object it is wearing or carrying.\
    \ On a success, a creature takes half the damage and doesn't lose an object. Each\
    \ object the golem steals must weigh no more than 20 pounds and not be wrapped\
    \ around or firmly attached to a creature. For example, the golem could steal\
    \ a belt pouch full of coins or a creature's jewel-encrusted dagger, but it can't\
    \ steal a creature's shirt or armor. The hoard golem steals objects of high value\
    \ over those of minimal value. The stolen object becomes part of the golem's body\
    \ and can't be retrieved until the golem dies."
  "name": "Thieving Whirlwind (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/hoard-golem-tob1-2023.webp"
```
^statblock

## Environment

underdark, urban
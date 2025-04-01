---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/11
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend/devil
statblock: inline
aliases: ["Koralk Devil"]
---
# [Koralk Devil](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/koralk-devil-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 97*  

*The fiendish hulk bears features taken from a nightmare scorpion, with three stinging tails and four limbs. It wields a massive scythe.*

## Shaped by Arbeyach

These fiends sprang from the dark imagination of Hell's Prince of Swarms, Arbeyach, who twisted them into being from lemures and scorpions. Arbeyach shaped the koralk to be annihilators in battle and to gather souls from the fallen, bypassing typical soul collection methods to feed his war machine more quickly. They are sometimes called "harvester devils."

## Transforming Poison

Poison from the koralk's stingers liquefies the victim's insides in an agonizing transformation. The creature swells as its organs, muscles, and skeleton rapidly break down and reform, transforming the creature into a lemure in a burst of fiendish goo. The new lemure is subject to the will of more powerful devils, and its fate from that moment on is the same as any lemure's. The koralk's poison can work this transformation on demons, giving Arbeyach's armies a unique edge.

## Infernal Mounts

A koralk is strong enough for many devils to ride. They prefer only powerful devils as riders, but they obey their superiors and carry even the lowest of devils into battle if directed. Arbeyach often rides an especially large specimen into battle, called the Grand Annihilator by his devilish troops.

```statblock
"name": "Koralk Devil (ToB1-2023)"
"size": "Large"
"type": "fiend"
"subtype": "devil"
"alignment": "Lawful Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "136"
"hit_dice": "16d10 + 48"
"stats":
- !!int "20"
- !!int "13"
- !!int "17"
- !!int "10"
- !!int "11"
- !!int "13"
"speed": "40 ft."
"saves":
  "Charisma": !!int "5"
  "Wisdom": !!int "4"
  "Constitution": !!int "7"
"damage_resistances": "cold; bludgeoning, piercing, slashing from nonmagical attacks\
  \ that aren't silvered"
"damage_immunities": "fire, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., passive Perception 10"
"languages": "Infernal, telepathy 120 ft."
"cr": "11"
"traits":
- "desc": "Magical darkness does not impair the koralk's darkvision."
  "name": "Devil's Sight"
- "desc": "The koralk produces a potent poison that liquefies the innards of those\
    \ affected by it. Every hour that elapses after a creature succumbs to this poison,\
    \ it must succeed on a DC 17 Constitution saving throw or take 7 (2d6) poison\
    \ damage, and its hp maximum is reduced by that amount. Creatures with resistance\
    \ or immunity to poison or the [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ condition can be affected by this poison. Such creatures have advantage on the\
    \ saving throw. This potent poison remains within the creature's body until removed\
    \ by the [greater restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-restoration.md)\
    \ spell or similar magic. If a creature dies while suffering from this poison,\
    \ it rises as a lemure 1 hour later under the control of the nearest non-lemure\
    \ devil within 1 mile."
  "name": "Harvester Venom"
- "desc": "The koralk has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The koralk can't be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ while it can see an ally within 30 feet of it."
  "name": "Steadfast"
"actions":
- "desc": "The koralk makes one Bite attack, one Scythe attack, and three Stinger\
    \ attacks. It can replace its Scythe attack with a Vestigial Arms attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 14\
    \ (2d8 + 5) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 16\
    \ (2d10 + 5) slashing damage."
  "name": "Scythe"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 7 (1d4\
    \ + 5) piercing damage plus 7 (2d6) poison damage, and the target must succeed\
    \ on a DC 17 Constitution saving throw or succumb to the devil's venom (see the\
    \ Harvester Venom trait)."
  "name": "Stinger"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: If\
    \ the target is a Medium or smaller creature, it is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 17). Until this grapple ends, the creature is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and the devil can't use its Vestigial Arms on another target."
  "name": "Vestigial Arms"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/koralk-devil-tob1-2023.webp"
```
^statblock

## Environment

planar
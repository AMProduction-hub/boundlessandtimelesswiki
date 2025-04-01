---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/ooze
statblock: inline
aliases: ["Skitterhaunt"]
---
# [Skitterhaunt](03 - Player Log & Handouts\Mechanics\CLI\bestiary\ooze/skitterhaunt-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 332*  

*This large beetle moves erratically, leaking noxious fluid from its cracked exoskeleton.*

## Ooze Vermin

This parasitic ooze lives in the shells of monstrous vermin, such as beetles, scorpions, and spiders, which it has infested and killed. A skitterhaunt creature might be mistaken for its original, living version at a glance, but the sluggish, erratic movements and oozing carapace of skitterhaunts quickly reveal their true nature.

## Wide Range of Prey

A skitterhaunt infection can decimate whole nests of vermin. When those are in short supply, these oozes move on to prey on other species, such as ants, crabs, and other creatures with exoskeletons or similar hard outer shells.

## Hosts Required

Skitterhaunts can't survive long outside their host creatures; they quickly liquefy and lose their cohesion. A body abandoned by a skitterhaunt is an eerie, hollowed-out husk with a strong, acidic odor.

```statblock
"name": "Skitterhaunt (ToB1-2023)"
"size": "Large"
"type": "ooze"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "95"
"hit_dice": "10d10 + 40"
"stats":
- !!int "15"
- !!int "11"
- !!int "19"
- !!int "3"
- !!int "7"
- !!int "1"
"speed": "30 ft."
"damage_immunities": "acid"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 8"
"languages": ""
"cr": "4"
"traits":
- "desc": "A creature that hits the skitterhaunt with a melee attack while within\
    \ 5 feet of it takes 4 (1d8) acid damage."
  "name": "Broken Shell"
- "desc": "The skitterhaunt doesn't require sleep."
  "name": "Ooze Nature"
- "desc": "The creature within the vermin's shell is a shapeless ooze protected by\
    \ the vermin's exoskeleton. When the skitterhaunt is reduced to 0 hp, the exoskeleton\
    \ breaks, and the skitterhaunt ooze exits it. Once out of its exoskeleton, the\
    \ ooze is Small, has an AC of 10, 10 hp, and a speed of 15 feet, and it can move\
    \ through a space as narrow as 1 inch wide without squeezing. In addition, its\
    \ only attack is a Slam that uses the same statistics as its Sting, except it\
    \ deals bludgeoning damage instead of piercing damage. The skitterhaunt dies if\
    \ it remains outside of a host for more than 24 hours. It can exit or enter a\
    \ dead host's exoskeleton as a bonus action."
  "name": "Vermin Encasement"
"actions":
- "desc": "The skitterhaunt makes one Mandibles attack and one Sting attack, or it\
    \ makes two Sting attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d4\
    \ + 2) slashing damage plus 9 (2d8) acid damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 12) if it is a Medium or smaller creature. Until this grapple ends,\
    \ the creature is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and the skitterhaunt can't use its Mandibles on another target."
  "name": "Mandibles"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 6\
    \ (1d8 + 2) piercing damage plus 9 (2d8) acid damage."
  "name": "Sting"
- "desc": "The skitterhaunt infests a Large or smaller Beast with an exoskeleton within\
    \ 5 feet of it. The target must succeed on a DC 14 Constitution saving throw or\
    \ become [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the skitterhaunt no longer infests it. Every 24 hours that elapse, the\
    \ target must repeat the saving throw or take 7 (2d6) acid damage, and its hp\
    \ maximum is reduced by that amount. This reduction lasts until the target finishes\
    \ a long rest after the skitterhaunt no longer infests it. The target dies if\
    \ this reduces its hp maximum to 0. The skitterhaunt then takes control of the\
    \ body, dissolving the flesh and hiding within the exoskeleton. A target that\
    \ succeeds on two consecutive saving throws forces the skitterhaunt out of its\
    \ body and is immune to the skitterhaunt's Infest Vermin for the next 24 hours."
  "name": "Infest Vermin"
- "desc": "The skitterhaunt spits acid in a 30-foot line that is 5 feet wide. Each\
    \ creature in that line must make a DC 14 Dexterity saving throw, taking 18 (4d8)\
    \ acid damage on a failed save, or half as much damage on a successful one."
  "name": "Acid Spray (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/ooze/token/skitterhaunt-tob1-2023.webp"
```
^statblock

## Environment

forest, underdark
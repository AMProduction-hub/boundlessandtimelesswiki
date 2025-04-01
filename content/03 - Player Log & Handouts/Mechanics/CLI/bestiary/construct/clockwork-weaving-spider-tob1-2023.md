---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Clockwork Weaving Spider"]
---
# [Clockwork Weaving Spider](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/clockwork-weaving-spider-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 65*  

*This mechanical spider has long, spindly legs, including one equipped with a sharp blade that's disproportionately large for the creature's body.*

## Cloth Makers

These tiny, useful devices are a boon to weavers as they help produce clothing. They also sometimes serve as spies and defenders, for nothing is so invisible as a simple machine making cloth, day in and day out. As their name implies, these devices resemble large spiders but with ten limbs instead of eight. Two of their legs are equipped with loops or crooks useful in guiding thread on a loom, six are for moving and climbing, one is for stitching and extremely fast needlework, and one has a razor-sharp blade used to trim thread or cloth (or for attacking foes).

## Throw Poison

Weaving spiders rarely initiate combat unless directed to by their owners, but they instinctively defend themselves, their masters, and other weavers. A weaving spider throws its poisoned shuttle at the nearest foe, then climbs along the strand to attack that foe. Weaving spiders fight until destroyed or ordered to stand down. When spying, they flee as soon as they are threatened, to preserve whatever information they have gathered

> [!note] Clockwork Weaving Spiders in Midgard
> 
> Weaving spiders are built by priests of Rava and imbued with her divine energy, although their shells and armatures are made by the Arms and Armory Guild and the Geargrinders Guild, respectively. They are maintained, operated, and directed by the Honorable Order of Weavers in the Free City of Zobeck, and it is believed that weaving spiders sometimes serve as vessels for a Norn or a skein witch to speak to humans.
^clockwork-weaving-spiders-in-midgard

```statblock
"name": "Clockwork Weaving Spider (ToB1-2023)"
"size": "Tiny"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "30"
"hit_dice": "12d4"
"stats":
- !!int "10"
- !!int "16"
- !!int "10"
- !!int "9"
- !!int "8"
- !!int "8"
"speed": "40 ft., climb 40 ft."
"skillsaves":
  "Perception": !!int "3"
  "Acrobatics": !!int "5"
"damage_immunities": "poison, psychic"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "understands Common but can't speak"
"cr": "1"
"traits":
- "desc": "The weaving spider doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The weaving spider is immune to any spell or effect that would alter its\
    \ form."
  "name": "Immutable Form"
- "desc": "The weaving spider has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
- "desc": "The weaving spider's speed and its slim, sharp blade can slice cloth, leather,\
    \ and paper into scraps very quickly. Whenever a weaving spider's Trimming Blade\
    \ attack roll exceeds the target's Armor Class by 5 or more, the target must succeed\
    \ on a DC 13 Dexterity saving throw or one nonmagical cloth, leather, or paper\
    \ object on the target becomes damaged and unusable until repaired. This effect\
    \ can deface or ruin clothing, backpacks, journals, and similar objects, but it\
    \ can't destroy armor."
  "name": "Unmaking"
"actions":
- "desc": "The clockwork weaving spider makes two Trimming Blade attacks or two Poisoned\
    \ Needle Shuttle attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4\
    \ + 3) slashing damage."
  "name": "Trimming Blade"
- "desc": "Ranged Weapon Attack: +5 to hit, range 30 ft., one target. Hit: 7\
    \ (1d8 + 3) piercing damage, and the target must succeed on a DC 13 Constitution\
    \ saving throw or become [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ for 1 minute. The target can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success."
  "name": "Poisoned Needle Shuttle"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/clockwork-weaving-spider-tob1-2023.webp"
```
^statblock

## Environment

urban
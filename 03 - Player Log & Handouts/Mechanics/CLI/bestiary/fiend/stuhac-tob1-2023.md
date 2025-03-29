---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/13
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fiend
statblock: inline
aliases: ["Stuhac"]
---
# [Stuhac](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/stuhac-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 351*  

*This pale-skinned, white-bearded hermit wears a winter cloak and travels the mountain paths, cliff sides, and trade routes alone.*

## Feigns Weakness

Living in isolated mountain passes and foraging along little-traveled slopes, the stuhac is a master of stealth and deception. Wrapping heavy furs around itself, it poses as a feeble hermit or traveler needing assistance. Only after its victims have been lured away from warmth and safety does the stuhac drop its disguise and show its true nature: the withered traveler's gnarled hands uncurl to reveal jagged yellow claws, its cataract-ridden eyes are exposed as waxen orbs wobbling loosely in their sockets, and its clothing is revealed to be woven layers of yellowed tendon and ligament.

## Hideous Garments

The stuhac's most prized possessions are its "clutters," garments woven of layered and tangled ligaments and tendons. These grisly trophies are taken from scores of victims, and stuhacs treasure each bit of their disgusting attire. When two stuhacs meet, they compare their garb, swapping anecdotes of their most horrifying kills and deceptions. Stuhacs weave new ligaments into their clutters while their still-living victims watch. Lying in crippled agony, they cannot flee as the stuhac tears fresh material from their bodies for its garments. To keep screams from disturbing their work, these monsters first sever their victim's vocal chords.

## Devour Victims

Once its clutters are done, the stuhac feeds on its live victim, devouring everything but the bones. Finding a clean-picked humanoid skeleton along a mountain path is a reliable sign of a stuhac's presence.

```statblock
"name": "Stuhac (ToB1-2023)"
"size": "Medium"
"type": "fiend"
"alignment": "Neutral Evil"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "209"
"hit_dice": "22d8 + 110"
"stats":
- !!int "22"
- !!int "18"
- !!int "20"
- !!int "12"
- !!int "16"
- !!int "15"
"speed": "40 ft., climb 40 ft."
"saves":
  "Charisma": !!int "7"
  "Dexterity": !!int "9"
  "Strength": !!int "11"
  "Constitution": !!int "10"
"skillsaves":
  "Deception": !!int "12"
"damage_resistances": "acid; fire; lightning; bludgeoning, piercing from nonmagical\
  \ attacks"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Abyssal, Common, Infernal, telepathy 120 ft."
"cr": "13"
"traits":
- "desc": "The stuhac can move across and climb rocky surfaces without needing to\
    \ make an ability check. Additionally, difficult terrain composed of rocks or\
    \ rocky debris doesn't cost it extra movement."
  "name": "Mountain Walk"
- "desc": "The stuhac's long jump is up to 30 feet and tis high jump is up to 15 feet,\
    \ with or without a running start."
  "name": "Standing Leap"
"actions":
- "desc": "The stuhac can use Hobble. It then makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 20\
    \ (4d6 + 6) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 28\
    \ (5d8 + 6) slashing damage."
  "name": "Claw"
- "desc": "The stuhac telekinetically tears the tendons and ligaments of one creature\
    \ it can see within 60 feet of it. The target must succeed on a DC 18 Constitution\
    \ saving throw or take 13 (3d8) force damage and its speed is reduced by 10\
    \ feet. The stuhac can't reduce a creature's speed below 0 feet with this action.\
    \ This reduction lasts until the creature finishes a long rest or until removed\
    \ by the [greater restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-restoration.md)\
    \ spell or similar magic."
  "name": "Hobble"
- "desc": "The stuhac covers itself and anything it is wearing or carrying with a\
    \ magical illusion that makes it look like another creature of its general size\
    \ and Humanoid shape. The illusion ends if the stuhac takes a bonus action to\
    \ end it or if the stuhac dies.\n\nThe changes wrought by this effect fail to\
    \ hold up to physical inspection. For example, the stuhac could appear to have\
    \ gnarled hands, but someone touching the stuhac's hands would feel its jagged\
    \ claws. Otherwise, a creature must take an action to visually inspect the illusion\
    \ and succeed on a DC 20 Intelligence ([Investigation](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Investigation))\
    \ check to discern that the stuhac is disguised."
  "name": "Illusory Appearance"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/stuhac-tob1-2023.webp"
```
^statblock

## Environment

arctic, mountain
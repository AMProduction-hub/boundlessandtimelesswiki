---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Malphas"]
---
# [Malphas](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/malphas-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 262*  

*Keen eyed and dangerous, this winged fey warrior is dressed in finery.*

## Sworn to the Shadow Fey

Raised with a sword in their hands, the malphas are fierce warriors who serve the aristocracy of the shadow fey unswervingly.

## Corvid Fey

The malphas have many crow-like features, including beaks, black-feathered bodies and wings, and clawed feet and hands. On occasion, a cloaked ravenfolk traveling in fey lands might be mistaken for a malphas, and some less scrupulous ravenfolk use this to their advantage to manipulate fey they encounter. Malphas don't take kindly to such impersonations and are merciless toward any ravenfolk they discover pretending to be one of them.

## Messengers

Laconic in speech, they nevertheless serve as envoys and messengers from time to time. However, as much or more is communicated by the choice in messenger as in the message itself. Their crow-like features and the tendency of their masters to send bad news via malphas has earned them the nickname "storm crows" among many fey.

```statblock
"name": "Malphas (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Neutral Evil"
"ac": !!int "16"
"ac_class": "[studded leather](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/studded-leather-armor.md)"
"hp": !!int "135"
"hit_dice": "18d8 + 54"
"stats":
- !!int "19"
- !!int "19"
- !!int "16"
- !!int "14"
- !!int "13"
- !!int "18"
"speed": "40 ft., fly 30 ft."
"saves":
  "Dexterity": !!int "7"
  "Wisdom": !!int "4"
  "Constitution": !!int "6"
"skillsaves":
  "Perception": !!int "4"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Common, Ravenfolk, Sylvan"
"cr": "6"
"traits":
- "desc": "The malphas's weapon attacks are magical. When it hits with any weapon,\
    \ the weapon deals an extra 3d6 necrotic damage (included in the attack)."
  "name": "Shadow-Infused Weapons"
- "desc": "While in sunlight, the malphas has disadvantage on attack rolls, as well\
    \ as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
"actions":
- "desc": "The malphas makes two Longsword attacks or three Shadow Bolt attacks. If\
    \ both Longsword attacks hit one creature, the target must succeed on a DC 15\
    \ Constitution saving throw or be [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the end of its next turn, as shadows fill its eyes. A creature that can\
    \ see through magical darkness has advantage on this saving throw."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (1d8\
    \ + 4) slashing damage, or 9 (1d10 + 4) slashing damage if used with two hands,\
    \ plus 10 (3d6) necrotic damage."
  "name": "Longsword"
- "desc": "Ranged Spell Attack: +7 to hit, range 60 ft., one target. Hit: 14\
    \ (3d6 + 4) necrotic damage."
  "name": "Shadow Bolt"
"reactions":
- "desc": "When the malphas is hit by a ranged attack, it can make one Shadow Bolt\
    \ attack against the attacker. The malphas doesn't have disadvantage on this attack\
    \ from being within 5 feet of a hostile creature, though it may still have disadvantage\
    \ from other sources."
  "name": "Shadow Call"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/malphas-tob1-2023.webp"
```
^statblock

## Environment

planar, urban
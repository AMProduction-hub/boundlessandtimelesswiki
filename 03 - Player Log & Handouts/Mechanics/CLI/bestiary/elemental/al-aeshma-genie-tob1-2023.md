---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Al-Aeshma Genie"]
---
# [Al-Aeshma Genie](03 - Player Log & Handouts\Mechanics\CLI\bestiary\elemental/al-aeshma-genie-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 197*  

*The lower half of this genie is composed of scorching winds and desert sand.*

## Sand Djinnis

The al-aeshma are former djinn and share the same powers, albeit in a twisted style. Their skin is black as pitch, and their whirlwind form includes much dust and sand. When they are injured, the desert sand flows to seal their wounds and reattach severed limbs.

## Obligation of Wishes

Granting three wishes to a mortal is a sacred obligation among the genies, referred to as being wishbound. The Lords of Air mandate this as celestial law, and many believe that a djinni cannot refuse to grant a wish. Certainly, the consequences of disobedience are dire. Djinn who decline to grant a wish, are stripped of their wish power and handed to efreeti for 1,001 years of torture and debasement. Those who survive are banished to wander the Material Plane.

```statblock
"name": "Al-Aeshma Genie (ToB1-2023)"
"size": "Large"
"type": "elemental"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "149"
"hit_dice": "13d10 + 78"
"stats":
- !!int "21"
- !!int "15"
- !!int "22"
- !!int "15"
- !!int "16"
- !!int "20"
"speed": "30 ft., fly 90 ft. (hover)"
"saves":
  "Charisma": !!int "9"
  "Dexterity": !!int "6"
  "Wisdom": !!int "7"
"damage_immunities": "lightning, thunder"
"senses": "darkvision 120 ft., passive Perception 13"
"languages": "Auran, Common, Ignan"
"cr": "9"
"traits":
- "desc": "The al-aeshma casts one of the following spells, requiring no material\
    \ components and using Charisma as the spellcasting ability (spell save DC 17):\n\
    \nAt will: [detect magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-magic.md)\n\
    \n1/day each: [gaseous form](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/gaseous-form.md),\
    \ [invisibility](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/invisibility.md)\n\
    \n3/day each: [create or destroy water](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/create-or-destroy-water.md)\
    \ (destroy only), [wind walk](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/wind-walk.md)\
    \ (as an action)"
  "name": "Spellcasting"
- "desc": "The al-aeshma has advantage on attack rolls against creatures that are\
    \ flying."
  "name": "Air Hatred"
- "desc": "The al-aeshma is anchored to the earth and can't fly far from it. The al-aeshma\
    \ can't willingly fly more than 30 feet above the ground. If it starts its turn\
    \ more than 30 feet away from the ground, it loses its damage immunities and is\
    \ vulnerable to lightning and thunder damage until it starts its turn within 30\
    \ feet of the ground."
  "name": "Earth Bound"
- "desc": "When an al-aeshma dies, its body disintegrates into a swirling spray of\
    \ coarse sand, leaving behind only equipment it was wearing or carrying."
  "name": "Elemental Demise"
- "desc": "The al-aeshma regains 10 hp at the start of its turn. If it takes fire\
    \ or radiant damage, this trait doesn't function at the start of the al-Aeshma's\
    \ next turn. The al‑aeshma dies only if it starts its turn at 0 hp and doesn't\
    \ regenerate."
  "name": "Regeneration"
"actions":
- "desc": "The al-aeshma makes three Scimitar attacks. It can replace one attack with\
    \ a use of Dust Devil or Spellcasting."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d6 + 5) slashing damage plus 7 (2d6) necrotic damage."
  "name": "Scimitar"
- "desc": "The al-aeshma creates a swirling dust devil centered on a point it can\
    \ see within 120 feet of it. The dust devil appears in the shape of a cylinder\
    \ that is 30 feet tall with a 5-foot radius. Each creature in the area and each\
    \ creature that enters the area for the first time on a turn or starts its turn\
    \ there must succeed on a DC 17 Strength saving throw or be [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ While [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ a creature takes 7 (2d6) slashing damage and 7 (2d6) necrotic damage at\
    \ the start of each of the al-aeshma's turns. A creature, including a [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature, can take an action to free the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature by succeeding on a DC 17 Strength check.\n\nThe al-aeshma can use a\
    \ bonus action on its turn to move the dust devil up to 30 feet. A [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature doesn't move with the dust devil when the dust devil moves and is freed\
    \ if the dust devil moves out of its space. The dust devil lasts until the al-aeshma\
    \ loses its [concentration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ (as if [concentrating](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ on a spell), and the alaeshma can have only one dust devil active at a time."
  "name": "Dust Devil"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/elemental/token/al-aeshma-genie-tob1-2023.webp"
```
^statblock

## Environment

desert
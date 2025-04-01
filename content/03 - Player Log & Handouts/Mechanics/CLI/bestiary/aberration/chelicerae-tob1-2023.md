---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/badlands
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Chelicerae"]
---
# [Chelicerae](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/chelicerae-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 53*  

*The massive spider stands perched on tall, stilted legs, and the disheveled body of a robed arcanist swings from its clenched mandibles.*

## Feed on Spellcasters

These massive arachnids are largely confined to great forests and occasional wastelands, although rumors persist of sightings in the dark alleys of magocratic cities, causing trepidation among the spellcasters there. Few creatures pose such a threat to spellcasters as chelicerae.

## Carry Their Prey

Walking on high, stilted legs, these creatures resemble gigantic harvesters. More often than not, they are found with the grisly bodies of humanoids dangling from their clenched mandibles.

## Cocoon Arcanists

Chelicerae stalk isolated victims, striking with a poisonous bite then pinning the victim within powerful jaws. There, the victim's helpless body can hang for days on end as the chelicerae pursues obscure and eldritch tasks. At best, victims wake up weeks later with no memory of the events, far from home, and drained of vitality and spells. Others are stored immobilized in thick cocoons in a high treetop until their body and mind recover. A few unlucky victims are slain and rise a week later as walking dead that obey and protect the chelicerae.

```statblock
"name": "Chelicerae (ToB1-2023)"
"size": "Large"
"type": "aberration"
"alignment": "Neutral Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "153"
"hit_dice": "18d10 + 54"
"stats":
- !!int "22"
- !!int "17"
- !!int "17"
- !!int "18"
- !!int "15"
- !!int "14"
"speed": "40 ft., climb 30 ft."
"saves":
  "Charisma": !!int "5"
  "Dexterity": !!int "6"
  "Wisdom": !!int "5"
"skillsaves":
  "Athletics": !!int "9"
  "Stealth": !!int "6"
  "Perception": !!int "5"
  "Acrobatics": !!int "6"
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 15"
"languages": "understands Common but can't speak"
"cr": "7"
"traits":
- "desc": "The chelicerae casts one of the following spells, requiring no material\
    \ or verbal components and using Intelligence as the spellcasting ability (spell\
    \ save DC 15):\n\nAt will: [mage hand](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mage-hand.md),\
    \ [minor illusion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/minor-illusion.md)\n\
    \n1/day each: [haste](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/haste.md),\
    \ [hold person](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hold-person.md),\
    \ [invisibility](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/invisibility.md),\
    \ [phantasmal killer](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/phantasmal-killer.md)"
  "name": "Spellcasting"
- "desc": "The chelicerae has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
- "desc": "The chelicerae can climb difficult surfaces, including upside down on ceilings,\
    \ without needing to make an ability check."
  "name": "Spider Climb"
"actions":
- "desc": "The chelicerae makes one Bite attack and two Claw attacks. It can replace\
    \ the Bite attack with a use of Spellcasting."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 17\
    \ (2d10 + 6) piercing damage, and the target must succeed on a DC 15 Constitution\
    \ saving throw or become [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. If the target is a Medium or smaller creature and the chelicerae\
    \ doesn't have another creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
    \ the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 15). A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ target is also [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ while [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way. The [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ target can repeat the saving throw at the end of each of its turns, ending the\
    \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ condition on itself on a success."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 15\
    \ (2d8 + 6) slashing damage."
  "name": "Claw"
- "desc": "The chelicerae releases some of its stored magical energy in a burst. Each\
    \ creature within 15 feet of the chelicerae must make a DC 15 Dexterity saving\
    \ throw, taking 36 (8d8) force damage on a failed save, or half as much damage\
    \ on a successful one. After using Magical Discharge, the chelicerae can't do\
    \ so again until it successfully siphons magic from a creature or until it finishes\
    \ a long rest."
  "name": "Magical Discharge (Recharge Special)"
"bonus_actions":
- "desc": "The chelicerae takes the Dash or Disengage action."
  "name": "Nimble Moves"
- "desc": "The chelicerae siphons magic from a spellcaster it is grappling. The target\
    \ must succeed on a DC 15 Intelligence saving throw or lose one spell slot of\
    \ the highest level it can cast. The chelicerae then regains an expended use of\
    \ its Spellcasting."
  "name": "Siphon Magic"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/chelicerae-tob1-2023.webp"
```
^statblock

## Environment

badlands, forest
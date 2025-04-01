---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fiend
statblock: inline
aliases: ["Chort Devil"]
---
# [Chort Devil](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/chort-devil-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 93*  

*Small horns crown this pig-faced devil's head. It stands on shaggy goat legs and holds a flaming polearm in its clawed hands. It bears a wicked gleam in its black eyes*.

## Bad Bargains

Quick and canny, a chort devil delights in enticing mortals to make terrible bargains. A chort wants its victim to know it is dealing with a devil. The relative straightforwardness of this approach enables the creature to better deceive victims. After all, the chort affirms, if the victims weren't so desperate, they wouldn't be bargaining with a devil. If necessary, an implied threat of immolation gives it greater bargaining power, but the devil is careful not to torture or otherwise harm its patsy, as that voids any potential contract.

## Recitation of Contracts

Occasionally, some poor fool believes he can trick a chort and escape a legal bargain. The devil appears and recites the entirety of the contract its victim signed, replete with embarrassing details about a dispatched rival, the ensnarement of a lover, and other disclosures. A chort ensures all those entangled in its victim's affairs are present to hear the recitation, and it disappears once all the victim's dark secrets have been revealed.

## Smear Tactics

An opponent of the chort often finds itself the victim of its own hubris, as the devil digs up or creates vile tales about the opponent. For example, it may steal a paladin's sword and use it to murder an especially pious person, leaving the sword in the victim. Thus, a chort dispatches a foe resistant to its manipulations, brings suspicion to a potential foe, and taints a weapon—at least in reputation—which might be used against it.

```statblock
"name": "Chort Devil (ToB1-2023)"
"size": "Medium"
"type": "fiend"
"alignment": "Lawful Evil"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "187"
"hit_dice": "15d8 + 120"
"stats":
- !!int "24"
- !!int "20"
- !!int "26"
- !!int "18"
- !!int "20"
- !!int "20"
"speed": "30 ft."
"saves":
  "Charisma": !!int "9"
  "Dexterity": !!int "9"
  "Intelligence": !!int "8"
  "Strength": !!int "11"
  "Constitution": !!int "12"
"skillsaves":
  "Athletics": !!int "11"
  "Deception": !!int "9"
  "Insight": !!int "9"
  "Perception": !!int "9"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks that\
  \ aren't silvered"
"damage_immunities": "cold, fire, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., passive Perception 19"
"languages": "Celestial, Common, Infernal, telepathy 120 ft."
"cr": "12"
"traits":
- "desc": "The chort devil casts one of the following spells, requiring no material\
    \ components and using Charisma as the spellcasting ability (spell save DC 17):\n\
    \nAt will: [charm person](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/charm-person.md),\
    \ [illusory script](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/illusory-script.md)\
    \ (as an action)\n\n1/day: [haste](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/haste.md)\n\
    \n3/day each: [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md),\
    \ [modify memory](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/modify-memory.md)"
  "name": "Spellcasting"
- "desc": "Magical darkness doesn't impede the chort devil's darkvision."
  "name": "Devil's Sight"
- "desc": "The chort devil's weapon attacks are magical. When the devil hits with\
    \ any weapon, the weapon deals an extra 4d6 fire damage (included in the attack)."
  "name": "Hellish Weapons"
- "desc": "The chort devil has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The chort devil makes one Claw attack and two Ranseur attacks, or it makes\
    \ four Hurl Flame attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d4 + 7) slashing damage plus 14 (4d6) fire damage, and the target must\
    \ succeed on a DC 17 Constitution saving throw or have disadvantage on ability\
    \ checks and saving throws that use Charisma for 1 hour or until cured by a [lesser\
    \ restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/lesser-restoration.md)\
    \ spell or similar magic."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 12\
    \ (1d10 + 7) piercing damage plus 14 (4d6) fire damage."
  "name": "Ranseur"
- "desc": "Ranged Spell Attack: +9 to hit, range 120 ft., one target. Hit: 19\
    \ (4d6 + 5) fire damage."
  "name": "Hurl Flame"
- "desc": "The chort devil magically teleports, along with any equipment it is wearing\
    \ or carrying, up to 120 feet to an unoccupied space it can see."
  "name": "Teleport"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/chort-devil-tob1-2023.webp"
```
^statblock

## Environment

farmland, planar, urban
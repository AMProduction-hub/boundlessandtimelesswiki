---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Bonepowder Ghoul"]
---
# [Bonepowder Ghoul](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/bonepowder-ghoul-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 201*  

*Distilled to nothing but dry, whispering sand and a full set of teeth, this ghoulish creature still hungers for flesh and blood.*

## Starved Into Dust

The bonepowder ghoul is a small and unassuming pile of dust and bone fragments. Ghouls can achieve this powdery form through long starvation, a process that invariably takes decades. Rarely purposefully created, a bonepowder ghoul typically rises from the remnants of a ghoul trapped away from food, becoming animate hunger and hatred.

## Whispering Voices

Though bonepowder ghouls speak, their voices are faint. When they drain life force from living creatures, their dusty forms gain some substance, strengthening their voices enough to cast spells and command allies.

> [!note] Darakhul Fever
> 
> Spread mainly through bite wounds, this disease makes itself known within 24 hours by swiftly debilitating the infected. An infected creature must make a DC 17 Constitution saving throw after every long rest. On a failed save, the victim takes 14 (`4d6`) necrotic damage, and its hp maximum is reduced by an amount equal to the damage taken. This reduction lasts until the victim finishes a long rest after the disease is cured. The victim recovers from the disease by making two consecutive successful saving throws. Greater restoration cures the disease, while lesser restoration gives the victim advantage on the next saving throw. Primarily spread among Humanoids, the disease can affect ogres, and therefore other Giants may be susceptible. If a creature dies while infected with darakhul fever, roll a `d20`, add the character's Constitution modifier, and find the result on the Adjustment Table below to determine what Undead form the victim's body rises in.
> 
> | Roll | Result |
> |------|--------|
> | 1-9 | None; victim is simply dead |
> | 10-16 | Ghoul |
> | 17-20 | Ghast |
> | 21+ | Darakhul |
> ^roll-result
^darakhul-fever

```statblock
"name": "Bonepowder Ghoul (ToB1-2023)"
"size": "Small"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "180"
"hit_dice": "24d6 + 96"
"stats":
- !!int "10"
- !!int "20"
- !!int "18"
- !!int "19"
- !!int "15"
- !!int "18"
"speed": "30 ft."
"saves":
  "Charisma": !!int "8"
  "Dexterity": !!int "9"
  "Wisdom": !!int "6"
  "Constitution": !!int "8"
"skillsaves":
  "Stealth": !!int "9"
  "Perception": !!int "6"
"damage_resistances": "cold; lightning; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 16"
"languages": "Common, Darakhul, Draconic, Dwarvish"
"cr": "12"
"traits":
- "desc": "The bonepowder ghoul casts one of the following spells, requiring no material\
    \ components and using Charisma as the spellcasting ability (spell save DC 16):\n\
    \nAt will: [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md),\
    \ [mage hand](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mage-hand.md),\
    \ [ray of enfeeblement](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/ray-of-enfeeblement.md)\n\
    \n1/day: [phantasmal killer](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/phantasmal-killer.md)\n\
    \n3/day each: [blindness/deafness](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/blindness-deafness.md),\
    \ [fear](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fear.md)"
  "name": "Spellcasting (Coalesced Form Only)"
- "desc": "The bonepowder ghoul can move through a space as narrow as 1 inch wide\
    \ without squeezing."
  "name": "Amorphous (Dust Form Only)"
- "desc": "The ghoul requires no air or sleep."
  "name": "Hungry Dead Nature"
- "desc": "The bonepowder ghoul and any ghouls within 30 feet of it have advantage\
    \ on saving throws against effects that turn Undead."
  "name": "Turning Defiance"
"actions":
- "desc": "The bonepowder ghoul makes two Bite attacks. It can replace one Bite attack\
    \ with a use of Gravedust or Spellcasting. If both Bite attacks hit the same creature,\
    \ the target must succeed on a DC 17 Constitution saving throw or be [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ for 1 minute. The target can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 18\
    \ (3d8 + 5) piercing damage plus 9 (2d8) necrotic damage, and the target's\
    \ Strength score is reduced by 1d4. The target dies if this reduces its Strength\
    \ to 0. Otherwise, the reduction lasts until the target finishes a short or long\
    \ rest. If the target is a Humanoid, it must succeed on a DC 17 Constitution saving\
    \ throw or contract the darakhul fever disease."
  "name": "Bite"
- "desc": "The ghoul projects a 30-foot cone of grave dust. Each creature in the area\
    \ must succeed on a DC 17 Dexterity saving throw or take 13 (3d8) necrotic damage.\
    \ If a creature is a Humanoid, it must also succeed on a DC 17 Constitution saving\
    \ throw or contract the darakhul fever disease."
  "name": "Gravedust"
- "desc": "The ghoul creates a whirlwind of bones and teeth in a 20-foot cube originating\
    \ from it. Each creature in that area must make a DC 17 Dexterity saving throw.\
    \ On a failure, a creature takes 55 (10d10) slashing damage, and its Strength\
    \ score is reduced by 1d6. The creature dies if this reduces its Strength to\
    \ 0. Otherwise, the reduction lasts until the target finishes a short or long\
    \ rest. On a success, a creature takes half the damage and its Strength score\
    \ isn't reduced."
  "name": "Whirlwind (Dust Form Only; Recharge 5-6)"
"reactions":
- "desc": "When a bonepowder ghoul deals necrotic damage with Gravedust to at least\
    \ one creature that isn't a Construct or Undead, it can magically transform from\
    \ its dusty form into a coalesced form. Its statistics are the same in each form,\
    \ except it can speak audibly only in its coalesced form. The coalesced form lasts\
    \ for a number of minutes equal to the total necrotic damage it dealt with Gravedust\
    \ to creatures that aren't Constructs or Undead or until the ghoul ends it as\
    \ a bonus action."
  "name": "Coalesce"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/bonepowder-ghoul-tob1-2023.webp"
```
^statblock

## Environment

underdark
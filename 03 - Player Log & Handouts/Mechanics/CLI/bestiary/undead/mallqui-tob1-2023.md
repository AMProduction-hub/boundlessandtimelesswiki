---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Mallqui"]
---
# [Mallqui](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/mallqui-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 261*  

*With skin stretched like vellum over wizened limbs, a desiccated humanoid form clad in splendid regalia emerges from a funerary tower. The imposing figure has yellow points of light for eyes.*

## Cold Plateau Mummies

The people of the cold, rainless, mountain plateaus take advantage of their dry climes to mummify their honored dead, but without the embalming and curing of the corpse practiced in hotter lands. To preserve the knowledge and the place of their ancestors in the afterlife, their dead remain among them as counsellors and honorees on holy days.

## Undead Judges

The mallqui are not seen as malevolent, though at times they are severe judges against transgressors of their culture's ideals.

## Icons of Growth

Through their ability to draw the very moisture from the air, they are seen as conduits to the fertility of the earth. Mallqui also means "sapling" in the language of the people who create them.

```statblock
"name": "Mallqui (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Lawful Neutral"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "120"
"hit_dice": "16d8 + 48"
"stats":
- !!int "16"
- !!int "9"
- !!int "16"
- !!int "11"
- !!int "18"
- !!int "14"
"speed": "30 ft."
"saves":
  "Charisma": !!int "5"
  "Intelligence": !!int "3"
"skillsaves":
  "Religion": !!int "3"
  "Insight": !!int "7"
  "History": !!int "3"
"damage_resistances": "cold; lightning; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "the languages it knew in life"
"cr": "8"
"traits":
- "desc": "The mallqui casts one of the following spells, requiring no material components\
    \ and using Wisdom as the spellcasting ability (spell save DC 15):\n\nAt will:\
    \ [druidcraft](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/druidcraft.md)\n\
    \n1/day each: [locate animals or plants](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/locate-animals-or-plants.md),\
    \ [wind wall](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/wind-wall.md)\n\
    \n3/day each: [create or destroy water](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/create-or-destroy-water.md),\
    \ [entangle](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/entangle.md)"
  "name": "Spellcasting"
- "desc": "The mallqui regains 10 hp at the start of its turn. If the mallqui takes\
    \ radiant damage, this trait doesn't function at the start of the mallqui's next\
    \ turn. The mallqui dies only if it starts its turn with 0 hp and doesn't regenerate."
  "name": "Regeneration"
- "desc": "The mallqui doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
- "desc": "For every 5 feet the mallqui moves in water, or for every gallon of water\
    \ splashed on it, it takes 2 (1d4) radiant damage. In addition, the mallqui\
    \ takes 10 radiant damage when it starts its turn at least partially submerged\
    \ in water."
  "name": "Water Hypersusceptibility"
"actions":
- "desc": "The mallqui can use its Xeric Aura. It then makes three Xeric Blast attacks.\
    \ It can replace one attack with a use of Spellcasting."
  "name": "Multiattack"
- "desc": "Melee or Ranged Spell Attack: +7 to hit, reach 5 ft. or range 60 ft.,\
    \ one target. Hit: 18 (4d6 + 4) necrotic damage."
  "name": "Xeric Blast"
- "desc": "Each creature within 20 feet of the mallqui must succeed on a DC 15 Constitution\
    \ saving throw or suffer one level of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
    \ as moisture is drained from its body. If a creature's saving throw is successful,\
    \ it is immune to the mallqui's Xeric Aura for the next 24 hours."
  "name": "Xeric Aura"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/mallqui-tob1-2023.webp"
```
^statblock

## Environment

arctic, mountain
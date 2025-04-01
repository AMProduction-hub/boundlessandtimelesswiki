---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Liosalfar"]
---
# [Liosalfar](03 - Player Log & Handouts\Mechanics\CLI\bestiary\elemental/liosalfar-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 256*  

*The curtain of rippling colors assumes a humanoid form. Its kaleidoscope body shifts and glitters with mesmeric patterns.*

Sometimes known as "light elves" because they assume a vaguely elvish shape, these enigmatic elementals make their home at the edge of the world, where reality bends and physical laws unravel. Liosalfars' mutable bodies are composed entirely of shifting colors. Among themselves, they communicate through flashing patterns and hues, but they talk to others in an echoing, choral tone that seems to emanate from everywhere and nowhere around them.

## Servants of Fate

Their aims often seem inconsequential or simply baffling, but they've also sundered mountains and toppled kingdoms. Many believe liosalfars are agents of Fate, while others believe their motivations are an alien aesthetic or for their own amusement. Those who've spoken with liosalfars say they talk as if all existence was a sea of patterns and colors to be set in pleasing shapes.

## Enemies of the Ramag

Liosalfars have a longstanding rivalry with the portal-making ramags, whom they despise as "corruptors of the patterns."

```statblock
"name": "Liosalfar (ToB1-2023)"
"size": "Large"
"type": "elemental"
"alignment": "Neutral"
"ac": !!int "17"
"hp": !!int "132"
"hit_dice": "24d10"
"stats":
- !!int "10"
- !!int "25"
- !!int "10"
- !!int "18"
- !!int "18"
- !!int "12"
"speed": "0 ft., fly 60 ft. (hover)"
"saves":
  "Charisma": !!int "5"
  "Wisdom": !!int "8"
  "Intelligence": !!int "8"
  "Constitution": !!int "4"
"skillsaves":
  "Insight": !!int "8"
  "Perception": !!int "8"
  "Arcana": !!int "8"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison, psychic, radiant"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "truesight 120 ft., passive Perception 18"
"languages": "Celestial, Common, Elvish, Giant"
"cr": "10"
"traits":
- "desc": "The liosalfar takes 15 necrotic damage when it starts its turn in magical\
    \ darkness. While in magical darkness, it has disadvantage on attack rolls and\
    \ ability checks."
  "name": "Darkness Hypersensitivity"
- "desc": "The liosalfar doesn't require air, food, drink, or sleep."
  "name": "Elemental Nature"
- "desc": "The liosalfar is immune to any effect that would sense its emotions or\
    \ read its thoughts, as well as any divination spell that it refuses. Wisdom ([Insight](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Insight))\
    \ checks made to ascertain the liosalfar's intentions or sincerity have disadvantage."
  "name": "Inscrutable"
- "desc": "The liosalfar can enter a hostile creature's space and stop there. It can\
    \ move through a space as narrow as 1 inch wide without squeezing. In addition,\
    \ it sheds bright light in a 10- to 30‑foot radius and dim light for an additional\
    \ number of feet equal to the chosen radius. The liosalfar can alter the radius\
    \ as a bonus action."
  "name": "Light Form"
"actions":
- "desc": "The liosalfar makes two Radiant Touch or Ray of Light attacks. If both\
    \ Radiant Touch attacks hit one creature, the target must succeed on a DC 16 Constitution\
    \ saving throw or be [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the end of its next turn."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 29\
    \ (4d10 + 7) radiant damage."
  "name": "Radiant Touch"
- "desc": "Ranged Spell Attack: +8 to hit, range 60 ft., one target. Hit: 31\
    \ (6d8 + 4) radiant damage, and the target must succeed on a DC 16 Constitution\
    \ saving throw or be [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the end of its next turn."
  "name": "Ray of Light"
- "desc": "The liosalfar causes the light radiating from its body to shift color and\
    \ pattern in a spellbinding display. Each creature within 60 feet of the liosalfar\
    \ and that can see it must succeed on a DC 16 Wisdom saving throw or be [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ until the display ends. The liosalfar must take a bonus action on its subsequent\
    \ turns to continue the display. It can stop the display at any time, and the\
    \ display ends if the liosalfar is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated).\
    \ While [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ by the liosalfar's display, a creature is also [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated),\
    \ and its speed is reduced to 0, as it is transfixed by the display. The effect\
    \ ends for a [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ creature if it takes any damage or if someone uses an action to shake the creature\
    \ out of its stupor."
  "name": "Mesmerizing Radiance"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/elemental/token/liosalfar-tob1-2023.webp"
```
^statblock

## Environment

planar
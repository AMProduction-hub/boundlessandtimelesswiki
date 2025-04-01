---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mpp
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/aberration/gith
statblock: inline
aliases: ["Githzerai Futurist"]
---
# [Githzerai Futurist](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/githzerai-futurist-mpp.md)
*Source: Morte's Planar Parade p. 30, Sigil and the Outlands*  

Githzerai futurists have transcended their limits through focused meditation and can now catch glimpses of the future. They foresee the possible outcomes of battles, using those portents to tilt the balance in their favor.

## Githzerai

Githzerai descend from an ancient people who were also the progenitors of the githyanki—all of whom were destroyed or transformed by mind flayers. Many githzerai dwell in Limbo, honing their psionic powers by shaping their homes on that chaotic plane. The githzerai described here oftentimes traverse the planes, crossing between them via the portals in Sigil and the Outlands. To learn more about other githzerai, see the*Monster Manual*.

```statblock
"name": "Githzerai Futurist (MPP)"
"size": "Medium"
"type": "aberration"
"subtype": "gith"
"alignment": "Any alignment"
"ac": !!int "16"
"ac_class": "psychic defense"
"hp": !!int "149"
"hit_dice": "23d8 + 46"
"stats":
- !!int "14"
- !!int "17"
- !!int "15"
- !!int "17"
- !!int "17"
- !!int "13"
"speed": "40 ft."
"saves":
  "Dexterity": !!int "7"
  "Wisdom": !!int "7"
  "Intelligence": !!int "7"
  "Strength": !!int "6"
"skillsaves":
  "Insight": !!int "7"
  "Perception": !!int "7"
  "Arcana": !!int "7"
"senses": "truesight 30 ft., passive Perception 17"
"languages": "Common, Gith"
"cr": "9"
"traits":
- "desc": "The githzerai casts one of the following spells, requiring no spell components\
    \ and using Wisdom as the spellcasting ability (spell save DC 15):\n\nAt will:\
    \ [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md),\
    \ [levitate](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/levitate.md)\
    \ (self only), [mage hand](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mage-hand.md)\
    \ (the hand is invisible), [see invisibility](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/see-invisibility.md)\n\
    \n1/day each: [plane shift](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/plane-shift.md)\
    \ (self only), [scrying](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/scrying.md)\
    \ (as an action), [slow](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/slow.md),\
    \ [telekinesis](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/telekinesis.md)"
  "name": "Spellcasting (Psionics)"
- "desc": "While the githzerai is wearing no armor and wielding no shield, its AC\
    \ includes its Wisdom modifier."
  "name": "Psychic Defense"
"actions":
- "desc": "The githzerai makes three Unarmed Strike or Psychic Bolt attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d8 + 3) bludgeoning damage plus 11 (2d10) psychic damage."
  "name": "Unarmed Strike"
- "desc": "Ranged Spell Attack: +7 to hit, range 60 ft., one creature. Hit:\
    \ 21 (4d8 + 3) psychic damage."
  "name": "Psychic Bolt"
"reactions":
- "desc": "When the githzerai or a creature it can see makes an attack roll, a saving\
    \ throw, or an ability check, the githzerai can cause the roll to be made with\
    \ advantage or disadvantage."
  "name": "Future Insight (3/Day)"
"source":
- "MPP"
- "SatO"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/githzerai-futurist-mpp.webp"
```
^statblock
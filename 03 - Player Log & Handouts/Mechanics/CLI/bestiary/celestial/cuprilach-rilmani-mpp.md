---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mpp
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Cuprilach Rilmani"]
---
# [Cuprilach Rilmani](03 - Player Log & Handouts\Mechanics\CLI\bestiary\celestial/cuprilach-rilmani-mpp.md)
*Source: Morte's Planar Parade p. 44, Sigil and the Outlands*  

Cuprilachs infiltrate places of power throughout the multiverse, serving as spies and assassins. They strike surgically, following the orders of aurumachs without question or emotion.

Cuprilachs have wiry copper frames, with torsos that float above their waists, separated by a hovering, polished sphere. Agile and armed with an arsenal of deceptive magic, cuprilachs do whatever they must to complete their missions.

## Rilmani

Rilmani protect the balance between the forces and philosophies of the multiverse. They seek to maintain planar equilibrium, assuring that good, evil, law, or chaos never grow too powerful or too weak. To the rilmani, each of these forces is fundamental to the multiverse's existence. Whenever one threatens to tip the balance in its favor or a plane is on the verge of collapse, the rilmani act to even the odds.

While the rilmani might be found anywhere, they're most frequently encountered on their home plane, the Outlands, where they work to ensure that no force overexerts itself on the Concordant Opposition.

Rilmani are bipedal, with bodies of living metal that ranges in appearance from cold iron to brilliant gold. Most have smooth faces with few features, and their extraordinary anatomies often act in defiance of natural forces.

```statblock
"name": "Cuprilach Rilmani (MPP)"
"size": "Medium"
"type": "celestial"
"alignment": "typically  Neutral"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "202"
"hit_dice": "27d8 + 81"
"stats":
- !!int "12"
- !!int "20"
- !!int "16"
- !!int "16"
- !!int "15"
- !!int "14"
"speed": "40 ft."
"saves":
  "Charisma": !!int "6"
  "Dexterity": !!int "9"
"skillsaves":
  "Stealth": !!int "13"
  "Perception": !!int "6"
"damage_resistances": "psychic"
"senses": "truesight 120 ft., passive Perception 16"
"languages": "telepathy 120 ft., any four languages"
"cr": "12"
"traits":
- "desc": "The cuprilach casts one of the following spells, requiring no material\
    \ components and using Intelligence as the spellcasting ability (spell save DC\
    \ 15):\n\nAt will: [detect magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-magic.md),\
    \ [disguise self](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/disguise-self.md)\n\
    \n1/day each: [alter self](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/alter-self.md),\
    \ [fog cloud](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fog-cloud.md),\
    \ [silence](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/silence.md)"
  "name": "Spellcasting"
"actions":
- "desc": "The cuprilach makes three Burnished Blade or Bolt attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 8 (1d6\
    \ + 5) piercing damage plus 13 (2d12) psychic damage."
  "name": "Burnished Blade"
- "desc": "Ranged Weapon Attack: +9 to hit, range 20/60 ft., one target. Hit:\
    \ 7 (1d4 + 5) piercing damage plus 13 (2d12) psychic damage."
  "name": "Bolt"
"bonus_actions":
- "desc": "The cuprilach takes the Dash or Disengage action, or it makes one Burnished\
    \ Blade attack."
  "name": "Assassin's Agility"
"reactions":
- "desc": "The cuprilach halves the damage it takes from an attack that hits it, provided\
    \ it can see the attacker."
  "name": "Uncanny Dodge"
"source":
- "MPP"
- "SatO"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/celestial/token/cuprilach-rilmani-mpp.webp"
```
^statblock
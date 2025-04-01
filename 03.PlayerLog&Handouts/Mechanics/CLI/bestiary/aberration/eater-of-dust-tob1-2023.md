---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Eater of Dust"]
---
# [Eater of Dust](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/eater-of-dust-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 153*  

*This terrible creature resembles an imposing knight wearing baroque plate armor made of calcified resin. Its helm is a blank gray oval without eye slots or mouthpiece, and one of its arms ends in a slavering, fanged mouth.*

Eaters of dust can consume just about anything with their horrible maw-arms, but they prefer the flesh and souls of mortals. This ability to sustain themselves on almost anything, even on dust and soil, earned them their current name, given by the fiends that employ them, after their original name was long forgotten. A typical eater of dust is 7 feet tall and weighs more than 350 pounds. While an eater of dust cannot speak, it can telepathically communicate.

## Mercenary Companies

Eaters of dust—or*yakat-shi*as they are sometimes called in ancient planar texts—roam the lower planes selling their services to arch-devils, demon lords, and other fiendish rulers for the chance to sample new flavors and morsels. Eaters of dust feel only contempt for most other life forms. They attack and eat their non-eater allies at the first sign of weakness. Because of this, eaters of dust often operate in small, deadly units of eaters led by a powerful leader, styled the*yakat-norog*.

## Armor Shell

While many sages confuse eaters of dust for some obscure variety of fiend, they are aberrations escaped from a far-flung dimension of madness and nightmares. Indeed, their armor is not armor at all, but a secreted resin that hardens into a shell as strong as steel. When cracked, it exudes a nacreous blood, and the resulting scar resembles mother-of-pearl. Some old eaters are covered in intricate networks of shimmering scars.

```statblock
"name": "Eater of Dust (ToB1-2023)"
"size": "Medium"
"type": "aberration"
"alignment": "Neutral Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "114"
"hit_dice": "12d8 + 60"
"stats":
- !!int "20"
- !!int "14"
- !!int "20"
- !!int "10"
- !!int "15"
- !!int "17"
"speed": "30 ft."
"saves":
  "Charisma": !!int "7"
  "Strength": !!int "9"
  "Constitution": !!int "9"
"skillsaves":
  "Intimidation": !!int "7"
  "Athletics": !!int "9"
  "Perception": !!int "6"
"damage_resistances": "acid; cold; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"damage_immunities": "lightning, poison"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 120 ft. (blind beyond this radius), passive Perception 16"
"languages": "telepathy 120 ft. understands Abyssal, Common, Infernal, and Void Speech\
  \ but can't speak"
"cr": "9"
"traits":
- "desc": "The eater of dust's Maw-Arm attacks are magical. When the eater hits with\
    \ its Maw-Arm, the weapon deals an extra 3d8 necrotic damage (included in the\
    \ attack)."
  "name": "Magic Maw"
- "desc": "The eater of dust regains 5 hp at the start of its turn. If it takes fire\
    \ damage, this trait doesn't function at the start of eater's next turn. The eater\
    \ dies only if it starts its turn with 0 hp and doesn't regenerate."
  "name": "Regeneration"
"actions":
- "desc": "The eater of dust makes one Maw-Arm attack and two Necrotic Blast attacks,\
    \ or it makes three Necrotic Blast attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 12\
    \ (2d6 + 5) piercing damage plus 13 (3d8) necrotic damage, and the target\
    \ must succeed on a DC 17 Constitution saving throw or its hp maximum is reduced\
    \ by amount equal to the necrotic damage taken, and the eater regains hp equal\
    \ to that amount. This reduction lasts until the target finishes a long rest.\
    \ The target dies if this effect reduces its hp maximum to 0."
  "name": "Maw-Arm"
- "desc": "Melee or Ranged Spell Attack: +7 to hit, reach 5 ft. or range 60 ft.,\
    \ one target. Hit: 16 (3d8 + 3) necrotic damage."
  "name": "Necrotic Burst"
"bonus_actions":
- "desc": "The eater of dust magically teleports, along with any equipment it is wearing\
    \ or carrying, up to 60 feet to an unoccupied space within 10 feet of a creature\
    \ that isn't a Construct or Undead."
  "name": "Hungry Step"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/eater-of-dust-tob1-2023.webp"
```
^statblock

## Environment

planar
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Dogmole Juggernaut"]
---
# [Dogmole Juggernaut](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/dogmole-juggernaut-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 107*  

*This mole-like creature is the size of a large dog, with a thick, barrel-shaped body. A ring of tentacles sprouts above a mouth dominated by spade-like incisors, and cataracts fill its tiny eyes.*

## Domesticated by Dwarves

Mountain dwarves have domesticated many subterranean creatures, among them a breed of giant talpidae commonly called dogmoles. Energetic and obedient, dogmoles pull ore trolleys through mines, sniff out toxic gases and polluted waters, and help excavate trapped miners.

## Sense Cave-Ins

Dogmoles are renowned for their ability to detect imminent cave-ins and burrowing monsters, making them welcome companions in the depths. Outside the mines, dogmoles serve as pack animals, guard beasts, and bloodhounds.

## Derro Juggernauts

Derro also use dogmoles, but such unfortunate creatures are brutalized from birth and hardened by scarification, drugs, and warping magic. This treatment forces the dogmole to grow into a large, furless mass of muscle, scar tissue, and barbed piercings with incisors the size of shortswords. Derro use dogmole juggernauts as mounts and improvised siege engines or, when not at war, as gladiatorial contestants.

```statblock
"name": "Dogmole Juggernaut (ToB1-2023)"
"size": "Large"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "126"
"hit_dice": "12d10 + 60"
"stats":
- !!int "21"
- !!int "14"
- !!int "20"
- !!int "2"
- !!int "10"
- !!int "2"
"speed": "30 ft., burrow 20 ft., swim 10 ft."
"saves":
  "Constitution": !!int "8"
"senses": "blindsight 30 ft., passive Perception 10"
"languages": ""
"cr": "5"
"traits":
- "desc": "If the juggernaut burrows at half its burrowing speed, it can leave a 10-foot\
    \ diameter tunnel in its wake."
  "name": "Burrowed Tunnels"
- "desc": "The juggernaut has advantage on Strength and Dexterity checks and saving\
    \ throws made against effects that would push it or knock it [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Stout"
- "desc": "If the juggernaut takes 15 damage or less that would reduce it to 0 hp,\
    \ it is reduced to 1 hp instead."
  "name": "Relentless (Recharges after a Short or Long Rest)"
"actions":
- "desc": "The dogmole juggernaut makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d6 + 5) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. it: 12 (3d4\
    \ + 5) slashing damage."
  "name": "Claw"
"reactions":
- "desc": "When the juggernaut takes damage from a Small or larger insectoid Beast,\
    \ such as a giant centipede, or when it deals damage to such a creature, it enters\
    \ a special rage for 3 rounds. While in this rage, it has advantage on attack\
    \ rolls and Strength checks and deals an extra 5 (2d4) piercing damage with\
    \ its Bite attack, but its Armor Class is reduced by 2. The juggernaut can't end\
    \ this rage willingly."
  "name": "Wormkiller Rage"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/dogmole-juggernaut-tob1-2023.webp"
```
^statblock

## Environment

underdark
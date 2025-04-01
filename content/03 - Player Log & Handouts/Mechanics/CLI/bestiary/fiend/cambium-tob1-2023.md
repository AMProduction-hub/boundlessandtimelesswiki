---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/14
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend
statblock: inline
aliases: ["Cambium"]
---
# [Cambium](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/cambium-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 49*  

*Unfolding impossibly from beneath voluminous robes, this creature's pockmarked, spindly arms end in clusters of narrow spikes. Its long, hollow, needle-like fingers and its many-jointed arms move with surprising speed and strength for such an emaciated creature.*

## Hunched and Robed

The cambium skulks through mortal society, hunched and contorted, concealing its nine-foot height and its supernumerary arms.

## Devours Bodily Humors

The source of a cambium's interest lies in every mortal body: the four humors. It drains these from victims in precise amounts, sometimes to fix its own imbalances, sometimes to concoct serums to sell in hellish markets. Its victims are left in a desperate state, eager for a corrective fix and willing to obey the cambium's every whim as servants and toadies.

## Abandons Victims

After a sufficient crop has been harvested, the cambium abandons these addicts to die slowly from violent withdrawals, and allows the local population to lie fallow for a decade or so.

```statblock
"name": "Cambium (ToB1-2023)"
"size": "Large"
"type": "fiend"
"alignment": "Neutral Evil"
"ac": !!int "19"
"ac_class": "natural armor"
"hp": !!int "264"
"hit_dice": "23d10 + 138"
"stats":
- !!int "21"
- !!int "16"
- !!int "23"
- !!int "17"
- !!int "16"
- !!int "18"
"speed": "40 ft., fly 30 ft. (hover)"
"saves":
  "Charisma": !!int "9"
  "Dexterity": !!int "8"
  "Wisdom": !!int "8"
  "Intelligence": !!int "8"
  "Constitution": !!int "11"
"skillsaves":
  "Medicine": !!int "8"
  "Deception": !!int "9"
  "Stealth": !!int "8"
  "Insight": !!int "8"
  "Perception": !!int "8"
  "Arcana": !!int "8"
"damage_immunities": "poison"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "darkvision 60 ft., passive Perception 18"
"languages": "Common, Draconic, Infernal"
"cr": "14"
"traits":
- "desc": "The cambium casts one of the following spells, requiring no material components\
    \ and using Charisma as the spellcasting ability (spell save DC 17):\n\nAt will:\
    \ [alter self](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/alter-self.md),\
    \ [detect thoughts](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-thoughts.md),\
    \ [spare the dying](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/spare-the-dying.md)\n\
    \n1/day: [plane shift](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/plane-shift.md)\
    \ (self only)\n\n3/day each: [hold person](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hold-person.md),\
    \ [protection from poison](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/protection-from-poison.md),\
    \ [heal](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/heal.md)"
  "name": "Spellcasting"
"actions":
- "desc": "The cambium makes four Needle Fingers or Poison Ray attacks. It can replace\
    \ two attacks with a use of Spellcasting."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 21\
    \ (3d10 + 5) piercing damage."
  "name": "Needle Fingers"
- "desc": "Ranged Spell Attack: +9 to hit, range 60 ft., one target. Hit: 22\
    \ (4d8 + 4) poison damage, and the target must succeed on a DC 17 Constitution\
    \ saving throw or become [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn."
  "name": "Poison Ray"
"bonus_actions":
- "desc": "The cambium twists the bodily humors of a creature within 30 feet of it\
    \ that isn't a Construct or Undead and that it hit with Needle Fingers in the\
    \ past minute. The target must succeed on a DC 17 Constitution saving throw or\
    \ its Strength, Dexterity, or Constitution score (the cambium's choice) is reduced\
    \ by 1d4. The target falls [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ if this reduces an ability score to 0. This reduction lasts until the target\
    \ finishes a long rest."
  "name": "Damage Ability"
- "desc": "If the cambium has hit a creature that isn't a Construct or Undead with\
    \ Needle Fingers in the past minute, it can cause a surge in one of the target's\
    \ bodily humors, causing an imbalance. The target must succeed on a DC 17 Constitution\
    \ saving throw or suffer one of the following effects of the cambium's choice.\
    \ Unless noted otherwise, the target can repeat the saving throw at the end of\
    \ each of its turns, ending the effect on itself on a success.\n\n- Sanguine\
    \ Flux. The target can't regain hp—naturally or magically—until after it finishes\
    \ a long rest.  \n- Choleric Flux. The target becomes confused for 1 minute.\
    \ This effect works as if the target failed a saving throw against the [confusion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/confusion.md)\
    \ spell, except the cambium doesn't have to maintain [concentration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration).\
    \  \n- Melancholic Flux. The target is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ and its speed is halved for 1 minute.  \n- Phlegmatic Flux. The target is\
    \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute.  "
  "name": "Imbalance Humors"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/cambium-tob1-2023.webp"
```
^statblock

## Environment

farmland, urban
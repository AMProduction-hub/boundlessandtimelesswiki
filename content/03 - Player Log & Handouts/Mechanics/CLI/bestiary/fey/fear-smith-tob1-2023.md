---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Fear Smith"]
---
# [Fear Smith](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/fear-smith-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 169*  

*This well-dressed figure appears elven, save for its featureless face and taloned hands.*

Known as a fiarsídhe among themselves, fear smiths are servants of shadow fey courts and other, similar dark fey courts. While its mouth is closed, a fear smith's face is featureless save for rows of deep wrinkles. Opening the large mouth in the center of its face reveals long needlelike teeth surrounding a single, massive eye.

## Icy-Cold Eyes

Fear smiths often serve as torturers or are dispatched to demoralize the court's enemies. Their stare stops enemies cold, making it easy for heavily-armed warriors to trap and finish a foe.

## Devour Fear

Fear smiths feed off strong emotions, and their favorite meal is terror. The fey prefer prolonging the death of victims, and, when free to indulge, a fear smith stalks its victim for days before attacking, hinting at its presence to build dread.

## Hoods and Masks

Fear smiths favor fine clothing and high fashion, donning hooded cloaks or masks when discretion is required. Eerily well-mannered and respectful, fear smiths enjoy feigning civility and playing the part of nobility, speaking genteelly but with a thick, unidentifiable accent.

```statblock
"name": "Fear Smith (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Chaotic Neutral"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "149"
"hit_dice": "23d8 + 46"
"stats":
- !!int "11"
- !!int "17"
- !!int "14"
- !!int "11"
- !!int "15"
- !!int "18"
"speed": "40 ft., climb 15 ft."
"saves":
  "Wisdom": !!int "6"
"skillsaves":
  "Intimidation": !!int "8"
  "Stealth": !!int "7"
"damage_resistances": "bludgeoning, piercing, slashing from attacks not made with\
  \ cold iron weapons"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "blindsight 30 ft., passive Perception 12"
"languages": "Common, Elvish, Sylvan"
"cr": "10"
"traits":
- "desc": "The fear smith casts one of the following spells, requiring no verbal or\
    \ material components and using Charisma as the spellcasting ability (spell save\
    \ DC 16):\n\nAt will: [detect thoughts](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-thoughts.md),\
    \ [fear](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fear.md)\n\n\
    2/day each: [charm person](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/charm-person.md),\
    \ [command](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/command.md)"
  "name": "Spellcasting"
- "desc": "Those who meet the gaze of the fear smith experience the world seeming\
    \ to twist at unnatural angles beneath their feet. When a creature that can see\
    \ the fear smith's eye starts its turn within 30 feet of the fear smith, the fear\
    \ smith can force the creature to make a DC 16 Wisdom saving throw if the fear\
    \ smith isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ and can see the creature. On a failed save, the creature is disoriented until\
    \ the start of its next turn. While disoriented, a creature can't take the Dash\
    \ or Disengage action, and when it moves for the first time on its turn, it must\
    \ succeed on a DC 16 Dexterity saving throw or fall [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\n\
    \nUnless surprised, a creature can avert its eyes to avoid the saving throw at\
    \ the start of its turn. If the creature does so, it can't see the fear smith\
    \ until the start of its next turn, when it can avert its eyes again. If the creature\
    \ looks at the fear smith in the meantime, it must immediately make the save."
  "name": "Distortion Gaze"
- "desc": "The fear smith has advantage on saving throws against being [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)."
  "name": "Hidden Eye"
- "desc": "The fear smith has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The fear smith makes three Claw attacks. It can replace one attack with\
    \ a use of Heart-Stopping Stare."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d8 + 3) slashing damage plus 9 (2d8) psychic damage. If the target is\
    \ disoriented by Distortion Gaze, the fear smith regains hp equal to the amount\
    \ of psychic damage dealt."
  "name": "Claw"
- "desc": "The fear smith terrifies a creature within 30 feet of it with a look. The\
    \ target must succeed on a DC 16 Wisdom saving throw or take 13 (3d8) psychic\
    \ damage and be [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the end of its next turn. The fear smith regains hp equal to the psychic\
    \ damage dealt."
  "name": "Heart-Stopping Stare"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/fear-smith-tob1-2023.webp"
```
^statblock

## Environment

planar, urban
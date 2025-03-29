---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/humanoid/derro
statblock: inline
aliases: ["Derro Fetal Savant"]
---
# [Derro Fetal Savant](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/derro-fetal-savant-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 88*  

*This creature resembles a blue-skinned dwarven infant, no older than a year. Its limbs flail, its head lolls with an obvious lack of coordination, and it screams incessantly.*

Of the madness and insanity that resonates so strongly in derro society, perhaps none is as twisted as the derro fetal savant, born insane by the blessing of their eldritch masters and destined to lead their people further into madness.

## Soul Swapping

Only the rarest of derro are born with the ability to exchange souls with other creatures, and the babbling infants are treated with maddened reverence. Oddly, this unique power causes an extreme sensitivity to bright light.

## Carried into Battle

Placed in small, pillowed cages and borne aloft on hooked staves, the wild-eyed, magically gifted newborns are used to sow confusion among enemy ranks. Though typically carried into battle, fetal savants can make their cages float, freeing their carriers to better defend them when necessary.

```statblock
"name": "Derro Fetal Savant (ToB1-2023)"
"size": "Tiny"
"type": "humanoid"
"subtype": "derro"
"alignment": "Chaotic Evil"
"ac": !!int "11"
"hp": !!int "32"
"hit_dice": "13d4"
"stats":
- !!int "5"
- !!int "12"
- !!int "10"
- !!int "8"
- !!int "12"
- !!int "20"
"speed": "10 ft."
"saves":
  "Charisma": !!int "7"
  "Wisdom": !!int "3"
"skillsaves":
  "Perception": !!int "3"
"damage_immunities": "psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Dwarvish, telepathy 60 ft."
"cr": "4"
"traits":
- "desc": "The savant is immune to damage and can't be the target of spells or effects\
    \ as long as its cage exists. The cage has a flying speed of 30 feet while the\
    \ savant is inside of it, moving at the mental command of the savant. When the\
    \ cage is destroyed, the savant floats gently to the ground. The cage has AC 19,\
    \ 75 hp, and is immune to piercing, poison, and psychic damage. A non-derro that\
    \ touches the cage or hits it with a melee weapon attack while within 5 feet of\
    \ it must succeed on a DC 15 Wisdom saving throw or take 7 (2d6) psychic damage\
    \ and be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ until the end of its next turn. The cage disintegrates if exposed to sunlight\
    \ for 1 hour."
  "name": "Enchanted Cage"
- "desc": "The savant constantly babbles eldritch nonsense while it can see any non-derro\
    \ creatures and isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated).\
    \ Each non-derro creature that starts its turn within 20 feet of the savant and\
    \ can hear the babbling must succeed on a DC 15 Wisdom saving throw or be [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ until the start of its next turn."
  "name": "Maddening Babble"
- "desc": "The savant takes 20 radiant damage when it starts its turn outside the\
    \ cage and in sunlight."
  "name": "Sunlight Hypersensitivity"
"actions":
- "desc": "The fetal savant makes two Psychic Burst attacks."
  "name": "Multiattack"
- "desc": "Melee or Ranged Spell Attack: +7 to hit, reach 5 ft. or range 60 ft.,\
    \ one target. Hit: 14 (2d8 + 5) psychic damage."
  "name": "Psychic Burst"
- "desc": "The savant exchanges its soul with one Humanoid it can see within 20 feet\
    \ of it. Its body becomes [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
    \ the target's soul inhabits the savant's [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ body, and the savant inhabits the target's body, taking full control of it.\
    \ The savant retains its alignment, its Intelligence, Wisdom, and Charisma scores,\
    \ its Psychic Burst action, and its immunity to being [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ and [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened).\
    \ It otherwise uses the target's statistics, but doesn't gain access to the target's\
    \ knowledge, class features, or proficiencies.\n\nThe exchange lasts until the\
    \ target's body or the savant's body is reduced to 0 hp, the savant ends it as\
    \ a bonus action, or the savant is forced out by an effect like the [dispel evil\
    \ and good](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-evil-and-good.md)\
    \ spell. When the exchange ends, the target returns to its body, regaining control,\
    \ and the savant's soul returns to its body, which is no longer [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed).\
    \ The target is immune to this savant's Soul Exchange for 24 hours after succeeding\
    \ on the saving throw or after the exchange ends."
  "name": "Soul Exchange (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/derro-fetal-savant-tob1-2023.webp"
```
^statblock

## Environment

underdark
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fiend/shapechanger
statblock: inline
aliases: ["Bouda"]
---
# [Bouda](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/bouda-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 42*  

*A hulking, hyena-faced humanoid with a heavily scarred, oversized muzzle steps forward, clouds of gnats and fleas roiling around it.*

## Glowing Eyes and Teeth

Bouda are peopleeaters and despoilers of purity and family. Resembling oversized gnolls, the web of scars along their muzzles provides evidence of their gluttonous eating habits. Forever leering, their teeth glow as yellow as their eyes.

## Fly-Bedecked Shapechangers

Bouda lurk on society's fringes, shapechanging to blend in with mortals. They seek out happy families, consuming the most vulnerable members in the night and leaving gruesome trophies behind. They may mark a victim nights before attacking to terrify the helpless family.

## Gluttons

Bouda have a weakness: they are incorrigible gluttons. When presented with a fresh corpse, even in combat, they attempt to gorge on it or at least defile it for later consumption. Bouda are vindictive, seeking revenge on anything that drives them from a kill.

```statblock
"name": "Bouda (ToB1-2023)"
"size": "Medium"
"type": "fiend"
"subtype": "shapechanger"
"alignment": "Neutral Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "93"
"hit_dice": "11d8 + 44"
"stats":
- !!int "19"
- !!int "14"
- !!int "18"
- !!int "10"
- !!int "12"
- !!int "15"
"speed": "30 ft. (50 ft. in hyena form)"
"saves":
  "Charisma": !!int "5"
  "Dexterity": !!int "5"
  "Wisdom": !!int "4"
  "Constitution": !!int "7"
"skillsaves":
  "Intimidation": !!int "5"
  "Athletics": !!int "7"
  "Deception": !!int "5"
  "Stealth": !!int "5"
  "Perception": !!int "4"
"damage_resistances": "acid; lightning; bludgeoning, piercing, slashing from nonmagical\
  \ attacks that aren't silvered"
"damage_immunities": "fire, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "magic. the bouda senses magic within 30 feet of it at will. this trait\
  \ otherwise works like the detect magic spell but isn't itself magical., passive\
  \ Perception 14"
"languages": "Celestial, Common, Infernal, telepathy 100 ft."
"cr": "5"
"actions":
- "desc": "The bouda makes one Bite attack and one Mephitic Claw attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) piercing damage plus 10 (3d6) poison damage."
  "name": "Bite (Giant Hyena or Hybrid Form Only)"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) slashing damage, and the target must succeed on a DC 15 Constitution\
    \ saving throw or become [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn."
  "name": "Mephitic Claw (Giant Hyena or Hybrid Form Only)"
- "desc": "The bouda consumes the organs of a corpse within 5 feet of it that is less\
    \ than 7 days old. It gains temporary hp equal to twice the dead creature's CR\
    \ for 1 hour. The bouda can't use Ravenous Gorge on a corpse if it or another\
    \ bouda has already use Ravenous Gorge on the corpse."
  "name": "Ravenous Gorge"
"bonus_actions":
- "desc": "The bouda transforms into a human, a hyena, or back into its true form,\
    \ which is a hyena-human hybrid. Its statistics, other than its speed, are the\
    \ same in each form. Any equipment it is wearing or carrying isn't transformed.\
    \ It reverts to its true form if it dies, then crumbles to dust moments later."
  "name": "Change Shape"
- "desc": "The bouda secretes a disgusting whitish-yellow substance with the viscosity\
    \ of tar and smears the substance on an object, unoccupied space, or creature\
    \ within 5 feet of it. An unwilling creature must succeed on a DC 15 Dexterity\
    \ saving throw to avoid the smear. Each creature, other than a bouda or hyena,\
    \ that starts its turn within 30 feet of the smeared target must succeed on a\
    \ DC 15 Constitution saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. If a creature's saving throw is successful or the effect ends\
    \ for it, the creature is immune to that source of Defiling Smear for the next\
    \ 24 hours. The stench of a smear remains potent for 7 days or until removed by\
    \ the [greater restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-restoration.md)\
    \ spell or similar magic."
  "name": "Defiling Smear (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/bouda-tob1-2023.webp"
```
^statblock

## Environment

farmland, urban
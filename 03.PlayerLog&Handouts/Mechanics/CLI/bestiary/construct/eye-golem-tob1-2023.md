---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/11
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Eye Golem"]
---
# [Eye Golem](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/eye-golem-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 216*  

*Eye-like sigils dot the smooth, marble skin of this statue. One of the eye sigils opens, and a beam of brilliant light shines out.*

## Covered in Arcana

Eye golems stand at least ten feet tall, and their magically durable hide is covered with real eyes as well as arcane sigils that resemble eyes.

## Blinds Victims

An eye golem rarely kills its victims, choosing to steal its victims' eyes instead. The victims are left blinded, wandering, and tormented, seeing only visions of the eye golem flashing through their memories. This drives some mad, while others instead choose to serve the golem, becoming devoted to the one who still holds sight.

## All Eyes Open

When killed, an eye golem does not simply fall down dead. All of its eyes open at once, and a blinding burst of light shines from the body. When the light stops, hundreds of perfectly preserved eyeballs remain where its body fell, still warm, fresh, and without scars or damage. Detectable only by those trained in the arcane arts, each eye emits a barely perceptible beam of light, connecting it to its owner. The creature that holds the golem's central eye after it is slain can use the eye to restore stolen eyes to their victims.

```statblock
"name": "Eye Golem (ToB1-2023)"
"size": "Large"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "20"
"ac_class": "natural armor"
"hp": !!int "157"
"hit_dice": "15d10 + 75"
"stats":
- !!int "22"
- !!int "9"
- !!int "20"
- !!int "5"
- !!int "11"
- !!int "1"
"speed": "30 ft."
"skillsaves":
  "Perception": !!int "8"
"damage_immunities": "poison; psychic; radiant; bludgeoning, piercing, slashing from\
  \ nonmagical attacks that aren't adamantine"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "truesight 120 ft., passive Perception 18"
"languages": "understands the languages of its creator but can't speak"
"cr": "11"
"traits":
- "desc": "When the golem reduces a creature to 0 hp, it can blind the creature permanently.\
    \ If it does so, the creature is reduced to 1 hp instead."
  "name": "Blinding Demise"
- "desc": "The golem doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The golem is immune to any spell or effect that would alter its form."
  "name": "Immutable Form"
- "desc": "The golem's Slam attacks are magical. When the golem hits with a Slam attack,\
    \ the attack deals an extra 4d8 radiant damage (included in the attack)."
  "name": "Light-Infused Fists"
- "desc": "The golem has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The eye golem can use its Primal Voice of Doom. It then makes two Slam\
    \ attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 17\
    \ (2d10 + 6) bludgeoning damage plus 18 (4d8) radiant damage."
  "name": "Slam"
- "desc": "The golem opens all of its eyes and emits a burst of blinding light. Each\
    \ creature within 30 feet of it must make a DC 17 Dexterity saving throw. On a\
    \ failure, a creature takes 35 (10d6) radiant damage and is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded).\
    \ A creature that fails the saving throw by 5 or more is also [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the end of its next turn. A [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Gaze of Ancient Light (Recharge 5-6)"
- "desc": "The golem intones a disturbing invocation of the sun god at one creature\
    \ it can see within 30 feet of it. The target must succeed on a DC 17 Wisdom saving\
    \ throw or be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. The [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ target can repeat the saving throw at the end of each of its turns, ending the\
    \ effect on itself on a success."
  "name": "Primal Voice of Doom"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/eye-golem-tob1-2023.webp"
```
^statblock

## Environment

any, urban
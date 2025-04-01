---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Sandman"]
---
# [Sandman](03 - Player Log & Handouts\Mechanics\CLI\bestiary\celestial/sandman-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 313*  

*Stick-thin and moon-faced with a raptor's eyes and a mane of hawk feathers, this grinning humanoid pirouettes as nimbly as a dancer. Between its long, taloned fingers trickles sand that gleams with the cold light of stars.*

## Bringers of Nightmares

Sandmen are sinister-looking bringers of sleep and dreams. Visiting the mortal world each night, sandmen ensure that their targets slumber deeply and experience vivid dreams that swell the dream realm's power. Some sandmen develop a talent for a specific flavor of dream; fantasies of lost love or childhood, prophecies and religious visions, or terrible nightmares.

## Abduct Dreamers

Powerful dreamers attract both the attention and the protection of sandmen: children, madmen, would-be tyrants, and heroes. They protect such charges fiercely but have also been known to abduct them, taking them on wild adventures to inspire yet greater dreams. To them, all dreams are vital and good, be they uplifting or terrifying. Although they bring horrific nightmares as well as idyllic dreams, sandmen are not specifically baneful. Their actions are motivated by their connection to the dream realm, not by concerns over good and evil.

## Ethereal Dreamscapes

When not on the Material Plane, sandmen ride bubble-like dreamscapes through the Ethereal Plane, breaching the Sea of Possibilities, nurturing and harvesting its contents. Sandmen are a common and welcome sight in markets across the Fey Realms, elemental planes, and even in Hell—anywhere that dreams or nightmares are a valuable commodity. They are merciless to any who threaten the sanctity of dreams, but especially dream eaters.

```statblock
"name": "Sandman (ToB1-2023)"
"size": "Medium"
"type": "celestial"
"alignment": "Chaotic Neutral"
"ac": !!int "14"
"hp": !!int "82"
"hit_dice": "11d8 + 33"
"stats":
- !!int "11"
- !!int "19"
- !!int "16"
- !!int "13"
- !!int "14"
- !!int "19"
"speed": "40 ft."
"saves":
  "Charisma": !!int "7"
  "Wisdom": !!int "5"
"damage_resistances": "cold; fire; lightning; bludgeoning, piercing, slashing from\
  \ nonmagical attacks"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "truesight 60 ft., passive Perception 12"
"languages": "Celestial, Common, telepathy 60 ft., Umbral"
"cr": "5"
"traits":
- "desc": "The sandman has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "Made partially from dreams and imagination, the sandman isn't fully real.\
    \ Any critical hit against the sandman is a normal hit."
  "name": "Stuff of Dreams"
"actions":
- "desc": "The sandman makes two Claw attacks. It can replace one attack with a use\
    \ of Dreamer's Sand, if available."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) slashing damage plus 7 (2d6) psychic damage. Damage from this\
    \ attack doesn't wake an [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ creature, unless the [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ creature is below half its hp maximum. If the sandman scores a critical hit,\
    \ the target is cursed with the eye-closer's curse. While cursed, the creature\
    \ is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until it finishes a long rest or until the curse is lifted by remove curse or\
    \ similar magic."
  "name": "Claw"
- "desc": "The sandman encourages powerful dreams in the minds of up to three [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ creatures it can see within 30 feet of it. Each target must make a DC 15 Charisma\
    \ saving throw. On a failure, nightmares fill the target's mind, and the target\
    \ takes 35 (10d6) psychic damage, wakes from its sleep, and is [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. On a success, pleasant dreams fill the target's mind, and the\
    \ target regains 10 3d6 hp and can choose to remain [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ or awaken. A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ target can repeat the saving throw at the end of each of its turns, ending the\
    \ effect on itself on a success."
  "name": "Encourage Dreams (Recharge 5-6)"
- "desc": "The sandman throws magical sand in a 30-foot cone. Each creature in that\
    \ area must succeed on a DC 15 Constitution saving throw or fall [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ for 10 minutes. This effect ends for a creature if the creature takes damage\
    \ or another creature uses an action to wake it."
  "name": "Dreamer's Sand (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/celestial/token/sandman-tob1-2023.webp"
```
^statblock

## Environment

planar
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/17
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Moonlit King"]
---
# [Moonlit King](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/moonlit-king-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 176*  

*Dressed in archaic nobleman's finery, this elf lord has wildly unkempt bluish hair and pale, almost luminous skin. His eyes bulge slightly from their sockets as they stare vacantly. The lord's shadow moves slightly out of sync with his body, which appears solid in some portions and nearly transparent in others*.

His Lunar and Royal Majesty, Ludomir Imbrium the XVI, is also known as the Moonlit King of the Shadow Fey, Lord of Shadows, Duke of the Elves, and Master of the Winter Palace. A creature consumed by madness, the Moonlit King is an ephemeral vestige of greatness lost. He barely lives in reality anymore, and he is beset by phantoms from his own mind conjured from shadows and regret.

## Dwindling Power

The Moonlit King lost the favor of his wife, the Queen of Night and Magic, long ago. When he fell from power, the Queen exiled him, banishing him from his seat in the courts of the shadow fey. Now he endures in the crumbling, far-flung Tower of the Moon. The King has sunk deep into madness during his isolation and has turned to bargains with demons and devils in a desperate bid to regain freedom.

## Fey Lords and Ladies

Fey are capricious, mischievous, and often dangerous beings. However, despite their chaotic reputations, they do follow a certain set of rules. These rules—widely misunderstood by outsiders—are codified and enforced by a cadre of lofty fey nobility. Befitting any courtly structure, the fey bow to lords and ladies: eldritch creatures of immense power who rule the courts.

### Heads of State

The fey lords and ladies are beings of high station and prodigious personal power. Each rules over at least a great city if not an entire nation. No matter the scope of a fey noble's domain, in his or her eyes, a fey ruler's word is law. Outsiders might not understand the edicts and interdicts of a fey noble, but that's no protection against the harsh penalties that await any who break them, knowingly or otherwise.

### Vacant Thrones

When a lord or lady of the fey dies, the court does not remain leaderless for long. Ambitious beings among the fey always hunger for more power and covet the stations of their superiors. After a traditional month or year of mourning, vicious power struggles winnow the weak and pave the way for the most cunning or the strongest to take the court's vacant throne.

## Moonlit King's Lair

The Moonlit King's lair is the Tower of the Moon, which is hidden in a spiral labyrinth deep within the Plane of Shadows. The tower is a run-down, forlorn place filled with false whispers and shadow ghosts of the mad fey lord's own creation.

```statblock
"name": "Moonlit King (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Neutral Good"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "204"
"hit_dice": "24d8 + 96"
"stats":
- !!int "16"
- !!int "20"
- !!int "18"
- !!int "20"
- !!int "18"
- !!int "20"
"speed": "30 ft."
"saves":
  "Charisma": !!int "11"
  "Wisdom": !!int "10"
  "Constitution": !!int "10"
"skillsaves":
  "Perception": !!int "10"
  "Arcana": !!int "11"
"damage_resistances": "bludgeoning, piercing, slashing, acid from attacks not made\
  \ with cold iron weapons"
"damage_immunities": "cold, fire, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 30 ft., darkvision 120 ft., passive Perception 20"
"languages": "Abyssal, Celestial, Common, Draconic, Elvish, Infernal, telepathy 120\
  \ ft., Umbral"
"cr": "17"
"traits":
- "desc": "The Moonlit King casts one of the following spells, requiring no material\
    \ components and using Charisma as the spellcasting ability (save DC 19):\n\n\
    At will: [continual flame](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/continual-flame.md),\
    \ [invisibility](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/invisibility.md)\
    \ (self only), [moonbeam](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/moonbeam.md),\
    \ [zone of truth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/zone-of-truth.md)\n\
    \n1/day each: [heal](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/heal.md),\
    \ [project image](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/project-image.md)\n\
    \n3/day each: [dispel evil and good](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-evil-and-good.md),\
    \ [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md),\
    \ [major image](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/major-image.md)"
  "name": "Spellcasting"
- "desc": "If the Moonlit King fails a saving throw, he can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "The Moonlit King's weapon attacks are magical. When he hits with any weapon,\
    \ the weapon deals an extra 14 (4d6) radiant damage (included in the attack)."
  "name": "Moonlit Weapons"
"actions":
- "desc": "The Moonlit King makes three Crystal Staff or Moon Bolt attacks. He can\
    \ replace one attack with a use of Spellcasting. If two Crystal Staff attacks\
    \ hit one creature, the target must succeed on a DC 19 Constitution saving throw\
    \ or be [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the end of its next turn."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d6 + 5) bludgeoning damage plus 14 (4d6) radiant damage."
  "name": "Crystal Staff"
- "desc": "Ranged Spell Attack: +11 to hit, range 120 ft., one target. Hit:\
    \ 27 (4d10 + 5) radiant damage, and the target sheds dim light in a 10-foot\
    \ radius until the end of its next turn. If the target is a creature in a form\
    \ other than its true form, it takes an extra 11 (2d10) radiant damage and must\
    \ succeed on a DC 19 Charisma saving throw or revert to its true form."
  "name": "Moon Bolt"
- "desc": "The Moonlit King causes the shadows of up to three creatures he can see\
    \ within 60 feet of him to animate and attack their owners. Each target must make\
    \ a DC 19 Dexterity saving throw. On a failure, a creature takes 49 (14d6) necrotic\
    \ damage, and its Strength score is reduced by 1d4. On a success, a creature\
    \ takes half the damage, and its Strength score isn't reduced. This reduction\
    \ lasts until the creature finishes a long rest. The creature dies if this effect\
    \ reduces its Strength to 0."
  "name": "Animate Shadows (Recharge 5-6)"
- "desc": "The Moonlit King magically calls a lunar devil to aid him. The devil arrives\
    \ in 1d4 rounds, acting as ally of the Moonlit King and obeying his spoken commands.\
    \ The devil remains for 1 hour, until the Moonlit King dies, or until the King\
    \ dismisses it as a bonus action."
  "name": "Summon Devil (1/Day)"
"bonus_actions":
- "desc": "The Moonlit King teleports, along with any equipment he is wearing or carrying,\
    \ up to 60 feet to an unoccupied space he can see. The origin and destination\
    \ spaces must contain moonlight."
  "name": "Moonlight Step"
"reactions":
- "desc": "When a creature the Moonlit King can see within 30 feet of him attacks\
    \ him, he takes on the quality of his manifest delusions, temporarily becoming\
    \ ghostly. The attack roll has disadvantage, and if it hits, the Moonlit King\
    \ takes only half the damage from the attack."
  "name": "Shadow Slip"
"legendary_actions":
- "desc": "The Moonlit King moves up to his speed without provoking opportunity attacks."
  "name": "Move"
- "desc": "The Moonlit King changes the brightness of each area of moonlight he can\
    \ see within 120 feet of him from dim light to bright light or vice versa."
  "name": "Shift Moonlight"
- "desc": "The Moonlit King makes a Crystal Staff or Moon Bolt attack."
  "name": "Attack (Costs 2 Actions)"
- "desc": "Each creature within 30 feet of the Moonlit King must succeed on a DC 19\
    \ Wisdom saving throw or suffer short-term madness. The Moonlit King can use this\
    \ legendary action only when he is in moonlight."
  "name": "Spread Madness (Costs 2 Actions)"
"lair_actions":
- "desc": "On initiative count 20 (losing initiative ties), the Moonlit King takes\
    \ a lair action to cause one of the following effects; the Moonlit King can't\
    \ use the same effect two rounds in a row:"
  "name": ""
- "desc": "- Frightful Whispers. Disembodied whispers speaking of despair and\
    \ failure erupt from a point the Moonlit King can see within 120 feet of him.\
    \ Each non-Fiend creature within 15 feet of that point must succeed on a DC 19\
    \ Wisdom saving throw or be frightened until the end of its next turn.  \n- Maddening\
    \ Hallucinations. Shadows and moonlight dance around up to three creatures the\
    \ Moonlit King can see within 60 feet of him. Each target must succeed on a DC\
    \ 19 Wisdom saving throw or be incapacitated until the end of its next turn as\
    \ hallucinations fill its mind. If the saving throw fails by 5 or more, the target\
    \ suffers short-term madness.  \n- Moonlit Illumination. Four beams of moonlight\
    \ appear on points the Moonlit King can see within 120 feet of him. Each beam\
    \ sheds dim light in a 10-foot radius centered on a point. The moon beams last\
    \ until the Moonlit King uses this lair action again or until he dies.  "
  "name": ""
"regional_effects":
- "desc": "The region containing the Moonlit King's lair is warped by his magic, which\
    \ creates one or more of the following effects:"
  "name": ""
- "desc": "- Constant Moonlight. Weather conditions don't inhibit moonlight shining\
    \ within 10 miles of the lair—clouds part, rain seems to channel moonbeams, and\
    \ snow takes on a luminous silver glow.  \n- Stryx Network. The area within\
    \ 5 miles of the Moonlit King's lair attracts hundreds of stryxes and owls. The\
    \ King can choose to see or hear through the senses of any stryx or owl in this\
    \ area.  \n- Waking Dreams. Dreams and fears take on a life of their own.\
    \ Minor visual and auditory hallucinations plague creatures within 3 miles of\
    \ the lair.  "
  "name": ""
- "desc": "If the Moonlit King dies, these effects fade over the course of 1d10\
    \ days."
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/moonlit-king-tob1-2023.webp"
```
^statblock

## Environment

planar, urban
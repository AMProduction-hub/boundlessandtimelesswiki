---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/21
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Queen of Night and Magic"]
---
# [Queen of Night and Magic](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/queen-of-night-and-magic-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 178*  

*A fey lady of stunning beauty with hair the color of midnight stands before a shining field of stars. A gown seemingly woven from the night sky drapes her flawless ivory skin. Bright lights glitter like diamonds in her crown and raiment, and some drift about her body and dance near her hand*.

Her Celestial and Royal Majesty, Sarastra Aestruum, Queen of Night and Magic, is also Duchess of the Heavens, Mistress of Air and Darkness, Lady of the Summer Palace, and Bride of Shadows. The Queen rules the court of the shadow fey with grace and majesty—most of the time. Queen Sarastra is the head of the Summer Court, which rules the shadow fey in its season. On the rare occasion when the courtly season turns, Sarastra steps aside in favor of her husband and rival, the Moonlit King, who is head of the Winter Court.

## Shadow Sorceress

The Queen of Night and Magic does not bear her moniker lightly. She is a devastatingly potent sorceress, augmented with command over the stuff of shadows. Though her nature is undeniably dark, Queen Sarastra is hardly unreasonable. She is quick to recognize the value in any supplicant, mortal or fey, who catches her royal eye. She is never one to ignore an opportunity to further her agenda or to gain further power over the Moonlit King.

## Fey Lords and Ladies

Fey are capricious, mischievous, and often dangerous beings. However, despite their chaotic reputations, they do follow a certain set of rules. These rules—widely misunderstood by outsiders—are codified and enforced by a cadre of lofty fey nobility. Befitting any courtly structure, the fey bow to lords and ladies: eldritch creatures of immense power who rule the courts.

### Heads of State

The fey lords and ladies are beings of high station and prodigious personal power. Each rules over at least a great city if not an entire nation. No matter the scope of a fey noble's domain, in his or her eyes, a fey ruler's word is law. Outsiders might not understand the edicts and interdicts of a fey noble, but that's no protection against the harsh penalties that await any who break them, knowingly or otherwise.

### Vacant Thrones

When a lord or lady of the fey dies, the court does not remain leaderless for long. Ambitious beings among the fey always hunger for more power and covet the stations of their superiors. After a traditional month or year of mourning, vicious power struggles winnow the weak and pave the way for the most cunning or the strongest to take the court's vacant throne.

## The Queen of Night and Magic's Lair

The Queen of Night and Magic makes her home in the Plane of Shadows in the ancient halls of the courts of the shadow fey. Her lair is a great castle of delicate spires and graceful bridges with sprawling wings that house various members of the court.

```statblock
"name": "Queen of Night and Magic (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Neutral Evil"
"ac": !!int "22"
"ac_class": "regal bearing"
"hp": !!int "225"
"hit_dice": "30d8 + 90"
"stats":
- !!int "12"
- !!int "19"
- !!int "17"
- !!int "20"
- !!int "18"
- !!int "26"
"speed": "30 ft., fly 60 ft. (hover)"
"saves":
  "Wisdom": !!int "11"
  "Constitution": !!int "10"
"skillsaves":
  "Intimidation": !!int "15"
  "Deception": !!int "15"
  "Stealth": !!int "11"
  "Perception": !!int "11"
  "Arcana": !!int "12"
"damage_resistances": "fire, lightning"
"damage_immunities": "bludgeoning, slashing, piercing, cold from nonmagical attacks\
  \ not made with cold iron weapons"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "truesight 120 ft., passive Perception 21"
"languages": "Celestial, Common, Elvish, Sylvan, telepathy 120 ft., Umbral"
"cr": "21"
"traits":
- "desc": "The Queen of Night and Magic casts one of the following spells, using Charisma\
    \ as the spellcasting ability (spell save DC 23):\n\nAt will: [command](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/command.md),\
    \ [dancing lights](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dancing-lights.md),\
    \ [darkness](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/darkness.md),\
    \ [mage hand](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mage-hand.md),\
    \ [suggestion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/suggestion.md)\n\
    \n1/day each: [dominate monster](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dominate-monster.md),\
    \ [plane shift](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/plane-shift.md),\
    \ [power word stun](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/power-word-stun.md)\n\
    \n3/day each: [confusion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/confusion.md),\
    \ [fear](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fear.md), [greater\
    \ invisibility](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-invisibility.md),\
    \ [mirror image](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mirror-image.md)"
  "name": "Spellcasting"
- "desc": "If the Queen of Night and Magic fails a saving throw, she can choose to\
    \ succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "The Queen of Night and Magic has advantage on saving throws against spells\
    \ and other magical effects."
  "name": "Magic Resistance"
- "desc": "While the Queen of Night and Magic is wearing no armor and wielding no\
    \ shield, her AC includes her Charisma modifier."
  "name": "Regal Bearing"
"actions":
- "desc": "The Queen of Night and Magic makes three Rapier or Star Strike attacks.\
    \ She can replace one attack with a use of Spellcasting or Unravel."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 8\
    \ (1d8 + 4) piercing damage plus 14 (4d6) cold damage."
  "name": "Rapier"
- "desc": "Ranged Spell Attack: +15 to hit, range 120 ft., one target. Hit:\
    \ 17 (2d8 + 8) fire damage plus 9 (2d8) radiant damage."
  "name": "Star Strike"
- "desc": "The Queen of Night and Magic ends one magical effect she can see within\
    \ 60 feet of her. To do so, she must succeed on a Charisma check against a DC\
    \ of 10 + the spell's level or the magical effect's DC, whichever is higher."
  "name": "Unravel"
- "desc": "The Queen of Night and Magic creates a shadowy rift on a point she can\
    \ see within 120 feet. Each creature within the 20 feet of the rift must make\
    \ a DC 23 Constitution saving throw. On a failure, a creature takes 36 (8d8)\
    \ cold damage and 36 (8d8) necrotic damage and is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by wisps of icy shadow for 1 minute. On a success, a creature takes half the\
    \ damage and isn't [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ A [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Shadow Rift (Recharge 5-6)"
"bonus_actions":
- "desc": "The Queen of Night and Magic magically teleports, along with any equipment\
    \ she is wearing or carrying, up to 60 feet to an unoccupied space she can see\
    \ and takes the Hide action."
  "name": "Hidden Step"
"reactions":
- "desc": "When the Queen of Night and Magic is targeted by a spell or included in\
    \ a spell's area and the spell doesn't have an instantaneous duration, she can\
    \ use Unravel on the spell, dispelling it after it is cast. She doesn't need to\
    \ see a spell to target it with this reaction, but she must be able to see at\
    \ least some portion of an area or object affected by the spell."
  "name": "Sudden Fraying"
"legendary_actions":
- "desc": "The Queen of Night and Magic makes one Star Strike attack. She doesn't\
    \ have disadvantage on this attack roll from being within 5 feet of a creature,\
    \ though she can have disadvantage from other sources."
  "name": "Attack"
- "desc": "The Queen of Night and Magic moves up to her walking speed or up to half\
    \ of her flying speed without provoking opportunity attacks."
  "name": "Move"
- "desc": "The Queen of Night and Magic uses Spellcasting."
  "name": "Cast a Spell (Costs 2 Actions)"
- "desc": "The stars on the Queen's gown pulse with brilliant starlight. Each creature\
    \ within 15 feet of her must succeed on a DC 23 Dexterity saving throw or be [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the end of its next turn."
  "name": "Swirling Stars (Costs 2 Actions)"
"lair_actions":
- "desc": "On initiative count 20 (losing initiative ties), the Queen of Night and\
    \ Magic takes a lair action to cause one of the following effects; the Queen of\
    \ Night and Magic can't use the same effect two rounds in a row:"
  "name": ""
- "desc": "- Demoralizing Assault. Visions of hopelessness and despair assail\
    \ the mind of one creature the Queen can see within 60 feet of her. The creature\
    \ must succeed on a DC 23 Wisdom saving throw or be stunned until initiative count\
    \ 20 on the next round.  \n- Extinguish Light. Each source of magical or nonmagical\
    \ bright light within 60 feet of the Queen becomes dim light, and each source\
    \ of magical or nonmagical dim light within 60 feet of her becomes darkness. This\
    \ effect lasts until the Queen uses this lair action again, until she dismisses\
    \ it as a bonus action, or until she dies.  \n- Wall of Shadow. An opaque\
    \ wall of writhing shadows springs up from a solid surface within 120 feet of\
    \ the Queen. The wall can be up to 60 feet long, 10 feet high, and 5 feet thick,\
    \ and it blocks line of sight. When the wall appears, each creature in its area\
    \ must succeed on a DC 23 Dexterity saving throw or take 18 (4d8) necrotic damage.\
    \ Creatures in the wall's space are pushed 5 feet out of the wall's space, appearing\
    \ on whichever side of the wall they choose. A creature can move through the wall,\
    \ but the semi-material shadow resists intrusion. For every 1 foot a creature\
    \ travels through the wall, it must spend 4 feet of movement. A creature that\
    \ starts its turn in the wall or enters the wall's space for the first time on\
    \ a turn must make a DC 23 Constitution saving throw, taking 18 (4d8) necrotic\
    \ damage on a failed save, or half as much damage on a successful one. The wall\
    \ dissipates when the Queen uses this lair action again or when she dies.  "
  "name": ""
"regional_effects":
- "desc": "The region containing the Queen of Night and Magic's lair is warped by\
    \ her magic, which creates one or more of the following effects:"
  "name": ""
- "desc": "- Constant Surveillance. The Queen of Night and Magic can cast her\
    \ senses to any area containing darkness, dim light, or shadows within 6 miles\
    \ of her lair. This effect works like the clairvoyance spell, except its range\
    \ is 6 miles.  \n- Living Shadow. Shadows come to life within 6 miles of the\
    \ Queen's lair. Most of the time these living shadows are unnerving and nothing\
    \ more, but when a creature acts against the interests of the Queen, the shadows\
    \ can interfere and cause the creature to have disadvantage on ability checks\
    \ made to act against her interests.  \n- Magically Active. Magic saturates\
    \ the area within 6 miles of the lair, causing temporary, minor, and harmless\
    \ magical effects, like random aromas wafting through the air, sudden chills,\
    \ spontaneous motes of light dancing in the sky, and similar.  "
  "name": ""
- "desc": "If the Queen of Night and Magic dies, these effects fade over the course\
    \ of 1d10 days."
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/queen-of-night-and-magic-tob1-2023.webp"
```
^statblock

## Environment

planar, urban
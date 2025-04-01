---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/ooze
statblock: inline
aliases: ["Treacle"]
---
# [Treacle](03 - Player Log & Handouts\Mechanics\CLI\bestiary\ooze/treacle-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 368*  

*The trapped rabbit squeals as it pulls against the rope binding it. Suddenly, the rabbit's form shifts, revealing it to be a pale, pearlescent ooze ready to pounce on prey.*

A curious bunny, an abandoned toy, or a delicate songbird can spell slow death for the unprepared. Beneath any of these facades may lurk a treacle waiting to feed on a gullible victim, mewling and cooing all the while. Whether by natural selection or arcane tampering, these compact oozes prey on kindness.

## Diet of Blood

Treacles feed on blood but lack the natural weapons or acid of larger slimes. To survive, prey must welcome and embrace them, unaware of the threat. The treacles' soft bodies absorb psychic impressions and take the shape of unthreatening creatures. In the wild, treacles assume the form of an animal's offspring to lie close and feed.

## Pet Polymorph

Among humanoids, treacles transform into pets, toys, or injured animals. Treacles don't choose their forms consciously, instead relying on a primitive form of telepathy to sense which shapes a potential victim finds least threatening or most enticing. They can hold a new shape for several hours, even if the intended victim is no longer present.

## Slow Drain

Once they have assumed a nonthreatening form, treacles mewl, sing, or make pitiful noises to attract attention. Once they're in contact with a potential victim, treacles drain blood slowly, ideally while their prey sleeps. If threatened or injured, treacles flee. A sated treacle detaches from its victim and seeks a cool, dark place to rest and digest.

```statblock
"name": "Treacle (ToB1-2023)"
"size": "Tiny"
"type": "ooze"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "22"
"hit_dice": "4d4 + 12"
"stats":
- !!int "4"
- !!int "15"
- !!int "17"
- !!int "1"
- !!int "1"
- !!int "10"
"speed": "15 ft., climb 10 ft."
"skillsaves":
  "Deception": !!int "4"
"senses": "blindsight 120 ft. (blind beyond this radius), passive Perception 5"
"languages": ""
"cr": "1/4"
"traits":
- "desc": "The treacle can move through a space as narrow as 1 inch wide without squeezing."
  "name": "Amorphous"
- "desc": "The treacle can mimic animal sounds. A creature that hears the sounds can\
    \ tell they are imitations with a successful DC 14 Wisdom ([Insight](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Insight))\
    \ check."
  "name": "Mimicry"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: The\
    \ treacle attaches to the target. While attached, the treacle can't attack, and\
    \ at the start of each of the treacle's turns, the target loses 5 2d4 hp due\
    \ to blood loss. Each time the target loses hp in this way, it must succeed on\
    \ a DC 14 Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ check to notice the treacle is attached and harming it, otherwise it is unaware\
    \ the hp loss is from the treacle. A creature that loses hp in this way while\
    \ below half its hp maximum automatically succeeds on this check.\n\nThe attached\
    \ treacle moves with the target whenever the target moves, requiring none of the\
    \ treacle's movement. It can detach itself by spending 5 feet of its movement\
    \ on its turn. A creature, including the target, can use its action to detach\
    \ the treacle."
  "name": "Blood Drain"
"reactions":
- "desc": "When a creature the treacle can see moves within 120 feet of it, the treacle\
    \ squishes, stretches, and molds its body into the shape of a Tiny Beast or object\
    \ the creature finds least threatening, such as an injured rabbit or a long-lost\
    \ toy. The treacle's body takes on most of the coloration of the desired shape,\
    \ but some part of it is always white, pale, or pearlescent. Regardless of the\
    \ shape, the treacle's flesh doesn't change and is soft and plush to the touch.\
    \ The treacle can maintain this shape for up to 8 hours or until another creature\
    \ it can see moves within 120 feet of it."
  "name": "Mimic Innocence"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/ooze/token/treacle-tob1-2023.webp"
```
^statblock

## Environment

farmland, urban
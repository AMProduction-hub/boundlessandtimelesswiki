---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/15
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend
statblock: inline
aliases: ["Arch-Devil Ia'Affrat"]
---
# [Arch-Devil Ia'Affrat](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/arch-devil-iaaffrat-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 90*  

*A dark, droning cloud containing thousands of gray, thumb-sized wasps, shifts and swarms around the black silhouette of a tall human with glowing red eyes. The wasps, too, glow with the heat of a low-burning coal and are wreathed in foul-smelling smoke.*

## Faithless Servant

Ia'Affrat the Insatiable is the inverted reflection of his unkempt, overly-unyielding creator, Arbeyach, Hell's Prince of Swarms. Ia'Affrat acts as Arbeyach's emissary to the courts of his rivals and to the mortal world as diplomat, spy, assassin, and scourge. Though he serves the rigid and resolute Prince of Hell, Ia'Affrat shows little loyalty to his maker. The eloquent and sophisticated creature has betrayed his master in thousands of small ways over the centuries, and eventually may betray him utterly. Until then, Ia'Affrat's shifting hive mind pursues an unquenchable lust for arcane mysteries, human interaction, and the material pursuit of unwholesome flavors and dark delights.

## Joker and Devourer

Ia'Affrat delights in comedy, wine, song, dance, food, and inflicting torture and public humiliation on his foes—he is a rapacious devourer, greedy for all transient pleasures.

```statblock
"name": "Arch-Devil Ia'Affrat (ToB1-2023)"
"size": "Large"
"type": "fiend"
"alignment": "Lawful Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "170"
"hit_dice": "20d10 + 60"
"stats":
- !!int "3"
- !!int "21"
- !!int "16"
- !!int "20"
- !!int "18"
- !!int "23"
"speed": "20 ft., fly 40 ft. (hover)"
"saves":
  "Charisma": !!int "11"
  "Dexterity": !!int "10"
  "Wisdom": !!int "9"
  "Constitution": !!int "8"
"skillsaves":
  "Deception": !!int "11"
  "Insight": !!int "9"
  "Perception": !!int "9"
  "Arcana": !!int "10"
  "Persuasion": !!int "11"
"damage_vulnerabilities": "cold"
"damage_immunities": "bludgeoning, fire, piercing, poison, slashing"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)"
"senses": "blindsight 10 ft., darkvision 120 ft., passive Perception 19"
"languages": "Common, Infernal, Primordial, telepathy 120 ft."
"cr": "15"
"traits":
- "desc": "Ia'Affrat's individual Fiends are connected via a hive mind. He can telepathically\
    \ communicate with any of his individual Fiends within 50 miles of him, and he\
    \ can't be surprised. If he is reduced to half his hp or lower, his Intelligence\
    \ score is reduced to 10, he immediately changes into his shapeless form, and\
    \ he can't take on a Humanoid form again until he regains hp to be above half\
    \ his hp or he finishes a long rest."
  "name": "Collective Mind"
- "desc": "Magical darkness doesn't impede Ia'Affrat's darkvision."
  "name": "Devil's Sight"
- "desc": "Ia'Affrat can wield weapons and hold, grasp, push, pull, or interact with\
    \ objects that might otherwise require a more Humanoid form to accomplish."
  "name": "Grasping Limbs (Humanoid Form Only)"
- "desc": "If Ia'Affrat fails a saving throw, he can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "Ia'Affrat has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "Ia'Affrat emits a cloud of dark smoke within 5 feet of himself. The area\
    \ is lightly obscured to all except Ia'Affrat, and each non-devil creature that\
    \ starts its turn in the smoke must succeed on a DC 18 Constitution saving throw\
    \ or be [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the end of its turn. At the start of each of his turns, Ia'Affrat chooses\
    \ whether this shroud is active."
  "name": "Smoke Shroud"
- "desc": "Ia'Affrat can occupy another creature's space and vice versa and can move\
    \ through any opening large enough for a Tiny insect, but he can't grapple or\
    \ be [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)."
  "name": "Swarm (Shapeless Form Only)"
"actions":
- "desc": "Ia'Affrat makes three Bite or Burning Claw attacks, or he makes four Flaming\
    \ Insect Bolt attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 0 ft., one target in the swarm's\
    \ space. Hit: 21 (6d6) piercing damage plus 14 (4d6) poison damage, or 10\
    \ (3d6) piercing damage plus 7 (2d6) poison damage if Ia'Affrat has half of\
    \ its hp or fewer. If the target is a creature, it must succeed on a DC 18 Constitution\
    \ saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn."
  "name": "Bite (Shapeless Form Only)"
- "desc": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 23\
    \ (4d8 + 5) slashing damage plus 10 (3d6) fire damage."
  "name": "Burning Claw (Humanoid Form Only)"
- "desc": "Ranged Spell Attack: +11 to hit, range 120 ft., one target. Hit:\
    \ 16 (3d6 + 6) fire damage plus 10 (3d6) poison damage."
  "name": "Flaming Insect Bolt"
- "desc": "Ia'Affrat crawls into the body of a Humanoid, or a Humanoid corpse that\
    \ has been dead no more than 7 days, that he can see within 5 feet of him. If\
    \ the target is unwilling, the target must succeed on a DC 18 Constitution saving\
    \ throw or the target loses control of its body, and Ia'Affrat takes control of\
    \ the body. Ia'Affrat controls the body but doesn't deprive the target of awareness.\
    \ Ia'Affrat can't be targeted by any attack, spell, or other effect, and he retains\
    \ his alignment, his Intelligence, Wisdom, and Charisma scores, his Hurl Flame\
    \ action and Teleport and Consume Host legendary actions, and his condition immunities.\
    \ He otherwise uses the target's statistics, but doesn't gain access to the target's\
    \ knowledge, class features, or proficiencies. If the target was a Humanoid corpse,\
    \ he uses the statistics it had before it died.\n\nIa'Affrat inhabits the target\
    \ until the target's body is reduced to 0 hp, Ia'Affrat ends it as a bonus action,\
    \ or Ia'Affrat is forced out by the dispel evil and good or [greater restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-restoration.md)\
    \ spell. When the inhabit ends, Ia'Affrat reappears in an unoccupied space within\
    \ 5 feet of the target. The target is immune to Ia'Affrat's Inhabit for 24 hours\
    \ after succeeding on the saving throw or after the inhabit ends."
  "name": "Inhabit (Shapeless Form Only)"
"bonus_actions":
- "desc": "Ia'Affrat can shape himself into a Large or smaller Humanoid or back into\
    \ a shapeless mass of Tiny insectoid Fiends. His statistics, other than his size,\
    \ are the same in each form, and he can't regain hp or gain temporary hp, except\
    \ for the Consume Host legendary action. He can't take on a Humanoid form if he\
    \ is occupying the space of another creature."
  "name": "Shape Swarm"
"legendary_actions":
- "desc": "Ia'Affrat teleports, along with any equipment he is wearing or carrying,\
    \ up to 120 feet to an unoccupied space he can see."
  "name": "Teleport"
- "desc": "Ia'Affrat exhales 1d4 swarms of insects in spaces he can see within 30\
    \ feet. The swarms take their turns immediately after Ia'Affrat, and they are\
    \ allies of Ia'Affrat, obeying his telepathic commands. They remain for 1 minute,\
    \ until Ia'Affrat dies, or until Ia'Affrat dismisses them as a bonus action. Ia'Affrat\
    \ can have no more than five swarms of insects under his control at a time."
  "name": "Vermin Breath (Costs 2 Actions; Humanoid Form Only)"
- "desc": "While inhabiting a Humanoid, Ia'Affrat consumes the host from the inside.\
    \ The host takes 18 (4d8) necrotic damage, and Ia'Affrat regains hp equal to\
    \ that amount."
  "name": "Consume Host (Costs 3 Actions; Shapeless Form Only)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/arch-devil-iaaffrat-tob1-2023.webp"
```
^statblock

## Environment

planar, urban
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/14
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Gypsosphinx"]
---
# [Gypsosphinx](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/gypsosphinx-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 340*  

*With black wings and a body pale as alabaster, the vulture-beaked sphinx is a striking figure.*

As powerful servants of the gods of death and the desert, the gypsosphinx's riddles and obsessions all hinge on death and carrion. Their eyes can spot prey miles away, and the distance they climb into the sky hides their enormous size. The pale gypsosphinx shines in the desert sun and stands out in underground tombs and caverns, yet it can conceal itself when it flies in moonlit clouds. Gypsosphinxes are found anywhere bodies are buried or left to rot, and they harvest corpses from battlefields of warring desert tribes.

## Gossips and Riddlers

Gypsosphinxes converse with intelligent undead, priests of death gods, and with other sphinxes, but they rarely gather among their own kind. They guard their territory jealously, typically claiming a necropolis as the heart of their region. Like all sphinxes, gypsosphinxes enjoy riddles. They rely on magic to solve challenging riddles they can't solve on their own.

## Night Flyers

Gypsosphinxes are gifted fliers capable of diving steeply from the night sky to snatch carrion or a sleeping camel. The stroke of midnight has a special but unknown significance for them.

## Foretell Doom

Occasionally, a paranoid noble seeks out a gypsosphinx and entreats the creature to reveal the time and place of his or her death, hoping to cheat fate. A gypsosphinx demands a high price for such a service, including payment in corpses of humans, unusual creatures, or near-extinct species. Even if paid, the gypsosphinx rarely honors its side of the bargain; instead, it turns its death magic against the supplicant, bringing about his or her death then and there.

> [!note] Gypsosphinx Temples and Riddles
> 
> Accompanied by flocks of vultures and often served by packs of gnolls, ogres, and hyenas, gypsosphinxes living in deserts, plains, hills, and even mountainous terrain often acquire a large number of followers and would-be helpers. This eventually leads a gypsosphinx to anger, as it requires some solitude and peace, and (depending on its mood) it either abandons its entourage or turns them into a hearty meal. In either case, survivors sometimes tell the tale of the creature's wrath, discouraging others from following a gypsosphinx in search of wisdom.
> 
> Gypsosphinx temples are another matter; there the sphinx is served by an order of priests who understand its hunger, entertain it with discussions of philosophy, butchery, and gossip, and know when to withdraw and leave their patron to silent contemplation. Such temples are often quite rich, as the gypsosphinx at its heart demands its priests live well, the better to reflect its own importance and status.
> 
> **11 Riddles.** The best riddles are ones you create yourself. However, here are a few easy and a few more difficult ones for a gypsosphinx.
> 
> - It is light as a feather yet no one can hold it for long. What is it? (Breath)  
> - I live where there is light, but I die if it shines on me. What am I? (A shadow)  
> - Always smiles or maybe frowns, sinks in water, never drowns. Catches prey on its barbed teeth, hunts all day but never eats. (A fishhook)  
> - I have rivers without water, forests without trees, mountains without stones, cities without houses. What am I? (A map)  
> - Soft as velvet, can't be touched, hides the world, but isn't much. (Darkness/night)  
> - I have a tail and a head but no body. What am I? (A coin)  
> - What should you add to a barrel of ale to make it lighter? (A hole)  
> - Round as an apple, deep as a cup, all the king's horses can't pull me up. What am I? (A well)  
> - I am open when I'm closed and closed when I'm open. (A drawbridge)  
> - Born of the earth, strengthened in fire, I sit on high, a master of water. (A roof tile)  
> - Unwelcome, difficult, precious, and rare. What am I? (The truth)  
^gypsosphinx-temples-and-riddles

```statblock
"name": "Gypsosphinx (ToB1-2023)"
"size": "Large"
"type": "monstrosity"
"alignment": "Neutral Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "190"
"hit_dice": "20d10 + 80"
"stats":
- !!int "20"
- !!int "14"
- !!int "18"
- !!int "18"
- !!int "18"
- !!int "18"
"speed": "40 ft., fly 70 ft."
"skillsaves":
  "Religion": !!int "9"
  "Perception": !!int "9"
  "History": !!int "9"
  "Arcana": !!int "9"
"damage_resistances": "necrotic; bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison, psychic"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "truesight 90 ft., passive Perception 19"
"languages": "Abyssal, Common, Darakhul, Sphinx"
"cr": "14"
"traits":
- "desc": "The sphinx casts one of the following spells, requiring no material components\
    \ and using Intelligence as the spellcasting ability (spell save DC 17):\n\nAt\
    \ will: [comprehend languages](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/comprehend-languages.md),\
    \ [detect magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-magic.md),\
    \ [mage hand](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/mage-hand.md)\n\
    \n1/day each: [major image](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/major-image.md),\
    \ [greater invisibility](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-invisibility.md)\n\
    \n3/day each: [blur](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/blur.md),\
    \ [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md),\
    \ [locate object](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/locate-object.md)"
  "name": "Spellcasting"
- "desc": "The sphinx can pinpoint, by scent, the location of each creature below\
    \ half its hp maximum within 60 feet of it, and it can sense the general direction\
    \ of creatures that don't have all of their hp within 1 mile of it. In addition,\
    \ the sphinx can foretell the age and manner of a creature's death by looking\
    \ at it. This effect doesn't take into account possible circumstances that might\
    \ change the outcome, such as the casting of powerful spells or the creature making\
    \ a radical change in its life's path."
  "name": "Death Sense"
- "desc": "The sphinx is immune to any effect that would sense its emotions or read\
    \ its thoughts, as well as any divination spell that it refuses. Wisdom ([Insight](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Insight))\
    \ checks made to ascertain the sphinx's intentions or sincerity have disadvantage."
  "name": "Inscrutable"
- "desc": "The sphinx's weapon attacks are magical."
  "name": "Magic Weapons"
"actions":
- "desc": "The sphinx makes one Beak attack and two Claw attacks. If both Claw attacks\
    \ hit one creature, the target must succeed on a DC 18 Strength saving throw or\
    \ take 14 (4d6) slashing damage and be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 10\
    \ (1d10 + 5) piercing damage."
  "name": "Beak"
- "desc": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 19\
    \ (4d6 + 5) slashing damage."
  "name": "Claw"
- "desc": "The gypsosphinx exhales rotting breath in a 30-foot cone. Each creature\
    \ in the area must make a DC 18 Constitution saving throw. On a failure, a creature\
    \ takes 21 (6d6) poison damage and 27 (6d8) necrotic damage and is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ While [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way, a creature has disadvantage on death saving throws. A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Carrion Breath (Recharge 5-6)"
"legendary_actions":
- "desc": "The sphinx makes one Beak attack."
  "name": "Beak Attack"
- "desc": "The sphinx uses Spellcasting."
  "name": "Cast a Spell (Costs 2 Actions)"
- "desc": "The sphinx magically teleports, along with any equipment it is wearing\
    \ or carrying, up to 120 feet to an unoccupied space it can see."
  "name": "Teleport (Costs 2 Actions)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/gypsosphinx-tob1-2023.webp"
```
^statblock

## Environment

desert, underdark, urban
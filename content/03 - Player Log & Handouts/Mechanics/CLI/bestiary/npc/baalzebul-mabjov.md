---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mabjov
- ttrpg-cli/monster/cr/26
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/fiend/devil
statblock: inline
aliases: ["Baalzebul"]
---
# [Baalzebul](03 - Player Log & Handouts\Mechanics\CLI\bestiary\npc/baalzebul-mabjov.md)
*Source: Minsc and Boo's Journal of Villainy p. 92*  

> [!quote] A quote from Volo  
> 
> I have no idea how the big dolt and his hamster scrounged up information on so many dangerous entities, but it's foolish to write about them if you ask me. There's a reason I've never written a book about the Nine Hells.

Baalzebul, is an archdevil and the lord of Maladomini, the seventh layer of the Nine Hells. He is known as the Lord of the Flies because his tightly woven web of intrigue traps even the smallest fly. In recent centuries he has been cursed with a new hideous form by the Lord of the Nine Hells—Asmodeus. This form has earned him a new title—The Slug Archduke.

Baalzebul was originally known as Triel, one of the most powerful and beautiful angels to be found in Celestia. Triel's selfish acts in the name of achieving his perfection resulted in his corruption and exile from Celestia. After his fall, Asmodeus, perhaps out of some lingering sense of sympathy, quickly promoted Baalzebul to the ranks of devilish nobility. Baalzebul's ruthless lust for power served him well and before long he not only displaced the ancient, original Lord of Maladomini but managed to become the only archdevil to rule two layers of the Nine Hells, although he ruled Malbolge through the devil Moloch.

However, Baalzebul's pride continued to be his undoing. When he attempted to take Asmodeus's throne, his schemes were discovered and thwarted. Asmodeus inflicted a series of bizarre penalties upon Baalzebul. He was cursed to appear as a slug for one year per lie he had told to a devil. Any deal he struck with a mortal would result in a disaster for the participant. His castle was turned to excrement and filled with filth and his dominion of Malbolge was stripped from him.

Despite his punishments, Baalzebul is still dangerously cunning and charismatic. Even if trapped in the form of a slug, he is still the Lord of Lies, whose every deception is made with ease. Every one of his untruths is told with a specific purpose in mind. Only other devils are safe from his lies, as Baalzebul wishes to return to his original beautiful form.

If forced into combat Baalzebul's first tactic is to belch out gargantuan clouds of flesh-devouring flies. Baalzebul's stench is so putrid that simply trying to get anywhere close to him is sickening. Despite his bloated form, he can still burrow underground and easily scale surfaces. He is easy to track, since he always leaves a thick layer of putrid slime in his wake.

```statblock
"name": "Baalzebul (MaBJoV)"
"size": "Huge"
"type": "fiend"
"subtype": "devil"
"alignment": "Lawful Evil"
"ac": !!int "19"
"ac_class": "natural armor"
"hp": !!int "540"
"hit_dice": "40d12 + 280"
"stats":
- !!int "28"
- !!int "15"
- !!int "25"
- !!int "24"
- !!int "24"
- !!int "26"
"speed": "20 ft., burrow 20 ft., climb 20 ft."
"saves":
  "Charisma": !!int "16"
  "Intelligence": !!int "15"
  "Strength": !!int "17"
  "Constitution": !!int "15"
"skillsaves":
  "Intimidation": !!int "16"
  "Athletics": !!int "17"
  "Deception": !!int "24"
  "Insight": !!int "15"
  "Persuasion": !!int "16"
"damage_resistances": "acid; cold; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"damage_immunities": "fire, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., tremorsense 10 ft., passive Perception 17"
"languages": "all, telepathy 120 ft."
"cr": "26"
"traits":
- "desc": "Baalzebul casts one of the following spells, requiring no material components\
    \ and using Charisma as the spellcasting ability (spell save DC 24):\n\nAt will:\
    \ [animate dead](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/animate-dead.md),\
    \ [darkness](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/darkness.md),\
    \ [detect evil and good](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-evil-and-good.md),\
    \ [detect magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-magic.md),\
    \ [dispel evil and good](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-evil-and-good.md),\
    \ [hallow](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hallow.md),\
    \ [hold monster](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hold-monster.md),\
    \ [suggestion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/suggestion.md),\
    \ [teleport](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/teleport.md),\
    \ [true seeing](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/true-seeing.md)\n\
    \n1/day each: [symbol](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/symbol.md)\
    \ (pain or insanity), [wish](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/wish.md)"
  "name": "Spellcasting"
- "desc": "Magical darkness doesn't impede Baalzebul's darkvision."
  "name": "Devil's Sight"
- "desc": "Baalzebul regains 20 hit points at the start of his turn. If he takes radiant\
    \ damage this trait doesn't function at the start of his next turn. Baalzebul\
    \ dies only if he starts his turn with 0 hit points and doesn't regenerate."
  "name": "Fiendish Regeneration"
- "desc": "Insects don't attack Baalzebul, and he can issue orders to them."
  "name": "Lord of Flies"
- "desc": "If Baalzebul fails a saving throw, he can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "Baalzebul has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "A creature that starts its turn within 10 feet of Baalzebul must succeed\
    \ on a DC 21 Constitution saving throw or have the [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ condition until the start of its next turn. On a successful save, a creature\
    \ is immune to this stench for 1 hour."
  "name": "Stench of the Slug"
"actions":
- "desc": "Baalzebul uses Heart of Pestilence (if available), then makes three Slam\
    \ attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +17 to hit, reach 10 ft., one target. Hit: 19\
    \ (3d6 + 9) bludgeoning damage plus 7 (2d6) necrotic damage."
  "name": "Slam"
- "desc": "Baalzebul causes refuse and caustic liquid to spill from the ground at\
    \ a point he can see within 300 feet. Each creature in a 15-foot-radius sphere\
    \ centered on that point must make a DC 21 Constitution saving throw. Targets\
    \ take 36 (8d8) acid damage on a failed save, or half as much on a successful\
    \ one. Creatures that fail the save have the [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ condition for 1 minute."
  "name": "Pungent Eruption (Recharge 4-6)"
- "desc": "Baalzebul channels pestilence into his body, sickening creatures within\
    \ 50 feet that can see him. Sickened creatures must make a DC 21 Charisma saving\
    \ throw, followed by a DC 21 Constitution saving throw. Failing the Charisma save\
    \ makes a creature have the [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ condition, while failing the Constitution save makes a creature weak. While\
    \ weakened, a creature deals half damage on melee attacks. Both effects last for\
    \ 1 minute or until a [greater restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-restoration.md)\
    \ spell or similar is cast."
  "name": "Heart of Pestilence (Recharge 5-6)"
"bonus_actions":
- "desc": "Baalzebul magically teleports, along with any equipment he is wearing and\
    \ carrying, up to 120 feet to an unoccupied space he can see."
  "name": "Displace"
"legendary_actions":
- "desc": "Baalzebul makes a Slam attack."
  "name": "Pummel"
- "desc": "Baalzebul uses Displace."
  "name": "Teleport"
- "desc": "Baalzebul disgorges a swarm of biting flies at a point he can see within\
    \ 300 feet of himself. Each creature within a 20-foot-radius sphere centered on\
    \ that point must make a DC 21 Constitution saving throw. A creature takes 44\
    \ (8d10) piercing damage on a failed save, or half as much damage on a successful\
    \ one. The biting flies persist for 1 minute, or until Baalzebul uses this ability\
    \ again. Creatures that enter the flies' area or end their turn inside it must\
    \ repeat the saving throw."
  "name": "Insect Gorge (Costs 2 Actions)"
- "desc": "Baalzebul summons an allied [bone devil](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/bone-devil.md)\
    \ in an unoccupied space that he can see."
  "name": "Call Underling (Costs 3 Actions)"
"source":
- "MaBJoV"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/npc/token/baalzebul-mabjov.webp"
```
^statblock
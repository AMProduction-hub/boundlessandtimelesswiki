---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Witchlight"]
---
# [Witchlight](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/witchlight-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 397*  

*This tiny ball of bright light seems to emanate from a crystalline center.*

## Wizard Servants

Also called a "spooklight," a witchlight is a wizard's servant created from a tiny piece of quartz. It appears as a floating ball of flickering light similar to a will-o'-wisp. The hue of quartz used during the creature's creation determines the color of each witchlight's illumination. After the quartz is prepared, it is animated through an extended magical ritual cast under a full moon and a clear, starry sky. Consequently, they are extremely rare.

## Flashing Light Code

A witchlight always shares the same alignment as its creator. Although it cannot speak, a witchlight understands the languages of its creator, and many spellcasters have taught their witchlights a coded cipher, allowing it to spell out words by flaring and dimming its light. When necessary, a witchlight can spell words in the air by flying so quickly that its trail of light forms letters.

## Free Roaming

If the witchlight's master dies within one mile of the witchlight, it explodes in a brilliant but harmless flash of light. If it loses its master under any other circumstance, it becomes masterless. While masterless, it's free to do as it pleases. Evil masterless witchlights can be surprisingly cruel, not unlike will-o'-wisps. They seek to lure lost travelers into swamps or traps by using their glow to imitate the light of a safe haven. Conversely, good masterless witchlights guide travelers to places of safety or along safe paths, and they are prized by pilots and guides. Neutral witchlights exhibit a playful nature—sometimes mingling inside the cavities of weapons, gems, or other curiosities, causing them to be mistaken for magic items. More than one "wizard's staff " is just an impressive-looking stick with a witchlight perched on top.

> [!note] Witchlight Familiars
> 
> Some witchlights are willing to serve spellcasters as a familiar. Such witchlights have the following trait.
> 
> **Familiar.** The witchlight can serve another creature as a familiar, forming a magic, telepathic bond with that willing companion. While the two are bonded, the companion can sense what the witchlight senses as long as they are within 1 mile of each other. While the witchlight is within 10 feet of its companion, the companion can't be blinded. At any time and for any reason, the witchlight can end its service as a familiar, ending the telepathic bond.
^witchlight-familiars

```statblock
"name": "Witchlight (ToB1-2023)"
"size": "Tiny"
"type": "construct"
"alignment": "Any alignment"
"ac": !!int "12"
"hp": !!int "20"
"hit_dice": "8d4"
"stats":
- !!int "1"
- !!int "14"
- !!int "10"
- !!int "10"
- !!int "15"
- !!int "7"
"speed": "0 ft., fly 40 ft. (hover)"
"skillsaves":
  "Perception": !!int "4"
"damage_immunities": "poison, psychic, radiant"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "understands the languages of its creator but can't speak"
"cr": "1/4"
"traits":
- "desc": "The witchlight is incapacitated while in the area of an [antimagic field](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/antimagic-field.md).\
    \ If targeted by [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md),\
    \ the witchlight must succeed on a Constitution saving throw against the caster's\
    \ spell save DC or fall unconscious for 1 minute."
  "name": "Antimagic Susceptibility"
- "desc": "The witchlight doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The witchlight sheds bright light in a 5- to 20-foot radius and dim light\
    \ for an additional number of feet equal to the chosen radius. The witchlight\
    \ can alter the radius as a bonus action."
  "name": "Variable Illumination"
"actions":
- "desc": "Melee or Ranged Spell Attack: +4 to hit, range 30 ft., one target.\
    \ Hit: 5 (1d6 + 2) radiant damage."
  "name": "Light Blast"
- "desc": "The witchlight emits a bright burst of light. Each creature within 20 feet\
    \ of the witchlight must succeed on a DC 12 Dexterity saving throw or be [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ for 1 minute. A creature can make a DC 12 Constitution saving throw at the end\
    \ of each of its turns, ending the effect on itself on a success."
  "name": "Flash (3/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/witchlight-tob1-2023.webp"
```
^statblock

## Environment

any
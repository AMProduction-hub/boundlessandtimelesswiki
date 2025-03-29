---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/11
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Baba Yaga's Horsemen"]
---
# [Baba Yaga's Horsemen](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/baba-yagas-horsemen-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 30*  

*These mounted knights wield great weapons as swift as dawn, as bright as the blazing sun, and as cold as the grave. The white horseman is a young rider full of promise, the red rider a man in his prime, and the black rider a scarred and bearded fellow, his eyes dark and his mouth set in a grim frown. They ride with purpose on powerful steeds*.

Baba Yaga's three horsemen are legends in their own right. Bright Day, Red Sun, and Black Night (also known as the White, Red, and Black horsemen) are her faithful emissaries, scouts, and warriors abroad. The three horsemen change over time, but they are typically male, human warriors. Their appearance is distinctive: each horseman dresses in colors and lacquered armor and trappings to suit their name, with their magical horses colored to match. Their roles appear to coincide with their appointed offices, although their precise relationship to Baba Yaga is the source of much speculation.

## Varied Origin

They may be serving Grandmother Winter for a time in exchange for a favor or bargain, or they may be cursed to replace a previous horseman they slew. In either case, Baba Yaga is the source of their power. The horsemen are innately connected to the domain of time; each represents part of the day, as measured by the sun. Bright Day is bound to and governs dawn to mid-day, Red Sun from mid‑day to sundown, and Black Night rules until daybreak. While Baba Yaga herself is wily and capricious, her three horsemen are bound to cosmological forces that are uniform and constant, which is reflected in their alignment and demeanor.

## One Rises, Two Set

The horsemen never co-exist with one another except within the confines of their mistresses' Dancing Hut and the fenced yard around it. Each one must yield his presence on the Material Plane to his successor in rotation (this varies on other planes, depending on intervals of day and night). Forcing two horsemen to co-exist on the Material Plane places a perilous strain on reality. Bringing all three together could trigger a primal magical event or chronal catastrophe.

> [!note] Encounters with Baba Yaga's Horsemen
> 
> The horsemen make good foes for the long term; their power is great enough that they can ignore considerable danger when serving their mistress. Here are some possible encounters involving them:
> 
> - Red Sun burns down a village while the PCs are sleeping at the inn. If questioned or challenged, he says nothing, but provides a scroll from Baba Yaga ordering the village's destruction. Red Sun rides off into the dawn. Black Night bears a similar scroll, asking an elvish character to provide Baba Yaga with a pint of blood; if the request is granted, Black Night leaves without incident, but if he is denied, a young human boy is found outside the party's sleeping chambers, drained of all blood.  
> - At noon, Bright Day leads a parade of strange creatures, everything from shadow fey duelists and enchantresses to a glowing will-o'-wisp and a bright malakbel demon, burning so bright it sets fire to crops and thatched huts near it. The fey mention Bright Day is going to pay Baba Yaga's respects to the River King. If the party chooses to join the procession, they can't leave it until sunset—and may find their company is not entirely welcome.  
^encounters-with-baba-yagas-horsemen

> [!note] The Three Horsemen
> 
> All three horsemen use the statistics presented here, but each has a few unique characteristics from his brethren, as defined below.
> 
> **Bright Day.** This horseman has darkvision out to a range of 60 feet and resistance to cold damage and fire damage.
> 
> **Red Sun.** This horseman is immune to being blinded, charmed, and frightened and has immunity to fire damage.
> 
> **Black Night.** This horseman has darkvision out to a range of 60 feet and magical darkness doesn't impede his darkvision. In addition, he has immunity to cold damage.
^the-three-horsemen

> [!note] The Horsemen in Midgard
> 
> The great witch Baba Yaga is a power to be reckoned with in Midgard, always plotting with her daughters, the vila, and seeking to gobble up the vile gnomes whose souls she claims are rightfully hers. Baba Yaga rules over great ley line magic and commands the elements and enchantments with ease, but she cannot be everywhere at once. Three of her most faithful servants are the White Horseman, the Red Horseman and the Black Horseman—embodied forms of the times of day and a symbol of Baba Yaga's mastery of time itself. She uses nicknames for them, calling them "My Bright Dawn, my Red Sun, and my Dark Midnight" because they are bound by time (and some believe, because they control dawn, noon, and sunset). She has many servants, but the horsemen, her dancing hut, and the sorcerer Koshchei the Deathless are the greatest.
^the-horsemen-in-midgard

```statblock
"name": "Baba Yaga's Horsemen (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Lawful Neutral"
"ac": !!int "20"
"ac_class": "[plate](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/plate-armor.md),\
  \ [shield](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/shield.md)"
"hp": !!int "171"
"hit_dice": "18d8 + 90"
"stats":
- !!int "22"
- !!int "11"
- !!int "21"
- !!int "16"
- !!int "18"
- !!int "18"
"speed": "30 ft."
"saves":
  "Dexterity": !!int "4"
  "Wisdom": !!int "8"
"skillsaves":
  "Athletics": !!int "10"
  "Perception": !!int "8"
  "History": !!int "7"
  "Arcana": !!int "7"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "lightning, poison"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "passive Perception 18"
"languages": "Celestial, Common, Infernal, telepathy 120 ft."
"cr": "11"
"traits":
- "desc": "The horseman casts one of the following spells, requiring no material components\
    \ and using Charisma as the spellcasting ability (spell save DC 16):\n\n1/day:\
    \ [plane shift](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/plane-shift.md)\
    \ (self and mount only)\n\n2/day each: [darkness](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/darkness.md)\
    \ (black night horseman only), [daylight](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/daylight.md)\
    \ (bright day and red sun horsemen only), [dimension door](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dimension-door.md),\
    \ [fire shield](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fire-shield.md)\n\
    \n3/day: [phantom steed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/phantom-steed.md)\
    \ (as an action)"
  "name": "Spellcasting"
- "desc": "The horseman's weapon attacks are magical. When the horseman hits with\
    \ any weapon, the weapon deals an extra 2d8 damage of a type depending on the\
    \ horseman: cold (black night), fire (red sun), radiant (bright day)."
  "name": "Enchanted Weapons"
- "desc": "The horseman has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "Any attacks directed at the horseman's mount target the horseman instead,\
    \ and the horseman confers his damage resistances and immunities and his condition\
    \ immunities to his mount. In addition, if the horseman and mount are subjected\
    \ to an effect that allows each to make a saving throw to take only half damage,\
    \ the mount takes no damage if the horseman succeeds on the saving throw."
  "name": "Peerless Rider"
- "desc": "The horseman doesn't age and doesn't require food, drink, or sleep."
  "name": "Timeless Nature"
"actions":
- "desc": "The horseman makes three Lance, Longsword, or Horseman's Bolt attacks.\
    \ The horseman can replace one attack with a use of Spellcasting."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 12\
    \ (1d12 + 6) piercing damage plus 9 (2d8) damage of the type defined in Enchanted\
    \ Weapons. The horseman has disadvantage on this attack roll if the target is\
    \ within 5 feet of him."
  "name": "Lance"
- "desc": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 10\
    \ (1d8 + 6) slashing damage, or 11 (1d10 + 6) slashing damage if used with\
    \ two hands, plus 9 (2d8) damage of the type defined in Enchanted Weapons."
  "name": "Longsword"
- "desc": "Ranged Spell Attack: +8 to hit, range 120 ft., one target. Hit: 22\
    \ (4d6 + 4) damage of the type defined in Enchanted Weapons."
  "name": "Horseman's Bolt"
"bonus_actions":
- "desc": "One creature the horseman can see and that the horseman hit with a Horseman's\
    \ Bolt or Longsword attack within the last minute must succeed on a DC 17 Constitution\
    \ saving throw or age 16 (3d10) years. A creature that ages this way has disadvantage\
    \ on attack rolls, ability checks, and saving throws that use Strength, Dexterity,\
    \ and Constitution until the aging is reversed. A creature that ages beyond its\
    \ lifespan dies immediately. The aging lasts until the creature finishes a long\
    \ rest, or until it is reversed by a [greater restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-restoration.md)\
    \ spell or similar magic. On a successful saving throw, the creature is immune\
    \ to the horseman's Temporal Strike for 24 hours."
  "name": "Temporal Strike (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/baba-yagas-horsemen-tob1-2023.webp"
```
^statblock

## Environment

any
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/mabjov
- ttrpg-cli/monster/cr/11
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/dwarf
statblock: inline
aliases: ["Kagain"]
---
# [Kagain](03 - Player Log & Handouts\Mechanics\CLI\bestiary\npc/kagain-mabjov.md)
*Source: Minsc and Boo's Journal of Villainy p. 118*  

> [!quote] A quote from MINSC  
> 
> The dwarf knew how to live by the axe, but Boo always thought that he needed a swift kick in the morals!

Kagain is an infamous dwarven mercenary, known as much for his sadistic cruelty and naked greed as his prodigious skill in battle. He is known by many nick names including "the Headhunter", "the Blood Dwarf" and most famously the "the Scream Hunter". This last name comes from his supposed love for the screams of his dying victims. Head of a small but elite mercenary company, Kagain is willing to take on unscrupulous contracts that most rivals would never stomach. His band is based out of Baldur's Gate, where he most often takes on jobs from the Flaming Fist.

Largely indifferent to the suffering of others, Kagain's sole motivations seem to be gold and unleashing death and bloodshed upon the world. This has led Kagain to indulge in increasingly depraved acts in order to get the gold that he craves, and there is no moral or ethical line he will not cross. He has been known to pass off the bones of Uthgardt tribespeople as a substitute for orc fingers in the hopes of claiming outstanding bounties, and he once slaughtered an entire village of innocent gnomes, then tried to pass off their scalps as goblin heads. No act is too despicable for the dwarf if it makes his pursuit of gold easier.

The return of Bhaal has given Kagain a unique opportunity to apply his skills. In his younger years he traveled with one of the Bhaalspawn, Abdel Adrian. This early exposure to the mythology of the Lord of Murder intrigued Kagain, but nothing ever came from it. However, one drunken night in Baldur's Gate, Kagain and several of his mercenaries were set upon by Bhaal while they stumbled home. Despite murdering all his companions, the god spared Kagain on the condition that he become one of his devout followers. Given his love for killing, his lust for gold, and his utter lack of loyalty to his slain brothers-in-arms, it was an easy choice for the black-hearted dwarf

Kagain employs a band of mercenaries that are equally unscrupulous. He has little care for their wellbeing, so membership changes on a regular basis. Current members include the tasloi poisoner named Gixis; a gnoll tracker that goes by the name "Hungry" and a dread doppelganger Kagain refers to as the "Face Peeler".

```statblock
"name": "Kagain (MaBJoV)"
"size": "Medium"
"type": "humanoid"
"subtype": "dwarf"
"alignment": "Neutral Evil"
"ac": !!int "18"
"ac_class": "[plate](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/plate-armor.md)"
"hp": !!int "161"
"hit_dice": "17d8 + 85"
"stats":
- !!int "18"
- !!int "13"
- !!int "20"
- !!int "10"
- !!int "11"
- !!int "10"
"speed": "30 ft."
"saves":
  "Strength": !!int "8"
  "Constitution": !!int "9"
"skillsaves":
  "Athletics": !!int "8"
  "Perception": !!int "4"
  "Survival": !!int "4"
"senses": "darkvision 30 ft., passive Perception 14"
"languages": "Common, Dwarvish"
"cr": "11"
"traits":
- "desc": "Kagain wields a [+3 greataxe](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/3-weapon.md).\
    \ While Kagain is attuned to this weapon, his hit point maximum increases to 178.\
    \ Whenever a hostile creature damages Kagain while the axe is in his possession,\
    \ he must succeed on a DC 15 Wisdom saving throw or go berserk. He can choose\
    \ to fail this saving throw. While berserk, Kagain gains advantage on all melee\
    \ attacks and attacks made against him are made with advantage."
  "name": "Special Equipment"
"actions":
- "desc": "Kagain makes three attacks with his Berserking Greataxe."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 13\
    \ (1d12 + 7) slashing damage."
  "name": "Berserking Greataxe"
- "desc": "Ranged Weapon Attack: +5 to hit, range 100/400 ft., one target. Hit:\
    \ 6 (1d10 + 1) piercing damage."
  "name": "Heavy Crossbow"
"legendary_actions":
- "desc": "Kagain makes a Berserking Greataxe attack."
  "name": "Weapon Attack"
- "desc": "Kagain makes a Berserking Greataxe attack against every creature within\
    \ 5 feet of him."
  "name": "Berserk Whirlwind (Costs 3 Actions)"
"source":
- "MaBJoV"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/npc/token/kagain-mabjov.webp"
```
^statblock
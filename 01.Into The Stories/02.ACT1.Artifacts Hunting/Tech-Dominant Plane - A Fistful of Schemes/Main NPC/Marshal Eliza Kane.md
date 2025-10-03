---
AssociatedGroup: The Frontier, Marshall of Ye Olde Town
Gender: Female
Race: Human
Age: Adult (30's)
Class: Fighter (Gunslinger)
Alignment: Lawful
Character-Role: Quest Related, Protector
Location: The Frontier, Ye Olde Town
NoteIcon: npc
---
> [!infobox]
> # `=this.file.name`
> ![[MarshalEliza.png|cover hmedium]]
> [[MarshalEliza.png|Show To Players]]
> ###### Basic Information
> Type |  Stat |
> ---|---|
> Home | `=this.Location` |
> Group | `=this.AssociatedGroup` |
> Sex | `=this.gender` |
> Race | `=this.race` |
> Age | `=this.age` |
> Condition | Healthy |
> ###### Rules Info
> Type |  Stat |
> ---|---|
> Alignment | `=this.alignment` |
> Class | `=this.class` |
> Character Role | `=this.character-role` |

# `=this.file.name`
## Profile


## Statblock
```statblock
"name": "Marshal Eliza Kane, 'The Iron Marshal'"
"size": "Medium"
"type": "humanoid (human)"
"alignment": "Lawful Neutral"
"ac": !!int "17"
"touch_ac": !!int "15"
"ac_class": "breastplate, grit-based reflexes"
"hp": !!int "112"
"hit_dice": "15d8 + 30"
"stats":
- !!int "12"   # STR
- !!int "18"   # DEX
- !!int "14"   # CON
- !!int "13"   # INT
- !!int "16"   # WIS
- !!int "12"   # CHA
"speed": "30 ft."
"saves":
  "Dexterity": !!int "8"
  "Wisdom": !!int "6"
"skillsaves":
  "Insight": !!int "6"
  "Perception": !!int "7"
  "Intimidation": !!int "5"
  "Sleight of Hand": !!int "7"
"senses": "passive Perception 17"
"languages": "Common, Thieves' Cant"
"cr": "7"
"traits":
- "name": "Gunslinger Features (Matt Mercer)"
  "desc": "Eliza uses grit points (6). She regains grit on a critical hit or killing blow. She knows multiple trick shots, including Deadeye Shot, Disarming Shot, Piercing Shot, and Violent Shot."
- "name": "Steely Resolve"
  "desc": "Eliza has advantage on saving throws against being frightened. When she would be reduced to 0 HP, she may make a DC 15 Con save to drop to 1 HP instead (once per long rest)."
- "name": "Iron Marshal"
  "desc": "She exerts a commanding presence in battle. Allies within 10 ft. of her gain +1 to attack rolls and saving throws while she is conscious."

"actions":
- "name": "Multiattack"
  "desc": "Eliza makes two attacks with her revolvers."
- "name": "Revolver (Pistol)"
  "desc": "Ranged Weapon Attack: +8 to hit, range 60/240 ft., one target. Hit: 12 (2d6 + 4) piercing damage. On a crit, regain 1 grit."
- "name": "Sharpshooter Rifle"
  "desc": "Ranged Weapon Attack: +8 to hit, range 150/600 ft., one target. Hit: 15 (2d10 + 4) piercing damage. On a crit, the shot ignores cover."
- "name": "Winging Shot (Trick Shot)"
  "desc": "When Eliza hits with a firearm attack, she can expend 1 grit point to force the target to make a DC 15 Strength save or be knocked prone."
"reactions":
- "name": "Quickdraw"
  "desc": "When a creature moves into melee range, Eliza can expend 1 grit to make a firearm attack as a reaction."

- "name": "Piercing Shot (Trick Shot)"
  "desc": "By spending 1 grit, Eliza fires in a line 30 ft. long and 5 ft. wide. All creatures in the line must succeed on a DC 16 Dexterity saving throw or take weapon damage."
- "name": "Disarming Shot (Trick Shot)"
  "desc": "On a hit, Eliza forces the target to make a DC 16 Strength saving throw or drop one held object of her choice."

"source":
- "Homebrew — Matt Mercer Gunslinger"
"image": "[[MarshalEliza.png]]"

```

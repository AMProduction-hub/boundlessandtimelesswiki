---
AssociatedGroup: Paladin's Past
Gender: Male
Race: Human
Age: Adult
Class: Fighter
Alignment: Lawful Good
Character-Role: Friend, Quest Related
Location: Aruendel
NoteIcon: npc
---
> [!infobox]
> # `=this.file.name`
> ![[DonQuixote.png|cover h300]]
> [[DonQuixote.png|Show to Players]]
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

Elian or Ser Elian is a noble son who inspired to become a knight of a tales.
### Personality 
#### **Ser Elian's Half-Remembered Heroic Quotes (d12)**
1. **"Steel may bend... but, uh, courage is harder!"**
2. **"The stars keep an eye on dreamers, or something like that!"**
3. **"A sword swung for justice doesn't need... a fancy cover!"**
4. **"One little candle can fight off a whole army of darkness!"**
5. **"Oaths are like wings! They, uh, help you... fly above fear!"**
6. **"The road to glory's just a lot of stubborn walking, really."**
7. **"Better to trip with honor than crawl like a coward!"**
8. **"A good heart makes the best kind of shield!"**
9. **"Valor’s like... a forge? No! A fire! A fire in your soul!"**
10. **"By wind, by stone, by... well, whatever's around — I’ll stand!"**
11. **"In the quiet between heartbeats... that's when real courage shouts!"**
12. **"No one sings about the folks who ran away, you know!"**

> [!info] Statblock
> ```statblock
> "name": "Ser Elian"
> "size": "Medium"
> "type": "humanoid (human)"
> "alignment": "Lawful Good"
> "ac": !!int "18"
> "ac_class": "plate armor"
> "hp": !!int "45"
> "hit_dice": "6d8 + 12"
> "stats":
> - !!int "14"
> - !!int "12"
> - !!int "14"
> - !!int "10"
> - !!int "12"
> - !!int "16"
> "speed": "30 ft."
> "skillsaves":
>   "Persuasion": !!int "5"
>   "History": !!int "2"
> "senses": "passive Perception 11"
> "languages": "Common, Elvish"
> "cr": "1"
> "traits":
> - "desc": "Ser Elian has advantage on saving throws against being frightened."
>   "name": "Brave Spirit"
> - "desc": "Ser Elian often utters half-remembered heroic lines during battle, inspiring allies. Once per short rest, he can grant an ally within 30 feet a d4 inspiration die as a bonus action."
>   "name": "Inspiring Words"
> "actions":
> - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage."
>   "name": "Longsword"
> - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) slashing damage if used with two hands."
>   "name": "Longsword (Two-Handed)"
> "equipment": "Plate armor, longsword, shield with family crest"
> "source":
> - "Homebrew: Boundless and Timeless"
> "image": ""
> ```


```encounter-table
name: Individual
creatures:
 - 1: Commoner
```
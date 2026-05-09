---
ImportedOn: Saturday, 18 December 2021 8:41:47 PM
tags:
  - Category/General-Characters-Article
parent:
  - General Characters Article
up:
  - General Characters Article
prev:
  - Template - Class
next:
  - Template - Race
RWtopicId: Topic_ADAM
AssociatedGroup: Barovia
Gender: Male
Race: Dhampir
Age: Adult
Class: Rogue (Arcane Trickster)
Alignment: Lawful Neutral
Character-Role: Quest Related / Enforcer
Location: Barovia
NoteIcon: npc
obsidianUIMode: preview
---
> [!infobox]
> 
> # `=this.file.name`
> 
> ![[adam.png|cover hmedium]] [[adam.png|Show To Players]]
> 
> ###### Basic Information
> 
> |Type|Stat|
> |---|---|
> |Home|`=this.Location`|
> |Group|`=this.AssociatedGroup`|
> |Sex|`=this.gender`|
> |Race|`=this.race`|
> |Age|`=this.age`|
> |Condition|Healthy|
> 
> ###### Rules Info
> 
> |Type|Stat|
> |---|---|
> |Alignment|`=this.alignment`|
> |Class|`=this.class`|
> |Character Role|`=this.character-role`|

# ADAM / Warga Lokal

## Overview

ADAM is not what the Bureau of Time and Plane sent him to be.

He was dispatched to Barovia as an artifact proximity agent — observe, contain, and if necessary eliminate variables. He has been in Barovia for years. He never left. He is now known locally as _Warga Lokal_ — the Local. A rumor to common folk. A proof of consequence to vampires. A man who has already decided how this ends and is watching to see if anyone surprises him.

He is a Dhampir. His mother was Strahd's lover. He is the heir of the plane he is trying to protect.

The party does not know this yet. [[Sephire]] is the only one who has been told — by the mummified Vampire Spawn in Castle Ravenloft's library, during Session 26.

ADAM does not debate morality. He executes conclusions.

---

## The Real Story

ADAM arrived in Barovia as a Bureau agent. He investigated the plane. He found the registration system — the blood tax, the wrist-marks, the coexistence compact — and understood what it was before [[HAWA]] arrived and began dismantling it.

He made a choice. He went native. He became Warga Lokal because refusing to complete the mission was the only moral option available to him inside the Bureau's framework.

He has been maintaining the registration system's physical infrastructure in the tunnels beneath Vallaki for decades. He is the reason the system has lasted a hundred years. Not Strahd's design alone — ADAM's maintenance.

When [[HAWA]] arrived six months ago and took the Stone, ADAM watched. He did not contact her. He did not warn her. There was nothing he could say that she would hear.

He has been watching and waiting ever since, running contingency plans, keeping [[Sephire]] alive in Castle Ravenloft, and preparing for the moment the Festival becomes a catastrophe.

---

## Plot Web

**Warga Lokal — Barovia's Quiet Keeper**

- Has been maintaining the registration infrastructure beneath Vallaki for decades
- Knows the location of every Black Hood operative in the city
- Knows about the Thieves Guild operation — has been quietly protecting it without their knowledge
- Has not intervened because intervention would require revealing what he knows, and what he knows would require explaining who he is

**Strahd's Son**

- Born of Strahd's lover during the final decades of Strahd's rule
- Dhampir — half mortal, half vampire-adjacent
- The only living being with a claim to Barovia's domain
- Has never exercised this claim. Has never told anyone about it. Until the mummified spawn told [[Sephire]].

**Bureau Agent — Inactive**

- His original orders: observe the artifact, eliminate variables if containment fails
- He filed no reports. He completed no mission objectives.
- The Bureau considers him a lost agent. They do not know he is Warga Lokal.
- If the Bureau sends a second team, ADAM will be their first problem.

**Relationship to HAWA**

- Does not work for her. Has never worked for her.
- She believes he is a reliable local enforcer. He is not.
- He would stop her if he could do so without destroying what she has accidentally become the anchor of.
- He cannot stop her without taking the Stone. Taking the Stone breaks the system.

**Relationship to [[Sephire]]**

- Has told Sephire more than he has told anyone in decades.
- Trusts him specifically — not emotionally, strategically. Sephire is the party member most likely to make the right choice when the moment comes.
- _"She did not ask what the mortals were being controlled away from."_ — The most honest thing ADAM has said to anyone in years.

---

## Personal Traits

- Speaks rarely. Answers directly. Never volunteers more than the question requires.
- Observes more than he intervenes. Has been observing for a very long time.
- Shows no visible cruelty or pleasure in violence. Treats it as weather.
- Has a dry, almost absent sense of humor — surfaces only under stress.
- Talks more than usual when something is about to go wrong and he is running out of time to prevent it.

---

## Beliefs & Ideology

- Law exists to prevent worse outcomes.
- Mercy is a resource, not a virtue.
- Monsters are defined by action, not nature.
- Hope is dangerous when unguarded.
- Someone must be willing to be hated.
- Barovia is worth protecting. Not because it is good. Because the alternative is worse.

---

## Key Dialogue Notes

ADAM never gives speeches. His words land because they are few.

> _"A hundred years. And the mortals still walk to the market on Tuesdays."_

> _"She did not ask what the mortals were being controlled away from."_

> _"You are not the first to mean well."_

> _"The moon is useful sometimes."_ _(said while opening shutters during the Valdris fight)_

> _"HAWA believes she is finishing something. She is not. She is beginning something. There is a difference. She cannot see it."_

> _"I am not here to convince you."_

> _"Decisions don't need witnesses."_

---

## Statblock

```statblock
name: ADAM, the Local
size: medium
type: humanoid
subtype: dhampir
alignment: True Neutral
ac: 20
hp: 168
hit_dice: 16d8 + 96
speed: 40 ft, climb 40 ft
stats: [12, 22, 18, 16, 14, 12]
saves:
- dex: 11
- con: 9
- int: 8
- wis: 7
skillsaves:
- acrobatics: 11
- stealth: 17
- sleight of hand: 11
- perception: 7
- insight: 7
- investigation: 8
damage_resistances: necrotic; bludgeoning, piercing, slashing from nonmagical attacks
damage_immunities: charm
condition_immunities: frightened
senses: darkvision 120 ft, blindsense 30 ft, passive Perception 17
languages: Common, Infernal, Thieves' Cant
cr: 13
traits:
- [Sneak Attack, Once per turn deals extra 7d6 damage when he has advantage or ally adjacent.]
- [Evasion, Takes no damage on successful Dex saves, half on fail.]
- [Uncanny Dodge, Reaction halves damage from one attack.]
- [Spider Climb, Can move on walls and ceilings.]
- [Mist Step, When reduced below 40 HP transforms into mist until end of next turn — immune to all damage, can move 40 ft. 1/Day.]
- [Tactical Observer, ADAM cannot be surprised and adds +5 to initiative.]
spellcasting:
- Spellcasting Ability: Intelligence (save DC 16, +8 to hit)
- At Will: mage hand, minor illusion, message
- 1st (4 slots): shield, disguise self, silent image
- 2nd (3 slots): invisibility, mirror image
- 3rd (3 slots): hypnotic pattern, counterspell
- 4th (2 slots): greater invisibility, dimension door
actions:
- [Multiattack, ADAM makes two Shadow Rapier attacks.]
- [Shadow Rapier, +11 to hit reach 5 ft 1 target. Hit 1d8+6 piercing + 4d6 necrotic.]
- [Vampiric Bite, +11 to hit 1d6+6 piercing + 3d6 necrotic. ADAM heals equal to necrotic dealt.]
- [Command Mark (Recharge 5-6), One creature ADAM can see must succeed DC 16 Wis save or become Marked for 1 minute. Marked targets grant advantage to ADAM and take +10 damage from his attacks.]
bonus_actions:
- [Cunning Action, Dash Disengage or Hide.]
- [Shadow Slip, Teleport 30 ft between dim light or darkness.]
reactions:
- [Uncanny Dodge, Halve damage from an attack.]
- [Counterspell, As spell.]
legendary_actions:
- ADAM can take 2 legendary actions per round.
- [Move, Move up to speed without provoking opportunity attacks.]
- [Cantrip, Cast a cantrip.]
- [Analyze (Costs 2), ADAM learns one creature's lowest saving throw.]
```

---

## GM Notes (Hidden)

**The bloodline secret:** ADAM is Strahd's son. His mother was Strahd's mortal lover during the final decades of Strahd's rule. He has known about the Stone's true nature — that it is Strahd's transformed body — for decades. He has been maintaining his father's domain while his father sleeps inside an artifact in HAWA's bag. He has told nobody. Until the mummified Vampire Spawn told [[Sephire]] in Session 26.

**What ADAM will do:**

- If the party chooses NOT to complete the Bureau mission: becomes an active ally, opens every resource he has including the tunnel network and his knowledge of every Black Hood operative
- If the party tries to take the Stone: one warning. Then he becomes an obstacle. He will not kill them — but he will stop them.
- If HAWA uses the Stone at the Festival: activates damage control immediately. This is the scenario he has been dreading for six months.
- If Strahd wakes: ADAM has no plan for this. Even he doesn't know what his father would do.

**ADAM's contingency plans — one per party member:** He has already calculated the most likely action each party member will take at the critical moment and prepared a response. He will not reveal these plans. He considers this standard administrative procedure. He does not consider it cruel.

**ADAM will lie** if it preserves Barovia's stability. He has not lied to Sephire yet. This is significant.

**The tunnel network:** ADAM knows every passage beneath Vallaki including a direct route to Vallaki Castle's foundation. He built some of these tunnels himself. The Guild's sewer network runs parallel — he designed the separation deliberately to protect their operation without their knowledge. He has been protecting the Thieves Guild for years without them knowing.

**He is fully aware** that history will remember him as a monster. He made peace with this a long time ago. Being remembered as a monster was always part of the job.
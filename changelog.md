# Retribution v1.4.0
#### Note: Re-save your missions in DCS' Mission Editor to avoid possible crashes due to datalink (usually the case when F-16C blk50s are used) when hosting missions on a dedicated server.

## Features/Improvements
* **[Payload Editor]** Ability to configure liveries on flight/flight-member level
* **[Factions]** Support for definitions in yml/yaml format
* **[Campaigns/Factions]** Support for inline recommended faction in campaign's yaml file
* **[Squadrons]** Ability to define a livery-set for each squadron from which Retribution will randomly choose during mission generation
* **[Modding]** Updated support for F/A-18E/F/G mod version 2.2.5
* **[Modding]** Added VSN F-106 Delta Dart mod support (v2.9.4.101)
* **[Modding]** Added OH-6 Cayuse (v1.2) mod support, including the Vietnam Asset Pack v1.0
* **[Modding]** Added VSN EA-6B Prowler mod support (v2.9.4.102)
* **[Modding]** Added tripod3 Cold War assets mod support (v1.0)
* **[Campaign Setup]** Allow adjustments to naval TGOs (except carriers) on turn 0
* **[Campaign Design]** Ability to configure specific carrier names & types in campaign's yaml file 
* **[Mission Generation]** Ability to inject custom kneeboards
* **[Options]** Extend option (so it can be disabled when fixed in DCS) to force air-starts (except for the slots that work) at Ramon Airbase, similar to the Nevatim fix in Retribution 1.3.0
* **[Options]** New option in Settings: Default start type for Player flights.
* **[AirWing]** Expose OPFOR Squadrons, giving the ability to change liveries, auto-assignable mission types & an easy way to retrieve debug information.
* **[ATO]** Allow planning as OPFOR
* **[Campaign Design]** Support for latest maps (Kola, Afghanistan, Iraq)
* **[UI]** Zoom level retained when switching campaigns
* **[UX]** Allow changing squadrons in flight's edit dialog
* **[Cheats]** Sink/Resurrect carriers instead of showing an error during cheat-capture (use AWCD-cheat to add squadrons upon resurrection)
* **[UI/UX]** Allow changing conditions such as Time, Date & Weather
* **[Modding]** Added support for Su-15 Flagon mod (v1.0)
* **[Plugins]** Support for Carsten's Arty Spotter script
* **[Plugins]** Support for MBot's Call Artillery script (using on-map artillery)
* **[Modding]** Added support for SK-60 mod (v1.2.1)
* **[Mission Generation]** Introducing the Armed Recon flight plan, i.e. CAS against any Theater Ground Object
* **[Doctrine]** Ability to customize the startup time allocated to the player
* **[Mission Generation]** Ability to choose whether player flights can spawn on the sixpack or not
* **[Options]** New options in Mission Generator section: Limit AI radio callouts & Suppress AI radio callouts.
* **[Options]** New option to use the combat landing flag in the landing waypoint task for helicopters.
* **[UI/UX]** Sync package waypoints when primary flight's waypoints are updated and recreate other flights within the package to ensure JOIN, INGRESS & SPLIT are synced
* **[UI/UX]** Allow changing loadout on flight creation
* **[UI]** Display TOT for all waypoints in the flight plan
* **[UI]** Edit basic datalink properties for applicable aircraft
* **[Mission Generation]** Automatic datalink network setup for applicable aircraft (_should_ in theory avoid the need to re-save the mission)
* **[Options]** New option to force-enable deck-crew for super-carriers on dedicated server.
* **[Mission Generation]** Enable Supercarrier's LSO & Airboss stations
* **[UX]** Default settings are now loaded from Default.zip
* **[Autoplanner]** Plan Air-to-Air Escorts for AWACS & Tankers
* **[Package Planning]** Ability to plan recovery tanker flights
* **[Modding]** Support for Bandit's cloud presets mod (v15)
* **[UX]** Reduce size of save-file by loading landmap data on the fly, which also implies no new campaign needs to be started to benefit from an updated landmap
* **[New Game Wizard]** Ability to save an edited faction during new game creation
* **[Options]** New option to make AI helicopters prefer vertical takeoff and landing
* **[Campaign Design/Mission Generation]** Introduction of "rebel zones" which randomly spawn units according to the campaign's definitions.
* **[Mission Generation]** Missile sites now fire at random times instead of all at the beginning of the mission
* **[Modding]** Support for CurrentHill's Chinese Asset Pack (v1.1.4)
* **[Modding]** Updated support for CurrentHill's Swedish Asset Pack (v1.1.0)
* **[Modding]** Support for CurrentHill's Russian Asset Pack (v1.2.0)
* **[Modding]** Support for CurrentHill's USA Asset Pack (v1.1.5)

## Fixes
* **[UI/UX]** A-10A flights can be edited again
* **[Mission Generation]** IADS bug sometimes triggering "no skynet usable units" error during mission generation
* **[New Game Wizard]** Campaign errors show a dialog again and avoid CTDs
* **[UI]** Landmap wasn't updating when switching to a different theater
* **[Mission Results Processor]** Squadrons of a sunken carrier are now disbanded
* **[Mission Generation]** Introduced option to switch alt-type to AMSL during mission generation to avoid helicopters wanting to submerge over certain parts of the sea.

# Retribution v1.3.1
#### Note: Re-save your missions in DCS' Mission Editor to avoid possible crashes due to datalink (usually the case when F-16C blk50s are used) when hosting missions on a dedicated server.

## Fixes
* **[UX]** Fix save-compatibility issue
* **[UX]** Avoid crash on startup due to incompatible save


# Retribution v1.3.0
#### Note: Re-save your missions in DCS' Mission Editor to avoid possible crashes due to datalink (usually the case when F-16C blk50s are used) when hosting missions on a dedicated server.

## Features/Improvements
* **[Engine]** Support for DCS v2.9.3.51704
* **[Package Planning]** Option to "Auto-Create" package
* **[Modding]** Custom weapons injection system (definition in aircraft's yaml file)
* **[Payload Editor]** Ability to save/back-up payloads
* **[Options]** New option in Settings: CAS engagement range (nmi)
* **[Options]** New option in Settings: Convert untasked OPFOR aircraft into client slots
* **[Options]** Split the **Disable idle aircraft at airfields** setting into **Disable untasked BLUFOR aircraft at airfields** and **Disable untasked OPFOR aircraft at airfields**
* **[Options]** Split off the **Automatic AWACS package planning** and **Automatic Theater tanker package planning** settings from **Automatic package planning behavior** so players can choose to have AWACS and theater tankers auto-planned, while managing everything else themselves
* **[Modding]** Updated support for Su-30 mod to V2.7.3 Beta
* **[Modding]** Updated support for Su-57 mod to build-04
* **[Modding]** Updated support for F-4B/C Phantom mod to 2.8.7.204
* **[Modding]** Updated Community A-4E-C mod version support to 2.2.0 release.
* **[Modding]** Added F/A-18E/F Super Hornet AI Tanker mod support (Chiller Juice Studios SuperBug Tanker AI version 1.4)
* **[Modding]** Added VSN Super Étendard mod support (v2.5.5)
* **[Modding]** Added F9F Panther mod support (version v2.8.7.101)
* **[Modding]** Updated Irondome support to IDF Assets Pack V1.1, adding support for the David's Sling
* **[Radios]** Added HF-FM band for AN/ARC-222
* **[Radios]** Ability to define preset channels for radios on squadron level (for human pilots only)
* **[Mission Planning]** Avoid helicopters being assigned as escort to planes and vice-versa
* **[Mission Planning]** Allow attack helicopters to escort other helicopters
* **[UI]** Allow changing waypoint names in FlightEdit's waypoints tab
* **[Waypoints]** Allow user to add navigation waypoints where possible without degrading to a custom flight-plan
* **[Campaign Management]** Improve squadron retreat logic to account for parking-slot sizes
* **[Autoplanner]** Support for auto-planning Air Assaults
* **[UI]** Improved frequency selector to support all modeled bands for every aircraft's intra-flight radio
* **[Options]** New options in Settings: Helicopter waypoint altitude (feet AGL) for combat & cruise waypoints
* **[Options]** New options in Settings: Spawn ground power trucks at ground starts in airbases/roadbases
* **[Options]** Option for hiding TGOs (with IADS roles) on MFD
* **[Plugins]** Splash Damage 2.1 with Clusters and Ship Radar effects.
* **[COMMs]** Aircraft-specific callsigns will now also be used.
* **[COMMs]** Ability to set a specific callsign to a flight.
* **[Mission Generator]** Channel terrain fix on exclusion zones, sea zones and inclusion zones
* **[Options]** Cheat-option for accessing Air Wing Config Dialog after campaign start (re-initializes turn if applied, thus plan your mission ___after___ making changes)
* **[Options]** Option to enable unlimited fuel for AI (player and non-player flights)
* **[Mission Generator]** F-15E Strike targets are automatically added as Mission Set 1 
* **[Mission Generator]** Set F-14's IP waypoint according to the flight-plan's ingress point
* **[Mission Generator]** Automatically de-spawn aircraft when arrival/divert is an off-map spawn
* **[Options]** Option to de-spawn AI flights in the air if their start-type was manually set to In-Flight
* **[Campaign Design]** Ability to add separate ground spawns for C-130 and other large aircraft to campaigns.
* **[Config]** Preference setting to use custom Liberation payloads instead of prioritizing Retribution's default
* **[Config]** Preference setting to configure the server-port on which Retribution's back-end will run
* **[Options]** Made AI jettisoning empty fuel tanks optional (disabled by default)
* **[Options]** Add option (so it can be disabled when fixed in DCS) to force air-starts (except for the slots that work) at Nevatim due to https://forum.dcs.world/topic/335545-29-nevatim-ramp-starts-still-bugged/
* **[Cheat]** Add cheat option to manually manage REDFOR's TGOs
* **[UX]** Buy/Replace TGOs for free before the campaign has started
* **[Data]** Ability to define "cruise" & "combat" altitudes for airplanes
* **[Options]** Option to randomize altitudes for flights with airplanes
* **[Options]** Options to configure/override maximum mission distance for airplanes & helicopters 

## Fixes
* **[Mission Generation]** Anti-ship strikes should use "group attack" in their attack-task
* **[New Game Wizard]** Faction selection overview doesn't update when inverting map
* **[New Game Wizard]** Aircraft mods are now handled better when they are disabled
* **[Payloads]** Added/Updated (missing) payloads
* **[Aircraft Tasking]** Revised aircraft tasking, filtering out incompatible tasks for several aircraft
* **[Data]** Corrected the class of the USS Samuel Chase from Logistics to LandingShip, in order to prevent it being spawned as part of AAA sites.
* **[Mission Generation]** Helicopters oscillating due to over-speeding
* **[Mission Generation]** Fix infinite loop when using "Fast-Forward to first contact"
* **[Capture Logic]** Release all parking slots when an airbase is captured
* **[Modding]** Swedish Military Assets Pack air defence presets are now correctly removed from the faction when the mod is disabled.
* **[Mission Generation]** Naval aircraft not always returning to carrier
* **[Mission Generation]** AI AirLift aircraft crashing into terrain due to insufficient waypoints
* **[Mission Generation]** Fix friendly AI shooting at fires on the front-line

# Retribution v1.2.1 (hotfix)

## Fixes
* **[Flight Plans]** SEAD Sweep not being auto-planned
* **[Modding]** Python-4 no longer overwrites AIM-9X
* **[Modding]** Restore original amount of pylons to F-16C when "ejecting" sufa mod

# Retribution v1.2.0

## Features/Improvements
* **[Preset Groups]** Add SA-2 with ZSU-23/57
* **[Campaign Design]** Ability to define almost all possible settings in the campaign's yaml file.
* **[Campaign Design]** Ability to add roadbases and/or ground spawns to campaigns.
* **[Campaign Design]** Ability to define SCENERY REMOVE OBJECTS ZONE triggers with the roadbase objects in campaign miz. This might not work reliably in multiplayer due to DCS issues. FARPs can be used to remove scenery objects in multiplayer.
* **[Options]** Implemented an option in settings to disable the above SCENERY REMOVE OBJECTS ZONE triggers.
* **[Campaign Management]** Improved squadron retreat logic at longer ranges.
* **[Options]** Ability to load & save your settings.
* **[Options]** Added a separate Doctrine page in settings with the following new options:
  * Minimum number of aircraft for autoplanner to plan OCA packages against 
  * Airbase threat range (nmi)
  * SEAD Sweep threat buffer distance (nmi)
  * SEAD Escort/Sweep threat buffer distance (nmi)
  * TARCAP threat buffer distance (nmi)
  * AEW&C threat buffer distance (nmi)
  * Theater tanker threat buffer distance (nmi)
* **[Options]** Improved the option to configure OPFOR autoplanner aggressiveness. The AI might now take even more risks and plan missions against defended targets.
* **[Options]** Added three new options in Settings:
  * Autoplanner plans refueling flights for Strike packages
  * Autoplanner plans refueling flights for OCA packages
  * Autoplanner plans refueling flights for DEAD packages
* **[UI]** Added fuel selector in flight's edit window.
* **[Plugins]** Expose Splash Damage's "game_messages" option and set its default to false.
* **[Mission Generation]** Improved AI SEAD capabilities, allowing for mixed loadouts using Decoys, ARMs & ASMs.
* **[Modding]** Support for A-7E Corsair II (presumed latest available version)
* **[Squadrons]** Added many new squadron's by Adecarcer
* **[Plugins]** Updated 'expl_table' in Splash Damage script.
* **[Mission Generation]** Also save kneeboards in txt-format, found under "kneeboards" within Retribution's installation folder after pressing take-off.
* **[Modding]** Support for SW mod v2.55
* **[Modding]** Support for Spanish & Australian Naval Assets v3.2.0 by desdemicabina
* **[Modding]** Support for Iron Dome v1.2 by IDF Mods Project
* **[New Game Wizard]** Re-organized generator options & show the regular settings menu instead of the limited "Difficulty & Automation" page.
* **[Campaign Management]** Ability to operate harriers from FOBs/FARPs for <ins>__human pilots only__</ins>. Please note that the autoplanner won't generate flights for harriers at FOBs/FARPs, which means you need to plan your missions manually.
* **[Mission Planning]** Allow NAV/REFUEL/DIVERT waypoints to be deleted without degrading to a custom flight-plan, also warning the user before actually degrading the flight-plan.
* **[Campaign Generation]** Split "full-strength start" from "squadron aircraft limits" option.
* **[Mission Generation]** General improvement w.r.t. DCS tasking, including a check for incompatible tasking.
* **[Mission Generation]** OCA-Runway flights will remain at altitude when using guided bombs.
* **[UX]** Added error message to indicate save-compatibility issues + fix to avoid total crash upon loading of last save.
* **[UI]** Improved parking space information in air wing configuration dialog.
* **[Squadrons]** Warning messages when opening up a squadron through the air wing dialog, indicating squadrons that potentially won't fit w.r.t. parking space.
* **[Squadrons Transfers]** Determine number of available parking slots more accurately w.r.t. squadron transfers, taking aircraft dimensions into account which should prevent forced air-starts.
* **[UX]** Allow usage of CTRL/SHIFT modifiers in ground unit transfer window.
* **[Campaign Design]** Ability to define "spawn-routes" for convoys, allowing them to start from the road without having to edit the mission
* **[Plugins]** Added "DCS Dismount" plugin.
* **[Plugins]** Added "EWR Jammer" plugin (only for humans, may change in the future).
* **[Campaign]** New campaign (Operation Desert Sabre) by Chimiste
* **[Plugins]** Updated CTLD to latest released version
* **[Options]** Renamed Maximum frontline length -> Maximum frontline width.
* **[Squadrons]** Add livery selector in Squadron Dialog, allowing you to change the livery during the campaign.
* **[New Game Wizard]** Automatically invert factions when 'Invert Map' is selected.
* **[Flight Plans]** Added "SEAD Sweep" flight plan, which basically reintroduces the legacy "SEAD Escort" flight plan where the flight will engage whatever it can find without actually escorting the primary flight.
* **[Flight Plans]** Added SEAD capability to F-16A MLU and SEAD Escort & SEAD to F-16A. 
* **[Mission Generation]** Spawn unused helicopters or LHA-capable aircraft at helipads at FOBs
* **[Modding]** Support for F-15I Ra'am v1.0 by IDF Mods Project

## Fixes
* **[New Game Wizard]** Settings would not persist when going back to a previous page (obsolete due to overhaul).
* **[Mission Generation]** Unused aircraft are no longer claimed, fixing a bug where these aircraft would no longer be available after aborting the mission.
* **[Mission Generation]** Fixed (potential) bug in helipad assignments at FOBs/FARPs.
* **[Mission Generation]** Fix AI immediately returning to base when forced to air-start due to insufficient parking space.
* **[Modding]** Fixed a bug where F-16Ds were not correctly removed from the faction when the F-16I/F-16D mod was not selected
* **[UI]** Fixed F-16A MLU icon and banner.

# Retribution v1.1.1  (hotfix)

## Features/Improvements
* **[Modding]** Support for IDF Mod Project F-16I Sufa & F-16D v3.6 mod
* **[Modding]** Support for JAS-39 Gripen v1.8.5-beta mod

## Fixes
* **[Plugins]** Fix bug where changes to plugin options doesn't do anything.
* **[Campaign Management]** Fix bug in procurement when no squadrons are present.
* **[Layouts]** Fix edge-case bug layout's group size.
* **[Campaign Design]** Preset groups assigned to specific TGOs not working as intended.

# Retribution v1.1.0

## Features/Improvements
* **[Mission Generation]** Given a CAS flight was planned, delay ground force attack until first CAS flight is on station
* **[Mission Generation]** Add option to switch ATFLIR to LITENING automatically for ground based F/A-18C flights
* **[Mission Generation]** Add option to configure OPFOR autoplanner aggressiveness and have the AI take risks and plan missions against defended targets
* **[Mission Generation]** Add option to configure the desired tanker on-station time in settings
* **[Mission Generation]** Reserve GUARD frequency on VHF/UHF
* **[Mission Generation]** Randomization in radio frequency allocation
* **[Mission Generation]** Configurable number of Combined Arms slots
* **[Mission Generation]** Enable spectating & F11 free camera when the "Allow external views" option is selected
* **[Cheat Menu]** Option to instantly transfer squadrons across bases.
* **[Modding]** Support for IDF Mod Project F-16I Sufa & F-16D v3.2 mod
* **[Modding]** Support for F/A-18E/F/G mod version 2.1
* **[Modding]** Support for Swedish Military Assets for DCS by Currenthill Version 1.10
* **[UI]** Add selectable units in faction overview during campaign generation.
* **[UI]** Add button to rename pilots in Air Wing's Squadron dialog.
* **[UI]** Add clone buttons for flights & packages.
* **[UI]** Editing of flight's custom name.
* **[UI]** Introduce custom names for packages (purely for organizational purposes).
* **[UI]** Configurable UHF frequency (225-400MHz) for Packages, Carriers, LHAs, FOBs & FARPs.
* **[UI]** Configurable Intra-Flight frequency for Flights.
* **[UI]** Configurable TACAN for Carriers, LHAs & Tankers.
* **[UI]** Configurable ICLS for capable Carriers & LHAs.
* **[UI]** Configurable LINK4 for Carriers.
* **[Kneeboard]** Show package information in Support page
* **[Kneeboard]** Show extra weather information on 'Mission info' page
* **[Kneeboard]** Show BRC in 'RWY' column for aircraft carriers on 'Mission info' page
* **[Campaign Design]** Ability to define designated CTLD zones for Control Points (Airbases & FOBs/FARPs)
* **[Campaign Design]** Ability to define preset groups for specific TGOs, given the preset group is accessible for the faction and the task matches.
* **[Campaign Management]** Additional options for automated budget management.
* **[Campaign Management]** New options to allow more control of randomized flight sizes (applicable for BARCAP/CAS/OCA/ANTI-SHIP).
* **[Plugins]** Updated Splash Damage script to v2.0 by RotorOps.
* **[Mission Generation]** Improvements to DEAD & STRIKE flights, allowing AI to handle a larger variety of weapons.
* **[Campaign]** New campaign (1968 Yankee Station) by Adecarcer

## Fixes
* **[UI]** Removed deprecated options
* **[UI]** Add missing icon & banner for C130 Hercules mod
* **[Mission Generation]** Avoid aircraft from being assigned to helicopter parking spots, resulting into air starts that usually crash.
* **[Mission Generation]** Use stacking algorithm to create vertical separation between flights spawning mid-mission over their departure, usually resulting into mid-air collisions.
* **[Mission Generation]** Fixed all callsigns being "Enfield 1-1" on dedicated servers.
* **[Mission Generation]** Fixed AI ferry flights for helicopters when transferring to a FOB/FARP.
* **[Mission Generation]** Fixed 'Uninitialized flight' exception when adding flights after aborted take-off.
* **[Modding]** Fixed conflicts caused by HDS units
* **[UX]** Gracefully handle corrupted preferences file.
* **[Mission Generation]** Aircraft not using decoys during SEAD.

# Retribution v1.0.1 (hotfix)
* **[Mission Generation]** Fix serialization issue when STRIKE flight has no escorts

# Retribution v1.0.0

## Features/Improvements
* **[Engine]** Support for DCS v2.8.1.34437.
* **[Briefing]** Add tanker info to mission briefing
* **[Campaign]** Add 5 new campaigns by Oscar Juliet from WRL
* **[Campaign]** Add ability to define livery overrides also for ground/naval units
* **[Data]** Added data to support C-47 Skytrain.
* **[Data]** Added data to support F-16A MLU.
* **[Data]** Added data to support KS-19 & SON-9, including support for "AAA Site" layout.
* **[Mission Generation]** Add option to configure the maximum front-line length in settings
* **[Mission Generation]** Use Escort & SEAD tasks for Escort & SEAD Escort flights
* **[Mission Generation]** Variable flight-size (2/3/4-ship) for 
BAI/ANTISHIP/DEAD/STRIKE/BARCAP/CAS/OCA/AIR-ASSAULT (main) missions
* **[Mission Generation]** Add option to only generate night missions
* **[Modding]** Support for F-15D 'Baz' mod version 1.0
* **[Modding]** Support for Su-30 mod version 2.01B
* **[Modding]** Support for A-6A Intruder version 2.7.5.01
* **[Modding]** Support for F-4B Phantom II mod version v2.7.10.02, patch 2022.10.02
* **[Modding]** Support for F-100 Super Sabre mod versions v2.7.18.01 & 2.7.18.30765 and patch 20.10.22
* **[Modding]** Support for F-105 mod version 2.7.12.23x
* **[Modding]** Support IDF Mod Project F-16I Sufa & F-16D v2.2 mod
* **[Modding]** Support for F-84G mod version 2.5.7.01
* **[Modding]** Updated F-104 mod version support to 2.7.11.222.01
* **[Modding]** Updated Community A-4E-C mod version support to 2.1.0 release.
* **[UI]** Add livery selector to Air Wing Configurator's squadrons.
* **[Performance]** Added performance option: Maximum front-line unit supply per control point.
* **[Performance]** Added performance option: Disable convoys.
* **[Performance]** Added performance option: Front-line troops prefer roads.
* **[Performance]** Added performance option: Disable idle aircraft at airfields.
* **[Squadrons]** Squadron pilot limits enabled by default.
* **[UI]** Add livery selector to Air Wing Configurator's squadrons.

## Fixes

* **[Mission Generation]** Fixed issue where aircraft carriers would return after being killed.
* **[Mission Generation]** Kneeboard STRIKE coordinates would sometimes get clipped when not fitting.
* **[UI]** Fix exception when trying to add a waypoints to a flightplan.


# Liberation:
## Features/Improvements

* **[Data]** Added support for the ARA Veinticinco de Mayo.
* **[Data]** Changed display name of the AI-only F-15E Strike Eagle for clarity.
* **[Flight Planning]** Improved IP selection for targets that are near the center of a threat zone.
* **[Flight Planning]** Moved CAS ingress point off the front line so that the AI begins their target search earlier.
* **[Flight Planning]** Loadouts and aircraft properties can now be set per-flight member. Warning: AI flights should not use mixed loadouts.
* **[Flight Planning]** Laser codes that are pre-assigned to weapons at mission start can now be chosen from a list in the loadout UI. This does not affect the aircraft's TGP, just the weapons. Currently only implemented for the F-15E S4+ and F-16C.
* **[Mission Generation]** Configured target and initial points for F-15E S4+.
* **[Modding]** Factions can now specify the ship type to be used for cargo shipping. The Handy Wind will be used by default, but WW2 factions can pick something more appropriate.
* **[Modding]** Unit variants can now set a display name separate from their ID.
* **[UI]** An error will be displayed when invalid fast-forward options are selected rather than beginning a never ending simulation.
* **[UI]** Added cheats for instantly repairing and destroying runways.
* **[UI]** Improved usability of the flight properties UI. It now shows human-readable names and uses more appropriate UI elements.
* **[UI]** The map now shows the real front line bounds.

## Fixes

* **[Campaign]** Fixed error when canceling squadron transfer if the current location would be exactly full.
* **[Data]** Fixed the class of the Samuel Chase so it can't be picked for a AAA or SHORAD site.
* **[Data]** Allow CH-47D, CH-53E and UH-60A to operate from carriers and LHAs.
* **[Data]** Added the F-15E's LANTIRN to the list of known targeting pods. Player F-15E flight with TGPs will now be assigned laser codes.
* **[Flight Planning]** Patrolling flight plans (CAS, CAP, refueling, etc) now handle TOT offsets.
* **[Mission Generation]** Restored previous AI behavior for anti-ship missions. A DCS update caused only a single aircraft in a flight to attack. The full flight will now attack like they used to.
* **[Mission Generation]** Fix generation of OCA Runway missions to allow LGBs to be used.
* **[Mission Generation]** Fixed AI flights flying far too slowly toward NAV points.
* **[Mission Generation]** Fixed "division by zero" error on mission generation when a flight has an "In-Flight" start type and starts on top of a mission waypoint.
* **[Modding]** Unit variants can now actually override base unit type properties.
* **[Plugins]** Fixed Lua errors in Skynet plugin that would occur whenever one coalition had no IADS nodes.
* **[UI]** Fixed deleting waypoints in custom flight plans deleting the wrong waypoint.
* **[UI]** Fixed flight properties UI to support F-15E S4+ laser codes.
* **[UI]** Fixed UI bug where altering an "ahead of package" TOT offset would change the offset back to a "behind pacakge" offset.
* **[UI]** Fixed bug where changing TOT offsets could result in flight startup times that are in the past.
* **[UI]** Flight plan paths are now drawn behind all other map elements, fixing rare cases where they could prevent other UI elements from being clickable.

# 8.1.0

Saves from 8.0.0 are compatible with 8.1.0

## Features/Improvements

* **[Engine]** Support for DCS 2.8.6.41363, including F-15E support.
* **[UI]** Flight loadout/properties tab is now scrollable.

## Fixes

* **[Campaign]** Fixed liveries for premade squadrons all being off-by-one.
* **[UI]** Fixed numbering of waypoints in the map and flight dialog (first waypoint is now 0 rather than 1).

# 8.0.0

Saves from 7.x are not compatible with 8.0.

## Features/Improvements

* **[Engine]** Support for DCS 2.8.6.41066, including the new Sinai map.
* **[UI]** Limited size of overfull airbase display and added scrollbar.
* **[UI]** Waypoint altitudes can be edited in Waypoints tab of Edit Flight window.
* **[UI]** Moved air wing and transfer menus to the toolbar to improve UI fit on low resolution displays.
* **[UI]** Added basic game over dialog.

## Fixes

* **[Campaign]** Fix bug introduced in 7.0 where map strike target deaths are no longer tracked.
* **[Mission Generation]** Fix crash during mission generation caused by out of date DCS data for the Gazelle.
* **[Mission Generation]** Fix crash during mission generation when DCS beacon data is inconsistent.

# 7.1.0

Saves from 7.0.0 are compatible with 7.1.0

## Features/Improvements

* **[Factions]** Replaced Patriot STRs "EWRs" with AN/FPS-117 for blue factions 1980 or newer.
* **[Mission Generation]** Added option to prevent scud and V2 sites from firing at the start of the mission.
* **[Mission Planning]** Per-flight TOT offsets can now be set in the flight details UI. This allows individual flights to be scheduled ahead of or behind the rest of the package.
* **[UI]** Waypoint altitudes can be edited in Waypoints tab of Edit Flight window.
* **[UI]** Parking capacity of each squadron's base is now shown during air wing configuration to avoid overcrowding bases when beginning the game with full squadrons.

## Fixes

* **[Mission Planning]** BAI is once again plannable against missile sites and coastal defense batteries.
* **[UI]** Fixed formatting of departure time in flight details dialog.

# 7.0.0

Saves from 6.x are not compatible with 7.0.

## Features/Improvements

* **[Engine]** Support for DCS 2.8.3.37556.
* **[Engine]** Saved games are now a zip file of save assets for easier bug reporting. The new extension is .liberation.zip. Drag and drop that file into bug reports.
* **[Campaign]** Added options to limit squadron sizes and to begin all squadrons at maximum strength. Maximum squadron size is defined during air wing configuration with default values provided by the campaign.
* **[Campaign]** Added handling for more DCS death events. This probably does not catch any deaths that weren't previously tracked, but it should record them sooner, which will improve results for game crashes or other early exits.
* **[Campaign AI]** The campaign AI now prefers fulfilling missions with squadrons which have a matching primary task. Previously distance from target held a stronger influence than task preference. Primary tasks for squadrons are set by campaign designers but are user-configurable.
* **[Flight Planning]** Package TOT and composition can be modified after advancing time in Liberation.
* **[Mission Generation]** Units on the front line are now hidden on MFDs.
* **[Mission Generation]** Preset radio channels will now be configured for both A-10C modules.
* **[Mission Generation]** The A-10C II now uses separate radios for inter- and intra-flight comms (similar to other modern aircraft).
* **[Mission Generation]** Wind speeds no longer follow a uniform distribution. Median wind speeds are now much lower and the standard deviation has been reduced considerably at altitude but increased somewhat at MSL.
* **[Mission Generation]** Improved task generation for SEAD flights carrying TALDs.
* **[Mission Generation]** Added task timeout for SEAD flights with TALDs to prevent AI from overflying the target.
* **[Modding]** Updated Community A-4E-C mod version support to 2.1.0 release.
* **[Modding]** Add support for VSN F-4B and F-4C mod.
* **[Modding]** Aircraft task capabilities and preferred aircraft for each task are now moddable in the aircraft unit yaml files. Each aircraft has a weight per task. Higher weights are given higher preference.
* **[Modding]** The `mission_types` field in squadron files has been removed. Squadron task capability is now determined by airframe, and the auto-assignable list has always been overridden by the campaign settings.
* **[Modding]** Wind speed generation inputs are now moddable. See https://dcs-liberation.rtfd.io/en/latest/modding/weather.html.
* **[New Game Wizard]** Choices for some options will be remembered for the next new game. Not all settings will be preserved, as many are campaign dependent.
* **[New Game Wizard]** Lua plugins can now be set while creating a new game.
* **[New Game Wizard]** Squadrons can be directly replaced with a preset during air wing configuration rather than needing to remove and create a new squadron.
* **[New Game Wizard]** Squadron liveries can now be selected during air wing configuration.
* **[Squadrons]** Squadron-specific mission capability lists no longer restrict players from assigning missions outside the squadron's preferences.
* **[New Game Wizard]** Squadrons can be directly replaced with a preset during air wing configuration rather than needing to remove and create a new squadron.
* **[UI]** The orientation of objects like SAMs, EWRs, garrisons, and ships can now be manually adjusted.

## Fixes

* **[Campaign]** Fixed a longstanding bug where oversized airlifts could corrupt a save with empty convoys.
* **[Campaign]** Aircraft with built-in TGPs but without an external pod will no longer degrade automatic loadouts to iron bombs.
* **[Engine]** Fixed crash in startup caused by a corrupted Liberation preferences file.
* **[Flight Planning]** AEW&C missions are now plannable over FOBs and LHAs.
* **[Flight Planning]** BAI is no longer plannable against buildings.
* **[Modding]** Fixed an issue where Falklands campaigns created or edited with new versions of DCS could not be loaded.
* **[Modding]** Fixed decoding of campaign yaml files to use UTF-8 rather than the system locale's default. It's now possible to use "Bf 109 K-4 Kurfürst" as a preferred aircraft type.
* **[Mission Generation]** Planes will no longer spawn in helipads that are not also designated for fixed wing parking.
* **[Mission Generation]** Potentially an issue where ground war planning game state could become corrupted, preventing mission generation.
* **[Mission Generation]** Refueling tasks will now only be created for flights that have a tanker in their package.
* **[Mission Generation]** Fixed missing Tanker task on recovery tanker missions.
* **[UI]** Fixed error when resetting air wing configuration during game setup.
* **[UI]** Fixed flight plan recreation when changing mission type with "Recreate as" flight options.
* **[UI]** Fixed failure to launch UI when Liberation persistent preferences file was corrupt.


# 6.1.1

## Fixes

* **[Data]** Fixed unit ID for the KS-19 AAA. KS-19 would not previously generate correctly in missions. A new game is required for this fix to take effect.
* **[Flight Planning]** Automatic flight planning will no longer accidentally plan a recovery tanker instead of a theater refueling package. This fixes a potential crash during mission generation when opfor plans a refueling task at a sunk carrier. You'll need to skip the current turn to force opfor to replan their flights to get the fix.
* **[Mission Generation]** Using heliports (airports without any runways) will no longer cause mission generation to fail.

# 6.1.0

Saves from 6.0.0 are compatible with 6.1.0

## Features/Improvements

* **[Factions]** Defaulted bluefor modern to use Georgian and Ukrainian liveries for Russian aircraft.
* **[Factions]** Added Peru.
* **[Modding]** Added support for the HMS Ariadne, Achilles, and Castle class.

## Fixes

* **[Flight Planning]** Fixes CAS flights not having landing waypoints.
* **[Squadrons]** Fixed the livery for the VF-33 F-14A squadron.
* **[UI]** Fixed an issue where manual submit of mission results did not end the mission correctly.

# 6.0.0

Saves from 5.x are not compatible with 6.0.

## Features/Improvements

* **[Engine]** Support for DCS 2.8.0.33006.
* **[Factions]** Updated the Faction file structure. Older custom faction files will not work correctly and have to be updated to the new structure.
* **[Flight Planning]** Added preset formations for different flight types at hold, join, ingress, and split waypoints. Air to Air flights will tend toward line-abreast and spread-four formations. Air to ground flights will tend towards trail formation.
* **[Flight Planning]** Added the ability to plan tankers for recovery on package flights. This mission type will not be planned automatically.
* **[Flight Planning]** Air to Ground flights now have ECM enabled on lock at the join point, and SEAD/DEAD also have ECM enabled on detection and lock at ingress.
* **[Flight Planning]** AWACS flightplan changed from orbit to a racetrack to reduce data link disconnects which were caused by blind spots as a result of the bank angle. 
* **[Flight Planning]** Added a new helo mission type: AirAssault which can be used to load and transport infantry troops from a pickup zone or a carrier to an enemy CP to capture it.
* **[Flight Planning]** Improved the Airlift mission type so that it now can be enforced within the unit transfer dialog and implemented CTLD support. This allows user to spawn sling loadable crates at the pickup location and fly transport flights.
* **[Mission Generation]** Added an option to fast-forward mission generation until the point of first contact (WIP).
* **[Mission Generation]** Added performance option to not cull IADS when culling would affect how mission is played at target area.
* **[Mission Generation]** Reworked the ground object generation which now uses a new layout system
* **[Mission Generation]** Added information about the modulation (AM/FM) of the assigned frequencies to the kneeboard and assign AM modulation instead of FM for JTAC.
* **[Mission Generation]** Added ice halos.
* **[Mission Generation]** Adjusted wind speeds. Wind speeds at high altitude are generally higher now.
* **[Mission Generation]** Added turbulence. Higher in Summer and Winter, also higher at day time than at nighttime.
* **[Modding]** Updated UH-60L mod version support to 1.3.1
* **[Modding]** Updated the High Digit SAMs implementation and added the HQ-2 as well as the upgraded SA-2 and SA-3 Launchers from the mod. Threat range circles will now also be displayed correctly.
* **[Modding]** Theater information such as climate properties is now moddable.
* **[Modding]** Allow campaign designers to define default values for the economy settings (starting budget and multiplier).
* **[Modding]** Campaigns can now optionally define their start time by including a time in the `recommended_start_date` field. There is not currently a way to override the start time in the UI.
* **[Plugins]** Allow full support of the SkynetIADS plugin with all advanced features (connection nodes, power sources, command centers) if campaign supports it.
* **[Plugins]** Added support for the CTLD script by ciribob with many possible customization options and updated the JTAC Autolase to the CTLD included script.
* **[UI]** Added options to the loadout editor for setting properties such as HMD choice.
* **[UI]** Added separate images for the different carrier types.
* **[UI]** Add Accept/Reset buttons to Air Wing Configurator screen.

## Fixes

* **[Engine]** Fixed issue that prevented some weapon types like torpedoes from being recognized.
* **[Flight Planning]** Fixed a miscalculation of waypoint TOTs that would require time travel.
* **[Loadouts]** Improved the range of the F-16 CAS loadout by adding bags.
* **[Mission Generation]** AAA ground units now spawn correctly at the frontline
* **[Mission Generation]** Fixed SA-13 incorrectly created as SA-8 Loading Unit which will not be spawned in the generated mission.
* **[Mission Generation]** Fixed adding additional mission types for a squadron causing error messages when the mission type is not supported by the aircraft type by default
* **[Mission Generation]** Fixed an issue where SEAD/DEAD/BAI flights fired all missiles / bombs against a single unit in a group instead of targeting the whole group.
* **[Mission Generation]** Fixed an issue which generated the helipads at FARPs incorrectly and placed the helicopters within each other.
* **[Mission Generation]** Fixed an issue with SEAD missions flown by the AI when using the Skynet Plugin and anti-radiation missiles (ARM). The AI now correctly engages the SAM when it comes alive instead of diving into it.
* **[Mission Generation]** Fixed generation issue that would cause AI helicopters to get stuck after taking off from a FARP.
* **[Mission Generation]** Fixed mission scripting error caused by control points with apostrophes in their names, such as Tha'lah.
* **[Modding]** Campaigns that used quad zones for scenery targets will no longer load. Only circular zones were ever supported, but an implementation quirk allowed them to load in a way that would misbehave. A "No white triggerzones found" message during campaign generation is the sign of a broken campaign.
* **[Modding]** Loadouts with invalid weapons (typically new DCS weapons not yet available in Liberation) will be ignored rather than causing an error.
* **[Squadrons]** Fixed issue in air wing configuration that would allow squadrons to be created with no home base if no base was available.
* **[Squadrons]** Helicopter squadrons can no longer be assigned to FOBs that are not FARPs.
* **[UI]** Add vanilla theme weather and time of day icons
* **[UI]** Disable player slots for non-flyable aircraft.
* **[UI]** Fixed and issue where the liberation main exe was still running after application close.

# 5.2.0

Saves from 5.1.0 are compatible with 5.2.0

## Features/Improvements

* **[Engine]** Support for DCS 2.7.11.21408, including the new Apache AH-64D and the Syria map extension
* **[Mission Generation]** Improved FARP Helipad handling and creation (now includes windsocks)
* **[Modding]** Add UH-60L mod support
* **[Modding]** Updated Community A-4E-C mod version support to 2.0.0 release. Version 1.4.2 is no longer compatible, unless the mod default loadouts are deleted/modified.
* **[Modding]** Updated JAS-39-C mod support for v1.8.0-beta
* **[Campaign]** Peace Spring, Vectron's Claw, Vegas Nerve, Scenic Route 2 campaign update
* **[Campaign]** Added Tripoint Hostility campaign by Fuzzle
* **[Campaign]** Add 3 new campaigns from Sith1144

## Fixes

* **[Mission Generation]** Fixed incorrect SA-5 and NASAMS threat range when TR destroyed. It will not count as threat anymore when the TR is dead.
* **[Mission Generation]** Fixed "Max Threat Range" error
* **[Mission Generation]** Fix unculled zones not updating when needed
* **[Mission Planner]** Now allows squadron transfers to control points where the number of free slots matches exactly the expected size of the transferring squadron next turn.
* **[Data]** Removed Fw 190 A-8 and D-9 from Germany 1940 and 1942 faction list for historical accuracy.
* **[Data]** Updated Loadouts for Tornado GR4, F-15E and F-16C
* **[Data]** Corrected some unit data
* **[UI]** Fixed various UI issues (for example Scaling and HighDPI)
* **[UI]** Typhoon GR4 and IDS images

# 5.1.0

Saves from 5.0.0 are compatible with 5.1.0

## Features/Improvements

* **[Engine]** Support for DCS 2.7.9.17830 and newer, including the HTS and ECM pod.
* **[Campaign]** Add option to manually add and remove squadrons and different aircraft type in the new game wizard / air wing configuration dialog.
* **[Mission Generation]** Add Option to enforce the Easy Communication setting for the mission
* **[Mission Generation]** Add Option to select between only night missions, day missions or any time (default).
* **[Modding]** Add F-104 mod support

## Fixes

* **[Campaign]** Fixed some minor issues in campaigns which generated error messages in the log.
* **[Campaign]** Changed the way how map object / scenery kills where tracked. This fixes issues with kill recognition after map updates from ED which change the object ids and therefore prevent correct kill recognition.
* **[Mission Generation]** Fixed incorrect radio specification for the AN/ARC-222.
* **[Mission Generation]** Fixed mission scripting error when using a dedicated server.
* **[Mission Generation]** Fixed an issue where empty convoys lead to an index error when a point capture made a pending transfer of units not completable anymore.
* **[Mission Generation]** Corrected Viggen FR22 & FR24 preset channels for the DCS 2.7.9 update
* **[Mission Generation]** Fixed the SA-5 Generator to use the P-19 FlatFace SR as a Fallback radar if the faction does not have access to the TinShield SR.
* **[UI]** Enable / Disable the settings, save and stats actions if no game is loaded to prevent an error as these functions can only be used on a valid game.
* **[UI]** Added missing icons for Tornado GR4, and Tornado IDS.

# 5.0.0

Saves from 4.x are not compatible with 5.0.

## Features/Improvements

* **[Campaign]** Weather! Theaters now experience weather that is more realistic for the region and its current season. For example, Persian Gulf will have very hot, sunny summers and Marianas will experience lots of rain during fall. These changes affect pressure, temperature, clouds and precipitation. Additionally, temperature will drop during the night, by an amount that is somewhat realistic for the region.
* **[Campaign]** Weapon data such as fallbacks and introduction years is now moddable. Due to the new architecture to support this, the old data was not automatically migrated.
* **[Campaign]** Era-restricted loadouts will now skip LGBs when no TGP is available in the loadout. This only applies to default loadouts; buddy-lasing can be coordinated with custom loadouts.
* **[Campaign]** FOBs control point can have FARP/helipad slot and host helicopters. To enable this feature on a FOB, add "Invisible FARP" statics objects near the FOB location in the campaign definition file.
* **[Campaign]** Squadrons now have a home base and will not operate out of other bases. See https://github.com/dcs-liberation/dcs_liberation/issues/1145 for status.
* **[Campaign]** Aircraft now belong to squadrons rather than bases to support squadron location transfers.
* **[Campaign]** Skipped turns are no longer counted as defeats on front lines.
* **[Campaign AI]** Overhauled campaign AI target prioritization.
* **[Campaign AI]** Player front line stances can now be automated. Improved stance selection for AI.
* **[Campaign AI]** Reworked layout of hold, join, split, and ingress points. Should result in much shorter flight plans in general while still maintaining safe join/split/hold points.
* **[Campaign AI]** Auto-planning mission range limits are now specified per-aircraft. On average this means that longer range missions will now be plannable. The limit only accounts for the direct distance to the target, not the path taken.
* **[Campaign AI]** Transport aircraft will now be bought only if necessary at control points which can produce ground units and are capable to operate transport aircraft.
* **[Campaign AI]** Aircraft will now only be automatically purchased or assigned at appropriate bases. Naval aircraft will default to only operating from carriers, Harriers will default to LHAs and shore bases, helicopters will operate from anywhere. This can be customized per-squadron.
* **[Engine]** Support for DCS 2.7.7.14727 and newer, including support for F-16 CBU-105s, SA-5s, and the Forrestal.
* **[Kneeboard]** Minimum required fuel estimates have been added to the kneeboard for aircraft with supporting data (currently only the Hornet and Viper).
* **[Kneeboard]** QNH (pressure MSL) and temperature have been added to the kneeboard.
* **[Mission Generation]** EWRs are now also headed towards the center of the conflict
* **[Mission Generation]** FACs can now use FC3 compatible laser codes. Note that this setting is global, not per FAC.
* **[Modding]** Can now install custom campaigns to <DCS saved games>/Liberation/Campaigns instead of the Liberation install directory.
* **[Modding]** Campaigns can now define a default start date.
* **[Modding]** Campaigns now specify the squadrons that are present in the campaign, their roles, and their starting bases. Players can customize this at game start but the campaign will choose the defaults.
* **[New Game Wizard]** Can now customize the player's air wing before campaign start to disable, relocate, or rename squadrons.
* **[Plugins]** Updated SkynetIADS to 2.4.0 (adds SA-5 support).
* **[UI]** Sell Button for aircraft will be disabled if there are no units available to be sold or all are already assigned to a mission
* **[UI]** Enemy aircraft inventory now viewable in the air wing menu.

## Fixes

* **[Campaign]** Naval control points will no longer claim ground objectives during campaign generation and prevent them from spawning.
* **[Campaign]** Units aboard sunk cargo ships will now have their losses tracked properly.
* **[Mission Generation]** Mission results and other files will now be opened with enforced utf-8 encoding to prevent an issue where destroyed ground units were untracked because of special characters in their names.
* **[Mission Generation]** Fixed generation of landing waypoints so that the AI obeys them.
* **[Mission Generation]** AI carrier aircraft with a start time of T+0 will now start at T+1s to avoid traffic jams.
* **[Mission Generation]** Fixed cases of unused aircraft not being spawned at airfields as soon as any airport filled up.
* **[Mission Generation]** Fixed cases with multiple client flights of the same airframe all received the same preset channels.
* **[Mission Generation]** F-14A is now generated with stored alignment.
* **[Mission Generation]** Su-33s set to cold or warm start on the Kuznetsov will always be generated as runway starts to avoid the AI getting stuck.
* **[Mission Generation]** Fixed AI not receiving anti-ship tasks against carriers and LHAs.
* **[Mods]** Fixed broken A-4 support causing no weapons to be available.
* **[UI]** Selling of Units is now visible again in the UI dialog and shows the correct amount of sold units
* **[UI]** Fixed bug where an incompatible campaign could be generated if no action is taken on the campaign selection screen.

# 4.1.1

Saves from 4.1.0 are compatible with 4.1.1.

## Fixes

* **[Campaign]** Fixed broken support for Mariana Islands map.
* **[Mission Generation]** Fix SAM sites pointing towards the center of the conflict.
* **[Flight Planning]** No longer using Su-34 for CAP missions.

# 4.1.0

Saves from 4.0.0 are compatible with 4.1.0.

## Features/Improvements

* **[Campaign]** Air defense sites now generate a fixed number of launchers per type.
* **[Campaign]** Added support for Mariana Islands map.
* **[Campaign AI]** Adjustments to aircraft selection priorities for most mission types.
* **[Engine]** Support for DCS 2.7.4.9632 and newer, including the Marianas map, F-16 JSOWs, NASAMS, and Tin Shield EWR.
* **[Flight Planning]** CAP patrol altitudes are now set per-aircraft. By default the altitude will be set based on the aircraft's maximum speed.
* **[Flight Planning]** CAP patrol speeds are now set per-aircraft to be more suitable/sensible. By default the speed will be set based on the aircraft's maximum speed.
* **[Mission Generation]** Improvements for better support of the Skynet Plugin and long range SAMs are now acting as EWR
* **[Mission Generation]** SAM sites are now headed towards the center of the conflict
* **[Mods]** Support for latest version of Gripen mod. In-progress campaigns may need to re-plan Gripen flights to pick up updated loadouts.
* **[Plugins]** Increased time JTAC Autolase messages stay visible on the UI.
* **[Plugins]** Updated SkynetIADS to 2.2.0 (adds NASAMS support).  
* **[UI]** Added ability to take notes and have those notes appear as a kneeboard page.
* **[UI]** Hovering over the weather information now dispalys the cloud base (meters and feet).
* **[UI]** Google search link added to unit information when there is no information provided.
* **[UI]** Control point name displayed with ground object group name on map.
* **[UI]** Buy or Replace will now show the correct price for generated ground objects like sams.
* **[UI]** Improved logging for frontline movement to be more descriptive about what happened and why.
* **[UI]** Brought ruler map module into source, which should fix file integrity issues with the module.

## Fixes

* **[Campaign]** Fixed the Silkworm generator to include launchers and not all radars.
* **[Data]** Fixed Introduction dates for targeting pods (ATFLIR and LITENING were both a few years too early).
* **[Data]** Removed SA-10 from Syria 2011 faction.
* **[Economy]** EWRs can now be bought and sold for the correct price and can no longer be used to generate money
* **[Flight Planning]** Helicopters are now correctly identified, and will fly ingress/CAS/BAI/egress and similar at low altitude.
* **[Flight Planning]** Fixed potential issue with angles > 360° or < 0° being generated when summing two angles.
* **[Mission Generation]** The lua data for other plugins is now generated correctly
* **[Mission Generation]** Fixed problem with opfor planning missions against sold ground objects like SAMs
* **[Mission Generation]** The legacy always-available tanker option no longer prevents mission creation.
* **[Mission Generation]** Prevent the creation of a transfer order with 0 units for a rare situtation when a point was captured.
* **[Mission Generation]** Planned transfers which will be impossible after a base capture will no longer prevent the mission result submit.
* **[Mission Generation]** Fix occasional KeyError preventing mission generation when all units of the same type in a convoy were killed.
* **[Mission Generation]** Fix for AAA Flak generator using Opel Blitz preventing the mission from being generated because duplicate unit names were used.
* **[Mission Generation]** Fixed a potential bug with laser code generation where it would generate invalid codes.  
* **[UI]** Statistics window tick marks are now always integers.
* **[UI]** Statistics window now shows the correct info for the turn
* **[UI]** Toggling custom loadout for an aircraft with no preset loadouts no longer breaks the flight.

# 4.0.0

Saves from 3.x are not compatible with 4.0.

## Features/Improvements

* **[Engine]** Support for DCS 2.7.2.7910.1 and newer, including Cyprus, F-16 JDAMs, and the Hind.
* **[Campaign]** Squadrons now (optionally, off by default) have a maximum size and killed pilots replenish at a limited rate.
* **[Campaign]** Added an option to disable levelling up of AI pilots.
* **[Campaign]** Added Russian Intervention 2015 campaign on Syria, for a small and somewhat realistic Russian COIN scenario.
* **[Campaign]** Added Operation Atilla campaign on Syria, for a reasonably large invasion of Cyprus scenario.
* **[Campaign AI]** AI will plan Tanker flights.
* **[Campaign AI]** Removed max distance for AEW&C auto planning.
* **[Economy]** Adjusted prices for aircraft to balance out some price inconsistencies.
* **[Factions]** Added more tankers to factions.
* **[Flight Planner]** Added ability to plan Tankers.
* **[Modding]** Campaign format version is now 7.0 to account for DCS map changes that made scenery strike targets incompatible with existing campaigns.
* **[Mods]** Added support for the Gripen mod.
* **[Mods]** Removes MB-339PAN support, as the mod is now deprecated and no longer works with DCS 2.7+.
* **[Mission Generation]** Added support for "Neutral Dot" label options.
* **[New Game Wizard]** Mods are now selected via checkboxes in the new game wizard, not as separate factions.
* **[UI]** Ctrl click and shift click now buy or sell 5 or 10 units respectively.
* **[UI]** Multiple waypoints can now be deleted simultaneously if multiple waypoints are selected.
* **[UI]** Carriers and LHAs now match the colour of airfields, and their destination icons are translucent.
* **[UI]** Updated intel box text for first turn.
* **[UI]** Base Capture Cheat is now usable at all bases and can also be used to transfer player-owned bases to OPFOR.
* **[UI]** Pass Turn button is relabled as "Begin Campaign" on Turn 0.  
* **[UI]** Added a ruler to the map.
* **[UI]** Liberation now saves games to `<DCS user directory>/Liberation/Saves` by default to declutter the main directory.

## Fixes

* **[Campaign AI]** Fix procurement for factions that lack some unit types.
* **[Campaign AI]** Fix auto purchase of aircraft for factions that have no transport aircraft.
* **[Campaign AI]** Fix refunding of pending aircraft purchases when a side has no factory available.  
* **[Mission Generation]** Fixed problem with mission load when control point name contained an apostrophe.
* **[Mission Generation]** Fixed EWR group names so they contribute to Skynet again.
* **[Mission Generation]** Fixed duplicate name error when generating convoys and cargo ships when creating manual transfers after loading a game.
* **[Mission Generation]** Fixed empty convoys not being disbanded when all units are killed/removed.
* **[Mission Generation]** Fixed player losing frontline progress when skipping from turn 0 to turn 1.
* **[Mission Generation]** Fixed issue where frontline would only search to the right for valid locations.
* **[UI]** Made non-interactive map elements less obstructive.
* **[UI]** Added support for Neutral Dot difficulty label
* **[UI]** Clear skies at night no longer described as "Sunny" by the weather widget.
* **[UI]** Removed ability to buy (useless) ground units at carriers and LHAs.
* **[UI]** Fixed enable/disable of buy/sell buttons.
* **[UI]** EWRs now appear in the custom waypoint list.

# 3.0.0

Saves from 2.5 are not compatible with 3.0.

## Features/Improvements

* **[Campaign]** Ground units can now be transferred by road, airlift, and cargo ship. See https://github.com/dcs-liberation/dcs_liberation/wiki/Unit-Transfers for more information.
* **[Campaign]** Ground units can no longer be sold. To move units to a new location, transfer them.
* **[Campaign]** Ground units must now be recruited at a base with a factory and transferred to their destination. When buying units in the UI, the purchase will automatically be fulfilled at the closest factory, and a transfer will be created on the next turn.
* **[Campaign]** Non-control point FOBs will no longer spawn.
* **[Campaign]** Added squadrons and pilots. See https://github.com/dcs-liberation/dcs_liberation/wiki/Squadrons-and-pilots for more information.
* **[Campaign]** Capturing a base now depopulates all of its attached objectives with units: air defenses, EWRs, ships, armor groups, etc. Buildings are captured.
* **[Campaign]** Ammunition Depots determine how many ground units can be deployed on the frontline by a control point.
* **[Campaign AI]** AI now considers Ju-88s for CAS, strike, and DEAD missions.
* **[Campaign AI]** AI planned AEW&C missions will now be scheduled ASAP.
* **[Campaign AI]** AI now considers the range to the SAM's threat zone rather than the range to the SAM itself when determining target priorities.
* **[Campaign AI]** Auto purchase of ground units will now maintain unit composition instead of buying randomly. The unit composition is predefined.
* **[Campaign AI]** Auto purchase will aim to purchase enough ground units to support the frontline, plus 30% reserve units.
* **[Campaign AI]** Auto purchase will now adjust its air/ground balance to favor whichever is under-funded.
* **[Flight Planner]** Desired mission length is now configurable (defaults to 60 minutes). A BARCAP will be planned every 30 minutes. Other packages will simply have their takeoffs spread out or compressed such that the last flight will take off around the mission end time.
* **[Flight Planner]** Flight plans now include bullseye waypoints.
* **[Flight Planner]** Differentiated SEAD and SEAD escort. SEAD is tasked with suppressing the package target, SEAD escort is tasked with protecting the package from all SAMs along its route.
* **[Flight Planner]** Planned airspeed increased to 0.85 mach for supersonic airframes and 85% of max speed for subsonic.
* **[Flight Planner]** Taxi time estimation for airfields increased from 5 minutes to 8 minutes.
* **[Flight Planner]** Reduce expected error margin for flight plans from 10% to 5%.
* **[Flight Planner]** SEAD flights are scheduled one minute ahead of the package's TOT so that they can suppress the site ahead of the strike.
* **[Flight Planner]** Automatic ATO generation for the player's coalition can now be disabled in the settings.
* **[Payloads]** AI flights for most air to ground mission types (CAS excluded) will have their guns emptied to prevent strafing fully armed and operational battle stations. Gun-reliant airframes like A-10s and warbirds will keep their bullets.
* **[Kneeboard]** ATC table overflow alleviated by wrapping long airfield names and splitting ATC frequency and channel into separate rows.
* **[UI]** Overhauled the map implementation. Now uses satellite imagery instead of low res map images. Display options have moved from the toolbar to panels in the map.
* **[UI]** Campaigns generated for an older or newer version of the game will now be marked as incompatible. They can still be played, but bugs may be present.
* **[UI]** DCS loadouts are now selectable in the loadout setup menu.
* **[UI]** Added global aircraft inventory view under Air Wing dialog.
* **[UI]** Base menu now shows information about ground unit deployment limits.
* **[Modding]** Campaigns now choose locations for factories to spawn.
* **[Modding]** Campaigns now choose locations for ammunition depots to spawn.
* **[Modding]** Campaigns now use map structures as strike targets.
* **[Modding]** Campaigns may now set *any* objective type to be a required spawn rather than random chance. Support for random objective generation was removed.
* **[Modding]** Campaigns may now place AAA objectives.
* **[Modding]** Can now install custom factions to <DCS saved games>/Liberation/Factions instead of the Liberation install directory.
* **[Performance Settings]** Added a settings to lower the number of smoke effects generated on frontlines. Lowered default settings for frontline smoke generators, so less smoke should be generated by default.
* **[Configuration]** Liberation preferences (DCS install and save game location) are now saved to `%LOCALAPPDATA%/DCSLiberation` to prevent needing to reconfigure each new install.
* **[Skynet]** Updated to 2.1.0.

## Fixes

* **[Campaign AI]** Fix purchase of aircraft by priority (the faction's list was being used as the priority list rather than the game's).
* **[Campaign AI]** Fixed bug causing AI to over-purchase cheap aircraft.
* **[Campaign AI]** Auto planner will no longer attempt to plan missions for which the faction has no compatible aircraft.
* **[Campaign AI]** Stop purchasing aircraft after the first unaffordable package to attempt to complete more packages rather than filling airfields with cheap escorts that will never be used.
* **[Campaign]** Fixed bug where offshore strike locations were being used to spawn ship objectives.
* **[Campaign]** EWR sites are now purchasable.
* **[Flight Planner]** AI strike flight plans now include the correct target actions for building groups.
* **[Flight Planner]** AI BAI/DEAD/SEAD flights now have tasks to attack all groups at the target location, not just the primary group (for multi-group SAM sites).
* **[Flight Planner]** Fixed some contexts where damaged runways would be used. Destroying a carrier will no longer break the game.

# 2.5.1

## Features/Improvements

* **[UI]** Engagement ranges are now displayed by default.
* **[UI]** Engagement range display generalized to work for all patrolling flight plans (BARCAP, TARCAP, and CAS).
* **[Flight Planner]** Front lines no longer project threat zones to avoid pushing BARCAPs back so much. TARCAPs will be forcibly planned but strike packages will not route around front lines even if it is reasonable to do so.

## Fixes

* **[Campaigns]** EWRs associated with a base will now only be generated near the base.
* **[Flight Planner]** Fixed error when generating AEW&C flight plans in campaigns with no front lines.

# 2.5.0

Saves from 2.4 are not compatible with 2.5.

## Features/Improvements

* **[Engine]** DCS 2.7 Support
* **[UI]** Improved FOB menu, added a custom banner, and do not display aircraft recruitment menu
* **[Flight Planner]** Added AEW&C missions. (by siKruger)
* **[Kneeboard]** Added dark kneeboard option (by GvonH)
* **[Campaigns]** Multiple EWR sites may now be generated, and EWR sites may be generated outside bases (by SnappyComebacks)
* **[Mission Generation]** Cloudy and rainy (but not thunderstorm) weather will use the cloud presets from DCS 2.7.
* **[Plugins]** Added LotATC export plugin (by drsoran)
* **[Plugins]** Added Splash Damage Plugin (by Wheelijoe)
* **[Loadouts]** Replaced Litening with ATFLIR for all default F/A-18C loadouts.

## Fixes

* **[Flight Planner]** Front lines now project threat zones, so TARCAP/escorts will not be pruned for flights near the front. Packages may also route around the front line when practical.
* **[Flight Planner]** Fixed error when planning BAI at SAMs with dead subgroups.
* **[Flight Planner]** Mig-19 was not allowed for CAS roles fixed
* **[Flight Planner]** Increased size of navigation planning area to avoid plannign failures with distant waypoints.
* **[Flight Planner]** Fixed UI refresh when unchecking the "default loadout" box in the loadout editor.
* **[Objective names]** Fixed typos in objective name : ARMADILLLO -> ARMADILLO (by SnappyComebacks)
* **[Payloads]** F-86 Sabre was missing a custom payload
* **[Payloads]** Added GAR-8 period restrictions (by Mustang-25)
* **[Campaign]** Date now progresses.
* **[Campaign]** Added game over message when a coalition runs out of functioning airbases.
* **[Mission Generation]** Fixed "invalid face handle" error in kneeboard generation that occurred on some machines.

## Regressions

* **[Mod Support]** Stopped support for 2.5.5 Rafale Mode, and removed factions that were using it
* **[Mod Support]** Su-57 mod support might be out of date

# 2.4.3

## Features/Improvements

* **[New Game Wizard]** Added the possibility to setup custom start date

## Fixes

* **[Mods]** Updated C-130J mod data to version 6.4
* **[Mods]** Updated F-22A mod to latest version

# 2.4.2

## Features/Improvements

* **[Factions]** Introduction dates and fallback weapons added for US, Russian, UK, and French weapons. Huge thanks to @TheCandianVendingMachine for the massive amount of data entry!
* **[Campaigns]** Added 1995 start dates.

## Fixes

* **[Economy]** Pending ground unit purchases will also be transferred when a connected base is captured.
* **[UI]** Fixed rounding of budget in recruitment menu.

# 2.4.1

## Fixes

* **[Units]** Fixed syntax error with the SH-60B payload file.
* **[Culling]** Missile sites generate reasonably sized non-cull zones rather than 100km ones.
* **[UI]** Budget display is also now rounded to 2 decimal places.
* **[UI]** Fixed some areas where the old, non-pretty name was displayed to users.

# 2.4.0

Saves from 2.3 are not compatible with 2.4.

## Highlights

* Improved flight plan generation to avoid loitering in or traveling through threatened areas when practical.
* Improved AI aircraft purchasing behavior.
* Era-restricted weapons (work in progress).
* Tons of UI polish.
* Rebalanced economy to keep opfor competitive over the course of the game.

## Features/Improvements

* **[Flight Planner]** Air-to-air and SEAD escorts will no longer be automatically planned for packages that are not in range of threats.
* **[Flight Planner]** Non-custom flight plans will now navigate around threat areas en route to the target area when practical.
* **[Flight Planner]** Flight plans along front lines now ensure that the race track start is closer to the departure airfield than the race track end.
* **[Campaign AI]** Auto-purchase now prefers airfields that are not within range of the enemy.
* **[Campaign AI]** Auto-purchase now prefers the best aircraft for the task, but will attempt to maintain some variety.
* **[Campaign AI]** Opfor now sells off odd aircraft since they're unlikely to be used.
* **[Campaign AI]** Multiple rounds of CAP will be planned (roughly 90 minutes of coverage). Default starting budget has increased to account for the increased need for aircraft.
* **[Mission Generator]** Multiple groups are created for complex SAM sites (SAMs with additional point defense or SHORADS), improving Skynet behavior.
* **[Mission Generator]** Default start type can now be chosen in the settings. This replaces the non-functional "AI Parking Start" option. **Selecting any type other than cold will break OCA/Aircraft missions.**
* **[Cheat Menu]** Added ability to toggle base capture and frontline advance/retreat cheats.
* **[Skynet]** Updated to 2.0.1.
* **[Skynet]** Point defenses are now configured to remain on to protect the site they accompany.
* **[Hercules]** Updated the Hercules Cargo list file.
* **[Balance]** Opfor now gains income using the same rules as the player, significantly increasing their income relative to the player for most campaigns.
* **[Balance]** Units now retreat from captured bases when able. Units with no retreat path will be captured and sold.
* **[Economy]** FOBs generate only $10M per turn (previously $20M like airbases).
* **[Economy]** Carriers and off-map spawns generate no income (previously $20M like airbases).
* **[Economy]** Sales of aircraft and ground vehicles can now be cancelled before the next turn begins.
* **[UI]** Multi-SAM objectives now show threat and detection rings per group.
* **[UI]** New icon for AA sites with no active threat.
* **[UI]** Unit names are now prettier and more accurate, and can now be set per-country for added historical flavour.
* **[UI]** Default loadout is now shown for flights with no custom loadout selected.
* **[UI]** Aircraft for a new flight are now only selectable if they match the task type for that flight.
* **[UI]** WIP - There is now a unit info button for each unit in the recruitment list, that should help newer players learn what each unit does.
* **[UI]** Docs for time-on-target and creating new theaters/factions/loadouts are now linked in the UI at the appropriate places.
* **[UI]** ASAP is now a checkbox rather than a button. Enabling this will disable the TOT selector but changes to the package structure will automatically re-ASAP the package.
* **[UI]** Arrival airfield is now shown in the flight list if it differs from the departure airfield.
* **[UI]** Start type can now be selected when creating a flight.
* **[UI]** Arrival and divert airfields can be edited after the flight is created.
* **[Factions]** Added option for date-based loadout restriction. Active radar homing missiles are handled, patches welcome for the other thousand weapons.
* **[Factions]** Added Poland 2010 faction.
* **[Factions]** Added Greece 2005 faction.
* **[Factions]** Added Iran 1988 faction.
* **[Units]** Support for E-2 Hawkeye, SH-60B Seahawk, S-3B Viking (thanks to awinterquest) and SpGH Dana - these are now being used by appropriate factions.
* **[Culling]** Missile sites are no longer culled.
* **[Campaigns]** Added campaign "Black Sea Lite" by Starfire
* **[Campaigns]** Added campaign "Exercise Vegas Nerve" by Starfire 
* **[New game Wizard]** The theater page is now the first page of the campaign wizard, recommended factions will be selected automatically on the faction selection page
* **[New game Wizard]** Added information text about the selected campaign performance.
* **[Mod Support]** Added support for High Digit SAMs mod 1.4.0
* **[Mod Support]** Added SAMs sites generator : KS19Generator, SA10BGenerator, SA12Generator, SA17Generator, SA20Generator, SA20BGenerator, SA23Generator    

## Fixes

* **[Hercules]** Updated the default Hercules radio frequency.
* **[Economy]** Pending unit orders at captured bases will be refunded.
* **[UI]** Carrier group SAM threat rings now move with the carrier.
* **[UI]** Base intel menu no longer compresses text, and is now scrollable.
* **[UI]** Edit Flight window is now dynamically sized to adapt to the width of waypoint names, so they no longer get truncated.
* **[UI]** Budget income display is now rounded to 2 decimal places.
* **[UI]** Fixed incorrect income per turn displayed for strike target tooltip.
* **[Factions]** USA with C-130 faction now links to the required mod.
* **[Campaign]** Fixed issue where destroyed buildings would sometimes not count as destroyed and thus respawn.
* **[Campaign]** Fixed issue where destroyed runways were not registered.
* **[Units]** J-11A is no longer spawned with empty loadout.
* **[Units]** F-14B is no longer spawned with empty loadout for fighter sweep tasks.
* **[Units]** Pyotr Velikiy cruiser has been removed for now as it's nearly unkillable.
* **[Units]** Submarines have been removed for now as they aren't wholly functional.
* **[Units]** Fixed "FACTION ERROR : Unable to find OliverHazardPerryGroupGenerator in pydcs" error at startup.
* **[Mission Generator]** Fixed a bug where units set to Aggressive stance sometimes did not move.
* **[Mission Generator]** Flyover points for OCA/Aircraft missions are now generated correctly.
* **[Flight Planner]** Fixed not being able to create custom waypoints for buildings.
* **[Flight Planner]** Strike missions will no longer be automatically planned against SAMs.
* **[Flight Planner]** Strike missions will no longer be automatically planned against FOB structures.

# 2.3.4

## Fixes:
[Mission Generator] Mission generator would crash when generating fire missions for destroyed SCUD sites - fixed

# 2.3.3

## Features/Improvements
* **[Campaigns]** Reworked Golan Heights campaign on Syria, (Added FOB and preset locations for SAMS)
* **[Campaigns]** Added a lite version of the Golan Heights campaign
* **[Campaigns]** Reworked Syrian Civil War campaign (Added FOB and preset locations for SAMS)
* **[Campaigns]** Reworked Emirates campaign
* **[Campaigns]** AA units added to frontlines and updated all factions to include some frontline AA units.
* **[Mission Generator]** Infantry will only be generated for APC and IFV groups
* **[Mission Generator]** Infantry squads size is not randomized anymore
* **[Mission Generator]** Infantry squads can have a mortar. 
* **[Mission Generator]** SCUD missiles sites will now fire on enemy controls points in range when possible
* **[Factions]** Updated Nato Desert Storm to include F-14A
* **[Factions]** Updated Iraq 1991 factions to include Zsu-57 and Mig-29A
* **[Factions]** Germany 1944, added Stug III and Stug IV
* **[Factions]** Added factions Insurgents (Hard) with better and more weapons
* **[Plugins]** [The EWRS plugin](https://github.com/Bob7heBuilder/EWRS) is now included.
* **[UI]** Added enemy intelligence summary and details window.

## Fixes:
* **[Factions]** AI would never buy artillery units for the frontline - fixed
* **[Factions]** Removed the F-111 unit from the NATO desert storm faction. (Recruiting it would cause crashes in DCS, since it is not a valid unit)
* **[Campaign]** Automatic redeployment of ground units would sometimes fail - fixed
* **[Mission Generator]** Artillery groups would retreat in the wrong direction - fixed
* **[Units]** Fixed SPG_Stryker_M1128_MGS not being in db
* **[UI]** Fixed and added many missing ground units icons
* **[UI]** Ship groups could be replaced by SAM sites in the UI, which would lead to broken mission being generated - fixed 
* **[New Game Wizard]** Removed the "mid game" campaign generator option which is currently broken
* **[Mission Generator]** Empty navy groups will no longer be generated
* **[Mission Generator]** Fixed BAI, SEAD, and DEAD flights ocassionally being assigned the wrong targets.
* **[Flight Planner]** Fixed not being able to plan packages against opfor carriers
* **[UI]** Repaired SAMs no longer show as dead.
* **[UI]** Fixed not being able to manage a disbanded site after disbanding and closing the base menu.

# 2.3.2

## Features/Improvements
* **[Units]** Support for newly added BTR-82A, T-72B3
* **[Units]** Added ZSU-57 AAA sites
* **[Culling]** BARCAP missions no longer create culling exclusion zones.
* **[Flight Planner]** Improved TOT planning. Negative start times no longer occur with TARCAPs and hold times no longer affect planning for flight plans without hold points.
* **[Factions]** Added Iraq 1991 faction (thanks again to Hawkmoon!)

## Fixes:
* **[Mission Generator]** Fix mission generation error when there are too many radio frequency to setup for the Mig-21
* **[Mission Generator]** Fix ground units not moving forward
* **[Mission Generator]** Fixed assigned radio channels overlapping with beacons.
* **[Flight Planner]** Fix creation of custom waypoints.
* **[Campaigns]** Fixed many cases of SAMs spawning on the runways/taxiways in Syria Full.

# 2.3.1

## Features/Improvements
* **[UX]** Added a warning message when the player is attempting to buy more planes at an already full airbase. 
* **[Campaigns]** Migrated Syria full map to new format. (Thanks to Hawkmoon)
* **[Faction]** Added NATO desert Storm faction (Thanks to Hawkmoon)

## Fixes:
* **[AI]** CAP flights will engage enemies again.
* **[Campaigns]** Fixed a missing path on the Caucasus Full Map campaign

# 2.3.0

## Features/Improvements
* **[Campaign Map]** Overhauled the campaign model
* **[Campaign Map]** Possible to add FOB as control points
* **[Campaign Map]** Added off-map spawn locations
* **[Campaign AI]** Overhauled AI recruiting behaviour
* **[Campaign AI]** Added AI procurement for Blue
* **[Campaign]** New Campaign: "Black Sea"
* **[Mission Planner]** Possible to move carrier and tarawa on the campaign map
* **[Mission Generator]** Infantry squads on frontline can have manpads
* **[Mission Generator]** Unused aircraft now spawned to allow for OCA strikes
* **[Mission Generator]** Opfor now obeys parking limits
* **[Mission Generator]** Support for Anubis C-130 Hercules mod
* **[Flight Planner]** Added fighter sweep missions.
* **[Flight Planner]** Added BAI missions.
* **[Flight Planner]** Added anti-ship missions.
* **[Flight Planner]** Differentiated BARCAP and TARCAP. TARCAP is now for hostile areas and will arrive before the package.
* **[Flight Planner]** Added OCA missions
* **[Flight Planner]** Added Alternate/divert airfields
* **[Culling]** Added possibility to include/exclude carriers from culling zones
* **[QOL]** On liberation startup, your latest save game is loaded automatically
* **[Units]** Reduced starting fuel load for C101
* **[UI]** Inform the user of the weather
* **[UI]** Added toolbar buttons to change map display settings
* **[Game]** Added new Economy options for adjusting income multipliers and starting budgets.

## Fixes :
* **[Map]** Missiles sites now have a proper icon and will not re-use the SAM sites icon
* **[Mission Generator]** Ground unit waypoints improperly set to "On Road" - fixed
* **[Mission Generator]** Target waypoints not at ground level - fixed
* **[Mission Generator]** Selected skill not applied to Helicopters - fixed
* **[Mission Generator]** Ground units do not always spawn - fixed
* **[Kneeboard]** Briefing waypoints off by one - fixed
* **[Game]** Destroyed buildings still granting budget - fixed

# 2.2.1

## Features/Improvements
* **[Factions]** Added factions : Georgia 2008, USN 1985, France 2005 Frenchpack by HerrTom
* **[Factions]** Added map Persian Gulf full by Plob
* **[Flight Planner]** Player flights with start delays under ten minutes will spawn immediately.
* **[UI]** Mission start screen now informs players about delayed flights.
* **[Units]** Added support for F-14A-135-GR
* **[Modding]** Possible to setup liveries overrides in factions definition files

## Fixes :
* **[Flight Planner]** Hold, join, and split points are planned cautiously near enemy airfields. Ascend/descend points are no longer planned.
* **[Flight Planner]** Custom waypoints are usable again. Not that in most cases custom flight plans will revert to the 2.1 flight planning behavior.
* **[Flight Planner]** Fixed UI bug that made it possible to create empty flights which would throw an error.
* **[Flight Planner]** Player flights from carriers will now be delayed correctly according to the player's settings.
* **[Misc]** Spitfire variant with clipped wings was not seen as flyable by DCS Liberation (hence could not be setup as client/player slot)
* **[Misc]** Updated Syria terrain parking slots database, the out-of-date database could end up generating aircraft in wrong slots (We are still experiencing issues with somes airbases, such as Khalkhalah though)

# 2.2.0

## Features/Improvements :
* **[Campaign Generator]** Added early warning radar generation
* **[Campaign Generator]** Added scud launcher sites
* **[Cheat Menu]** Added ability to capture base from mission planner
* **[Cheat Menu]** Added ability to show red ATO
* **[Factions]** Added WW2 factions that do not depend on WW2 asset pack
* **[Factions]** Cold War / Middle eastern factions will use Flak sites
* **[Flight Planner]** Flight planner overhaul, with package and TOT system
* **[Flight Planner]** Pick runways and ascent/descent based on headwind
* **[Map]** Added polygon debug mode display
* **[Map]** Highlight the selected flight path on the map
* **[Map]** Improved SAM display settings
* **[Map]** Improved flight plan display settings
* **[Map]** Caucasus and The Channel map use a new system to generate SAM and strike target location to reduce probability of targets generated in the middle of a forests
* **[Misc]** Flexible Dedicated Hosting Options for Mission Files via environment variables
* **[Moddability]** Custom campaigns can be designed through json files
* **[Moddability]** LUA plugins can now be injected into Liberation missions.
* **[Moddability]** Optional Skynet IADS lua plugin now included
* **[New Game]** Starting budget can be freely selected
* **[New Game]** Exanded information for faction and campaign selection in the new game wizard
* **[UI]** Add double and right click actions to many UI elements.
* **[UI]** Add polygon drawing mode for map background
* **[UI]** Added a warning if you press takeoff with no player enabled flights
* **[UI]** Packages and flights now visible in the main window sidebar
* **[Units/Factions]** Added bombers to some coalitions
* **[Units/Factions]** Added support for SU-57 mod by Cubanace
* **[Units]** Added Freya EWR sites to german WW2 factions
* **[Units]** Added support for many bombers (B-52H, B-1B, Tu-22, Tu-142)
* **[Units]** Added support for new P-47 variants

## Fixes :
* **[Campaign Generator]** Big airbases could end up without any airbase defense.
* **[Campaign generator]** Ship group and offshore buildings should not be generated on land anymore
* **[Flight Planner]** Fix waypoint alitudes for helicopters
* **[Flight Planner]** Fixed CAS aircraft wandering away from frontline
* **[Maps]** Incirlik airbase was missing exclusions zones, so SAMS could end up being generated on the runway
* **[Mission Generator]** Fixed player/client confusion when a flight had only one player slot.
* **[Radios]** Fix A-10C radio
* **[UI]** Many missing unit icons were added
* **[UI]** Missing TER weapons in custom payload now selectable.

# 2.1.5

## Features/Improvements :
* **[Units/Factions]** Enabled EPLRS for ground units that supports it (so they appear on A-10C II TAD and Helmet)

## Fixes :
* **[UI]** Fixed an issue that prevent saving after aborting a mission
* **[Mission Generator]** Fixed aircraft landing point type being wrong

# 2.1.4

## Fixes :
* **[UI]** Fixed an issue that prevented generating the mission (take off button no working) on old savegames.

## Features/Improvements :
* **[Units/Factions]** Added A-10C_2 to USA 2005 and Bluefor modern factions
* **[UI]** Limit number of aircraft that can be bought to the number of available parking slots.
* **[Mission Generator]** Use inline loading of the JSON.lua library, and save to either %LIBERATION_EXPORT_DIR%, or to DCS working directory

## Changes :
* **[Units/Factions]** Bluefor generic factions will now use the new "Combined Joint Task Forces Blue" country in the generated mission instead of "USA"

## Fixes :
* **[UI]** Fixed icon for Viggen
* **[UI]** Added icons for some ground units
* **[Misc]** Fixed issue with Chinese characters in pydcs preventing generating the mission. (Take Off button not working) (thanks to spark135246)
* **[Misc]** Fixed an error causing with ATC frequency preventing generating the mission. (Take Off button not working) (thanks to danalbert)

# 2.1.2

## Fixes :
* **[Mission Generator]** Fix mission generation issues with radio frequencies (Thanks to contributors davidp57 and danalbert)
* **[Mission Generator]** AI should now properly plan flights for Tornados

# 2.1.1

## Features/Improvements :
* **[Other]** Added an installer option (thanks to contributor parithon)
* **[Kneeboards]** Generate mission kneeboards for player flights. Kneeboards include
  airfield/carrier information (ATC frequencies, ILS, TACAN, and runway
  assignments), assigned radio channels, waypoint lists, and AWACS/JTAC/tanker
  information. (Thanks to contributor danalbert)
* **[Radios]** Allocate separate intra-flight channels for most aircraft to reduce global
  chatter. (Thanks to contributor danalbert)
* **[Radios]** Configure radio channel presets for most aircraft. Currently supported are:
  * AJS37
  * AV-8B
  * F-14B
  * F-16C
  * F/A-18C
  * JF-17
  * M-2000C (Thanks to contributor danalbert)
* **[Base Menu]** Added possibility to repair destroyed SAM and base defenses units for the player (Click on a SAM site to fix it)
* **[Base Menu]** Added possibility to buy/sell/replace SAM units
* **[Map]** Added recon images for buildings on strike targets, click on a Strike target to get detailled informations
* **[Units/Factions]** Added F-16C to USA 1990
* **[Units/Factions]** Added MQ-9 Reaper as CAS unit for USA 2005
* **[Units/Factions]** Added Mig-21, Mig-23, SA-342L to Syria 2011
* **[Cheat Menu]** Added buttons to remove money

## Fixed issues :
* **[UI/UX]** Spelling issues (Thanks to contributor steveveepee)
* **[Campaign Generator]** LHA was placed on land in Syrian Civil War campaign
* **[Campaign Generator]** Fixed inverted configuration for Syria full map
* **[Campaign Generator]** Syria "Inherent Resolve" campaign, added Incirlik Air Base
* **[Mission Generator]** AH-1W was not used by AI to generate CAS mission by default
* **[Mission Generator]** Fixed F-16C targeting pod not being added to payload
* **[Mission Generator]** AH-64A and AH-64D payloads fix. 
* **[Units/Factions]** China will use KJ-2000 as awacs instead of A-50

# 2.1.0

## Features/Improvements :

* **[Campaign Generator]** Added Syria map
* **[Campaign Generator]** Added 5 campaigns for the Syria map
* **[Campaign Generator]** Added 2 small scale campaign for Persian Gulf map
* **[Units/Factions]** Added factions for Syria map : Syria 2011, Arab Armies 1982, 1973, 1968, 1948, Israel 1982, 1973, 1948
* **[Base Menu]** Budget is visible in recruitment menu. (Thanks to Github contributor root0fall)
* **[Misc]** Added error message in mission when the state file can not be written
* **[Units/Factions]** China, Pakistan, UAE will now use the new WingLoong drone as JTAC instead of the MQ-9 Reaper
* **[Units/Factions]** Minor changes to Syria 2011 and Turkey 2005 factions
* **[UI]** Version number is shown in about dialog

## Fixed issues :

* **[Mission Generator]** Caucasus terrain improvement on exclusions zone (added forests between Vaziani and Beslan to exclusion zones)
* **[Mission Generator]** The first unit of every base defenses group could not be controlled with Combined Arms.
* **[Mission Generator]** Reduced generated helicopter altitude for CAS missions
* **[Mission Generator]** F-16C default CAS payload was asymmetric, fixed.
* **[Mission Generator]** AH-1W couldn't be bought, and added default payloads.
* **[UI/UX]** Fixed Mi-28N missing thumbnail
* **[UI/UX]** Fixed list of flights not refreshing when changing the mission departure (T+).

# 2.0.11

## Features/Improvements :

* **[Units/Factions]** Added Mig-31, Su-30, Mi-24V, Mi-28N to Russia 2010 faction.
* **[Units/Factions]** Added F-15E to USA 2005 and USA 1990 factions.
* **[Mission Generator]** Added a parameter to choose whether the JTACs should use smoke markers or not

## Fixed issues : 

* **[Units/Factions]** Fixed big performance issue in new release UI that occurred only when running the .exe
* **[Units/Factions]** Fixed mission generation not working with Libya faction
* **[Units/Factions]** Fixed OH-58D not being used by AI
* **[Units/Factions]** Typo in UK 1990 name (fixed by bwRavencl)
* **[Units/Factions]** Fixed Tanker Tacan channel not being the same as the briefing one. (Sorry)
* **[Mission Generator]** Neutral airbases services will now be disabled. (Not possible to refuel or re-arm there)
* **[Mission Generator]** AI will be configured to limit afterburner usage
* **[Mission Generator]** JTAC will not use laser codes above 1688 anymore
* **[Mission Generator]** JTAC units were misconfigured and would not be invisible/immortal. 
* **[Mission Generator]** Increased JTAC status message duration to 25s, so you have more time to enter coordinates;
* **[Mission Generator]** Destroyed units carcass will not appear on airfields to avoid having a destroyed vehicle blocking a runway or taxiway.


# 2.0.10

## Features/Improvements :
* **[Misc]** Now possible to save game in a different file, and to open DCS Liberation savegame files. (You are not restricted to a single save file anymore)
* **[UI/UX]** New dark UI Theme and default theme improvement by Deus
* **[UI/UX]** New "satellite" map backgrounds
* **[UX]** Base menu is opened with a single mouse click
* **[Units/Factions/Mods]** Added Community A-4E-C support for faction Bluefor Cold War
* **[Units/Factions/Mods]** Added MB-339PAN support for faction Bluefor Cold War  
* **[Units/Factions/Mods]** Added Rafale AI mod support
* **[Units/Factions/Mods]** Added faction "France Modded" with units from frenchpack v3.5 mod
* **[Units/Factions/Mods]** Added faction "Insurgent modded" with Insurgent units from frenchpack v3.5 mod (Toyota truck)
* **[Units/Factions/Mods]** Added factions Canada 2005, Australia 2005, Japan 2005, USA Aggressors, PMC
* **[New Game Wizard]** Added the list of required mods for modded factions.
* **[New Game Wizard]** No more RED vs BLUE opposing faction restrictions.
* **[New Game Wizard]** New campaign generation settings added : No aircraft carrier, no lha, no navy, invert map starting positions.
* **[Mission Generator]** Artillery units will start firing mission after a random delay. It should reduces lag spikes induced by artillery strikes by spreading them out.
* **[Mission Generator]** Ground units will retreat after taking too much casualties. Artillery units will retreat if engaged.
* **[Mission Generator]** The briefing will now contain the carrier ATC frequency
* **[Mission Generator]** The briefing contains a small situation update.
* **[Mission Generator]** Previously destroyed units are visible in the mission. (And added a performance settings to disable this behaviour)
* **[Mission Generator]*c* Basic JTAC on Frontlines
* **[Campaign Generator]** Added Tarawa in caucasus campaigns
* **[Campaign Generator]** Tuned the various existing campaign parameters
* **[Campaign Generator]** Added small campaign : "Russia" on Caucasus Theater 

## Fixed issues :
* **[Mission Generator]** Carrier will sail into the wind, not in the same direction
* **[Mission Generator]** Carrier cold start was not working (flight was starting warm even when cold was selected)
* **[Mission Generator]** Carrier group ships are more spread out
* **[Mission Generator]** Fixed wrong radio frequency for german WW2 warbirds
* **[Mission Generator]** Fixed FW-190A8 spawning with bomb rack for CAP missions
* **[Mission Generator]** Fixed A-20G spawning with no payload
* **[Mission Generator]** Fixed Su-33 spawning too heavy to take off from carrier
* **[Mission Generator]** Fixed Harrier AV-8B spawning too heavy to take off from tarawa
* **[Mission Generator]** Base defense units were not controllable with Combined Arms
* **[Mission Generator]** Tanker speed was too low
* **[Mission Generator]** Tanker TACAN settings were wrong
* **[Mission Generator]** AI aircraft should start datalink ON (EPLRS)
* **[Mission Generator]** Base defense units should not spawn on runway and or taxyway. (The chance for this to happen should now be really really low)
* **[Mission Generator]** Fixed all flights starting "In flight" after playing a few missions (parking slot reset issue)
* **[Mission Script/Performance]** Mission lua script will not listen to weapons fired event anymore and register every fired weapons. This should improve performance especially in WW2 scenarios or when rocket artillery is firing. 
* **[Campaign Generator]** Carrier name will now not appear for faction who do not have carriers
* **[Campaign Generator]** SA-10 sites will now have a tracking radar.
* **[Units/Factions]** Remove JF-17 from USA 2005 faction
* **[Units/Factions]** Remove AJS-37 from Russia 2010
* **[Units/Factions]** Removed Oliver Hazard Perry from cold war factions (too powerful sam system for the era)
* **[Bug]** On the persian gulf full map campaign, the two carriers were sharing the same id, this was causing a lot of bugs
* **[Performance]** Tuned the culling setting so that you cannot run into situation where no friendly or enemy AI flights are generated
* **[Other]** Application doesn't gracefully exit.
* **[Other]** Other minor fixes, and multiples factions small changes

# 2.0 RC 9

## Features/Improvements :
* **[UI/UX]** New icons from contributor Deus

## Fixed issues :
* **[Mission Generator]** Carrier TACAN was wrongfully set up as an A/A TACAN
* **[Campaign Generator]** Fixed issue with Russian navy group generator causing a random crash on campaign creation.

# 2.0 RC 8

## Fixed issues :
* **[Mission Generator]** Frequency for P-47D-30 changed to 124Mhz (Generated mission with 251Mhz would not work)
* **[Mission Generator]** Reduced the maximum number of uboat per generated group
* **[Mission Generator]** Fixed an issue with the WW2 LST groups (superposed units).
* **[UI]** Fixed issue with the zoom

# 2.0 RC 7

## Features/Improvements :

* **[Units/Factions]** Added P-47D-30 for factions allies_1944
* **[Units/Factions]** Added factions : Bluefor Coldwar, Germany 1944 Easy

* **[Campaign/Map]** Added a campaign in the Channel map
* **[Campaign/Map]** Changed the Normandy campaign map
* **[Campaign/Map]** Added new campaign Normandy Small

* **[Mission Generator]** AI Flight generator has been reworked
* **[Mission Generator]** Add PP points for JF-17 on STRIKE missions
* **[Mission Generator]** Add ST point for F-14B on STRIKE missions
* **[Mission Generator]** Flights with client slots will never be delayed
* **[Mission Generator]** AI units can start from parking (With a new setting in Settings Window to disable it)
* **[Mission Generator]** Tacan for carrier will only be in Mode X from now
* **[Mission Generator]** RTB waypoints for autogenerated flights

* **[Flight Planner]** Added CAS mission generator
* **[Flight Planner]** Added CAP mission generator
* **[Flight Planner]** Added SEAD mission generator
* **[Flight Planner]** Added STRIKE mission generator
* **[Flight Planner]** Added buttons to add autogenerated waypoints (ASCEND, DESCEND, RTB)
* **[Flight Planner]** Improved waypoint list
* **[Flight Planner]** WW2 factions uses different parameters for flight planning.

* **[Settings]** Added settings to disallow external views
* **[Settings]** Added settings to choose F10 Map mode (All, Allies only, Player only, Fog of War, Map Only)
* **[Settings]** Added settings to choose whether to auto-generate objective marks on the F10 map

* **[Info Panel]** Added information about destroyed buildings in info panel
* **[Info Panel]** Added information about destroyed units at SAM site in info panel
* **[Debriefing]** Added information about units destroyed outside the frontline in the debriefing window
* **[Debriefing]** Added destroyed buildings in the debriefing window

* **[Map]** Tooltip now contains the list of building for Strike targets on the map
* **[Map]** Added "Oil derrick" building
* **[Map]** Added "ww2 bunker" building (WW2)
* **[Map]** Added "ally camp" building (WW2)
* **[Map]** Added "V1 Site" (WW2)

* **[Misc]** Made it possible to setup DCS Saved Games directory and DCS installation directory manually at first start
* **[Misc]** Added culling performance settings 

## Fixed issues :

* **[Units/Factions]** Replaced S3-B Tanker by KC130 for most factions (More fuel)
* **[Units/Factions]** WW2 factions will not have offshore oil station and other modern buildings generated. No more third-reich operated offshore stations will spawn on normandy's coast. 
* **[Units/Factions]** Aircraft carrier will try to move in the wind direction
* **[Units/Factions]** Missing icons added for some aircraft

* **[Mission Generator]** When playing as RED the activation trigger would not be properly generated
* **[Mission Generator]** FW-190A8 is now properly considered as a flyable aircraft
* **[Mission Generator]** Changed "strike" payload for Su-24M that was ineffective
* **[Mission Generator]** Changed "strike" payload for JF-17 to use LS-6 bombs instead of GBU
* **[Mission Generator]** Change power station template. (Buildings could end up superposed).

* **[Maps/Campaign]** Now using Vasiani airbase instead of Soganlung airport in Caucasus campaigns (more parking slot)
* **[Info Panel]** Message displayed on base capture event stated that the enemy captured an airbase, while it was the player who captured it.
* **[Map View]** Graphical glitch on map when one building of an objective was destroyed, but not the others 
* **[Mission Planner]** The list of flights was not updated on departure time change. 


# 2.0 RC 6

Saves file from RC5 are not compatible with the new version. 
Sorry :(

## Features/Improvements :
* **[Units/Factions]** Supercarrier support (You have to go to settings to enable it, if you have the supercarrier module)
* **[Units/Factions]** Added 'Modern Bluefor' factions, containing all most popular DCS flyable units
* **[Units/Factions]** Factions US 2005 / 1990 will now sometimes have Arleigh Burke class ships instead of Perry as carrier escorts 
* **[Units/Factions]** Added support for newest WW2 Units
* **[Campaign logic]** When a base is captured, refill the "base defenses" group with units for the new owner.
* **[Mission Generator]** Carrier ICLS channel will now be configured (check your briefing)
* **[Mission Generator]** SAM units will spawn on RED Alarm state
* **[Mission Generator]** AI Flight planner now creates its own STRIKE flights
* **[Mission Generator]** AI units assigned to Strike flight will now actually engage the buildings they have been assigned.
* **[Mission Generator]** Added performance settings to allow disabling : smoke, artillery strike, moving units, infantry, SAM Red alert mode.
* **[Mission Generator]** Using Late Activation & Trigger in attempt to improve performance & reduce stutter (Previously they were spawned through 'ETA' feature)
* **[UX]** : Improved flight selection behaviour in the Mission Planning Window
 
## Fixed issues :
* **[Mission Generator]** Payloads were not correctly assigned in the release version. 
* **[Mission Generator]** Game generation does not work when "no night mission" settings was selected and the current time was "day"
* **[Mission Generator]** Game generation does not work when the player selected faction has no AWACS
* **[Mission Generator]** Planned flights will spawn even if their home base has been captured or is being contested by enemy ground units. 
* **[Campaign Generator]** Base defenses would not be generated on Normandy map and in some rare cases on others maps as well
* **[Mission Planning]** CAS waypoints created from the "Predefined waypoint selector" would not be at the exact location of the frontline
* **[Naming]** CAP mission flown from airbase are not named BARCAP anymore (CAP from carrier is still named BARCAP)

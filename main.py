#!/usr/bin/python

from random import shuffle
from time import perf_counter

ashe = [
    "Ashe",
    {
        "Total HP" : "200",
        "Normal HP" : "200",
        "Armor HP" : "0",
        "Shield HP" : "0",
        "The Viper Damage" : "20-40",
        "The Viper Fire Rate" : "4rps",
        "The Viper Ammo" : "12",
        "The Viper Reload Cast Time" : "0.5s",
        "The Viper Reload Time Per Bullet" : "0.25s",
        "The Viper (Scoped) Damage" : "40-80",
        "The Viper (Scoped) Fire Rate" : "1.4s",
        "The Viper (Scoped) Movement Speed" : "80%",
        "Coach Gun Damage Per Pellet" : "6",
        "Coach Gun Pellet Count" : "15",
        "Coach Gun Cooldown" : "10s",
        "Dynamite Explosion Damage" : "30-75",
        "Dynamite Burn Damage" : "20dps",
        "Dynamite Burn Duration" : "5s",
        "Dynamite Fuse Time" : "2s",
        "Dynamite Cooldown" : "12s",
        "B.O.B. Initial Hit Damage" : "120",
        "B.O.B. Damage Per Bullet" : "14",
        "B.O.B. Fire Rate" : "8rps",
        "B.O.B. HP" : "1200",
        "B.O.B. Duration" : "10s"
    }
]

bastion = [
    "Bastion",
    {
        "Total HP" : "300",
        "Normal HP" : "200",
        "Armor HP" : "100",
        "Shield HP" : "0",
        "Ironclad Damage Reduction While Transformed" : "20%",
        "Configuration: Recon Damage" : "6-20",
        "Configuration: Recon Fire Rate" : "8rps",
        "Configuration: Recon Ammo" : "35",
        "Configuration: Recon Reload Time" : "2s",
        "Configuration: Sentry Damage" : "4-15",
        "Configuration: Sentry Fire Rate" : "35rps",
        "Configuration: Sentry Ammo" : "300",
        "Configuration: Sentry Reload Time" : "2s",
        "Self-Repair Heal Rate" : "90hp/s",
        "Self-Repair Recharge Time" : "7s",
        "Self-Repair Max Duration" : "3.33s",
        "Self-Repair Cooldown" : "1s",
        "Reconfigure into Sentry Cast Time" : "1s",
        "Reconfigure into Recon Cast Time" : "0.5s",
        "Configuration: Tank Direct Damage" : "205",
        "Configuration: Tank Splash Damage" : "70-145",
        "Configuration: Tank Self Damage" : "28",
        "Configuration: Tank Fire Rate" : "1rps",
        "Configuration: Tank Cast Time" : "1.5s",
        "Configuration: Tank Duration" : "8s"
    }
]

doomfist = [
    "Doomfist",
    {
        "Total HP" : "250",
        "Normal HP" : "250",
        "Armor HP" : "0",
        "Shield HP" : "0",
        "The Best Defense... Max Shield HP" : "150",
        "The Best Defense... Shield HP Gained Per Ability Hit (Not ult)" : "30",
        "The Best Defense... Shield HP Gained Per Ability Hit (Ult)" : "70",
        "The Best Defense... Shield HP Decay" : "3hp/s",
        "Hand Cannon Damage Per Pellet" : "6",
        "Hand Cannon Fire Rate" : "3.3rps",
        "Hand Cannon Pellet Count" : "11",
        "Hand Cannon Ammo" : "4",
        "Hand Cannon Reload Time per Round" : "0.65s",
        "Rocket Punch Initial Hit Damage" : "50-100",
        "Rocket Punch Wall Hit" : "50-150",
        "Rocket Punch Charge Time (To Full)" : "1.4s",
        "Rocket Punch Max Hold Time After Charge" : "0.6s",
        "Rocket Punch Cooldown" : "4s",
        "Rising Uppercut Damage" : "50",
        "Rising Uppercut Cooldown" : "6s",
        "Rising Uppercut Recovery Time" : "0.35s",
        "Seismic Slam Damage (Scales with the distance traveled)" : "40-125",
        "Seismic Slam Cooldown" : "6s",
        "Meteor Strike Inner Ring Damage" : "300",
        "Meteor Strike Outer Ring Damage" : "0-200",
        "Meteor Strike Cast Time" : "1s",
        "Meteor Strike Duration" : "4s",
        "Meteor Strike Movement Speed" : "200%"
    }
]

dva = [
    "D.va",
    {
        "Mech Total HP" : "600",
        "Baby D.va Total HP" : "150",
        "Mech Normal HP" : "400",
        "Mech Armor HP" : "200",
        "Mech Shield HP" : "0",
        "Eject Cast Time" : "1s",
        "Fusion Cannon Damage (per pellet/11)" : "0.6-2",
        "Fusion Cannon Fire Rate" : "6.67rps",
        "Fusion Cannon Movement Speed" : "60%",
        "Defense Matrix Max Duration" : "2s",
        "Defense Matrix Recharge" : "7s",
        "Defense Matrix Cooldown" : "1s",
        "Defense Matrix Range" : "10m",
        "Boosters Damage" : "10",
        "Boosters Movement Speed" : "230%",
        "Boosters Duration" : "2s",
        "Boosters Cooldown" : "4s",
        "Micro Missiles Damage" : "2-7",
        "Micro Missiles Count" : "18",
        "Micro Missiles Duration" : "1.6s",
        "Micro Missiles Cooldown" : "8s",
        "Self-Destruct Area Radius" : "20m",
        "Self-Destruct Damage" : "1000",
        "Self-Destruct Time Fuse" : "3s",
        "Baby D.va Light Gun Damage" : "14",
        "Baby D.va Light Gun Fire Rate" : "7rps",
        "Baby D.va Light Gun Ammo" : "20",
        "Baby D.va Light Gun Reload Time" : "1.5s",
        "Call Mech Damage" : "50",
        "Call Mech Cast Time" : "2s"
        }
    ]

echo = [
    "Echo",
    {
        "Total HP" : "200",
        "Normal HP" : "200",
        "Armor HP" : "0",
        "Shield HP" : "0",
        "Glide Horizontal Speed" : "150%",
        "Glide Vertical Speed" : "4m/s",
        "Tri-Shot Damage Per Pellet" : "17",
        "Tri-Shot Fire Rate" : "3rps",
        "Tri-Shot Ammo" : "15",
        "Tri-Shot Reload Time" : "1.5s",
        "Sticky Bombs Impact Damage" : "5",
        "Sticky Bombs Explosion Damage" : "25",
        "Sticky Bombs Self Damage" : "12.5",
        "Sticky Bombs Bomb Count" : "6",
        "Sticky Bombs Cast Time" : "1s",
        "Sticky Bombs Cooldown" : "6s",
        "Flight Movement Speed" : "8m/s",
        "Flight Duration" : "3s",
        "Flight Cooldown" : "6s",
        "Focusing Beam Damage (Enemy has more than half HP)" : "50dps",
        "Focusing Beam Damage (Enemy has less than half HP)" : "200dps",
        "Focusing Beam Duration" : "2.5s",
        "Focusing Beam Cooldown" : "8s",
        "Duplicate Ult Charge Speed Multiplier" : "6.5",
        "Duplicate Cast Time" : "1.35s",
        "Duplicate Duration" : "15s",
        "Duplicate Range" : "40m"
    }
]

genji = [
    "Genji",
    {
        "Total HP" : "200",
        "Normal HP" : "200",
        "Armor HP" : "0",
        "Shield HP" : "0",
        "Shuriken Damage per Shuriken" : "28",
        "Shuriken Fire Rate" : "1.11rps",
        "Shuriken Count" : "3",
        "Shuriken Ammo" : "30",
        "Shuriken Reload Time" : "1s",
        "Fan of Blades Damage per Shuriken" : "28",
        "Fan of Blades Shuriken Count" : "3",
        "Fan of Blades Recovery Time" : "0.75s",
        "Fan of Blades Ammo" : "24",
        "Fan of Blades Reload Time" : "1s",
        "Swift Strike Damage" : "50",
        "Swift Strike Cooldown" : "8s",
        "Swift Strike Duration" : "0.4s",
        "Deflect Cooldown" : "8s",
        "Deflect Duration" : "2s",
        "Dragonblade Damage" : "120",
        "Dragonblade Fire Rate" : "1rps",
        "Dragonblade Duration" : "6s"
    }
]

hanzo = [
    "Hanzo",
    {
        "Total HP" : "200",
        "Normal HP" : "200",
        "Armor HP" : "0",
        "Shield HP" : "0",
        "Lunge Cooldown" : "5s",
        "Storm Bow Damage" : "29-125",
        "Storm Bow Fire Rate" : "0.8-2rps",
        "Storm Bow Movement Speed" : "70%",
        "Sonic Arrow Radius" : "9m",
        "Sonic Arrow Duration" : "6s",
        "Sonic Arrow Cooldown" : "12s",
        "Storm Arrows Damage per arrow" : "70",
        "Storm Arrows Fire Rate" : "4rps",
        "Storm Arrows Arrow Count" : "5",
        "Storm Arrows Duration" : "5s",
        "Storm Arrows Cooldown" : "10s",
        "Dragonstrike Arrow Damage" : "125",
        "Dragonstrike Dragon Damage" : "200/s",
        "Dragonstrike Cast Time" : "1.5s"
    }
]

junkrat = [
    "Junkrat",
    {
        "Total HP" : "200",
        "Normal HP" : "200",
        "Armor HP" : "0",
        "Shield HP" : "0",
        "Total Mayhem per Grenade Damage" : "50",
        "Total Mayhem Grenade Count" : "6",
        "Frag Launcher Direct Damage" : "120",
        "Frag Launcher Splash Damage" : "12.5-80",
        "Frag Launcher Fire Rate" : "1.66rps",
        "Frag Launcher Ammo" : "5",
        "Frag Launcher Reload Time" : "1.5s",
        "Frag Launcher Bounces Count" : "2",
        "Concussion Mine Damage" : "50-120",
        "Concussion Mine Ammo" : "2",
        "Concussion Mine Cooldown" : "8s",
        "Steel Trap HP" : "100",
        "Steel Trap Damage" : "80",
        "Steel Trap Trapped Duration" : "3s",
        "Steel Trap Cooldown" : "10s",
        "RIP-Tire HP" : "100",
        "RIP-Tire Damage" : "60-600",
        "RIP-Tire Cast Time" : "1s",
        "RIP-Tire Duration" : "10s",
        "RIP-Tire Movement Speed" : "12m/s"
    }
]

mccree = [
    "McCree",
    {
        "Total HP" : "200",
        "Normal HP" : "200",
        "Armor HP" : "0",
        "Shield HP" : "0",
        "Peacekeeper Damage" : "20-70",
        "Peacekeeper Fire Rate" : "2rps",
        "Peacekeeper Ammo" : "6",
        "Peacekeeper Reload Time" : "1.5s",
        "Fan the Hammer Damage Per Shot" : "27.5-50",
        "Fan the Hammer Fire Rate" : "6rps",
        "Fan the Hammer Ammo" : "6",
        "Fan the Hammer Reload Time" : "1.5s",
        "Combat Roll Cooldown" : "6s",
        "Combat Roll Duration" : "0.5s",
        "Flashbang Damage" : "25",
        "Flashbang Cooldown" : "10s",
        "Flashbang Stun Duration" : "0.7s",
        "Deadeye Damage 0.2-1s Damage Ramp-up" : "100/s",
        "Deadeye Damage 1s-1.5s Damage Ramp-up" : "275/s",
        "Deadeye Damage 1.5s+ Damage Ramp-up" : "550/s",
        "Deadeye Cast Time" : "0.2s",
        "Deadeye Range" : "200m",
        "Deadeye Duration" : "6s",
        "Deadeye Movement Speed" : "35%"
    }
]

mei = [
    "Mei",
    {
        "Total HP" : "250",
        "Normal HP" : "250",
        "Armor HP" : "0",
        "Shield HP" : "0",
        "Endothermic Blaster Damage" : "2.75",
        "Endothermic Blaster Fire Rate" : "20rps",
        "Endothermic Blaster Ammo" : "120",
        "Endothermic Blaster Reload Time" : "1.5s",
        "Endothermic Blaster Slowdown Duration" : "1s",
        "Endothermic Blaster Freeze Duration" : "1.3s",
        "Icicle Damage" : "25-75",
        "Icicle Delay" : "0.4s",
        "Icicle Fire Rate" : "1.2rps",
        "Icicle Ammo (10 used per shot)" : "120",
        "Icicle Reload Time" : "1.5s",
        "Cryo-Freeze Heal Rate" : "37.5hp/s",
        "Cryo-Freeze Duration" : "4s",
        "Cryo-Freeze Cooldown" : "12s",
        "Ice Wall HP per pillar" : "400",
        "Ice Wall Pillar Count" : "5",
        "Ice Wall Duration" : "4.5s",
        "Ice Wall Cooldown" : "13s",
        "Blizzard Area Radius" : "10m",
        "Blizzard Damage" : "20/s",
        "Blizzard Cast Time" : "1.5s",
        "Blizzard Duration" : "4.25s"
    }
]

orisa = [
    "Orisa",
    {
        "Total HP" : "400",
        "Normal HP" : "200",
        "Armor HP" : "200",
        "Shield HP" : "0",
        "Fusion Driver Damage" : "11",
        "Fusion Driver Fire Rate" : "12rps",
        "Fusion Driver Ammo" : "150",
        "Fusion Driver Reload Time" : "2.5s",
        "Fusion Driver Movement Speed" : "70%",
        "Halt! Area Radius" : "5m",
        "Halt! Cast Time (fire)" : "0.1s",
        "Halt! Cast Time (pull)" : "0.45s",
        "Halt! Duration" : "0.65s",
        "Halt! Cooldown" : "8s",
        "Fortify Dmg. Reduction" : "40%",
        "Fortify Duration" : "4s",
        "Fortify Cooldown" : "10s",
        "Protective Barrier Shield HP" : "600",
        "Protective Barrier Duration" : "20s",
        "Protective Barrier Cooldown" : "8s",
        "Supercharger Health" : "200",
        "Supercharger Damage Boost" : "50%",
        "Supercharger Cast Time" : "1s",
        "Supercharger Duration" : "15s"
        }
    ]

pharah = [
    "Pharah",
    {
        "Total HP" : "200",
        "Normal HP" : "200",
        "Armor HP" : "0",
        "Shield HP" : "0",
        "Hover Jets Movement Speed" : "120%",
        "Hover Jets Max Duration" : "2s",
        "Hover Jets Recharge Rate" : "35%/s",
        "Rocket Launcher Direct Damage" : "120",
        "Rocket Launcher Splash Damage" : "25-80",
        "Rocket Launcher Fire Rate" : "1.18rps",
        "Rocket Launcher Ammo" : "6",
        "Rocket Launcher Reload Time" : "1s",
        "Jump Jet Height" : "25m",
        "Jump Jet Movement Speed" : "20m/s",
        "Jump Jet Cooldown" : "10s",
        "Concussive Blast Knockback Radius" : "8m",
        "Concussive Blast Cooldown" : "9s",
        "Barrage Damage per Rocket" : "40",
        "Barrage Fire Rate" : "40rps",
        "Barrage Duration" : "2.5s"
    }
]

reaper = [
    "Reaper",
    {
        "Total HP" : "250",
        "Normal HP" : "250",
        "Armor HP" : "0",
        "Health HP" : "0",
        "The Reaping HP Refill" : "30%",
        "Hellfire Shotguns Damage" : "2-7 per pellet",
        "Hellfire Shotguns Pellet Count" : "20",
        "Hellfire Shotguns Ammo Count" : "8",
        "Hellfire Shotguns Reload Time" : "1.5s",
        "Wraith Form Cooldown" : "8s",
        "Wraith Form Duration" : "3s",
        "Wraith Form Movement Speed" : "150%",
        "Shadow Step Range" : "35m",
        "Shadow Step Cooldown" : "10s",
        "Shadow Step Entering Duration" : "1s",
        "Shadow Step Exiting Duration" : "0.5s",
        "Death Blossom Total Damage" : "510",
        "Death Blossom Duration" : "3s",
        "Death Blossom Movement Speed" : "55%"
    }
]

reinhardt = [
    "Reinhardt",
    {
        "Total HP" : "500",
        "Normal HP" : "300",
        "Armor HP" : "200",
        "Shield HP" : "0",
        "Steadfast knockback reduction" : "30%",
        "Rocket Hammer Damage" : "75",
        "Rocket Hammer Fire Rate" : "1.11rps",
        "Rocket Hammer Range" : "5m",
        "Barrier Field Shield HP" : "1600",
        "Barrier Field Shield Regen Rate" : "195hps",
        "Barrier Field Regen Cooldown (Not broken)" : "2s",
        "Barrier Field Cooldown (When broken)" : "5s",
        "Barrier Field Movement Speed" : "70%",
        "Charge Bump Damage" : "50",
        "Charge Pin Damage" : "300",
        "Charge Movement Speed" : "300%",
        "Charge Cooldown (Not interrupted)" : "10s",
        "Charge Cooldown (If interrupted)" : "3s",
        "Fire Strike Damage" : "100",
        "Fire Strike Cast Time" : "0.6s",
        "Fire Strike Cooldown" : "6s",
        "Earthshatter Damage" : "50",
        "Earthshatter Stun Time" : "2.5s",
        "Earthshatter Cast Time" : "0.6s",
        "Earthshatter Range" : "20m"
    }
]

roadhog = [
    "Roadhog",
    {
        "Total HP" : "600",
        "Normal HP" : "600",
        "Armor HP" : "0",
        "Shield HP" : "0",
        "Scrap Gun Damage (per pellet/25)" : "1.8-6",
        "Scrap Gun Total Damage" : "45-150",
        "Scrap Gun Fire Rate" : "1.18rps",
        "Scrap Gun Ammo" : "5",
        "Scrap Gun Reload Time" : "1.5s",
        "Shrapnel Ball Damage (per pellet/25)" : "1.8-6",
        "Shrapnel Ball Total Damage" : "50",
        "Shrapnel Ball Fire Rate" : "1.18rps",
        "Shrapnel Ball Ammo" : "5",
        "Shrapnel Ball Reload Time" : "1.5s",
        "Chain Hook Damage" : "30",
        "Chain Hook Range" : "20m",
        "Chain Hook Cooldown" : "8s",
        "Take a Breather Dmg. Reduction" : "50%",
        "Take a Breather Heal Amount" : "300hp",
        "Take a Breather Cast Time" : "0.5s",
        "Take a Breather Duration" : "1s",
        "Take a Breather Cooldown" : "8s",
        "Whole Hog Total Damage" : "5000",
        "Whole Hog Cast Time" : "0.5s",
        "Whole Hog Duration" : "6s",
        "Whole Hog Movement Speed" : "45%"
    }

]

sigma = [
    "Sigma",
    {
        "Total HP" : "400",
        "Normal HP" : "300",
        "Armor HP" : "0",
        "Shield HP" : "100",
        "Hyperspheres Direct Damage" : "60",
        "Hyperspheres Splash Damage" : "30",
        "Hyperspheres Self Damage" : "8.75",
        "Hyperspheres Fire Rate (to fire both)" : "1.5s",
        "Hyperspheres Explosion radius" : "3m",
        "Hyperspheres Max Range" : "20m",
        "Experimental Barrier HP" : "700hp",
        "Experimental Barrier HP Regen Rate" : "80hp/s",
        "Experimental Barrier HP Regen Cooldown (When not in use)" : "2s",
        "Experimental Barrier Cooldown (Not broken)" : "1s",
        "Experimental Barrier Cooldown (When broken)" : "5s",
        "Kinetic Grasp Damage Absorbed" : "60%",
        "Kinetic Grasp Max Shield" : "400",
        "Kinetic Grasp Shield Decay Rate" : "7hp/s",
        "Kinetic Grasp Duration" : "2s",
        "Kinetic Grasp Cooldown" : "12s",
        "Accretion Direct Damage" : "80",
        "Accretion Splash Damage" : "40",
        "Accretion Self Damage" : "25",
        "Accretion Direct Knockback" : "4m",
        "Accretion Splash Knockback" : "2m",
        "Accretion Self Knockback" : "2m",
        "Accretion Cast Time" : "0.65s",
        "Accretion Knockback Duration" : "0.8s",
        "Accretion Cooldoown" : "10s",
        "Gravitic Flux Lift Damage" : "50",
        "Gravitic Flux Slam Damage" : "50% max hp",
        "Gravitic Flux Intro Cast Time" : "0.6s",
        "Gravitic Flux Lift Cast Time" : "0.9s",
        "Gravitic Flux Radius" : "7m",
        "Gravitic Flux Targeting Duration" : "5s",
        "Gravitic Flux Suspension Duration" : "2s",
        "Gravitic Flux Post-Slam Slowdown Duration" : "0.6s"
    }
]

soldier_76 = [
    "Soldier 76",
    {
        "Total HP" : "200",
        "Normal HP" : "200",
        "Armor HP" : "0",
        "Shield HP" : "0",
        "Heavy Pulse Rifle Damage" : "9-20",
        "Heavy Pulse Rifle Fire Rate" : "9rps",
        "Heavy Pulse Rifle Ammo" : "25",
        "Heavy Pulse Rifle Reload Time" : "1s",
        "Helix Rockets Damage" : "120",
        "Helix Rockets Cooldown" : "6s",
        "Sprint Movement Speed" : "150%",
        "Sprint Firing Delay" : "0.3s",
        "Biotic Field HP Heal Rate" : "40/s",
        "Biotic Field Duration" : "5s",
        "Biotic Field Cooldown" : "15s",
        "Tactical Vison Cast Time" : "1.4s",
        "Tactical Visor Duration" : "6s",
        "Tactical Visor Reload Time" : "0.75s"
    }
]

sombra = [
    "Sombra",
    {
        "Total HP" : "200",
        "Normal HP" : "200",
        "Armor HP" : "0",
        "Shield HP" : "0",
        "Opportunist Enemy Health Bar Visibility When Enemy HP Below" : "100%",
        "Opportunist Enemy Wall Hack Visibility When Enemy HP Below" : "50%",
        "Machine Pistol Damage" : "2.4-8",
        "Machine Pistol Fire Rate" : "20rps",
        "Machine Pistol Ammo" : "60",
        "Machine Pistol Reload Time" : "1.5s",
        "Hack Cast Time" : "0.65s",
        "Hack Cooldown (Enemy Hack)" : "8s",
        "Hack Cooldown (Health Pack Hack)" : "4s",
        "Hack Cooldown (Interrupted)" : "2s",
        "Hack Duration (Hero Abilities)" : "5s",
        "Hack Duration (HP/Ult Status Reveal Time)" : "20s",
        "Hack Duration (Health Packs)" : "60s",
        "Hack Duration (Turret)" : "10s",
        "Hack Small Health Pack Respawn Time" : "2.5s",
        "Hack Large Health Pack Respawn Time" : "3.5s",
        "Stealth Cast Time" : "0.7s",
        "Stealth Movement Speed" : "150%",
        "Stealth Cooldown" : "6s",
        "Translocator HP" : "5",
        "Translocator Cooldown" : "6s",
        "EMP Area Radius" : "15m",
        "EMP Cast Time" : "0.65s",
        "EMP Duration" : "6s"
    }
]

symmetra = [
    "Symmetra",
    {
        "Total HP" : "200",
        "Normal HP" : "100",
        "Armor HP" : "0",
        "Shield HP" : "100",
        "Photon Projector Level 1 Damage" : "60",
        "Photon Projector Level 2 Damage" : "120",
        "Photon Projector Level 3 Damage" : "180",
        "Photon Projector Upgrade Time (Continuous Connection)" : "1.33s",
        "Photon Projector Range" : "12m",
        "Photon Projector Ammo" : "70",
        "Photon Projector Barrier Ammo Regen Rate" : "7rps",
        "Photon Projector Fire Rate" : "7rps",
        "Photon Projector Reload Time" : "1.8s",
        "Energy Ball Impact Damage" : "60",
        "Energy Ball Explosive Damage" : "60",
        "Energy Ball Charge Time" : "0.2-1s",
        "Energy Ball Ammo" : "70",
        "Energy Ball Ammo Use" : "1-10",
        "Energy Ball Reload Time" : "1.8s",
        "Sentry Turret HP" : "30",
        "Sentry Turret DPS" : "40",
        "Sentry Turret Movement Slowdown" : "1m/s",
        "Sentry Turret Casting Speed" : "0.5s",
        "Sentry Turret Deploy Time" : "1s",
        "Sentry Turret Ammo" : "3",
        "Sentry Turret Cooldown" : "10s",
        "Teleporter Total HP" : "300",
        "Teleporter Normal HP" : "50",
        "Teleporter Shield HP" : "250",
        "Teleporter Cast Time" : "1s",
        "Teleporter Deploy Time" : "2s",
        "Teleporter Range" : "30m",
        "Teleporter Cooldown" : "10s",
        "Photon Barrier HP" : "4000",
        "Photon Barrier Cast Range" : "25m",
        "Photon Barrier Duration" : "12s"
    }
]

torbjorn = [
    "Torbjorn",
    {
        "Total HP" : "250",
        "Normal HP" : "200",
        "Armor HP" : "50",
        "Shield HP" : "0",
        "Rivet Gun Damage" : "70",
        "Rivet Gun Fire Rate" : "1.67rps",
        "Rivet Gun Ammo" : "18",
        "Rivet Gun Reload Time" : "2s",
        "Rivet Gun Alt Damage" : "3.75-12.5 per pellet",
        "Rivet Gun Alt Pellet Count" : "10",
        "Rivet Gun Alt Fire Rate" : "1.25rps",
        "Rivet Gun Alt Ammo (3 per shot)" : "18",
        "Rivet Gun Alt Reload Time" : "2s",
        "Forge Hammer Damage" : "55",
        "Forge Hammer Turret HP Repair" : "50",
        "Forge Hammer Fire Rate" : "1.25rps",
        "Deploy Turret Deploy Time" : "3s",
        "Deploy Turret Health" : "250",
        "Deploy Turret Damage" : "14",
        "Deploy Turret Fire Rate" : "4rps",
        "Deploy Turret Cooldown (Not Destroyed)" : "5s",
        "Deploy Turret Cooldown (When Destroyed)" : "10s",
        "Overload Armor HP Boost" : "100",
        "Overload Movement Speed" : "130%",
        "Overload Duration" : "5s",
        "Overload Cooldown" : "10s",
        "Molten Core Damage to Normal HP and Shield HP per second" : "160",
        "Molten Core Damage to Armor HP per second" : "190",
        "Molten Core Fire Rate" : "6.66rps",
        "Molten Core Ammo" : "10",
        "Molten Core Fire Duration" : "6s",
        "Molten Core Pool Duration" : "10s"
    }
]

winston = [
    "Winston",
    {
        "Total HP" : "500",
        "Normal HP" : "400",
        "Armor HP" : "100",
        "Shield HP" : "0",
        "Tesla Cannon Damage" : "3",
        "Tesla Cannon Fire Rate" : "20rps",
        "Tesla Cannon Ammo" : "100",
        "Tesla Cannon Reload Time" : "1.5s",
        "Jump Pack Damage" : "1-45",
        "Jump Pack Area Radius" : "5m",
        "Jump Pack Cooldown (not in Primal Rage)" : "6s",
        "Jump Pack Cooldown in Primal Rage" : "2s",
        "Barrier Projector HP" : "600hp",
        "Barrier Projector Area Radius" : "5m",
        "Barrier Projector Duration" : "9s",
        "Barrier Projector Cooldown" : "13s",
        "Primal Rage HP" : "1000",
        "Primal Rage Damage" : "40",
        "Primal Rage Fire Rate" : "1.8rps",
        "Primal Rage Duration" : "10s",
        "Primal Rage Movement Speed" : "130%"
    }
]

wrecking_ball = [
    "Wrecking Ball",
    {
        "Total HP" : "600",
        "Normal HP" : "500",
        "Armor HP" : "100",
        "Shield HP" : "0",
        "Quad Cannons Damage" : "5",
        "Quad Cannons Fire Rate" : "25rps",
        "Quad Cannons Ammo" : "80",
        "Quad Cannons Reload Time" : "1s",
        "Grappling Claw Damage" : "50",
        "Grappling Claw Movement Speed" : "20m/s",
        "Grappling Claw Range" : "15m",
        "Grappling Claw Cooldown" : "5s",
        "Roll Movement Speed" : "150%",
        "Adaptive Shield Base HP" : "100",
        "Adaptive Shield HP per Nearby Enemy" : "100",
        "Adaptive Shield Duration" : "7s",
        "Adaptive Shield Cooldown" : "15s",
        "Piledriver Damage" : "20-100",
        "Piledriver Radius" : "8m",
        "Piledriver Cooldown" : "10s",
        "Minefield Mine Count" : "12",
        "Minefield Damage (Per Mine)" : "130",
        "Minefield Mine HP" : "50",
        "Minefield Cast Time" : "0.1s",
        "Minefield Duration" : "20s"
    }
]

zarya = [
    "Zarya",
    {
        "Total HP" : "400",
        "Normal HP" : "200",
        "Armor HP" : "0",
        "Shield HP" : "200",
        "Energy Max Charges" : "100",
        "Energy Decay Rate" : "1.6charge/s",
        "Energy, 1 Charge per X dmg absorbed" : "5",
        "Particle Cannon Base Damage" : "95dps",
        "Particle Cannon Additional Damage Per Charge" : "0.75",
        "Particle Cannon Ammo" : "100",
        "Particle Cannon Fire Rate" : "20rps",
        "Particle Cannon Reload Time" : "1.5s",
        "Particle Cannon Alt Base Damage" : "45",
        "Particle Cannon Alt Additional Damage Per Charge" : "1%",
        "Particle Cannon Alt Fire Rate" : "1rps",
        "Particle Cannon Alt Ammo" : "100",
        "Particle Cannon Alt Ammo Used Per Shot" : "25",
        "Particle Cannon Reload Time" : "1.5s",
        "Particle Barrier HP" : "200",
        "Particle Barrier Duration" : "2s",
        "Particle Barrier Cooldown" : "10s",
        "Projected Barrier HP" : "200",
        "Projected Barrier Duration" : "2s",
        "Projected Barrier Cooldown" : "8s",
        "Graviton Surge Damage" : "22",
        "Graviton Surge Area Radius" : "6",
        "Graviton Surge Duration" : "4s"
    }
]

heroes = [
    ashe,
    bastion,
    doomfist,
    dva,
    echo,
    genji,
    hanzo,
    junkrat,
    mccree,
    mei,
    orisa,
    pharah,
    reaper,
    reinhardt,
    roadhog,
    sigma,
    soldier_76,
    sombra,
    symmetra,
    torbjorn,
    winston,
    wrecking_ball,
    zarya
    ]

flashcards = {}
flashcards_keys = []
correct_keys = []
questions_asked = 0.0

tic = perf_counter()

for hero in heroes:
    hero_name = hero[ 0 ]
    hero_questions = hero[ 1 ]
    for question in hero_questions:
        key = hero_name + " | " + question
        if not isinstance( hero_questions[ question ] , str ):
            print( "ERROR: Not a string" )
            print( key )
            print( hero_questions[ question ] )
            exit(2)
        flashcards[ key ] = hero_questions[ question ]
        flashcards_keys.append( key )

while len( flashcards_keys ) != len( correct_keys ):
    shuffle( flashcards_keys )
    for question in flashcards_keys:
        if question not in correct_keys:
            user_response = input( question + ": " )
            questions_asked += 1
            if user_response == flashcards [ question ]:
                print( "CORRECT!" )
                correct_keys.append( question )
            else:
                print( "INCORRECT" )
                print( "Correct answer was: " + flashcards[ question ] )
            print("")

print("")
toc = perf_counter()
print( "Completed in " + str(int(toc-tic)) + " seconds." )
accuracy = "{:.2f}".format( ( len(flashcards) / questions_asked ) * 100 )
print( "Accuracy: " + str( accuracy ) + "%" )   

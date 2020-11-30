#!/usr/bin/python

from random import shuffle
from time import perf_counter

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
    dva,
    orisa,
    reinhardt,
    roadhog,
    sigma,
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
toc = perf_counter()
print( "Completed in " + str(int(toc-tic)) + " seconds." )
accuracy = "{:.2f}".format( ( len(flashcards) / questions_asked ) * 100 )
print( "Accuracy: " + str( accuracy ) + "%" )   

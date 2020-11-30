#!/usr/bin/python

from random import shuffle

dva = [ 
        "D.va", 
        { 
            "Mech Total HP" : "600",
            "Baby D.va Total HP" : "150",
            "Mech Normal HP" : "400",
            "Mech Armor HP" : "200",
            "Mech Shield HP" : "0",
            "Eject Cast Time" : "1s",
            "Fusion Cannon Damage" : "0.6-2",
            "Fusion Cannon Fire Rate" : "6.67 rps",
            "Fusion Cannon Speed Drop" : "60%",
            "Defense Matrix Max Duration" : "2s",
            "Defense Matrix Recharge" : "7s",
            "Defense Matrix Cooldown" : "1s",
            "Defense Matrix Range" : "10m",
            "Boosters Damage" : "10",
            "Boosters Speed" : "230%",
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
            "Baby D.va Light Gun Fire Rate" : "7 rps",
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
            "Armor HP": "200"
        }
    ]

heroes = [ dva, orisa ]
flashcards = {}
flashcards_keys = []
correct_keys = []
for hero in heroes:
    hero_name = hero[ 0 ]
    hero_questions = hero[ 1 ]
    for question in hero_questions:
        key = hero_name + "|" + question
        if not isinstance( hero_questions[ question ] , str ):
            print( "ERROR: Not a string" )
            print( key )
            print( hero_questions[ question ] )
            exit(2)
        flashcards[ key ] = hero_questions[ question ]
        flashcards_keys.append( key )

while len( flashcards_keys ) != len( correct_keys ):
    shuffle( flashcards_keys )
    questions_asked = 0
    correct_responses = 0
    for question in flashcards_keys:
        if question not in correct_keys:
            user_response = input(question + ": ")
            questions_asked += 1
            if user_response == flashcards [ question ]:
                print( "CORRECT!" )
                correct_responses += 1
                correct_keys.append( question )
            else:
                print( "INCORRECT" )
                print( "Correct answer was: " + flashcards[ question ] )

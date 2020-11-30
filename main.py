#!/usr/bin/python

from random import shuffle

dva = [ 
        "D.va", 
        { 
            "Mech Total HP" : "600",
            "Baby D.va Total HP" : "150",
            "Mech Normal HP" : "400",
            "Mech Armor HP" : "200",
            "Mech Shield HP" : "0"
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

shuffle( flashcards_keys )
questions_asked = 0
correct_responses = 0
for question in flashcards_keys:
    user_response = input(question + ": ")
    questions_asked += 1
    if user_response == flashcards [ question ]:
        print( "CORRECT!")
        correct_responses += 1

print( "You got " + str(correct_responses) + " out of " + str(questions_asked) + " correct.")

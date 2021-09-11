# Game Concept: Elemental Roshambo (A.K.A. Elemental Rock-Paper-Scissors) Fighting Game

0. Determine the Elemental attacks that the user and Computer are launching at each other
1. Computer secretly selects a random option between Fire, Earth, Water, Wind, and Lightning
2. The Computer then assigns a random(randint(0, MAX_POWER where MAX_POWER starts off at 100)) POWER level behind the attack in the range of 0 to the MAX_POWER the Computer still has
3. Subtract the chosen POWER from the Computer's MAX_POWER
4. Prompt the user to choose between Fire, Earth, Water, Wind, and Lightning and at what POWER level between 0 and the User's remaining MAX_POWER
5. Subtract the chosen POWER from the user's MAX_POWER
6. Take the string input from the user and compare it against the computer's choice
7. Determine who has won the Elemental exchange:
    1. If user and computer choose the same Element, it is a tie that will need to be broken by the amount of POWER that either has put behind the attack
    2. If one chose Fire and one chose Lightning, Fire wins
    3. If one chose Fire and one chose Wind, Fire wins
    4. If one chose Lightning and one chose Wind, Lightning wins
    5. If one chose Lightning and one chose Water, Lightning wins
    6. If one chose Wind and one chose Earth, Wind wins
    7. If one chose Wind and one chose Water, Wind wins
    8. If one chose Water and one chose Earth, Water wins
    9. If one chose Water and one chose Fire, Water wins
    10. If one chose Earth and one chose Fire, Earth wins
    11. If one chose Earth and one chose Lightning, Earth wins
8. Determine the damage to either user or Computer-based off of the POWER exchange
    1. If it was the same elemental type of attack
        1. If Player X had more than 5 points more POWER than Player Y apply the difference in POWER as DAMAGE to Player Y's health
        2. If Player X had less than 5 points more POWER than Player Y apply the difference in POWER as DAMAGE to Player X's health
        3. If Player X and Player Y were within 5 points of POWER to each other attacks cancel out
    2. If Player X's elemental type of attack had an advantage
        1. If Player X had more than 5 points more POWER than Player Y apply the difference in POWER as DAMAGE multiplied by 2 to Player Y's health
        2. If Player X had less than 5 points more POWER than Player Y apply the difference in POWER as DAMAGE multiplied by 0.75 to Player Y's health
        3. If Player X and Player Y were within 5 points of POWER to each other apply the difference in POWER as DAMAGE multiplied by 0.25 to Player X's health
    3. If Player X's elemental type of attack had a disadvantage
        1. If Player X had more than 5 points more POWER than Player Y apply the difference in POWER as DAMAGE multiplied by 0.75 to Player Y's health
        2. If Player X had less than 5 points more POWER than Player Y apply the difference in POWER as DAMAGE multiplied by 0.75 to Player X's health
        3. If Player X and Player Y were within 5 points of POWER to each other apply the difference in POWER as DAMAGE multiplied by 0.25 to Player X's health
9. If no one has won the battle another round of exchanges begins

## Notes for 08/19/2021

The Martial Arts Styles: [Boxing:Outboxer], [BrazillianJuJitsu], [Taekwondo], [Karate], [Capoeira], [MuayThai], [KravMaga]
The Elements: [Lightning], [Fire], [Water], [Earth], [Wind]
The Combination
[Wind] <=> [Capoeira], [Boxing:Outboxer]

1. Float like a butterfly
2. Sting like a bee
3. Weave
4. Snaking Counter
5. Sonic Boom
6. Flurry
7. Agile

[Lightning] <=> [MuayThai], [KravMaga]

1. Quick Jab
2. Push Kick
3. Diagonal Kick (shin)
4. Quick relfex reversal
5. Quick disarm
6. Claw Attack
7. Elbow Strike

[Fire] <=> [Taekwondo], [Karate]

1. Solar Plexus Punch
2. Hammer Fist
3. Kick
4. Uppercut
5. Strangle Hold
6. Sweep Kick
7. Knee
8. Jump Kick
9. Dropkick

[Water] <=> [FreeForm], [MMA] (First free, then becoming as hard as a rock, ice)

1. Spin Kick
2. Round House Kick
3. Tackle
4. Sweep
5. Aliigator Spin

[Earth] <=> [BrazillianJuJitsu]

1. Tackle
2. Choke Hold

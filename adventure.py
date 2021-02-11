import time


def playNBAFinals2013():
    print("\nIt's Game 6 of the 2013 NBA Finals between The Miami Heat and The San Antonio Spurs in the closing seconds of the game.\nThe Heat are down 92-95 and LeBron James has just missed a 3.\nYou are playing as Chris Bosh in this short game and will decide whether the Heat can tie this game or not.\n")
    print('---LeBron shoots a 3 from the left elbow---\n')
    first_choice = input(
        '\nNext Play: Pick a number (1 - 2): \n1. Fight for the rebound passively\n2. Fight for the rebound and get the ball back into the Heat\'s hands\n')

    if(first_choice == '1'):
        time.sleep(2)
        print('You were too passive and Manu Ginóbili grabs it instead giving the Spurs possession of the ball again.')
        time.sleep(2)
        second_choice = input(
            '\nNext Play: Pick a number (1 - 2): \n1. Foul Manu Ginóbili\n2. Let the Spurs run the clock out\n')

        if (second_choice == '1'):
            time.sleep(2)
            print('\n---Popovich subs Danny Green for Tim Duncan to make sure the Spurs can grab a potential rebound now that they don\'t have to worry about a 3---')
            time.sleep(2)
            print('\n---Ginóbili does his free throw routine...---')
            time.sleep(2)
            print('\n---With 7.2 seconds left and the clock stopped, Ginóbili goes to the line and sinks in the first free throw---')
            time.sleep(2)
            print('\n---Ginóbili does his free throw routine...---')
            time.sleep(2)
            print('\n---Ginóbili bricks his second free throw with either team being having the chance to get the rebound!---')
            time.sleep(2)
            print('\n---Tim Duncan grabs the rebound over Chris Bosh---')
            print('\nThe San Antonio Spurs are your 2013 NBA Champions. What moves will the Heat make this summer as they try to rebound from this loss? Is the Big 3 superteam a failure?')

        if (second_choice == '2'):
            time.sleep(2)
            print('\nDespite the Heat almost pulling off the miracle comeback, a questionable decision to not foul has led them to a 2nd finals loss in 3 years. Will the Big 3 stay together after this offseason? This offseason will be very interesting for Miami fans....')
    elif(first_choice == '2'):
        print('---Chris Bosh successfully grabs the rebound!---')

        second_choice = input(
            '\nNext Play: Pick a number (1 - 2): \n1. Shoot over the defenders in an attempt to get an and-1 for a 3pt play\n2. Pass to Ray Allen for a corner 3\n')

        if (second_choice == '1'):
            time.sleep(2)
            print('---Chris Bosh shoots over 2 defenders for 2pts and despite being elbowed by Ginóbili the refs do not call a foul.---')
            print('The Heat are still down 94-95')
            time.sleep(2)
            print('---After being forced to foul the Spurs again the Heat are down 94-97 once they make both their free throws.---')
            time.sleep(2)
            print('---LeBron passes to Ray Allen---')
            time.sleep(2)
            print('---Ray Allen shoots a 3 and...')
            time.sleep(2)
            print('---The ball rims out---')
            time.sleep(2)
            print('\nThe San Antonio Spurs are your 2013 NBA Champions. What moves will the Heat make this summer as they try to rebound from this loss? Is the Big 3 superteam a failure?')
        elif (second_choice == '2'):
            time.sleep(2)
            print('---Chris Bosh passes to Ray Allen for a corner 3')
            time.sleep(2)
            print('---Ray Allen shoots a 3---')
            time.sleep(2)
            print('BAAAAAAANG!!!!')
            print('Ray Allen makes the 3 and ties the game which the Heat will then win in overtime after many clutch defensive stops and force a Game 7.')
            time.sleep(2)
            print('The Heat will go on to win Game 7 95-88.')
            time.sleep(2)
            print('\nThe Miami Heat are your 2013 NBA Champions as LeBron James captures that elusive 2nd title. Is this the end for the Tim Duncan era Spurs? Will the Heat be the first team since the Shaq-Kobe Lakers to 3-peat? The 2014 season should be very interesting indeed.')


def playSuperBowlXLIX():
    print(f"It's SuperBowl 49 between The New England Patriots and The Seattle Seahawks. The Patriots are up 28-24 on the Seahawks.")
    print(f"You are playing as Pete Caroll, Seattle's Coach and must draw up a play to win on this last drive to the endzone.")

    time.sleep(5)
    first_choice = input(
        '\nNext Play: Pick a number (1 - 2): \n1. Run the ball\n2. Have Russell Wilson pass the ball\n')

    if(first_choice == '1'):
        time.sleep(2)
        print('The Seattle Seahawks are your Super Bowl XLIX (49) Champions.')
    elif(first_choice == '2'):
        time.sleep(2)
        print('---Pass is intercepted by Malcolm Butler!---')
        time.sleep(2)
        print(
            'After a decade, The New England Patriots are once again Super Bowl Champions.')


choice = input(
    '\nWhich game do you want to play?: Pick a number (1 - 2): \n1. Closing seconds of 2013 NBA Finals\n2. Closing seconds of Super Bowl XLIX (49)\n')

if(choice == '1'):
    playNBAFinals2013()
else:
    playSuperBowlXLIX()

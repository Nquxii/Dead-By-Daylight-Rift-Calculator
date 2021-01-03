tier = int(input('what is your current tier :'))
mchallenges = int(input('enter how many master challenges (5pts) you expect to complete by the end of the rift :'))
nchallenges = int(input('enter how many normal challenges (3pts) you expect to complete by the end of the rift :'))
fragsrem = int(input('enter the progress on your current tier (e.g. 7/10, enter 7) :'))
daysleft = int(input('enter the days remaining in your rift :'))

fragsneeded = 690 - (tier * 10 + mchallenges * 5 + nchallenges * 3 + fragsrem)

if fragsneeded <= 0:
    print('''you're already maxed!''')
    exit()

hoursneeded = fragsneeded * 800 / 60 / 60
eachday = hoursneeded/daysleft

if eachday > 24:
    print('it is impossible for you to max the battle pass!')
    exit()

print('To maximize your rift progress, you need to play about ' + str(hoursneeded) + ' hours, which is roughly ' + str(eachday) + ' each day. ' + 'Keep in mind that this is raw game time, not application times. Lobby time or browsing through the shop is not included.')

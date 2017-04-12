"""
    Bringing a Gun to a Guard Fight
    ===============================

    Uh-oh - you've been cornered by one of Commander Lambdas elite guards!
    Fortunately, you grabbed a beam weapon from an abandoned guardpost while you were running through the station,
    so you have a chance to fight your way out. But the beam weapon is potentially dangerous to you as well as to the elite guard:
    its beams reflect off walls, meaning youll have to be very careful where you shoot to avoid bouncing a shot toward yourself!

    Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage.
    You also know that if a beam hits a corner, it will bounce back in exactly the same direction.
    And of course, if the beam hits either you or the guard, it will stop immediately (albeit painfully). 

    Write a function answer(dimensions, your_position, guard_position, distance) that gives an array of
    2 integers of the width and height of the room, an array of 2 integers of your x and y coordinates in the room,
    an array of 2 integers of the guard's x and y coordinates in the room, and returns an integer of the number of
    distinct directions that you can fire to hit the elite guard, given the maximum distance that the beam can travel.

    The room has integer dimensions [1 < x_dim <= 1000, 1 < y_dim <= 1000]. You and the elite guard are both positioned
    on the integer lattice at different distinct positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim].
    Finally, the maximum distance that the beam can travel before becoming harmless will be given as an integer 1 < distance <= 10000.

    For example, if you and the elite guard were positioned in a room with dimensions [3, 2], you_position [1, 1],
    guard_position [2, 1], and a maximum shot distance of 4, you could shoot in seven different directions to hit the elite guard
    (given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2].
    As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2]
    bounces off the left wall and then the bottom wall before hitting the elite guard with a total shot distance of sqrt(13),
    and the shot at bearing [1, 2] bounces off just the top wall before hitting the elite guard with a total shot distance of sqrt(5).

    Languages
    =========

    To provide a Python solution, edit solution.py
    To provide a Java solution, edit solution.java

    Test cases
    ==========

    Inputs:
        (int list) dimensions = [3, 2]
        (int list) captain_position = [1, 1]
        (int list) badguy_position = [2, 1]
        (int) distance = 4
    Output:
        (int) 7

    Inputs:
        (int list) dimensions = [300, 275]
        (int list) captain_position = [150, 150]
        (int list) badguy_position = [185, 100]
        (int) distance = 500
    Output:
        (int) 9
"""

import math

def commonFactor(x,y):
    if x == 0: return 'inf'
    if y == 0: return 0
    big = max(x,y)
    small = min(x,y)
    while(small!=0):
        r = small
        small = big % r
        big = r
    return abs(big)

def position(dimensions, captainPosition, badguyPosition,source):
    captains = []
    badguys = []
    width = dimensions[0]
    height = dimensions[1]
    cx = captainPosition[0]
    cy = captainPosition[1]
    gx = badguyPosition[0]
    gy = badguyPosition[1]
    for x,y in source[(0,0)]:
        captains.append((x,y))
        badguys.append((x+gx-cx,y+gy-cy))
    for x,y in source[(1,0)]:
        captains.append((x+width-2*cx,y))
        badguys.append((x+width-gx-cx,y+gy-cy))
    for x,y in source[(0,1)]:
        captains.append((x,y+height-2*cy))
        badguys.append((x+gx-cx,y+height-gy-cy))
    for x,y in source[(1,1)]:
        captains.append((x+width-2*cx,y + height-2*cy))
        badguys.append((x+width-gx-cx,y + height-gy-cy))
    return captains,badguys

def origin(dimensions, distance):
    sources = {}
    sources[(0,0)]=[]
    sources[(1,0)]=[]
    sources[(0,1)]=[]
    sources[(1,1)]=[]
    width = dimensions[0]
    height = dimensions[1]
    w = (distance/width) + 1
    h = (distance/height) + 1
    for x in range(-w,w+1):
        for y in range(-h,h+1):
            if x % 2 == y % 2:
                if x % 2 == 0:
                    sources[(0,0)].append((x*width,y*height))
                else:
                    sources[(1,1)].append((x*width,y*height))
            else:
                if x % 2 == 0:
                    sources[(0,1)].append((x*width,y*height))
                else:
                    sources[(1,0)].append((x*width,y*height))
    return sources

def countPossibilities(captain,badguy):
    global possibilities
    possibilities = {}
    for x,y in badguy:
        common = commonFactor(x,y)
        if common == 0:
            if (0 not in possibilities or possibilities[0]>abs(x)):
                possibilities[0]= abs(x)
        elif common == 'inf':
            if ('inf' not in possibilities or possibilities['inf']>abs(y)):
                possibilities['inf']= abs(y)
        elif (x/common,y/common) not in possibilities or possibilities[(x/common,y/common)]>math.sqrt(x**2+y**2):
            possibilities[(x/common,y/common)]= math.sqrt(x**2+y**2)
    for x,y in captain:
        common = commonFactor(x,y)
        if common == 0:
            if 0 in possibilities and possibilities[0]>abs(x):
                del possibilities[0]
        elif common == 'inf':
            if 'inf' in possibilities and possibilities['inf']>abs(y):
                del possibilities['inf']
        elif (x/common,y/common) in possibilities and possibilities[(x/common,y/common)]>math.sqrt(x**2+y**2):
            del possibilities[(x/common,y/common)]
    return possibilities

def answer(dimensions, captainPosition, badguyPosition, distance):
    origins = origin(dimensions, distance)
    captain,badguy = position(dimensions, captainPosition, badguyPosition,origins)
    captain = [x for x in captain if math.sqrt(x[0]**2+x[1]**2) <= distance and not (x[0]==x[1]==0)]
    badguy = [x for x in badguy if math.sqrt(x[0]**2+x[1]**2) <= distance and not (x[0]==x[1]==0)]
    possibilities = countPossibilities(captain,badguy)
    return len(possibilities)

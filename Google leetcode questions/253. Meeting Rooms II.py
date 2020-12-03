Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]]
return 2.


def no_of_meeting_rooms(l):
    room = 0
    starttime = sorted( [ i[0] for i in l])
    endtime = sorted([ i[1] for i in l ])
    while len(starttime)>0:
        start = starttime.pop(0)
        end = endtime[0]
        if end<=start:
            endtime.pop(0)
        else:
            room+=1
            
    return room
    
    

from collections import deque
match_list = deque()
def undoTeamEntry():
    if match_list:
        match_list.pop()
    else:
        print("No Match Found")

def scheduleMatch():
    if match_list:
        match_list.popleft()
    else:
        print("No Match Found")
def createMatchEntry(a,b):
    match_list.append([a,b])

createMatchEntry("Team Ange", "Team Grace")
createMatchEntry("Team A", "Team B")
createMatchEntry("Team F", "Team C")
undoTeamEntry()
scheduleMatch()

print(f"all available Matches Ranking: {match_list}")


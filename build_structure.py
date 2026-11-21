import os

PARTICIPANTS = ["Jacob", "Jake", "Jayde", "Quinn", "Campbell", "Grant", "Beau", "Dave", "Louis"]
PWD = os.getcwd()

advent_days = [f"advent_day_{day_number}" for day_number in range(1, 26)]


for day in advent_days:
    day_base_path = os.path.join(PWD, day)

    for participant in PARTICIPANTS:
        participant_path = os.path.join(day_base_path, participant)
        os.makedirs(participant_path, exist_ok=True)
        open(os.path.join(participant_path, ".gitkeep"), "w").close()
    
    with open(os.path.join(day_base_path, "votes.md"), "w") as votes_file:
        for participant in PARTICIPANTS:
            votes_file.write(f"Votes For {participant}: \n\n")


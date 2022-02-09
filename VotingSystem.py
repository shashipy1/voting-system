
nominee1 = input("Enter the name of 1st nominee: ")
nominee2 = input("Enter the name of 2nd nominee: ")

nm1_votes = 0
nm2_votes = 0

voter_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

no_of_voters = len(voter_id)

while True:
    if voter_id == []:
        print("Voting session is over !!")
        if nm1_votes > nm2_votes:
            percent = (nm1_votes/no_of_voters)*100
            print(nominee1, "has Won the election with ", percent,  "% of votes")
            break
        elif nm2_votes > nm1_votes:
            percent = (nm2_votes/no_of_voters)*100
            print(nominee2, "has Won the election with ", percent,  "% of votes")
            break
        else:
            print(
                "Both have equal numbers has vots!!! Government will decided  who will rule")

    voter = int(input("Enter your voter id: "))
    if voter in voter_id:
        print("You are a voter")
        voter_id.remove(voter)
        print('-'*40)

        print("To give vote to", nominee1, "Press 1")
        print("To give vote to", nominee2, "Press 2")
        
        print('-'*40)

        vote = int(input("Enter your precios vote: "))
        if vote == 1:
            nm1_votes += 1
            print(nominee1, "Thank you to give your vote!")
        elif vote == 2:
            nm2_votes += 1
            print(nominee2, "Thank you to give your vote!")
        elif vote > 2:
            print("Check your pressed key!!")
        else:
            print("You are not voter or You have already voted")

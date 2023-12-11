class cricket:
    def __init__(self,name,score) -> None:
        self.name = name
        self.score = score
    
    def change_score(self,newscore):
        self.score = newscore
        

class football:
    def __init__(self) -> None:
        pass

cricket_team = cricket(name="cricket team!!!", score="4 wins")

print(cricket_team.name, cricket_team.score)

cricket_team.change_score("1200 wins")

print (cricket_team.score)
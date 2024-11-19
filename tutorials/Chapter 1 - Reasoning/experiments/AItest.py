from lnn import And, Fact, Proposition

#Rules
Messi = Proposition("Name is Messi")
AFC = Proposition("Plays for Argentina National Football Club(AFC)")
AND= And(Messi, AFC)

#Data
AFC.add_data(Fact.TRUE)
Messi.add_data(Fact.TRUE)

#Reasoning 
AND.upward()
AND.print()
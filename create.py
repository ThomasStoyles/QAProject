from application import db
from application.models import Games, Developer

# db.drop_all()
db.create_all()

# test data adding 
# Activision = Developer(dev_name='Activision')
# Microsoft = Developer(dev_name='Microsoft')
# Riot = Developer(dev_name='Riot')

# Call_Of_Duty = Games(name='Call Of Duty', age = 18, price=49.99, dev=Activision)
# Minecraft = Games(name='Minecraft', age = 3, price=20, dev=Microsoft)
# League = Games(name='League Of Legends', age = 12, price=0, dev=Riot)

# db.session.add_all([Activision, Microsoft, Riot, Call_Of_Duty, Minecraft, League])
# db.session.commit()



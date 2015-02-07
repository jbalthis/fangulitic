#!/usr/bin/env python2

from app.astores.models import db as astores_db
from app.customs.models import db as customs_db
#from app.replicated.models import db as replicated_db
from app.users.models import db as users_db
from app.users.models import User
from app.users.views import new_password
from app.wordpress.models import db as wordpress_db

astores_db.create_all()
customs_db.create_all()
#replicated_db.create_all()
users_db.create_all()
wordpress_db.create_all()

admin = User('admin', new_password('password'), 'united', 1)
users_db.session.add(admin)
users_db.session.commit()

from flask_script import Manager
from flask_migrate import MigrateCommand
from homework import create_user

# manager是入口
# create_app可以指定config
app=create_user()
manager=Manager(app)
manager.add_command('db',MigrateCommand)

if __name__=='__main__':
    manager.run()


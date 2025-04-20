import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_student, create_company, create_staff, get_all_users_json, get_all_users, initialize )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create-student", help="Creates a student user")
@click.argument("username", default="john")
@click.argument("email", default="john@email.com")
@click.argument("password", default="johnpass")
@click.argument("first_name", default="John")
@click.argument("last_name", default="Smith")
def create_student_command(username, email, password, first_name, last_name):
    create_student(username, email, password, first_name, last_name)
    print(f'{username} created!')

@user_cli.command("create-company", help="Creates a company user")
@click.argument("username", default="bill")
@click.argument("email", default="bill@email.com")
@click.argument("password", default="billpass")
@click.argument("company_name", default="Company")
def create_company_command(username, email, password, company_name):
    create_company(username, email, password, company_name)
    print(f'{username} created!')

@user_cli.command("create-staff", help="Creates a staff user")
@click.argument("username", default="steve")
@click.argument("email", default="steve@email.com")
@click.argument("password", default="stevepass")
@click.argument("position", default="admin")
def create_staff_command(username, email, password, position):
    create_staff(username, email, password, position)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)
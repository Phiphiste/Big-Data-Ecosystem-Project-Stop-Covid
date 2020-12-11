#!/usr/bin/env python
# coding: utf-8

#imports
import sqlite3
import random
random.seed()

# set up connection
connection = sqlite3.connect('stop_covid.db')
cursor = connection.cursor()

# create table people informations and positions
command1 = """CREATE TABLE IF NOT EXISTS
people(people_id INTEGER PRIMARY KEY, 
phone_nb INTEGER, 
pos_x INTEGER, 
pos_y INTEGER, 
health_state INTEGER)"""
cursor.execute(command1)

# create interactions table with IDs of people
command2 = """CREATE TABLE IF NOT EXISTS
interactions(interaction_id INTEGER PRIMARY KEY,
people1_id INTEGER,
people2_id INTEGER)"""
cursor.execute(command2)

# Create Database
def create_database(size):

    #initialize values
    
    db_size = size
    people_id = -1
    phone_nb = -1
    pos_x = -1
    pos_y = -1
    health_status = -1


    # add to people table random values

    for i in range(1,db_size):
        people_id = i
        phone_nb = random.randint(33600000000,33699999999)
        pos_x = random.randint(0,100)
        pos_y = random.randint(0,100)
        random_health = random.randint(0,20)
        if random_health == 20:
            health_status = 2
        elif 15 <= random_health < 20:
            health_status = 1
        else:
            health_status = 0
        cursor.execute("INSERT INTO people VALUES({},{},{},{},{})".format(people_id,phone_nb,pos_x,pos_y,health_status))

# Delete people table
def delete_table(table):
    cursor.execute("DELETE FROM {}".format(table))

# Get people database

def get_all_people(nb):
    cursor.execute("SELECT * FROM people")
    results = cursor.fetchall()
    print(results[:nb])

# Update position of one people

def update_position(people_id, pos_x, pos_y):
    cursor.execute("UPDATE people SET pos_x = pos_x + {}, pos_y = pos_y + {} WHERE people_id = {} ".format(pos_x,pos_y,people_id))

# Update position of the whole people database
def update_all_positions():
    for i in range(1,100):
        new_pos_x = random.randint(-5,5)
        new_pos_y = random.randint(-5,5)
        update_position(i, new_pos_x, new_pos_y)

#delete_table("people") #uncomment this line if you already created the table
create_database(100)

try:
    while(True):
        update_all_positions()
except KeyboardInterrupt: # CTLR-C to interrupt process
    pass


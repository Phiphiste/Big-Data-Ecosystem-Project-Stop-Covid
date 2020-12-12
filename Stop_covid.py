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
health_status INTEGER)"""
cursor.execute(command1)


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
        phone_nb = random.randint(33600000000,33799999999)
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
        # def update interaction table

# Update interactions table
'''
for i in range(1,100):
    if p1_x == p2_x and p1_y == p2_y:
        check if someone has 1/2
        if yes => other one is 1
'''

def update_health_status(people_id):
    cursor.execute("UPDATE people SET health_status = 1 WHERE people_id = {}".format(people_id))
    # un-comment to verify update
    #cursor.execute("SELECT * FROM people WHERE people_id = {}".format(people_id))
    #result = cursor.fetchone()
    #print(result)

def add_notification(people_id):
    cursor.execute("SELECT people_id, phone_nb, health_status FROM people WHERE people_id = {}".format(people_id))
    result = cursor.fetchone()
    with open('msg_queue.txt', 'a') as f:
        f.write(str(result[0]) + ' ' + str(result[1]) + ' ' + str(result[2]) + '\n')
        f.close()


def update_all_health_status():
    cursor.execute("SELECT A.* FROM people A INNER JOIN (SELECT pos_x, pos_y FROM people GROUP BY pos_x, pos_y HAVING COUNT(*) > 1) B ON A.pos_x = B.pos_x AND A.pos_y = B.pos_y ")
    results = cursor.fetchall()
    for i in range(len(results)):
        if results[i][4] == 0:
            print(results[i])
            new_list = list(results[i])
            new_list[4] = 1
            print(new_list)
            update_health_status(new_list[0])
            add_notification(new_list[0])
            
delete_table("people")
create_database(100)
get_all_people(10)

try:
    i = 0
    while(True):
        print("---------------- Loop #" + str(i) + "--------------------")
        update_all_positions()
        update_all_health_status()
        print("---------------- END LOOP --------------------------------\n\n")
        i+=1
except KeyboardInterrupt:
    pass

connection.close()

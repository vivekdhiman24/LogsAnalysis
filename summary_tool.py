#!/usr/bin/env python3

# import psycopg2 module
import psycopg2

# What are the most popular three articles of all time?
sql_query1 = "select title,views from view_articles limit 3;"

# Who are the most popular article authors of all time?
sql_query2 = """select authors.name,sum(view_articles.views) as views from
view_articles,authors where view_articles.author = authors.id
group by authors.name order by views desc;"""

# On which days did more than 1% of requests lead to errors?
sql_query3 = "select * from view_log where \"Error %\" > 1;"


# returns result set for the executed query
def get_result_set(cursor, query):
    cursor.execute(query)
    result_set = cursor.fetchall()
    return result_set


def connect():
    """Connect to the PostgreSQL database. Returns a database connection """
    try:
        db = psycopg2.connect("dbname=news")
        cursor = db.cursor()
        return db, cursor
    except:  # exception while connecting to database
        print("Unable to connect to the database")

# returns a Connection and Cursor object
db, cursor = connect()

print("1. The 3 most popular articles of all time are:\n")
result_set = get_result_set(cursor, sql_query1)
for column in result_set:
    print('\t' + str(column[0]) + ' ---- ' + str(column[1]) + ' views')

print("\n2. The most popular article authors are:\n")
result_set = get_result_set(cursor, sql_query2)
for column in result_set:
    print('\t' + str(column[0]) + ' ---- ' + str(column[1]) + ' views')

print("\n3. Days with more than 1% of error requests are:\n")
result_set = get_result_set(cursor, sql_query3)
for column in result_set:
    print('\t' + str(column[0]) + ' ---- ' + str(column[1]) + ' % errors')

db.close()

from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

# import google.generativeai as genai



import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## drop the table
cursor.execute("DROP TABLE IF EXISTS STUDENT")

## Create the table structure
table_info='''Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);'''
cursor.execute(table_info)

## Insert Some more records

students = [
    ('Krish', 'Data Science', 'A', 90),
    ('Sudhanshu', 'Data Science', 'B', 100),
    ('Darius', 'Data Science', 'A', 86),
    ('Vikash', 'DEVOPS', 'A', 50),
    ('Dipesh', 'DEVOPS', 'A', 35)
]

cursor.executemany("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", students)

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()
## Configure Genai Key

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



# ## Function To Load Google Gemini Model and provide queries as response

# def get_gemini_response(question,prompt):
#     model=genai.GenerativeModel('gemini-pro')
#     response=model.generate_content([prompt[0],question])
#     return response.text

# ## Fucntion To retrieve query from the database

# def read_sql_query(sql,db):
#     conn=sqlite3.connect(db)
#     cur=conn.cursor()
#     cur.execute(sql)
#     rows=cur.fetchall()
#     conn.commit()
#     conn.close()
#     for row in rows:
#         print(row)
#     return rows

# ## Define Your Prompt
# prompt=[
#     """
#     You are an expert in converting English questions to SQL query!
#     The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
#     SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
#     the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
#     \nExample 2 - Tell me all the students studying in Data Science class?, 
#     the SQL command will be something like this SELECT * FROM STUDENT 
#     where CLASS="Data Science"; 
#     also the sql code should not have ``` in beginning or end and sql word in output

#     """


# ]

# ## Streamlit App

# st.set_page_config(page_title="I can Retrieve Any SQL query")
# st.header("Gemini App To Retrieve SQL Data")

# question=st.text_input("Input: ",key="input")

# submit=st.button("Ask the question")

# # if submit is clicked
# if submit:
#     response=get_gemini_response(question,prompt)
#     print(response)
#     response=read_sql_query(response,"student.db")
#     st.subheader("The REsponse is")
#     for row in response:
#         print(row)
#         st.header(row)
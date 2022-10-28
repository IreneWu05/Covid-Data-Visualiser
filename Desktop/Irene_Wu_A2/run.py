from flask import Flask, render_template, request
app = Flask(__name__)

#import database
import sqlite3

@app.route('/')
def index():
    #import map data
    active = []
    con = sqlite3.connect('citydata.db')
    cur = con.cursor()
    sql = 'SELECT Active from citydata WHERE ID BETWEEN 0 AND 16'

    data = cur.execute(sql)
    for item in data:
        active.append(' '.join(str(i) for i in item))#remove the brackets


    #values on the bar
    Value = []
    con = sqlite3.connect('activedata.db')
    cur = con.cursor()
    sql = 'SELECT Value from data WHERE ID IN ( 749, 752, 751, 747)'
    data1 = cur.execute(sql)
    for item in data1:
        Value.append(item)

    #graph1, bar graph, monthly active cases
    graph1 = []
    con = sqlite3.connect('activedata.db')
    cur = con.cursor()
    sql = 'SELECT Value from data WHERE ID IN (225,294,369,429,504,570,630,708,743,747)'
    #752 OR ID = 739 OR ID = 706 OR ID = 628 OR ID = 568 OR ID = 502 OR IN = 427 OR ID = 367
    
    data2 = cur.execute(sql)
    for item in data2:
        graph1.append(' '.join(str(i) for i in item))#remove the brackets


    #graph2 - linear graph, anually active cases by month
    graph2 = []
    con = sqlite3.connect('data-fullrange.db')
    cur = con.cursor()
    sql = 'SELECT Value from data WHERE ID IN (4,97,187,280,370,463,556,646,739,829,892,  934,1003, 1078,1147,1225,1300,1378,1456,1534,1609,1681,1753,  1819,1888,1963,2023,2098,2164,2224,2302,2335,2346)'

    data3 = cur.execute(sql)
    for item in data3:
        graph2.append(' '.join(str(i) for i in item))#remove the brackets

    cur.close()
    con.close()
    return render_template('index.html',Value=Value, graph1=graph1, graph2=graph2, active=active)
from django.shortcuts import render, redirect
from pathlib import Path
import sqlite3
from sqlite3 import Error
from datetime import date
from django.contrib import messages
from json import dumps

BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
def creategraph(request):
    if request.method == 'POST' and 'addbutton' in request.POST:
        jikan = request.POST['jikan']
        point = request.POST['point']
        contentvi = request.POST['contentvi']
        contentja = request.POST['contentja']
        if len(jikan.strip()) > 0:
            rows = None
            try:
                conn = sqlite3.connect(BASE_DIR / 'Database/database.db')
                cur = conn.cursor()
                query = 'SELECT * FROM GRAPH WHERE JIKAN = \"' + jikan + '\"'
                cur.execute(query)
                rows = cur.fetchall()
                conn.close()
            except Error as e:
                print(e)
            if len(rows) > 0:
                try:
                    conn = sqlite3.connect(BASE_DIR / 'Database/database.db')
                    cur = conn.cursor()
                    query = 'UPDATE GRAPH SET JIKAN = \"' + jikan + '\", POINT = ' + point + ', CONTENTVI = \"' + contentvi + '\", CONTENTJA = \"' + contentja + \
                            '\" WHERE JIKAN = \"' + jikan + '\"'
                    cur.execute(query)
                    conn.commit()
                    conn.close()
                except Error as e:
                    print(e)
            else:
                try:
                    conn = sqlite3.connect(BASE_DIR / 'Database/database.db')
                    cur = conn.cursor()
                    if point != '':
                        query = 'INSERT INTO GRAPH VALUES (\"' + jikan + '\", ' + point + ', \"' + contentvi + '\", \"' + contentja + '\")'
                    else:
                        query = 'INSERT INTO GRAPH (JIKAN) VALUES (\"' + jikan + '\")'
                    cur.execute(query)
                    conn.commit()
                    conn.close()
                except Error as e:
                    print(e)
    rows = None
    try:
        conn = sqlite3.connect(BASE_DIR / 'Database/database.db')
        cur = conn.cursor()
        query = 'SELECT * FROM GRAPH'
        cur.execute(query)
        rows = cur.fetchall()
        conn.close()
    except Error as e:
        print(e)
    if len(rows) > 0:
        data = {}
        for row in rows:
            data[row[0]] = [row[1], row[2], row[3]]
        data = dumps(data)
        context = {
            'data': data,
        }
        return render(request, 'creategraph.html', context)
    return render(request, 'creategraph.html')

def motivation(request):
    return redirect('/motivationgraph/vi')

def motivation_vi(request):
    if request.method == 'POST':
        if 'language_ja' in request.POST:
            return redirect('/motivationgraph/ja')
    rows = None
    try:
        conn = sqlite3.connect(BASE_DIR / 'Database/database.db')
        cur = conn.cursor()
        query = 'SELECT * FROM GRAPH'
        cur.execute(query)
        rows = cur.fetchall()
        conn.close()
    except Error as e:
        print(e)
    if len(rows) > 0:
        data = {}
        for row in rows:
            data[row[0]] = [row[1], row[2], row[3]]
        data = dumps(data)
        context = {
            'data': data,
        }
        return render(request, 'motivationvi.html', context)
    return render(request, 'motivationvi.html')

def motivation_ja(request):
    if request.method == 'POST':
        if 'language_vi' in request.POST:
            return redirect('/motivationgraph/vi')
    rows = None
    try:
        conn = sqlite3.connect(BASE_DIR / 'Database/database.db')
        cur = conn.cursor()
        query = 'SELECT * FROM GRAPH'
        cur.execute(query)
        rows = cur.fetchall()
        conn.close()
    except Error as e:
        print(e)
    if len(rows) > 0:
        data = {}
        for row in rows:
            data[row[0]] = [row[1], row[2], row[3]]
        data = dumps(data)
        context = {
            'data': data,
        }
        return render(request, 'motivationja.html', context)
    return render(request, 'motivationja.html')

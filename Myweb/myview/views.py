# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
import pymysql
# Create your views here.

def index(request):
    return render(request,"index.html")
def search(request):
    conn = pymysql.connect(host='localhost',port=3306,user="root",password="yjcGNN199726",database="Klebsiella")
    cur = conn.cursor()
    if request.POST:
        content = str(request.POST["name"])
        SQL = 'SELECT Name, USA, Type, Length, GC, Organism, Description FROM Klebsiella WHERE Name like "%'+content+'%"'
        cur.execute(SQL)
        items = cur.fetchall()
        results = []
        for item in items:
        	results.append({"USA":item[1],"Name":item[0],"Type":item[2],"Length":item[3],"GC":item[4],"Organism":item[5],"Description":item[6]})
        count = len(items)
        if count <> 0:
        	return render(request, "search.html", {"flag":"1","results":results, "count":count})
        else:
        	return render(request, "search.html", {"flag":"2", "content":content})
    return render(request, "search.html")
def about(request):
	return render(request, "contact.html")
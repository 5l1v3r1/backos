#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json
import string
import random
import re
import sqlite3
FN = ""
class S(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header("Access-Control-Allow-Origin", "*");
        self.send_header("Access-Control-Allow-Credentials", "true");
        self.send_header("Access-Control-Allow-Methods", "GET,HEAD,OPTIONS,POST,PUT");
        self.send_header("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Header,Access-Control-Allow-Origin");
        self.end_headers()
        self.wfile.write("1")
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*");
        self.send_header("Access-Control-Allow-Credentials", "true");
        self.send_header("Access-Control-Allow-Methods", "GET,HEAD,OPTIONS,POST,PUT");
        self.send_header("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Header,Access-Control-Allow-Origin");
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        self._set_headers()
        #print(type(post_data))
        data = json.loads(post_data)
        #print(post_data)
        global FN
        if "fn" in data:
            FN = data["fn"]
            #print(data["fn"]);
        else:
            #print("fn:" + FN)
            if(len(FN)>0):
                self.write_to_file(FN,data["html"])
        self.wfile.write(post_data)
    def write_to_file(self,fn,post_data):
        fnnew = fn.replace(".pdf",".html")
        resdata = post_data.replace("<br>\n"," ")
        f = open('output/'+fnnew,'w')
        resdata = resdata.encode('ascii', 'ignore')
        resdata,keys = self.addtage(resdata)
        f.write('<blockquote><p><i class="fa fa-tags" aria-hidden="true"></i> '+ keys +' - </p></blockquote>\n<h3>TITLE</h3>\n')
        f.write(resdata)
        f.close();
        pass
    def addtage(self,html):
        '''
    	tags = {
        " c ":["/category/czuoyedaixie/","C语言代写 C++代写 代写C++ 代做C"],
        "java":["/category/java/","java代写 代写java "],
        "swing":["/tag/swing/","swing代写 GUI代写 java代写 代写java"],
        "c++":["/category/czuoyedaixie/","C++语言代写 C++代写 代写C++ 代做C"],
        "c#":["/tag/csharp/","C#代写 代写c# 代写.net"],
        "Asp":["/tag/asp/","asp代写 代写asp 代写.net "],
        "unity":["/tag/unity/","unity代写 代写unity 代写3D unity"],
        "D3":["/tag/d3-js","d3.js代写 代写d3.js 代写d3.js  "],
        "Python":["/category/python/","python代写 代写python "],
        "Network":["/category/networkzuoyedaixie/","network代写 代写计算机网络"],
        "Data structure":["/category/data-structure-assignment/","数据结构代写 代写数据结构 Data structure代写 算法代写"],
        "oracle":["/tag/oracle/","数据库代写 代写oracle oracle代写"],
        "mysql":["/tag/mysql/","mysql代写 代写mysql mysql代写"],
        "database":["/category/databasezuoyedaixie/","数据库代写 代写数据库 database代做 sql代写"],
        "Mongo":["/tag/mongodb/","mongodb代写 代写mongodb 数据库代写"],
        "sql":["/tag/sqlzuoyedaixie/","sql代写 代写sql 数据库代写"],
        "oop":["/tag/oop代写/","OOP代写 代写oop"],
        "javafx":["/tag/javafx代写/","javafx代写 代写javafx gui代写 图形编程 java代写 代写java"],
        "shell":["/tag/linux-shell代写/","shell代写代写 代写shell bash代写"],
        "thread":["/category/multi-threading-daixie/","多线程代写 代写多线程 multi-threading代写"],
        "web":["/category/webdaixie/","web代写 代写web 网站代写"],
        "html5":["/tag/html5代写/","html5代写 代写html5 网页设计 网页代写"],
        "html":["/tag/html代写/","html代写 代写html 网站代写 网页代写"],
        "javascript":["/tag/js/","js代写 代写js javascript代写 代写javascript"],
        "jquery":["/tag/jquery/","jquery代写 代写jquery jquery代写 代写jquery"],
        "css":["/tag/css/","css代写 代写css 网页代做"],
        "nodejs":["/tag/nodejs代写/","nodejs代写 代写nodejs"],
        "php":["/tag/phpdaixie/","php代写 代写php web代做 代做web web开发"],
        "Android":["/tag/android代写/","android代写 代写android 移动开发 安卓代写"],
        "Swift":["/tag/ios代写/","ios代写 代写ios swift代写 移动开发 苹果代写"],
        "ios":["/tag/ios代写/","ios代写 代写ios swift代写 移动开发 苹果代写"],
        "Algorithm":["/category/algorithmdaixie/","算法代写 代写算法 Algorithm代写 代写Algorithm  算法作业代写"],
        "matlab":["/tag/matlab代写/","matlab代写 代写matlab"],
        "Machine learning":["/category/machinelearningdaixie/","机器学习代写 代做机器学习 ai代做 machine learning代写 ML代做"],
        "AI":["/category/aizuoyedaixie/","AI代写 代做机器学习 ai代做 machine learning代写 ML代做"],
        "spark":["/tag/spark/","spark代写 代做spark 大数据代写 bigdata代写"],
        "Operating Systems":["/tag/caozuoxitongzuoyedaixie/","操作系统代写 代做操作系统 OS代写 Operating System代写"],
        "Operating System":["/tag/caozuoxitongzuoyedaixie/","操作系统代写 代做操作系统 OS代写 Operating System代写"],
        "Data Structures": ["/category/data-structure-assignment/","数据结构代写 代做数据结构 算法代写 "],
        "shell":["/tag/linux-shell代写/","shell代写代写 代写shell"],
        "scala":["/tag/scala代写/","scala代写 代写scala 大数据代写 big data代做"],
        "math":["/tag/math代写/","math代写 代写math 数学代做"],
        "assignment":["/category/assignmentzuoyedaixie/","ass代做 assignment代写 代写assignment"],
        "lab":["/category/lab代写/","lab代写 代写lab"],
        "project":["/category/project代写/","project代写 代写project"],
        "homework":["/category/cshomework/","homework代写 代写homework hw代做"],
        "Haskell":["/tag/haskell/","haskell代写 代写haskell"],
        "racket":["/tag/racket代写/","racket代写 代写racket lisp代做"],
        "Mvc":["/tag/mvc/","MVC代写 代写MVC"],
        "GUI":["/tag/gui代写/","GUI代写 代写GUI"],
        "postgresql":["/tag/postgresql/","postgresql代写 代写postgresql database代做 sql代写"],
        "hadoop":["/tag/hadoop代写/","hadoop代写 代做hadoop 大数据代写 代做大数据 big data代做"],
        "neo4j":["/tag/neo4j/","neo4j代做 代写neo4j database代做"],
        "redis":["/tag/redis代做/","redis代做 database代写 代写database"],
        "react":["/tag/reactjs代写/","reactjs代写 js代写 前端代写 web代写"],
        "express":["/tag/express/","express代写 代写express nodejs代做 web代写"],
        "aws":["/tag/aws/","aws代写 代做aws bigdata代做 大数据代写"],
        "vue":["/tag/vue/","js代写 vue代写 vue.js代写 web代写 javascript代写"],
        "pygame":["/tag/pygame/","pygame代写 gui代写 代做gui python代写 图形界面编程"],
        "scheme":["/tag/scheme/","scheme代写 代做scheme"],
        "tkinter":["/tag/tkinter/","tkinter代写 gui代写 python代做"],
        "pyqt":["/tag/pyqt/","pyqt代写 代做pyqt python代写 gui代写"],
        "angular":["/tag/angularjs代写/","angularjs代写 angularjs代做 web代写 js代写 javascript代做"],
        "Objective":["/tag/objective-c/","Objective-c代写 代写Objective-c 代写swift app代做 ios代做"],
        "big data":["/tag/big-data/","big data代写 大数据代写"],
        "security":["/tag/security代写/","security代做 网络安全 网安代写 计算机网络安全"],
        "x86":["/tag/x86汇编代写/","x86汇编代写 汇编代写 assembly"],
        "mips":["/tag/mips汇编代写/","mips汇编代写 代写汇编 assembly"],
        "arm":["/tag/arm/","arm代写 汇编代写 代写arm assembly"],
        "assembly":["/tag/assembly/","assembly代写 汇编代写 代写assembly"],


        "bash":["/tag/bash/","bash代写 linux shell 代做 script代写"],
        "uml":["/tag/uml代做/","UML代写 OOP编程 面向对象代做"],
        "Artificial Intelligence":["/category/aizuoyedaixie/","AI代写 代做机器学习 ai代做 machine learning代写 ML代做"],
        "app":["/tag/app代写/","app代写 代写app 移动开发"],

        }'''
        conn = sqlite3.connect('../../sendWP.db')
        cursor = conn.cursor()
        cursor.execute('select * from pdftags')
        values = cursor.fetchall()
        #print values
        tags = {}
        for item in values:
            tags[item[1]] = [item[2],item[3]]
            #print tags
            #break
        cursor.close()
        somestrs = ["","代写","代做","作业","代写","代做",""]
        keys=[]
        for key in tags:
            if re.search(re.escape(key+" "),html,re.IGNORECASE):
                reg = re.compile(re.escape(key+" "), re.IGNORECASE)
                tmp = '<a href=\"'+ tags[key][0]+'\" title=\"'+ tags[key][1]+'\"> '+ key+' </a>'	#'<a href=\"'+ tags[key][0]+'\" title=\"'+ tags[key][1]+'\">'+ key+'</a>'
                html = reg.sub(tmp,html,1)
                if random.randint(0,1) == 0:
                    print(key)
                    print(string.capwords(key))
                    keys.append(string.capwords(key))
                    #keys.append(string.capwords(key)+str(somestrs[random.randint(0,len(somestrs)-1)]))
                else:
                    keys.append(string.capwords(key))
                    print(str(somestrs[random.randint(0,len(somestrs)-1)]))
                    #keys.append(str(somestrs[random.randint(0,len(somestrs)-1)]) + string.capwords(key))
        print("|".join(keys))
        return html,(" | ".join(keys))

def run(server_class=HTTPServer, handler_class=S, port=6001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv
    #print("123")
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

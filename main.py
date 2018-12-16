from flask.views import MethodView
from flask import Flask
from flask import render_template
from flask import request
import config
import re 
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import json

host = config.host
user = config.user
passwd = config.passwd
db = config.db

regex = re.compile(r'[^a-zA-Z0-9]')

app = Flask(__name__)

class HostAPI(MethodView):

    def get(self):
        errorMSg = "No host Found"
        #return render_template('error.html',errMsg=errorMSg)
        return render_template('index.html',data={})

    def post(self):
        form_hostname = request.form['hostname']
        hostname = form_hostname.strip()
        print (hostname)
        data=[]
        """
        if (regex.search(hostname) == None):
            dbs = MySQLdb.connect(host,user,passwd,db)
            sql_query = config.query(hostname)
            cur = dbs.cursor()
            count = cur.execute(sql_query)
            if count > 0:
                data = cur.fetchall()
            else:
                return hostname+" - Unable to find information"
        else:
            return hostname+" - Invalid Hostname, please check the server name"
        """
        return render_template('hostinfo.html',data=data)

class ServerAPI(MethodView):

    def get(self):
        data=[]
        hostname = request.args.get('hostname')
        dbs = MySQLdb.connect("localhost","mahesh","password","servers")
        sql_query = "select server_name as value from servers where server_name like '%{0}%'".format(hostname)
        cur = dbs.cursor(MySQLdb.cursors.DictCursor)
        count = cur.execute(sql_query)
        if count:
            data = cur.fetchall()
        return json.dumps(data)

app.add_url_rule('/', view_func=HostAPI.as_view('index'))
app.add_url_rule('/searchhost', view_func=ServerAPI.as_view('searchhost'))


if __name__ == '__main__':
    app.run()

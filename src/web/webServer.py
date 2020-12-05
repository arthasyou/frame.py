import tornado.ioloop
import tornado.web
import json
import datetime
from db.mysql import m


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        a = tornado.escape.json_decode(self.request.body)
        print(a)
        query = m.select('roominfo')+m.where([('id', '=', 13927)])
        (_,data) = m.fetch(query)
        # a = self.get_body_argument('a')
        # print(a)
        # a = self.get_argument('a')
        # # print(a)
        
        d = data[0]
        # print(d)
        d['param'] = json.loads(d['param'])
        d['player_data'] = json.loads(d['player_data'])
        d['create_time'] = '2020-11-14 00:30:51'
        d['code'] = 0
        

        # print(d['create_time']())

        # c = json.dumps(data[0])
        b = {'b':1}
        self.write(json.dumps(d))

def make_app():
    return tornado.web.Application([
        (r"/api/guildrecord/player_record_3days", MainHandler),
    ])

# if __name__ == "__main__":
app = make_app()
app.listen(9999)


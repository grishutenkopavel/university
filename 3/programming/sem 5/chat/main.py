import tornado.ioloop
import tornado.web
import tornado.websocket

clients = []
savingMassages = []

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class WebSock(tornado.websocket.WebSocketHandler):
    
    def open(self):
        print("WebSocket opened")
        clients.append(self)
        for mes in savingMassages:
            self.write_message("you: "+mes)
    
    def on_message(self, message):
        savingMassages.append(message)
        print(savingMassages)
        for client in clients:
            client.write_message("you: "+message)

    def on_close(self):
        clients.remove(self)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", WebSock),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
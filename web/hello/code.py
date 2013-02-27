import web

urls = (
    '/','index',
    '/add','index'
)

app = web.application(urls,globals())
render = web.template.render("templates/")

class index:
    def GET(self,name=None):
        return render.index(name)
       # return "Hello World!"
    def POST(self):
        post_data = web.input()
        return 'you post '+post_data.t+' to the server '

if __name__ == "__main__":app.run()
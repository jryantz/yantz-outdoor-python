import os
import web

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)

if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 8080))
    # app.run(host='0.0.0.0', port=port)
    app.run()

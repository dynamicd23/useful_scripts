from bottle import route, run

@route('/')
def hello():
    return "Welcome to my bottle!"

run(host='192.168.2.5', port=8888)

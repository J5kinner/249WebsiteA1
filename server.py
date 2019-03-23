from bottle import template, static_file, route, run, get

@get('/comp249')
def whatever():
    return template('index', title='Joe')

@get('/styles.css')
def stylesheets():
    return static_file('styles.css', root='css/')
@get('/files/<filename>')
def server_file(filename):
    return static_file(filename, root='files/')

run(host='localhost', port=5000, debug=False)

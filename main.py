from website import create_app


app = create_app()

if __name__ == '__main__':     #main is the name of the file main.py, hence this always is true __name__ means current file name
    app.run(debug = True)      #reruns server whenever the python code is changed.  
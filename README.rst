1.  To install the server, first copy the contents of js_example in a directory.
2.  Install a python virtual environment in js_exmaple. http://flask.pocoo.org/docs/1.0/installation/
3.  Install Vienna RNA in <virtual environment>/Scripts folder.
4.  Set the virtual environment variables $env:FLASK_ENV="development" for debug mode. Default is production.
5.  Set the startup app in $env:FLASK_APP = "__init__.py".
6.  Run <virtual environment>/Scripts/activate to activate the virtual environment.
7.  Run flask (python -m flask run in Windows) to run the flask app.
8.  The html pages are present in templates folder. Base is the base template.
9.  The CSS and JS for our pages and forna is present in static folder.
10. The different pages and route information is present in "views.py".
11. The output file is written in J<timestamp>.output file. If you give the same name in the URL as http://localhost:5000/output/J<timestamp>, you can see the output results.

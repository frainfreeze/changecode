# changecode
This repository contains code that solves <ChangeCode> hackaton by King ICT challenge. 
- [solver.bash](https://raw.githubusercontent.com/frainfreeze/changecode/master/solver.bash) solves task by task using cURL (we initially finished challenge this way)
- additionally we made a [web interface](https://changecode.herokuapp.com/) for the challenge

<br><br>



## Setting up web interface locally

Make sure you have [Python](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installing/) installed.

```bash
git clone https://github.com/frainfreeze/changecode.git
cd changecode
pip install -r requirements.txt
python app.py
```

The webserver should now be running on http://localhost:5000. Editing app.py will cause cherrypy to reload itself.

## Deploying to Heroku

Install the [Heroku toolbelt](https://toolbelt.heroku.com/), and make sure you commit your changes to git. Now you can deploy:

```bash
heroku create
git push heroku master
```

If all goes well, you can open your app in the browser:

```bash
heroku open
```
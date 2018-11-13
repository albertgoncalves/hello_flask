# Hello, Flask!

First foray into Flask. Trying, for now, to hold off from using `Class` and `@`.

Needed things
---
  * [Nix](https://nixos.org/nix/)
  * [SQLite Sample Database](http://www.sqlitetutorial.net/sqlite-sample-database/)

Making moves
---
```bash
$ curl http://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip > chinook.zip
$ unzip chinook.zip -d ./
$ nix-shell
```
```
$ python hello_flask.py
 * Serving Flask app "hello_flask" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5002/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 ...
```

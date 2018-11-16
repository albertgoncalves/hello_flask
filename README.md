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
 ...
```

The fruits of our labor
---
  * <http://localhost:5002/>
  * <http://localhost:5002/index>
  * <http://localhost:5002/blob/foo>
  * <http://localhost:5002/now>
  * <http://localhost:5002/user/yourname>
  * <http://localhost:5002/user/query/4>

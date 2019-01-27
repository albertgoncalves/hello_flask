# QR code API

Simple sketch of _something like_ a QR code API pipeline.

Needed things
---
  * [Nix](https://nixos.org/nix/)
  * `../shell.nix`
  * Local IP address

Making moves
---
Create a file named `ip` with your local IP address. Something like this would do the trick:
```bash
$ echo 123.456.7.89 > ip
```

```bash
$ cd ../ && nix-shell
[nix-shell:~/hello_flask]$ cd api_demo/
```

```bash
[nix-shell:~/hello_flask/api_demo]$ python qr.py
[nix-shell:~/hello_flask/api_demo]$ sh init_db.sh
[nix-shell:~/hello_flask/api_demo]$ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 ...
```

Running `qr.py` should have created `qr.png`; scanning this file will produce a URL. Visit the URL to insert a timestamped row into the newly minted `sqlite3` database through the API-esque pipeline being served up in `server.py`.

If everything worked...
---
```bash
[nix-shell:~/hello_flask/api_demo]$ sqlite3 qr.db
```
```
sqlite> SELECT * FROM qrs;
```

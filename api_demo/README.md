# QR code API

Simple sketch of _something like_ a QR code API pipeline.

Needed things
---
  * [Nix](https://nixos.org/nix/)
  * `../shell.nix`

Making moves
---
```bash
$ cd ../ && nix-shell
```
```bash
$ cd api_demo/
$ python qr.py
```
```bash
$ sh init_db.sh
```
```bash
$ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 ...
```

Running `qr.py` should have created `qr.png`; scanning this file will produce a URL. Visit the URL to insert a timestamped row into the newly minted `sqlite3` database through the API-esque pipeline being served up in `server.py`.

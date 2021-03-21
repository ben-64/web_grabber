# Introduction

Some tiny tools, that might help when grabbing the content of a web server.

# Scripts

## har_extract_uri.py

This script is used to extract uri from `har` file that can be generated from the `inspect` menu of chrome (on the network tab).

```bash
$ ./har_extract_uri.py --root https://www.example.com file.har > uri.txt
```

## wget_uri.sh

This script is used to download with `wget` some uri from a website.

```bash
$ ./wget_uri.sh uri.txt https://www.example.com
```

## webserver.py

This script acts has a tiny webserver that is going to write every 404 uri inside a text file, in order to download those missing uri later. Its listens on port 8000.

```bash
$ ./webserver.py --output 404.txt
```

A certificate and a key can also be passed to the commande line, in order to act as an HTTPS server.

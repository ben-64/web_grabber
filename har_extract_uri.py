#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import argparse
from pprint import pprint

def parse_args():
    """ Parse command line arguments """
    parser = argparse.ArgumentParser(description="Description of python program")
    parser.add_argument("har",metavar="HAR_FILE",nargs="?")
    parser.add_argument("--root","-r",metavar="ROOT",type=lambda u:u.strip("/"),help="Website root")
    return parser.parse_args()

def extract_url_har(har):
    r = []
    with open(har,"r") as f:
        j = json.load(f)
        for entry in j["log"]["entries"]:
            r.append(entry["request"]["url"])
    return r


def split_url(url,root):
    return url[len(root):]

def main():
    """ Entry Point Program """
    args = parse_args()

    for url in extract_url_har(args.har):
        if args.root in url:
            print(split_url(url,args.root))

    return 0


if __name__ == "__main__":
   sys.exit(main())

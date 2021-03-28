#!/bin/bash

[ $# -ne 2 ] && echo "Usage: $0 file url" && exit 1

URI=$1
URL=$2

while read line; do
   wget -x -nH -nc $URL/${line}
done < $URI

exit 0

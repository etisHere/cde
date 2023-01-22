#!/usr/bin/env sh
#
#This will download wallpapers from search. 
#This is a example from BugsWritter Youtube. (https://www.youtube.com/@bugswriter_)
#
read -p "Search: " file
page=1;
while [ $page -lt 7 ] ; do curl -s "https://wallhaven.cc/api/v1/search?q=$search&page=$page" | jq '.data[].path' | xargs -I{} wget {} ; page=$((page+1)) ; done

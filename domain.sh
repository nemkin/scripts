#!/bin/bash 
 
# Name: Check for domain name availability 
# linuxconfig.org 
# Please copy, share, redistribute and improve 
 
if [ "$#" == "0" ]; then 
    echo "You need to supply at least one argument!" 
    exit 1
fi 
 
DOMAINS=('.com')
 
ELEMENTS=${#DOMAINS[@]} 
 
while (( "$#" )); do 
 
  for (( i=0;i<$ELEMENTS;i++)); do 
      whois $1${DOMAINS[${i}]} | egrep -q \
      '^No match|^NOT FOUND|^Not fo|AVAILABLE|^No Data Fou|has not been regi|No entri' 
	  if [ $? -eq 0 ]; then 
	      echo "$1${DOMAINS[${i}]} : available" 
	  fi 
  done 
 
shift 
 
done 

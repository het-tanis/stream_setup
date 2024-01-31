#!/bin/bash

#Input a number
read -n 1 -t 10 -p "Make your selection from the items below
You have 10 seconds

1. Tell me a joke and exit
2. Go to the dungeons
3. Exit
" input

case $input in

1 )
  echo "Loading a joke"
  #curl command against an api for jokes
  /bin/curl -k 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt'
  sleep 5
  ;;
2 )
  echo "You are being sent to the dungeon"
  /bin/ssh -l inmate 192.168.200.2
  ;;
3 )
  echo "Have a good day"
  exit 0;
  ;;
* )
  echo "You have not entered a valid input"
  echo "You get a joke and you get to leave"
  /bin/curl -k 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt'
  exit 0;
  ;;

esac

exit 0;

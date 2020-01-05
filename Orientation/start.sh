#! /bin/sh

while true; do
  python Orientation.py
  if [ $? -eq 0 ]
  then
    emulationstation --screenrotate 3
  else
    emulationstation
  fi
done


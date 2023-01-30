#!/bin/sh
echo "Enter your option"
echo "1. Python"
echo "2. Python_Test"
echo "3. C++"
read pass
if [ $pass -eq 1 ]
then
  python 'Exercise 1'/Ex1Py.py
  # python 'Exercise 1'/Prueba.py
elif [ $pass -eq 2 ] 
then
  python 'Exercise 1'/Prueba.py
  #echo "Choose a corre" 
else
  echo "Choose a corret option" 
fi

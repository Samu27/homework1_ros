#!/bin/bash

# Avvio roscore
xterm -hold -e roscore &

# Attesa 2 secondi
sleep 2s

# Avvio nodo talker
xterm -hold -e "rosrun homework1_ros talker.py" &
# Avvio nodo filter
xterm -hold -e "rosrun homework1_ros filter.py" & 
# Avvio nodo listener
xterm -hold -e "rosrun homework1_ros listener.py" &

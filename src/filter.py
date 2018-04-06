#!/usr/bin/env python2
#coding=utf-8

import rospy
from std_msgs.msg import String
import sys
import signal


def signal_term_handler(signal, frame):
  '''Handles KeyboardInterrupts to ensure smooth exit'''
  print("\n")
  rospy.logerr('User Keyboard interrupt')
  sys.exit(0)

def filter():
	pub = rospy.Publisher('filter', String, queue_size=10)
	rospy.init_node('Filter', anonymous=True)

	while True:
		choice = raw_input('''\nDigitare:
\t- 'a' verrà stampato tutto il messaggio
\t- 'n' mostrerà solo il nome
\t- 'e' mostrerà solo l’età
\t- 'c' mostrerà solo il corso di laurea
\t- '0' terminerà filter MA non talker e listener.
>>> ''')
		if choice in ("e", "n", "a", "c"):
			rospy.loginfo(choice)
			pub.publish(choice)
		if choice == "0":
			exit(0)


if __name__ == '__main__':
	signal.signal(signal.SIGINT, signal_term_handler)
	signal.signal(signal.SIGQUIT, signal_term_handler)
	signal.signal(signal.SIGTSTP, signal_term_handler)
	filter()

#!/usr/bin/env python2
#coding=utf-8

'''
Nodo filter.
Invia sul topic "filter" la modalita' di stampa scelta dall'utente.
'''

import rospy
from std_msgs.msg import String
import sys
import signal


def signal_term_handler(signum, frame):
  ''' Gestisce gli interrupt da tastiera '''
  print('\n')
  rospy.logerr('User Keyboard interrupt')
  sys.exit(128+signum)


def filter():
	''' Nodo filter '''
	pub = rospy.Publisher('filter', String, queue_size=10)
	rospy.init_node('Filter', anonymous=True)

	while True:
		# Menu
		choice = raw_input('''\nDigitare:
\t- 'a' per stampare tutto il messaggio
\t- 'n' per stampare solo il nome
\t- 'e' per stampare solo l’eta'
\t- 'c' per stampare solo il corso di laurea
\t- '0' per terminare il nodo filter.
>>> ''')

		if choice in ("a", "n", "e", "c"):
			rospy.loginfo(choice)
			pub.publish(choice)
		if choice == "0":
			exit(0)


if __name__ == '__main__':
	# Settaggio handler dei segnali
	signal.signal(signal.SIGINT, signal_term_handler)
	signal.signal(signal.SIGQUIT, signal_term_handler)
	signal.signal(signal.SIGTSTP, signal_term_handler)

	try:
		filter()
	except rospy.ROSInterruptException:
		pass
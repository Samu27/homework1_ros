#!/usr/bin/env python2

import rospy
from std_msgs.msg import String


def filter():
	pub = rospy.Publisher('filter', String, queue_size=10)
	rospy.init_node('filter', anonymous=True)

	while True:
		choice = raw_input('''\nDigitare:
\t• 'a' verrà stampato tutto il messaggio
\t• 'n' mostrerà solo il nome
\t• 'e' mostrerà solo l’età
\t• 'c' mostrerà solo il corso di laurea
\t• '0' terminerà filter MA non talker e listener.
>>> ''')
		if choice in ("e", "n", "a", "c"):
			rospy.loginfo(choice)
			pub.publish(choice)
		if choice == "0":
			exit(0)


if __name__ == '__main__':
	filter()

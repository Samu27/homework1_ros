#!/usr/bin/env python2
#coding=utf-8

'''
Nodo listener.
Riceve messaggi dai topic "students" e "listener" e stampa i dati filtrati.
'''

import rospy
from homework1.msg import Student
from std_msgs.msg import String


print_mode = "a"


def callback_students(data):
	''' Callback del tocpi students'''
	if print_mode == "a":
		rospy.loginfo('Info studente:\n nome:\t\t{}\n eta:\t\t{} \
			\n corso laurea:\t{}\n'.format(data.nome, \
				data.eta, data.corso_laurea))
	if print_mode == "n":
		rospy.loginfo('Info studente:\n nome:\t\t{}\n'.format(data.nome))
	if print_mode == "e":
		rospy.loginfo('Info studente\n eta:\t\t{}\n'.format(data.eta))
	if print_mode == "c":
		rospy.loginfo('Info studente\n corso laurea:\t{}\n'.format(data.corso_laurea))
	

def callback_filter(data):
	''' Callback del topic filter '''
	rospy.loginfo("Print_mode = %s\n", data.data)

	# Cambia modilita' di stampa
	global print_mode
	print_mode = data.data


def listener():
	''' Nodo listener '''
	rospy.init_node('Listener', anonymous=True)

	rospy.Subscriber("students", Student, callback_students)
	rospy.Subscriber("filter", String, callback_filter)

	rospy.spin()


if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass

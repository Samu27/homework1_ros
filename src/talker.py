#!/usr/bin/env python2

'''
Nodo talker.
Invia Student, generati casualmente, sul topic "student".
'''

import rospy
import random_student
from homework1.msg import Student


def talker():
	''' Nodo talker '''
	student = Student()

	pub = rospy.Publisher('students', Student, queue_size=10)
	rospy.init_node('Talker', anonymous=True)
	rate = rospy.Rate(1) # 1hz -> 1sec

	while not rospy.is_shutdown():
		# Generazione studente casuale
		student = random_student.randStudent()

		rospy.loginfo('Info studente:\n nome:\t\t{}\n eta:\t\t{}\
			\n corso laurea:\t{}\n'.format(student.nome, \
				student.eta, student.corso_laurea))

		pub.publish(student)
		rate.sleep()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass

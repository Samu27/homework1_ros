#!/usr/bin/env python2

import rospy
import random_student
from homework1.msg import Student


def talker():
	student = Student()

	pub = rospy.Publisher('students', Student, queue_size=10)
	rospy.init_node('Talker', anonymous=True)
	rate = rospy.Rate(1) # 1hz -> 1sec

	while not rospy.is_shutdown():
		student = random_student.randStudent()

		rospy.loginfo(student)
		pub.publish(student)
		rate.sleep()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass

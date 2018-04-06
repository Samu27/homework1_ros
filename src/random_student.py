#!/usr/bin/env python2

from homework1.msg import Student
from random import randint, seed
from time import time


def randName():
	global names
	return names.get(randint(1,30))


def randAge():
	return randint(20,70)


def randDegreeCourse():
	global deegree_courses
	return deegree_courses.get(randint(1,20))


def randStudent():
	seed(time())

	student = Student()
	student.nome = randName()
	student.eta = randAge()
	student.corso_laurea = randDegreeCourse()
	return student


names = {
	1:"Sofia",
	2:"Aurora",
	3:"Giulia",
	4:"Emma",
	5:"Giorgia",
	6:"Martina",
	7:"Alie",
	8:"Greta",
	9:"Ginevra",
	10:"Chiara",
	11:"Anna",
	12:"Sara",
	13:"Beatrice",
	14:"Nicole",
	15:"Gaia",
	16:"Francesco",
	17:"Alessandro",
	18:"Leonardo",
	19:"Lorenzo",
	20:"Mattia",
	21:"Andrea",
	22:"Gabriele",
	23:"Matteo",
	24:"Tommaso",
	25:"Riccardo",
	26:"Edoardo",
	27:"Giuseppe",
	28:"Davide",
	29:"Antonio",
	30:"Federico"}


deegree_courses= { 
	1:"Laurea in Beni culturali",
	2:"Laurea in Bioinformatica",
	3:"Laurea in Biotecnologie",
	4:"Laurea in Economia Aziendale",
	5:"Laurea in Economia e Commercio",
	6:"Laurea in Filosofia",
	7:"Laurea in Fisioterapia",
	8:"Laurea in Infermieristica",
	9:"Laurea in Informatica",
	10:"Laurea in Lettere",
	11:"Laurea in Lingue e culture per il turismo e il commercio internazionale",
	12:"Laurea in Lingue e culture per l'editoria",
	13:"Laurea in Lingue e letterature straniere",
	14:"Laurea in Logopedia",
	15:"Laurea in Matematica Applicata",
	16:"Laurea in Scienze dei servizi giuridici",
	17:"Laurea in Scienze della comunicazione",
	18:"Laurea in Scienze dell'educazione",
	19:"Laurea in Scienze e tecnologie viticole ed enologiche",
	20:"Laurea in Scienze psicologiche per la formazione"}
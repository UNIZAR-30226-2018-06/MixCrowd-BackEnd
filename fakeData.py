from faker import Faker
import random                         

fake = Faker()

usernames=[]
projectnames=[]
listnames=[]

for i in range(0, 1000):
	usernames.append(fake.user_name())
	print("INSERT INTO usuario VALUES ('{}');".format(usernames[i]))

for i in range(0, 400):
	projectnames.append(fake.word(ext_word_list=None))
	print("INSERT INTO proyecto VALUES ('{}','{}','{}',NULL,NULL,{},NULL,'{}');".format(projectnames[i],fake.iso8601(tzinfo=None, end_datetime=None),fake.iso8601(tzinfo=None, end_datetime=None),fake.boolean(chance_of_getting_true=50),usernames[random.randint(0,999)]))

for i in range(0, 1000):
	print("INSERT INTO etiqueta VALUES ('{}','{}');".format(fake.word(ext_word_list=None),projectnames[random.randint(0,399)]))

for i in range(0, 3000):
	print("INSERT INTO colabora VALUES ('{}','{}');".format(projectnames[random.randint(0,399)],usernames[random.randint(0,999)]))

for i in range(0, 3000):
	print("INSERT INTO amistad VALUES ('{}','{}');".format(usernames[random.randint(0,399)],usernames[random.randint(0,999)]))

for i in range(0, 400):
	print("INSERT INTO comentario VALUES ('{}','{}','{}','{}',NULL);".format(fake.iso8601(tzinfo=None, end_datetime=None),fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None),projectnames[random.randint(0,399)],usernames[random.randint(0,999)]))

for i in range(0, 1000):
	listnames.append(fake.word(ext_word_list=None))
	print("INSERT INTO lista VALUES ('{}','{}');".format(listnames[i],fake.iso8601(tzinfo=None, end_datetime=None)))

for i in range(0, 3000):
	print("INSERT INTO pertenece VALUES ('{}','{}');".format(projectnames[random.randint(0,399)],listnames[random.randint(0,999)]))

for i in range(0, 4000):
	print("INSERT INTO pista VALUES ('{}','{}',NULL,'{}');".format(fake.file_name(category=None, extension='mp3'),projectnames[random.randint(0,399)],fake.iso8601(tzinfo=None, end_datetime=None)))

for i in range(0, 400):
	print("INSERT INTO valoracion VALUES ('{}','{}',{});".format(projectnames[random.randint(0,399)],usernames[random.randint(0,999)],random.randint(0,1)))

for i in range(0, 2000):
	print("INSERT INTO visita VALUES ('{}','{}','{}');".format(projectnames[random.randint(0,399)],usernames[random.randint(0,999)],fake.iso8601(tzinfo=None, end_datetime=None)))

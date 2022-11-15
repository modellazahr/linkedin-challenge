# linkedin-challenge

* Create a free email account use python. For example - https://github.com/jinxx0/ProtonMail-Account-Creator
* Register a new account in LinkedIn use this email.
* For the challenge - make a screenshoot for quiz, save it a file and read answer from command line
* Complete registration
* Submit link from email account

## Limitation

* Please work with mail system and LinkedIn use web (no API, no mail protocols)
* Your code should work under Linux system in a docker container
* For start challenge - please fork this repo at your git account

___
### Installation
In order for the program to work, you must have a Chrome browser. 
If you don't have one, go to another installation option.

First you must clone this repository
```
git clone 
```
Next, you need to go into the main directory
```
cd sep_scripts
```

Next all the necessary requirements must be installed:
```
pip install -r requirements.txt
```
Now you need to run the script that generates the email address for you, this can be done with the following command:
```
python3 create_temp.py
```
⛔️⛔️⛔️Once you close the program, your email account will be deleted.

Next, open a new terminal and run a script that creates a new user on LinkedIn, you can do this with the following command:
```
python3 script.py
```

---

### Installation without Chrome browser
First you must clone this repository
```
git clone 
```
Next, you need to go into the main directory
```
cd sep_scripts
```
Next all the necessary requirements must be installed:
```
pip install -r requirements.txt
```
Now you need to run the script that generates the email address for you, this can be done with the following command:
```
python3 create_temp.py
```
⛔️⛔️⛔️Once you close the program, your email account will be deleted.

Then open a new terminal and enter the following command:
```
docker built -t <name of your container> .
```
You can now run the program with this command:
```
docker run -ti <name of your container>
```

---

### Known problems🪲
If LinkedIn asks for a phone number, the program will stop with an error. 
The program cannot enter a phone number and receive an SMS with a code, and cannot pass the captcha from LinkedIn.
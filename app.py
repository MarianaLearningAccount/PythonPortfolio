from flask import Flask, render_template, request

import random

app = Flask(__name__)


global comp_num, number_of_guesses
comp_num = random.randint(1, 100)
number_of_guesses = 0 

@app.route('/program1', methods = ['GET', 'POST'])
def program1():
    global comp_num, number_of_guesses
    message = ''
    if request.method == 'POST':
        form = request.form
        user_guess = int(form['guess'])
        if user_guess != comp_num:
          number_of_guesses += 1  
        if comp_num == user_guess:
           message = 'Bingo! You guessed the number! Random number:' 
           return render_template('program1.html', message = message, random = comp_num, number = number_of_guesses)
        elif comp_num > user_guess:
            message = "Ups! Try again and choose a higher number!"
        else:
           message = "Ups! Try again and choose a lower number!"   
    return render_template('program1.html', message = message, number = number_of_guesses)

@app.route('/program2', methods = ['GET', 'POST'])
def program2():
    result = ''
    converted_time = None
    if request.method == 'POST':
        form = request.form
        user_time = form['time']
        time_list = user_time.split(" ")
        if time_list[1].lower() == "pm":
         digit_list = time_list[0].split(":")
         h = int(digit_list[0])
         if h == 12:
          converted_time = 12
         else:
          converted_time = h + 12
         result = str(converted_time) + ":" + str(digit_list[1])
        if time_list[1].lower() == "am":
         digit_list = time_list[0].split(":")
         h = int(digit_list[0])
         if h == 12:
          converted_time = 00
         else:
          converted_time = h
         result = str(converted_time) + ":" + str(digit_list[1])
    return render_template('program2.html', result = result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

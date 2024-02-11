from flask import Flask, render_template, request, url_for, redirect

import random

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
  return render_template('index.html')


random_num = None
attempts = 0

def reset_game():
    global random_num, attempts
    random_num = random.randint(1, 100)
    attempts = 0

@app.route('/program1', methods = ['GET', 'POST'])
def program1():
    global random_num, attempts
    if request.method == 'GET':
       reset_game()
       return render_template('program1.html')
    elif request.method == 'POST':
       user_guess = int(request.form['guess']) 
       attempts += 1
       if user_guess == random_num:
          message = f'Bingo! You guessed the number in {attempts} attempts! Random number: {random_num}' 
          reset_game()
       elif user_guess < random_num:
          message = "Ups! Try again and choose a higher number!"
       else:
          message = "Ups! Try again and choose a lower number!"   
    return render_template('program1.html', message = message, number = attempts)
    
@app.route('/program1/reset', methods=['POST'])   
def reset():
   reset_game()
   return redirect('/program1') 

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

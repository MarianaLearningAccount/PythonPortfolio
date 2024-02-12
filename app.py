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
          message = f'Bingo! You guessed the random number: {random_num} in {attempts} attempts!' 
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
        user_time = request.form['time']
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

@app.route('/program3', methods = ['GET', 'POST'])
def program3():
    result = ''
    if request.method == 'POST':
        user_temp = request.form['temp']
        temp_list = user_temp.split(" ")
        digit = float(temp_list[0])
        letter = temp_list[1]
        if letter.lower() == "c":
           result = str((digit * 9 / 5) + 32) + " F" 
        elif letter.lower() == "f":
           result = str((digit - 32) * 5 / 9) + " C"
        else:
           result = f'Unknown conversion to "{letter}". Please retry and provide valid data.'
    return render_template('program3.html', result = result)  

@app.route('/program4', methods = ['GET', 'POST'])
def program4():
    result = ''
    if request.method == 'POST':
        password = request.form['pswd']
        lower_list = []
        upper_list = []
        sp_ch_list = []
        digit_list = []
        for i in password:
         if not i.isalnum():
             sp_ch_list.append(i)
        for l in password:
         if l.isalpha() and l == l.lower():
             lower_list.append(l)
        for u in password:
         if u.isalpha() and u == u.upper():
             upper_list.append(u)
        for d in password:
         if d.isnumeric():
             digit_list.append(d)
        if (len(password) >= 8 and len(lower_list) >= 1 and len(upper_list) >= 1 and len(digit_list) >= 1
            and len(sp_ch_list) >= 1):
         result = 'The provided password meets the strength criteria'
        else:
         result = 'The provided password does not meet the strength criteria'
    return render_template('program4.html', result = result) 

@app.route('/program5', methods = ['GET', 'POST'])
def program5():
    result = ''
    if request.method == 'POST':
        email = request.form['email']
        at_symbol_count = email.count("@")
        dots_count = email.count(".")
        reverse_email = email[::-1]
        dot_position = reverse_email.find(".")
        at_symbol_position = reverse_email.find("@")
        username = reverse_email[at_symbol_position + 1:]
        server_name = reverse_email[dot_position + 1 : at_symbol_position]
        if len(username) > 0 and len(server_name) > 0 and at_symbol_count == 1 and dots_count >= 1 and dot_position < at_symbol_position and dot_position >= 2:
         result = 'The provided email meets the validation criteria'
        else:
         result = 'The provided email does not meet the validation criteria'
    return render_template('program5.html', result = result)  

if __name__ == '__main__':
    app.run(debug=True, port=5000)

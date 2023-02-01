from flask import Flask, render_template, request

app = Flask(__name__)

# planning for this app: index.html = hello page, ask for name 
# greet.html = greet the user + ask about subject and grade
# failure.html = tell them to enter properly 
# success.html = tell them how many more marks to desired grade ++ some enxouraging statement 
 
@app.route("/", methods=["POST"])
def index():
  # Validate submission 
  if not request.form.post("subject") or request.form.post("grade") not in ['A', 'B', 'C', 'D', 'E', 'S', 'U']:
    return render_template("failure.html") 
  else:
    return render_template("success.html") # return the function that calculates 

desired_grade = request.form.post("grade")
current = request.form.post("current_marks") # rmbr to make this

def mark_determiner(grade):
  if grade == 'A':
    return 70
  elif grade =='B':
    return 60
  elif grade =='C':
    return 55
  elif grade =='D':
    return 50
  elif grade =='E':
    return 45
  else:
    return 35

def calculate(marks):
  needed_marks = (desired_grade - 0.2*current) / 0.8
  return needed_marks 

  
  
  
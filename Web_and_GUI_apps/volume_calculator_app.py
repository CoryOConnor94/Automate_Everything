from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
  print("Get request string")
  return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def home_post():
  dim_one = request.form['first_dim']
  dim_two = request.form['second_dim']
  dim_three = request.form['third_dim']
  volume = float(dim_one) * float(dim_two) * float(dim_three)
  print()

  print("Post request string")
  return render_template('index.html', output=volume,
                         dim_1=dim_one, dim_2=dim_two, dim_3=dim_three)


app.run(host='0.0.0.0')
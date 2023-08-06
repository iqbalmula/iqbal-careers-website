from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Jakarta, Indonesia',
    'salary': 'Rp. 5.950.000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Bandung, Indonesia',
    'salary': 'Rp. 6.950.000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rp. 7.950.000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Surabaya, Indonesia',
    'salary': 'Rp. 8.950.000'
  },
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS,
                        company_name = 'Iqbal')

@app.route("/api/jobs")
def list_job():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
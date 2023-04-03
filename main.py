from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,800'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': 'Rs. 15,800'
}, {
  'id': 3,
  'title': 'Front end Emngineer',
  'location': 'Remote',
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Nairobi, Kenya',
  'salary': 'Rs. 9,800'
}]


@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

from flask import Flask, render_template, session, url_for
import json

app = Flask(__name__)

data_stats = {}

for stats_t in ['base_stats','clean_stats','merge_stats']:
    with open('./stats/' + stats_t + '.json') as f:
        data_stats[stats_t] = json.load(f)

print(data_stats)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')
    
@app.route('/about')
def about():
    return render_template('about.html')
    

if __name__ == '__main__':
    app.run()

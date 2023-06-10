from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index2.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/info', methods=['GET'])
def get_info():
    my_name = request.args.get('my_name')
    print(my_name)
    return jsonify({
        'msg': 'Get Info'
    })

@app.route('/info', methods=['POST'])
def post_info():
    my_name = request.form['my_name']
    print(my_name)
    return jsonify({
        'msg': 'Post Info'
    })

if __name__ == '__main__':  
    app.run('0.0.0.0', port=7000, debug=True)
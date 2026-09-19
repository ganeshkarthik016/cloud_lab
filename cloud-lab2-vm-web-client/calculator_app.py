from flask import Flask, request, render_template_string

app = Flask(__name__)

FORM = '''
<h2>Simple Calculator</h2>
<form method="get" action="/calculate">
 <input name="a" placeholder="first number" required>
 <select name="op">
  <option value="add">+</option>
  <option value="sub">-</option>
  <option value="mul">*</option>
  <option value="div">/</option>
 </select>
 <input name="b" placeholder="second number" required>
 <button type="submit">Calculate</button>
</form>
{% if result is not none %}<h3>Result: {{ result }}</h3>{% endif %}
'''

OPS = {
    'add': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mul': lambda a, b: a * b,
    'div': lambda a, b: a / b,
}

@app.route('/')
def home():
    return render_template_string(FORM, result=None)

@app.route('/calculate')
def calculate():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    op = request.args.get('op', 'add')
    result = OPS.get(op, OPS['add'])(a, b)
    return render_template_string(FORM, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
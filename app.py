from flask import request, Flask, render_template

from gpt import GPT

app = Flask(__name__)
gptAPI = GPT("your key ")


@app.route("/")
def index():
    return render_template("Flaskdemo.html")


@app.route("/aaron", methods=['GET', 'POST'])
def aaron():
    if gptAPI is None:
        return "Error: API key not set"
    if request.method == 'POST':
        prompt = request.form['prompt']
        newprompt = prompt + ''' put comments on the code above in the style of the code below. strip the actual code
        from the inside of the method leaving just // origin code
/**
 * O(1)
 * Method getFirst() returns a pointer to the first element in the list.
 * @return a pointer to the first element in the list
 */
public Node<T> getFirst()
{
  // origin code 
}
'''
        answer = gptAPI.getResponse(newprompt)
        return render_template("response.html", answer=answer, prompt=prompt)
    else:
        return '''
            <h1>GPT Demo App</h1>
            Enter your code below to receive java style comments 
            <form method="post">
                <textarea name="prompt"></textarea>
                <p><input type=submit value="get response">
            </form>
            '''

if __name__ == '__main__':
    app.run(debug=True, port=5001)

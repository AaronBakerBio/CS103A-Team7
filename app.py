from flask import request, Flask, render_template

from gpt import GPT

app = Flask(__name__)
gptAPI = GPT("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")




def process_request(prompt, new_prompt, htmlarg):
    if gptAPI is None:
        return "Error: API key not set"
    if request.method == 'POST':
        prompt = request.form['prompt']
        new_prompt += prompt
        answer = gptAPI.getResponse(new_prompt)
        return render_template(htmlarg, answer=answer, prompt=prompt)
    else:
        return render_template(htmlarg)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about", methods=['GET', 'POST'])
def about_all():
    return render_template("about.html")

'''
Help Notes:
- create new route by copy pasting
- change def name
- change url
- change prompt 
- change title arg
- change prompt_content arg

'''


'''
Aby Code Start 

'''


@app.route("/aby", methods=['GET', 'POST'])
def aby_home():
    return render_template("aby.html")

@app.route("/prompt_aby/businessModel", methods=['GET', 'POST'])
def model(prompt_content="Give me a business model for my app", title="Business Model"):
    if request.method == 'POST':
        prompt = request.form['prompt']
        new_prompt = "Give me a business model for my app idea"
        return process_request(prompt, new_prompt, "response.html")
    else:
        return render_template('prompt.html', prompt_content=prompt_content, title=title)
    
@app.route("/prompt_aby/business", methods=['GET', 'POST'])
def business(prompt_content="Is my app worth any money?", title="Money"):
    if request.method == 'POST':
        prompt = request.form['prompt']
        new_prompt = "Is my app worth any money?"
        return process_request(prompt, new_prompt, "response.html")
    else:
        return render_template('prompt.html', prompt_content=prompt_content, title=title)
    
@app.route("/prompt_aby/patent", methods=['GET', 'POST'])
def patent(prompt_content="Is there a patent for my app?", title="Patent"):
    if request.method == 'POST':
        prompt = request.form['prompt']
        new_prompt = "Is there a patent for my app?"
        return process_request(prompt, new_prompt, "response.html")
    else:
        return render_template('prompt.html', prompt_content=prompt_content, title=title)

'''
Aby Code End

'''



'''
Eugenio Code Start 

'''

@app.route("/eugenio", methods=['GET', 'POST'])
def eugenio_home():
    return render_template("eugenio.html")
    
@app.route("/eugenio/runningtime", methods=['GET', 'POST'])
def eugenio(prompt_content="This tool does the runtime analysis of the input code. Please type your method in the following text box.", title=" Runtime Analysis Developer Tool"):
    if request.method == 'POST':
        prompt = request.form['prompt']
        new_prompt = " Can you please the the runtime of the follow method? ."
        return process_request(prompt, new_prompt, "response.html")
    else:
        return render_template('prompt.html', prompt_content=prompt_content, title=title)

@app.route("/eugenio/space", methods=['GET', 'POST'])
def eugenio1(prompt_content=" This tool does a space complexity analysis for your methods or algorithms. Please type your method in the following text box. ", title=" Space Complexity analysis Developer Tool"):
    if request.method == 'POST':
        prompt = request.form['prompt']
        new_prompt = " Can you please find the Space Complexity analysis of the follow method? The complexity analysis refers to the total amount of memory space used by the program."
        return process_request(prompt, new_prompt, "response.html")
    else:
        return render_template('prompt.html', prompt_content=prompt_content, title=title)

@app.route("/eugenio/recursion", methods=['GET', 'POST'])
def eugenio2(prompt_content= "This tool informes the developer on recursive options for their methods or algorithms. Please type your method in the following text box.", title=" Recursive Options Developer Tool"):
    if request.method == 'POST':
        prompt = request.form['prompt']
        new_prompt = " Is there a recursive option for the following method or algorithm? Please describe the ways this can be implemented recursively?"
        return process_request(prompt, new_prompt, "response.html")
    else:
        return render_template('prompt.html', prompt_content=prompt_content, title=title)


'''
Eugenio Code End 

'''



'''
Rue Code Start 

'''



@app.route("/rue", methods=['GET', 'POST'])
def rue_home():
    return render_template("rue.html")
    
@app.route("/rue/sample", methods=['GET', 'POST'])
def rue_prompt(prompt_content=" Rue Sample", title=" Rue Sample"):
    if request.method == 'POST':
        prompt = request.form['prompt']
        new_prompt = " is the name for my new car. Make up a car and give me its specs. It should fly, and talk " \
                     "obviously, so you should mention that in your response. Keep it to 500 words."
        return process_request(prompt, new_prompt, "response.html")
    else:
        return render_template('prompt.html', prompt_content=prompt_content, title=title)
        



@app.route("/rue/dingus_bop", methods=['GET', 'POST'])
def fairytale_generator(prompt_content="Prompt that generates a ~fun silly story~",
                    title="~Story Time~" ):
    if request.method == 'POST':
        prompt = request.form['prompt']
        newprompt = ''' 
        Here is a list of nouns: 
        [pumpkin, onion, dress, cotton, window, shoe, fairy, forest, clock]
        Here is a list of verbs:
        [discover, chant, punish, pursue, interpret, spin, escape]
        Please incorporate up to 3 of the nouns and up to 3 of the verbs, along with 1-10 words from the following
        input, and write a fairytale-style story: 
        '''
        return process_request(prompt, newprompt, "dankresponse.html")
    else:
        # Handle GET request
        # ...
        return render_template('prompt.html', prompt_content=prompt_content, title=title)



@app.route('/rue/docstring-maker', methods=['GET', 'POST'])
def code_generator(prompt_content="Prompt that generates comments for python code",
                    title="Python Code Commenter" ):
    if request.method == 'POST':
        prompt = request.form['prompt']
        newprompt = '''
put comments on the python methods above in the style of the code below. 

Example :
def process_file(input_filename, output_filename, encode_decode, key):
    """Function that is used to encode or decode a file based on user input.
    Returns true if opening, closing, and writing to output_filename were
    successful, otherwise returns false.
    :param input_filename
    File name (tested only for .txt) that will be read
    :param output_filename
    File that will be written to (tested only for .txt)
    :param encode_decode
    if encode_decode == 'e', encoding will be performed,
    otherwise decode the file
    :param key
    Amount to encode or decode (right-shift amount)
    """

        
        '''
        return process_request(prompt, newprompt, "dankresponse.html")
    else:
        # Handle GET request
        # ...
        return render_template('prompt.html', prompt_content=prompt_content, title=title)



'''
Rue Code End 

'''


'''
Aaaron Code Start 

'''

@app.route("/aaron_about")
def about():
    return render_template("aaron_about.html")

@app.route("/aaron", methods=['GET', 'POST'])
def aaron_home():
    return render_template("aaron.html")
   
@app.route("/aaron_descriptions", methods=['GET', 'POST'])
def descriptions(prompt_content="  Enter your code below to receive description of what code does", title="Code description maker"):
    if request.method == 'POST':
        prompt = request.form['prompt']
        new_prompt = ''' for the code I entered, explain what it did. If it uses data structures, use examples where 
        you explain step by step what happens to those data structures. I am not a long time coder and need it clear 
        and very descriptive, with numbered steps in your examples.'''
        return process_request(prompt, new_prompt, "dankresponse.html")
    else:
        return render_template('prompt.html', prompt_content=prompt_content, title=title)



@app.route("/aaron_pseudo", methods=['GET', 'POST'])
def pseudo(prompt_content="Enter your code below to receive java style pseudocode", title="Java pseudocode generator"):
    if request.method == 'POST':
        prompt = request.form['prompt']
        new_prompt = ''' based on my above java code, turn it into pseudocode.The format for methods 
        should match as follows:Stacks have push(), pop(), top(), size(), and isEmpty(). Linked lists have 
        Queues have only enqueue(element), dequeue(),size(), and isEmpty(). Nodes only have prev, next, hasNext(), 
        hasPrev() and a data field. Linked lists have isEmpty(), insertNode(), findNode(), deleteNode(), and 
        displayList(). Assignment uses <- not =. = is reserved for comparison. Replace any nonconforming methods with 
        one of these if valid. 
        Do not return the original prompt in any way whatsoever. No comments or sentences, just line numbered 
        pseudocode. If the code is not java or not code, tell the user their argument is illegal. Proper pseudocode 
        contains no curly braces. Method name, input, and output should be bolded. Font should be courier new 12.
        Below are 2 examples, first is the code for the example then the pseudocode.
    Example 1: 
        public static void sort_stack(Stack<Integer> stack) {
      if (!stack.isEmpty()) {
          int temp = stack.pop();
          sort_stack(stack);
          if (!stack.isEmpty() && stack.peek() > temp) {
              int top = stack.pop();
              sort_stack(stack);
              stack.push(temp);
              sort_stack(stack);
              stack.push(top);
          } else {
              stack.push(temp);
          }
      }
      
Respond with something like below
1  sort_stack(stack)
2  Input: A stack that needs to be sorted in ascending order.
3  Output: The sorted stack in ascending order.
4      if (!stack.isEmpty()) then
5          temp <- stack.pop()
6          sort_stack(stack)
7          if (!stack.isEmpty() and stack.peek() > temp) then
8              top = stack.pop()
9              sort_stack(stack)
10             stack.push(temp)
11             sort_stack(stack)
12             stack.push(top)
13         else
14             stack.push(temp)

Example 2: 

public static void printNumbers(int start, int end) {
    int i = start;
    do {
        System.out.print(i + " ");
        i++;
    } while (i <= end);

    while (i <= end + 10) {
        System.out.print(i + " ");
        i++;
    }
}

Pseudocode: 
1  printNumbers(start, end)
2  Input: Two integers indicating the start and end of the range of numbers to be printed. 
3  Output: Prints the numbers from the start to the end and from the end + 10 to the end + 19. 
4      i <- start 
5      do 
6          System.out.print(i + " ")
7          i++
8      while (i <= end)
9      while (i <= end + 10) do
10          System.out.print(i + " ")
11          i++

        '''
        return process_request(prompt, new_prompt, "dankresponse.html")
    else:
        return render_template('prompt.html', prompt_content=prompt_content, title=title)

            
@app.route("/aaron_comment", methods=['GET', 'POST'])
def comment(prompt_content="This method will convert code in java into pseudocode.", title="Pseudocode generator for java"):
    if request.method == 'POST':
        prompt = request.form['prompt']
        new_prompt = ''' put comments on the code above in the style of the code below. strip the actual code
            from the inside of the method leaving just // origin code. Do not include any other stuff
            /**
* O(1)
* Method getFirst() returns a pointer to the first element in the list.
* @return A pointer to the first element in the list.
*/
public Node<T> getFirst()
    {
        // origin code
    }
        '''
        return process_request(prompt, new_prompt, "dankresponse.html")
    else:
        return render_template('prompt.html', prompt_content=prompt_content, title=title)
        

'''
Aaron Code End 

'''

@app.route('/rue/code-generator', methods=['GET', 'POST'])
def code_generator(prompt_content="Prompt that generates comments for python code",
                    title="Python Code Commenter" ):
    if request.method == 'POST':
        prompt = request.form['prompt']
        newprompt = '''
put comments on the python methods above in the style of the code below. 

Example :
def process_file(input_filename, output_filename, encode_decode, key):
    """Function that is used to encode or decode a file based on user input.
    Returns true if opening, closing, and writing to output_filename were
    successful, otherwise returns false.
    :param input_filename
    File name (tested only for .txt) that will be read
    :param output_filename
    File that will be written to (tested only for .txt)
    :param encode_decode
    if encode_decode == 'e', encoding will be performed,
    otherwise decode the file
    :param key
    Amount to encode or decode (right-shift amount)
    """

        
        '''
        return process_request(prompt, newprompt, "dankresponse.html")
    else:
        # Handle GET request
        # ...
        return render_template('prompt.html', prompt_content=prompt_content, title=title)

@app.route("/rue_about", methods = ['GET', 'POST'])
def rue_about():
    return render_template("rue_about.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)

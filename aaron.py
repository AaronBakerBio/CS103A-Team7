import shared

def descriptions():
    if request.method == 'POST':
        prompt = request.form['prompt']
        new_prompt = ''' for the code I entered, explain what it did. If it uses data structures, use examples where 
        you explain step by step what happens to those data structures. I am not a long time coder and need it clear 
        and very descriptive, with numbered steps in your examples.'''
        return process_request(prompt, new_prompt, "pseudo.html")
    else:
        return '''
                    <h1>GPT Demo App</h1>
                    Enter your code below to receive a description at a low level
                    <form method="post">
                        <textarea name="prompt"></textarea>
                        <p><input type=submit value="get response">
                    </form>
                    '''

def pseudo():
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
        return process_request(prompt, new_prompt, "pseudo.html")
    else:
        return '''
                <h1>GPT Demo App</h1>
                Enter your code below to receive java style comments 
                <form method="post">
                    <textarea name="prompt"></textarea>
                    <p><input type=submit value="get response">
                </form>
                '''


def comment():
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
        return process_request(prompt, new_prompt, "comment.html")
    else:
        return '''
            <h1>GPT Demo App</h1>
            Enter your code below to receive java style comments 
            <form method="post">
                <textarea name="prompt"></textarea>
                <p><input type=submit value="get response">
            </form> 
            '''


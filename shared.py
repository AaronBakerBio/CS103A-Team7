def process_request(prompt, new_prompt, htmlarg):
    if gptAPI is None:
        return "Error: API key not set"
    if request.method == 'POST':
        prompt = request.form['prompt']
        new_prompt += prompt
        answer = gptAPI.getResponse(new_prompt)
        return render_template("response.html", answer=answer, prompt=prompt)
    else:
        return render_template(htmlarg)

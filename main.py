from flask import Flask, request, render_template, redirect, url_for, session
from openrouter import OpenRouter

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def homepage():
    api_key = ""
    user_msg = ""
    model = ""
    bot_response = ""
    server_url = ""

    if request.method == "POST":
        api_key = request.form.get("api_key", "")
        user_msg = request.form.get("user_msg", "")
        model = request.form.get("model", "")
        server_url = request.form.get("server_url", "")

        if not api_key:
            return "Enter an api key please", 400

        client = OpenRouter(
            api_key=api_key,
            server_url="https://ai.hackclub.com/proxy/v1",
        )   

        response = client.chat.send(
            model=model,
            messages=[
                {"role": "user", "content": user_msg}
            ],
        )

        bot_response = response.choices[0].message.content
        print(bot_response)

    return render_template("index.html", api_key=api_key, user_msg=user_msg, model=model, 
    bot_response=bot_response, server_url=server_url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

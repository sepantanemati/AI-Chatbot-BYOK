from flask import Flask , request, render_template,redirect, url_for, session
from openrouter import OpenRouter

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def homepage():
    api_key=""
    user_msg=""
    model=""

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

    print(response.choices[0].message.content)
    return render_template("index.html", api_key=api_key, user_msg=user_msg, model=model)


app.run(host='0.0.0.0', port=5000, debug=True)
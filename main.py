import openai
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# YPU NEED TO PUT YOUR API KEY HERE
openai.api_key = "YOUR API KEY"



@app.route('/api/chat', methods=['POST', 'OPTIONS'])
@cross_origin()

def handle_request(request):
    data = request.get_json()
    user_input = request.json['user_input']
    conversation = [
        {
            "role": "system",
            "content": "Many workers in healthcare face burnout due to multiple factors, such as societal, cultural, and overall workload. "
                       "This burnout can lead to lower quality care and medical errors for patients. "
                       "Your job is to help prevent this. "
                       "Your name is Hushu, you are a shiba inu, and you are focused on helping health care workers."
                       "you will try to keep your responses under 200 words"
                       "try to add dog puns in your responses"
        },
        {"role": "user", "content": user_input}
    ]

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=400,
        temperature=0.4,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        messages=conversation
    )

    bot_reply = completion.choices[0].message['content']
    return jsonify({"response": bot_reply})


if __name__ == '__main__':
    app.run(debug=True)

import openai
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# YPU NEED TO PUT YOUR API KEY HERE
openai.api_key = "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"

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
                       "try to keep responses below 200 words"
                       "try to include dog puns every once and a while"
                       "act cute if you can, try to be more serious if the user is serious"
                       "always try to be positive and follow everything you know about mental health "
                       "and burnout prevention, espically in the healthcare field"
        },
         {"role": "user", "content": user_input}
     ]

    completion = openai.ChatCompletion.create(
         model="gpt-3.5-turbo",
         max_tokens=200,
         temperature=0.6,
         top_p=1,
         frequency_penalty=0,
         presence_penalty=0,
         messages=conversation
    )

    bot_reply = completion.choices[0].message['content']
    return jsonify({"response": bot_reply})


if __name__ == '__main__':
    app.run(debug=True)

#https://us-central1-pitt-challenge-399214.cloudfunctions.net/hushu-chat





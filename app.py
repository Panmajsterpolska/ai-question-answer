from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Skonfiguruj swój klucz API OpenAI
openai.api_key = '5157c7a8568f6af8da0e46c25621f7d6'

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data['user_input']

    # Komunikacja z GPT (wysyłanie zapytania)
    response = openai.Completion.create(
        engine="text-davinci-003",  # Możesz wybrać inny model
        prompt=user_input,
        max_tokens=100,
        temperature=0.7
    )

    # Odpowiedź generowana przez GPT
    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

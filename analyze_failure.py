import openai
import sys

# Komut satırından alınan argümanlar
error_log_file = sys.argv[1]
response_file = sys.argv[2]
openai_api_key = sys.argv[3]

# OpenAI API anahtarınızı ayarlayın
openai.api_key = openai_api_key

# Hata logunu okuyun
with open(error_log_file, 'r') as file:
    error_contents = file.read()

# OpenAI API'sine sorguyu gönderin
try:
    response = openai.Completion.create(
        engine="davinci",  # En son mevcut modeli kullanabilirsiniz
        prompt="I encountered an error in my Spring Boot application:\n" + error_contents + "\n\nHow can I resolve it?",
        max_tokens=150
    )

    # OpenAI'den alınan yanıtı dosyaya yazın
    with open(response_file, 'w') as file:
        file.write(response.choices[0].text.strip())
except Exception as e:
    print("An error occurred while communicating with OpenAI API: ", e)
    sys.exit(1)


import os
import openai

# API 키 설정
openai.api_key = "$OPENAI_API_KEY"

try:
    # GPT-3.5 모델 호출
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Translate the following English text to French: 'Hello world.'",
        max_tokens=50
    )

    # 모델 응답 출력
    print(response.choices[0].text)
    
except Exception as e:
    print(f"An error occurred: {e}")
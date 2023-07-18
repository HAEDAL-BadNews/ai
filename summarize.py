import openai
import json

with open('./secret.json') as f:
    secrets = json.loads(f.read())
DB_API_KEY = secrets["API_KEY"]


def summarize(page):
    openai.api_key = DB_API_KEY

    text = f"""{page}"""
    instruction = f"""아래 지문을 5줄로 요약해줘.\n\n\n{text}"""
    
    model="gpt-3.5-turbo"
    messages=[{"role": "user", "content":instruction}]
        
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0.5,
        top_p = 0.3,
        max_tokens=512,
        presence_penalty=0,
        frequency_penalty=0,
    )
    

    output_text = response.choices[0].message["content"]
    print(output_text)
    return output_text




def receive_text(news):
    result = summarize(news)

    return {'summarize':result}


article = "‘서핑성지’ 양양군에 한해 평균 1500만 명의 방문객이 몰려드는 등 서핑을 즐기는 사람이 늘어나는 가운데 국립해양조사원이 서핑 사고 예방과 안전한 서핑 환경 조성을 위해 ‘서핑지수’를 제공한다. 해양수산부 국립해양조사원은 18일 국민들이 안전하게 서핑을 즐길 수 있도록 서핑지수 서비스 제공 지역을 확대하겠다고 발표했다. 서핑지수 서비스는 해당 해역에서의 서핑이 용이한 지를 매우 좋음부터 매우 나쁨까지 5단계로 나타낸 지수로 기상청 특보 등을 반영했다. 국립해양조사원은 작년 6월부터 서비스 중인 동·남·서해안 4개 해수욕장(부산 송정·동해 망상·양양 죽도·태안 만리포)에 이어 올해 제주 곽지·부산 다대포·울산 진하·고성 송지호까지 추가해 총 8개 해수욕장에 대해 서핑지수를 제공한다. 해당 해수욕장들은 연평균 약 50만 명 이상의 이용자들이 찾는 곳으로 해수욕장 이용객들이 서핑지수를 많이 활용할 것으로 예상된다."

print(receive_text(article))
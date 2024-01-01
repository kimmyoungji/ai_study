from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

text = f"""데브시스터즈(공동대표 이지훈, 김종흔)의 모바일 RPG '쿠키런: 킹덤'이 중국 서비스를 시작해 현지 앱 마켓 인기 순위 2위를 기록했다.

쿠키런: 킹덤(중국명 冲呀! 饼干人: 王国)은 현지 주요 안드로이드 앱 마켓과 애플 앱스토어를 통해 이날 현지시간 오전 7시 출시됐다. 이 게임은 서비스 시작 약 1시간 만에 중국 애플 앱스토어 인기 2위에 올랐으며 앱마켓 플랫폼 '탭탭'과 '빌리빌리'에서는 현재 인기 3위에 자리했다.

쿠키런: 킹덤의 공동 퍼블리셔인 텐센트게임즈와 창유는 게임의 핵심 재미 요소를 전달하기 위해 현지 콘텐츠 최적화와 홍보를 진행해 왔다. 그 결과 정식 출시까지 사전예약자가 1000만명을 돌파하고 중국 소셜미디어 웨이보에서 출시일을 해시태그로 단 게시물 조회수가 3800만회를 기록하기도 했다."""

prompt = f"""다음의 ```로 감싸진 뉴스 본문을 3가지 오점과 설명을 기반으로 요약해줘 ```{text}```"""


client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "너는 YTN 뉴스 기자로써, 뉴스를 발행하는 역할을 하고 있어. 이모티콘을 사용해서 글을 쓰는게 장점이야"},
    {"role":"user", "content":prompt}
  ],
  temperature = 0.5
)

print(response.choices[0].messages)
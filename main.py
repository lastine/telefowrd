import telethon
from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
# https://my.telegram.org/apps

# 봇 토큰 넣을 수 없음
api_id = 'api_id'
api_hash = 'api_hash'
bot_token = 'bot_token' # 공지전용 봇 새로 만듦

announcement_channel = announcement_channel
shrimp_channel = shrimp_channel
test_channel = test_channel

forward_to = forward_to # 포워드 대상
forward_from = forward_from # 포워드 당하는


messagelist = ['마켓 디지털 자산 추가', '금일 업비트에 아래와 같은 신규 디지털 자산이 추가됩니다.', '업비트(Upbit) 거래 대기', '업비트(Upbit) 신규 지갑', '업비트(Upbit) 신규 마켓',
                '디지털 자산 유의종목 지정 안내', '디지털 자산 거래지원 종료',
                'Binance Will List', 'Binance Announcement Binance Will List',
                '빗썸(Bithumb) 공지 - [상장'
            ]

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token) # 따로 인증이 필요없음 client만
client = TelegramClient('name', api_id, api_hash) # 일반
@client.on(events.NewMessage)
async def handler(event): # 돌아가는 동안 채팅 발생시 프린트
    chat_id = event.chat_id # 특정 채널 방 id
    msg = event.raw_text # 오로지 사진만, 이모티콘 같은 경우에는 포워딩 안됨(raw_text)
    print("{}{}".format(chat_id, msg))

    if chat_id == shrimp_channel: # 새우잡이 채널에서 감지
        # 업비트 등 특정 마켓 추가시 알람
        for catch_message in messagelist:
            if catch_message in msg:
                print("감지왼료!!!!!!!!!")
                await bot.send_message(announcement_channel, msg)
                break

    if chat_id in [forward_to, shrimp_channel, wings_test_channel]:
        for catch_message_test in ['업비트', '바이낸스', 'Korbit', '후오비', '빗썸']:
            if catch_message_test in msg:
                print("감지왼료!!!!!!!!!")
                await bot.send_message(forward_from, msg)
                break

client.start()
client.run_until_disconnected()

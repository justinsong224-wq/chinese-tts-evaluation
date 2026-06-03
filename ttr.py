import asyncio
import edge_tts

TEXT = """
今儿个天气不错，您要是有空的话，咱们可以去公园走走。
2025年以来，人工智能技术发展得越来越快，但很多人还是觉得，机器说话嘛，总归少了点儿人情味。
您说是不是这个理儿？
"""
VOICES = [
    ("zh-CN-XiaoxiaoNeural", "01xiaoxiao_女声_标准"),
    ("zh-CN-YunxiNeural", "02yunxi_男声_标准"),
    ("zh-CN-XiaoyiNeural", "03xiaoyi_女声_活泼"),
    ("zh-CN-YunjianNeural", "04yunjian_男声_激昂"),
]

async def generate():
    for voice, filename in VOICES:
        tts = edge_tts.Communicate(TEXT, voice)
        await tts.save(f"{filename}.mp3")
        print(f"已生成：{filename}.mp3")
        await asyncio.sleep(2)

asyncio.run(generate())
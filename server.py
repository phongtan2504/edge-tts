import asyncio
import edge_tts
import requests

# 1. Hàm gọi API giọng nói RIÊNG của bạn
async def call_custom_voice_api(text):
    api_url = "https://api.your-voice-service.com/v1/tts" # Link API của bạn
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    payload = {"text": text, "voice": "my_custom_voice"}
    
    response = requests.post(api_url, json=payload, headers=headers)
    return response.content # Trả về dữ liệu âm thanh (bytes)

# 2. Hàm xử lý chung (Kiểm tra và chọn đúng nguồn giọng)
async def generate_speech(text, voice_name, output_file):
    # Nếu người dùng chọn giọng mới của bạn
    if voice_name == "giong-rieng-cua-toi":
        print("Đang tạo bằng API riêng...")
        audio_data = await call_custom_voice_api(text)
        with open(output_file, "wb") as f:
            f.write(audio_data)
            
    # Nếu chọn các giọng Edge-TTS mặc định (ví dụ: vi-VN-HoaiMyNeural)
    else:
        print(f"Đang tạo bằng giọng Edge-TTS ({voice_name})...")
        communicate = edge_tts.Communicate(text, voice_name)
        await communicate.save(output_file)

    print("Đã hoàn thành!")

# Dùng thử:
# asyncio.run(generate_speech("Xin chào", "giong-rieng-cua-toi", "output.mp3"))
# asyncio.run(generate_speech("Xin chào", "vi-VN-HoaiMyNeural", "output.mp3"))

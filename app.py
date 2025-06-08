import streamlit as st
import os
from datetime import datetime

# 页面标题
st.title("🏋️ 健身记录上传系统")

# 用户输入文字记录
note = st.text_area("💬 今天的健身记录", "")

# 上传图片和视频
uploaded_images = st.file_uploader("📷 上传健身照片", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
uploaded_videos = st.file_uploader("🎥 上传健身视频", type=["mp4", "mov", "avi"], accept_multiple_files=True)

# 创建保存目录
if not os.path.exists("records"):
    os.makedirs("records")

# 点击按钮后保存
if st.button("✅ 保存记录"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder = os.path.join("records", timestamp)
    os.makedirs(folder)

    # 保存文字
    with open(os.path.join(folder, "note.txt"), "w") as f:
        f.write(note)

    # 保存图片
    for i, img in enumerate(uploaded_images):
        with open(os.path.join(folder, f"image_{i+1}.jpg"), "wb") as f:
            f.write(img.read())

    # 保存视频
    for i, vid in enumerate(uploaded_videos):
        with open(os.path.join(folder, f"video_{i+1}.mp4"), "wb") as f:
            f.write(vid.read())

    # 简单关键词分析
    advice = ""
    food = ""

    if "腿" in note:
        advice = "明天建议休息或练上肢。"
        food = "补充蛋白质（鸡蛋、豆腐），增加碳水（红薯、糙米）。"
    elif "胸" in note or "三头" in note:
        advice = "建议下一次练背或下肢，避免同组肌群连续高强度训练。"
        food = "补充蛋白质（鸡胸肉、乳清蛋白），适量碳水（燕麦、水果）。"
    elif "背" in note:
        advice = "下一次可以练核心或有氧，注意拉伸放松。"
        food = "高蛋白+轻脂饮食，增加绿叶蔬菜。"
    else:
        advice = "建议安排规律训练计划，确保均衡发展。"
        food = "均衡摄入蛋白、碳水和脂肪。"

    st.success("🎉 健身记录保存成功！")
    st.markdown("### 💪 健身建议：")
    st.write(advice)
    st.markdown("### 🥗 饮食建议：")
    st.write(food)
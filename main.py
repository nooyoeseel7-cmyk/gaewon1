import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI Music Vibe", page_icon="🎵", layout="centered")

# 메인 타이틀 및 소개
st.title("🎧 MBTI Music Vibe")
st.subheader("당신의 성격과 완벽하게 어울리는 선율을 찾아보세요.")

# 사용자 이름 입력
name = st.text_input("당신의 이름을 알려주세요!", placeholder="예: 코딩꿈나무")

if name:
    st.success(f"🔥 반가워요, {name}님! 준비가 되셨다면 왼쪽 메뉴에서 'Music Recommend'를 클릭해 주세요.")
    st.info("당신의 MBTI가 가진 고유한 에너지를 분석하여 최적의 음악을 추천해 드립니다.")
    
    # 애니메이션 효과 (바이브 코딩의 묘미!)
    st.balloons()
else:
    st.warning("이름을 입력하면 음악 여행을 시작할 수 있어요! 👇")

import streamlit as st

st.title("💬 Music Talk")
st.write("추천받은 음악이 어떠셨나요? 여러분의 감상을 남겨주세요!")

# 세션 상태를 이용한 간단한 방명록 저장 (새로고침 시 초기화되지만 수업용으론 충분해요!)
if 'comments' not in st.session_state:
    st.session_state['comments'] = []

# 입력창
user_comment = st.text_area("음악 감평이나 친구들에게 추천하고 싶은 곡을 적어보세요.")

if st.button("등록하기"):
    if user_comment:
        st.session_state['comments'].append(user_comment)
        st.balloons()
    else:
        st.error("내용을 입력해 주세요!")

# 등록된 내용 보여주기
st.divider()
st.subheader("최근 남겨진 메시지")

if st.session_state['comments']:
    for comment in reversed(st.session_state['comments']):
        st.chat_message("user").write(comment)
else:
    st.write("아직 등록된 메시지가 없어요. 첫 번째 메시지를 남겨보세요! 🚀")

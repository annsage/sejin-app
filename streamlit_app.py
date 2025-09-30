import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# 1. 제목, 부제목, 본문, 마크다운
st.title("Streamlit 요소 예시")  # 페이지의 큰 제목
st.header("헤더 예시")           # 섹션 헤더
st.subheader("서브헤더 예시")    # 소제목
st.text("일반 텍스트입니다.")    # 일반 텍스트
st.markdown("**마크다운** _포맷_ 예시")  # 마크다운 포맷

# 2. 입력 위젯들
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)  # 숫자 입력
agree = st.checkbox("동의하십니까?")  # 체크박스
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])  # 라디오 버튼
hobby = st.selectbox("취미를 선택하세요", ["독서", "운동", "음악", "여행"])  # 셀렉트박스
multi_hobby = st.multiselect("복수 취미 선택", ["독서", "운동", "음악", "여행"])  # 멀티셀렉트
level = st.slider("만족도를 선택하세요", 0, 100, 50)  # 슬라이더
date = st.date_input("날짜를 선택하세요")  # 날짜 입력
time = st.time_input("시간을 선택하세요")  # 시간 입력

# 3. 버튼, 파일 업로드
if st.button("버튼을 눌러보세요"):
    st.write("버튼이 눌렸습니다!")  # 버튼 클릭 시 동작

uploaded_file = st.file_uploader("파일을 업로드하세요")  # 파일 업로드
if uploaded_file is not None:
    st.write("업로드된 파일 이름:", uploaded_file.name)

# 4. 데이터프레임/표
df = pd.DataFrame({
    "A": np.random.rand(5),
    "B": np.random.rand(5)
})
st.dataframe(df)  # 데이터프레임 표시
st.table(df.head(3))  # 표 형태로 표시

# 5. 차트
st.line_chart(df)  # 라인 차트
st.bar_chart(df)   # 바 차트
st.area_chart(df)  # 영역 차트

# 6. 이미지, 오디오, 비디오
st.image("https://placekitten.com/200/300", caption="고양이 이미지")  # 이미지 표시
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # 오디오
st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # 비디오

# 7. 코드, 메시지
st.code("print('Hello, Streamlit!')", language="python")  # 코드 블록
st.success("성공 메시지입니다!")  # 성공 메시지
st.info("정보 메시지입니다!")    # 정보 메시지
st.warning("경고 메시지입니다!")  # 경고 메시지
st.error("에러 메시지입니다!")    # 에러 메시지

# 각주: 각 요소 옆에 주석으로 설명을 달았습니다.

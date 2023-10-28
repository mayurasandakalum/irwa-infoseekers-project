import numpy as np
import streamlit as st
from streamlit_elements import elements, mui, html, sync
import pickle
import os

model = pickle.load(open('artifacts/model.pkl', 'rb'))
movie_names = pickle.load(open('artifacts/movie_names.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
movie_pivot = pickle.load(open('artifacts/movie_pivot.pkl', 'rb'))

root_path =  os.getcwd()

directory_path = f"{root_path}/movies"
# print("directory_names:", os.listdir(directory_path))
images = os.listdir(directory_path)
# print(images)


IMAGES = [
    "https://collider.com/wp-content/uploads/the-avengers-movie-poster-banners-03.jpg",
    "https://unsplash.com/photos/eHlVZcSrjfg/download?force=true&w=1920",
    "https://unsplash.com/photos/zVhYcSjd7-Q/download?force=true&w=1920",
    "https://unsplash.com/photos/S5uIITJDq8Y/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjUyOTAzMzAz&force=true&w=1920",
    "https://unsplash.com/photos/E4bmf8BtIBE/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjUyOTEzMzAw&force=true&w=1920",
]

recommendations = [
    ["Recommendation 1", "https://th.bing.com/th/id/OIP.AkqQU6wiR_50f-Qd-jYA7wHaK-?w=202&h=300&c=7&r=0&o=5&dpr=1.3&pid=1.7"],
    ["Recommendation 2", "https://th.bing.com/th/id/OIP.AkqQU6wiR_50f-Qd-jYA7wHaK-?w=202&h=300&c=7&r=0&o=5&dpr=1.3&pid=1.7"],
    ["Recommendation 3", "https://th.bing.com/th/id/OIP.AkqQU6wiR_50f-Qd-jYA7wHaK-?w=202&h=300&c=7&r=0&o=5&dpr=1.3&pid=1.7"],
    ["Recommendation 4", "https://th.bing.com/th/id/OIP.AkqQU6wiR_50f-Qd-jYA7wHaK-?w=202&h=300&c=7&r=0&o=5&dpr=1.3&pid=1.7"],
    ["Recommendation 5", "https://th.bing.com/th/id/OIP.AkqQU6wiR_50f-Qd-jYA7wHaK-?w=202&h=300&c=7&r=0&o=5&dpr=1.3&pid=1.7"],
    ["Recommendation 6a", "https://th.bing.com/th/id/OIP.AkqQU6wiR_50f-Qd-jYA7wHaK-?w=202&h=300&c=7&r=0&o=5&dpr=1.3&pid=1.7"],
]

def clean_string(img_link):
    return img_link.replace(" ", "-").replace("'", "-").replace("(", "").replace(")", "").replace(",", "").replace("!", "").replace(":", "").replace("é", "-")
    


def recommend_movie(movie_name):
    movie_list =[]
    movie_id = np.where(movie_pivot.index == movie_name)[0][0]
    distance, suggestion = model.kneighbors(movie_pivot.iloc[movie_id,:].values.reshape(1,-1), n_neighbors=6 )

    for i in range(len(suggestion)):
            movies = movie_pivot.index[suggestion[i]]

            for j in movies:
                movie_list.append(j)
    return movie_list


st.markdown(
    """
    <style>
    .centered-header {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Center the header
st.markdown("<h1 class='centered-header'>Movie Recommender System</h1>", unsafe_allow_html=True)


def slideshow_swipeable(images):
    # Generate a session state key based on images.
    key = f"slideshow_swipeable_{str(images).encode().hex()}"

    # Initialize the default slideshow index.
    if key not in st.session_state:
        st.session_state[key] = 0

    # Get the current slideshow index.
    try:
        index = st.session_state[key]
    except:
        pass

    # Create a new elements frame.
    with elements(f"frame_{key}"):

        with mui.SwipeableViews(index=index, resistance=True, onChangeIndex=sync(key), css={"height": "500px", "overflow": "hidden"}):
            for image in images:
                html.img(src=image, css={"width": "100%"})

            def handle_change(event, value):
                st.session_state[key] = value-1

            mui.Pagination(page=index+1, count=len(images), color="primary", onChange=handle_change)

slideshow_swipeable(IMAGES)



selected_movies = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_names
)

recommend_btn = st.button('Show Recommendation')

if recommend_btn:
    print("selected_movies", selected_movies)
    recommend_movie = recommend_movie(selected_movies)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        # st.text(recommend_movie[1])
        # st.image(f"./movies/{recommend_movie[1].lower()}.jpg")
        st.markdown(
            f"""
        <div style="display: flex; flex-direction: column; width: 100%; height: 100%; justify-content: center; margin-top: 30px;">
        <h5 style="text-transform: capitalize; height: 80px">{recommend_movie[1].lower()}</h5>
        <div style="width: 300px; height: 400px;">
            <img src="https://irwa-project.weebly.com/uploads/1/4/7/4/147496024/{clean_string(str(recommend_movie[1].lower()))}.jpg" style="width: 100%; height: 100%;">
        </div>
        """,
        unsafe_allow_html=True
        )
    with col2:
        # st.text(recommend_movie[2])
        # st.image(f"./movies/{recommend_movie[2].lower()}.jpg")
        st.markdown(
            f"""
        <div style="display: flex; flex-direction: column; width: 100%; height: 100%; justify-content: center; margin-top: 30px;">
        <h5 style="text-transform: capitalize; height: 80px">{recommend_movie[2].lower()}</h5>
        <div style="width: 300px; height: 400px;">
            <img src="https://irwa-project.weebly.com/uploads/1/4/7/4/147496024/{clean_string(str(recommend_movie[2].lower()))}.jpg" style="width: 100%; height: 100%;">
        </div>
        """,
        unsafe_allow_html=True
        )

    with col3:
        # st.text(recommend_movie[3])
        # st.image(f"./movies/{recommend_movie[3].lower()}.jpg")
        st.markdown(
            f"""
        <div style="display: flex; flex-direction: column; width: 100%; height: 100%; justify-content: center; margin-top: 30px;">
        <h5 style="text-transform: capitalize; height: 80px">{recommend_movie[3].lower()}</h5>
        <div style="width: 300px; height: 400px;">
            <img src="https://irwa-project.weebly.com/uploads/1/4/7/4/147496024/{clean_string(str(recommend_movie[3].lower()))}.jpg" style="width: 100%; height: 100%;">
        </div>
        """,
        unsafe_allow_html=True
        )
    with col4:
        # st.text(recommend_movie[4])
        # st.image(f"./movies/{recommend_movie[4].lower()}.jpg")
        st.markdown(
            f"""
        <div style="display: flex; flex-direction: column; width: 100%; height: 100%; justify-content: center; margin-top: 30px;">
        <h5 style="text-transform: capitalize; height: 80px">{recommend_movie[4].lower()}</h5>
        <div style="width: 300px; height: 400px;">
            <img src="https://irwa-project.weebly.com/uploads/1/4/7/4/147496024/{clean_string(str(recommend_movie[4].lower()))}.jpg" style="width: 100%; height: 100%;">
        </div>
        """,
        unsafe_allow_html=True
        )


if not recommend_btn:

    st.markdown(
        f"""
        <div>
            <h1>Top Movies...</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    num_rows = 3
    num_columns = 4

    rows = [st.columns(num_columns) for _ in range(num_rows)]

    count = 0
    for row in rows:
        for i in range(num_columns):
            with row[i]:
                if recommendations:
                    image = images[count + i].replace(" ", "-").replace("'", "-").replace("(", "").replace(")", "").replace(",", "")
                    print(image)

                    recommendation, poster_url = recommendations.pop(0)
                    st.markdown(
                        f"""
                        <div style="display: flex; flex-direction: column; width: 100%; height: 100%; justify-content: center; margin-top: 30px;">
                        <h5 style="text-transform: capitalize; height: 80px">{images[count + i].split(".")[0]}</h5>
                        <div style="width: 300px; height: 400px;">
                            <img src="https://irwa-project.weebly.com/uploads/1/4/7/4/147496024/{image}" style="width: 100%; height: 100%;">
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        count =+ num_columns

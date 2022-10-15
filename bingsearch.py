import requests
import json
import streamlit as st
from PIL import Image
from io import BytesIO
import urllib.request
from api_secrets import key

BASE_URI = 'https://api.bing.microsoft.com/v7.0/images/visualsearch'
SUBSCRIPTION_KEY = key
HEADERS = {'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}


@st.cache
def load_image_from_file(image_file):
    img = Image.open(image_file)
    return img


def load_image_from_url(url):
    file_name = "myfile"
    urllib.request.urlretrieve(url, file_name)
    img = Image.open(file_name)
    return img


@st.cache
def start_visual_search(file):
    globals()
    response = requests.post(BASE_URI, headers=HEADERS, files=file)
    response.raise_for_status()
    res_json = response.json()
    return res_json


if __name__ == "__main__":
    st.title("Bing Visual Search Demo")
    img = ""
    file_mode = st.selectbox("Choose a way to upload an image", [
                             "Local File", "URL"])
    if file_mode == "Local File":
        uploaded_file = st.file_uploader(
            "Upload an image", type=['png', 'jpeg', 'jpg'])
        if uploaded_file is not None:
            img = load_image_from_file(uploaded_file)
            st.image(img)

    elif file_mode == "URL":
        img_url = st.text_input("Enter the url of an image",
                                value="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBJdljisCbs-ZpmIhLQmtY4dAH7mHJ_Supiw&usqp=CAU")
        img = load_image_from_url(img_url)
        st.image(img)

    if img != "" and st.checkbox("Start Searching"):
        output = BytesIO()
        img.save(output, format=img.format)
        hex_data = output.getvalue()
        file = {'image': ('myfile', hex_data)}
        try:
            res = start_visual_search(file)
            with open("./response.json", "w") as fh:
                json.dump(res, fh)
            res_list = res['tags'][0]['actions']
            for action in res_list:
                if action['actionType'] != "PagesIncluding" and action['actionType'] != "VisualSearch":
                    continue
                image_list = []
                for idx, value in enumerate(action['data']['value']):
                    if idx >= 10:
                        break
                    try:
                        url = value['contentUrl']
                        if url[-3:] in ['jpg', 'png']:
                            image_list.append((value['name'], url))
                    except:
                        pass
                st.header(action['actionType'])
                st.write(f"found {len(image_list)}")
                st.image([item[1] for item in image_list],
                         use_column_width=True,
                         caption=[item[0] for item in image_list])

        except Exception as ex:
            st.warning(ex)
            raise ex

# action['actionType'] != "PagesIncluding" and

# Bing-Visual-Search-Demo

This repository demonstrates the capabilities of Bing's Visual Search using Python and Streamlit. The application allows users to upload an image either from their local machine or via a URL. Once uploaded, the application uses the Bing Visual Search API to find similar images and displays the results.

## Set Up

### Installation

To get started, first install all the required packages:

```bash
pip install -r requirements.txt
```

### Configuration

1. Create a Bing resource on Azure.
2. Create a new file named `api_secrets.py`.
3. Inside `api_secrets.py`, add your API key:

```python
key = <your_api_key>
```

### Running the App

To start the application, use the following command:

```bash
streamlit run bingsearch.py
```

## Features

- **Image Upload**: Users can upload images either from their local machine or by providing a URL.
- **Visual Search**: Once an image is uploaded, users can initiate a visual search to find similar images using Bing's Visual Search API.
- **Results Display**: The application displays the found images along with their names.

## Languages Used

- [Python](https://github.com/ShaoXiangChien/Bing-Visual-Search-Demo/search?l=python) (100%)

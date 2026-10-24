# Streamlit CSV Uploader App

This project is a simple Streamlit application that allows users to upload a CSV file, view its contents, and visualize data.

## Features

- Upload a CSV file.
- Display the first 10 rows of the uploaded file.
- Show basic statistics (mean, min, max) for numeric columns.
- Select a numeric column to plot as a line chart.
- Error handling for empty files or files without numeric columns.

## Requirements

To run this app, you need to have Python installed along with the following packages:

- pandas
- streamlit

## Installation

1. Clone the repository or download the files.
2. Navigate to the project directory.
3. Install the required packages using pip:

```
pip install -r requirements.txt
```

## Running the App

To run the Streamlit app, use the following command:

```
streamlit run app.py
```

Open your web browser and go to the URL provided in the terminal to interact with the app.
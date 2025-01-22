# Machine Downtime Prediction API

This is a RESTful API built using Flask, which allows users to upload data, train a machine learning model for predicting machine downtime, and make predictions based on input features.

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
  - [POST /upload](#post-upload)
  - [POST /train](#post-train)
  - [POST /predict](#post-predict)
- [Example Requests and Responses](#example-requests-and-responses)

---

## Setup Instructions

1. **Clone the repository** (or create a directory to store the code).

   ```bash
   git clone https://github.com/jd1t25/Machine-Prediction.git
   cd Machine-Prediction
   ```

2. **Create Virtual Environment**: Create python virtual environment using venv
    
    - For Windows
    ```bash
    python -m venv myenv
    myenv\Scripts\activate
    ```

    - For Linux
    ```bash
    python -m venv myenv
    source myenv/bin/activate
    ```
    
3. **Install dependencies**: Make sure you have Python 3.8+ installed, then install the necessary dependencies using pip:
    
    ```bash
    pip install -r requirements.txt
    ```

## Running the APP

To start the Flask APP locally, simply run:

``` bash
python app.py
```
    
The APP will be available at `http://localhost:5000`

## API Endpoints

- Tested on POSTMAN

### POST /upload

This endpoint allows users to upload a CSV file containing the data to train the model.

## POST /upload

This endpoint allows users to upload a CSV file containing the data to train the model.

#### Request:

- **Method**: `POST`
- **URL**: `/upload`
- **Body**: Multipart form data containing the file (CSV).

#### Example Request (using Postman or cURL):

- **Form Data**:
    - **Key**: `file`
    - **Value**: `<your-csv-file>`

#### Response:

- **Status Code**: `200 OK`
- **Body**:
    ```json
    {
        "Message": "Uploaded Successful and File Saved"
    }
    ```

## POST /train

This endpoint processes the uploaded CSV file, trains the Gradient Boosting model, and returns a classification report.

### Request:

- **Method**: `POST`
- **URL**: `/train`

### Response:

- **Status Code**: `200 OK`
- **Body**:
    ```json
    f1_score: ...
    support: ...
    ```

## POST /predict

This endpoint predicts whether there will be downtime based on the input features.

### Request:

- **Method**: `POST`
- **URL**: `/predict`
- **Body**:
    ```json
    {
        "Machine_ID": 2.0,
        "Coolant_Temperature": 28.7,
        "Cutting(kN)": 2.57
    }
    ```

### Response:

- **Status Code**: `200 OK`
- **Body**:
    ```json
    {
        "Downtime": "No",
        "Confidence": 0.92
    }
    ```

### More Examples

- **Example1**:
    ```json
    {
    "Machine_ID": 0,
    "Coolant_Temperature": 20.9,
    "Cutting(kN)": 1.99
    }
    ```
- **Example2**:
    ```json
    {
    "Machine_ID": 1,
    "Coolant_Temperature": 50,
    "Cutting(kN)": 2.5
    }
    ```


# Machine Downtime Prediction API

This is a RESTful API built using Flask, which allows users to upload data, train a machine learning model for predicting machine downtime, and make predictions based on input features.

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
  - [POST /upload](#post-upload)
  - [POST /train](#post-train)
  - [POST /predict](#post-predict)
- [Example Requests and Responses](#example-requests-and-responses)

---

## Setup Instructions

1. **Clone the repository** (or create a directory to store the code).

   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Install dependencies: Make sure you have Python 3.8+ installed, then install the necessary dependencies using pip:
    
    ```bash
    pip install -r requirements.txt
    ```

## Running the APP

To start the Flask APP locally, simply run:

    ```bash
    python app.py
    ```
The APP will be available at `http://localhost:5000`

## API Endpoints

- Tested on POSTMAN

### POST /upload

This endpoint allows users to upload a CSV file containing the data to train the model.

## POST /upload

This endpoint allows users to upload a CSV file containing the data to train the model.

#### Request:

- **Method**: `POST`
- **URL**: `/upload`
- **Body**: Multipart form data containing the file (CSV).

#### Example Request (using Postman or cURL):

- **Form Data**:
    - **Key**: `file`
    - **Value**: `<your-csv-file>`

#### Response:

- **Status Code**: `200 OK`
- **Body**:
    ```json
    {
        "Message": "Uploaded Successful and File Saved"
    }
    ```

## POST /train

This endpoint processes the uploaded CSV file, trains the Gradient Boosting model, and returns a classification report.

### Request:

- **Method**: `POST`
- **URL**: `/train`

### Response:

- **Status Code**: `200 OK`
- **Body**:
    ```json
    f1_score: ...
    support: ...
    ```

## POST /predict

This endpoint predicts whether there will be downtime based on the input features.

### Request:

- **Method**: `POST`
- **URL**: `/predict`
- **Body**:
    ```json
    {
        "Machine_ID": 2.0,
        "Coolant_Temperature": 28.7,
        "Cutting(kN)": 2.57
    }
    ```

### Response:

- **Status Code**: `200 OK`
- **Body**:
    ```json
    {
        "Downtime": "No",
        "Confidence": 0.92
    }
    ```

### More Examples

- **Example1**:
    ```json
    {
    "Machine_ID": 0,
    "Coolant_Temperature": 20.9,
    "Cutting(kN)": 1.99
    }
    ```
- **Example2**:
    ```json
    {
    "Machine_ID": 1,
    "Coolant_Temperature": 50,
    "Cutting(kN)": 2.5
    }
    ```

### Outputs

- Upload
[/upload](assets/pic1.png)

- Train
[/train](assets/pic2.png)

- Predict
[/predict](assets/pic3.png)
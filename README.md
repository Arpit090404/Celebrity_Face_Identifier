# Celebrity_Face_Identifier
# Celebrity Face Identifier

## About the Project

The **Celebrity Face Identifier** is a web-based application that leverages machine learning to detect and identify celebrities from user-uploaded images. Users can simply upload a picture, and the application will process it to determine if a known celebrity face is present and, if so, identify them.

This project demonstrates an end-to-end machine learning pipeline, from model training using various image processing techniques to deployment as a user-friendly web interface.

## Features

- **Image Upload**: Easy and intuitive image upload functionality via a drag-and-drop interface.
- **Celebrity Recognition**: Utilizes a pre-trained machine learning model to identify celebrities.
- **Web Interface**: A simple and clean web application for user interaction.
- **Backend Processing**: Efficient backend for handling image uploads and running inference.

## Technologies Used

The project is built using a combination of Python for the backend and machine learning, and standard web technologies for the frontend.

### Frontend:

- HTML5  
- CSS3 (`app.css`, `dropzone.min.css`)  
- JavaScript (`app.js`, `dropzone.min.js`)  

### Backend & Machine Learning:

- Python  
- Flask (likely used in `server.py` for the web server)  
- Scikit-learn / OpenCV / Keras / TensorFlow (likely used in `Image_classifier_model.ipynb` and related utilities like `wavelet.py` for image preprocessing)  
- Jupyter Notebook (`Image_classifier_model.ipynb`)  

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.x  
- `pip` (Python package installer)

You will also need to install the necessary Python libraries. It's recommended to create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Arpit090404/Celebrity_Face_Identifier.git
cd Celebrity_Face_Identifier
```

2. Install Python dependencies:  
(Note: You might need to infer the exact libraries from `Image_classifier_model.ipynb` and `server.py` or create a `requirements.txt`.)

```bash
pip install Flask
pip install numpy
pip install opencv-python
pip install scikit-learn
pip install pandas
pip install matplotlib
pip install jupyter
```

> 💡 **Recommendation:** Create a `requirements.txt` file listing all exact dependencies for easier setup.

### Train the Model (if not already trained/provided)

- Open and run the `Image_classifier_model.ipynb` Jupyter notebook.
- This notebook should handle:
  - Data loading
  - Preprocessing (potentially using `wavelet.py`)
  - Model training
  - Saving the trained model artifact

Ensure the trained model is saved in a location accessible by `server.py`.

## Usage

### Start the backend server:

```bash
python server.py
```

The server will typically start on [http://127.0.0.1:5000](http://127.0.0.1:5000) or a similar local address.

### Open the web application:

- Navigate to `app.html` in your web browser.
- You might need to open it directly if `server.py` is serving only the API.
- Alternatively, configure `server.py` to serve `app.html` on the root endpoint.

### Upload an image:

- Use the drag-and-drop area or click to upload an image containing a face.
- The application will then display the detected celebrity (or "unknown" if not identified).

## Project Structure

```
.
├── Image_classifier_model.ipynb   # Jupyter Notebook for model training and evaluation
├── README.md                      # This README file
├── app.css                        # Stylesheet for the web application
├── app.html                       # Frontend HTML for the web interface
├── app.js                         # Frontend JavaScript for interactivity and API calls
├── dropzone.min.css               # Styles for the Dropzone.js library
├── dropzone.min.js               # JavaScript for the Dropzone.js library (file uploads)
├── server.py                      # Flask backend server for API endpoints and model inference
├── util.py                        # Utility functions (e.g., for image preprocessing)
├── wavelet.py                     # Specific script likely for wavelet transformations (image features)
├── saved_model/                   # (Suggested) Directory to store the trained model
└── images/                        # (Suggested) Directory for sample images or datasets
```

> 📂 **Note:** The `saved_model/` and `images/` directories are suggestions. If you have trained models or sample data, ensure they are structured and mentioned accordingly.

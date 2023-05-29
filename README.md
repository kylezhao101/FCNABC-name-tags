# FCNABC Name Tags

This is a web application that allows users to input names, which are stored in a text file. It generates a PDF file containing name tags by merging the inputted names with an existing PDF template.

## Features

- Users can input names through a web interface.
- The inputted names are stored in a text file.
- The names are merged with an existing PDF template to generate a PDF file with name tags.
- Users can download the generated PDF file.

## Technologies Used

- Python
- Flask
- PyPDF2
- reportlab

## Installation

1. Clone the repository:

git clone https://github.com/kylezhao101/FCNABC-name-tags.git

2. Install the required Python packages using pip:

pip install -r requirements.txt

3. Place your existing PDF template file in the project directory with the name `original.pdf`. Make sure it has the appropriate layout for name tags.

4. Run the Flask application:

python app.py

5. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Enter the names of the individuals, with each name on a separate line, in the input field on the home page.

2. Click the "Save" button to save the names to the text file.

3. To generate the name tags, click the "Download PDF" button. This will merge the inputted names with the existing PDF template and initiate the download of the generated PDF file.

## Customization

- You can customize the layout and design of the name tags by modifying the existing PDF template file (`original.pdf`). Ensure that the coordinates for placing the names are adjusted accordingly in the Python script (`pdfScript.py`).


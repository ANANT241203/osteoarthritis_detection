# Osteoarthritis Detection Web Application

This is a web application developed using Django, TensorFlow, and Python to detect the presence of Osteoarthritis and assess its severity. The application utilizes a convolutional neural network (CNN) to analyze the uploaded X-ray image and provide instant results.

## Features

- User registration: The web application provides a simple registration page for users to create an account.
- Osteoarthritis detection: Users can upload an X-ray image through the application.
- Severity assessment: The application uses a CNN to analyze the X-ray image and determine the severity of Osteoarthritis.
- Instant results: Once the analysis is complete, the application displays the detection results immediately.

## Requirements

To run this project locally, you need to have the following installed:

- Python 3.x: The programming language used for the backend development.
- Django: A Python web framework used for building the web application.
- TensorFlow: An open-source machine learning framework used for training and deploying the CNN model.
- Other Python dependencies: These are listed in the `requirements.txt` file.

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/your-repo.git
```

2. Navigate to the project directory:

```
cd osteoarthritis-detection
```

3. Create and activate a virtual environment (optional but recommended):

```
python3 -m venv venv
source venv/bin/activate
```

4. Install the project dependencies:

```
pip install -r requirements.txt
```

5. Set up the database:

```
python manage.py migrate
```

6. Run the development server:

```
python manage.py runserver
```

7. Access the application in your web browser at `http://localhost:8000`.

## Usage

1. Register an account using the provided registration page.
2. Log in with your credentials.
3. Once logged in, you will be redirected to the main application page.
4. Click on the "Upload X-ray" button to select an X-ray image for analysis.
5. Wait for the analysis to complete.
6. The application will display the detection results, including the presence of Osteoarthritis and its severity.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Develop and test your changes locally.
4. Commit your changes and push them to your forked repository.
5. Submit a pull request explaining your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to the developers of Django, TensorFlow, and other open-source libraries used in this project.

## Contact

If you have any questions or suggestions, please feel free to contact the project maintainer at anant241203@gmail.com
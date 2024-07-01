
# Streamlit Projects

Welcome to the Streamlit Projects repository! This repository contains three small projects built using Streamlit:

1. **Correction Word**: Utilizes Levenshtein distance for word correction.
2. **Object Detection**: Implements object detection functionalities.
3. **Chatbot**: Employs Hugging Chat for chatbot capabilities.

## Table of Contents
- [Installation](#installation)
- [Project Descriptions](#project-descriptions)
  - [Correction Word](#correction-word)
  - [Object Detection](#object-detection)
  - [Chatbot](#chatbot)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/hiephoangt/Streamlit.git
    cd Streamlit
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    conda create --name streamlit-env
    conda activate streamlit-env
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Project Descriptions

### Correction Word
This project uses Levenshtein distance to provide word correction functionalities. It takes an input word from the user and suggests corrections based on the closest matches.
![Correction Word](D:\Github\AIO_project\Streamlit\data\word_correction.png)
### Object Detection
This project implements object detection using pre-trained models. It allows users to upload images and the application will identify and label objects within the image.
![Correction Word](D:\Github\AIO_project\Streamlit\data\objectdetection.png)

### Chatbot
The Chatbot project leverages Hugging Chat to create an interactive chatbot. Users can have real-time conversations with the chatbot, which utilizes advanced natural language processing models.
![Correction Word](D:\Github\AIO_project\Streamlit\data\chatbot.png)

## Usage

To run any of the projects, navigate to the respective directory and start the Streamlit application:

```bash
streamlit run app.py
```

Replace `app.py` with the appropriate script for the project you want to run. For example, if you are in the `correction_word` directory, the command might look like:

```bash
streamlit run correction_word.py
```

Follow similar steps for the `object_detection` and `chatbot` projects.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any enhancements or bug fixes.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

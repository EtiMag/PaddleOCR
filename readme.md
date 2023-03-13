#### Setup the environment:
Assumed environment is the docker image defined [here](https://github.com/InseeFrLab/images-datascience/tree/main/python-datascience), within the Onyxia catalog.
1. Clone the repository:
    ```
    git clone https://$GIT_USER_NAME:$GITHUB_PERSONAL_ACCESS_TOKEN@github.com/EtiMag/PaddleOCR.git
    cd PaddleOCR
    ```
    
2. Run setup file
    ```
    chmod +x install.sh
    ./install.sh && source ~/.bashrc && cd PaddleOCR
    ```

3. Test PaddleOCR on an image
    ```
    poetry run paddleocr --image_dir test-files/ticket-de-caisse-5.png --use_gpu false --lang en
    ```

#### Documentation
[PaddleOCR PyPi documentation](https://pypi.org/project/paddleocr/)

#### View OCR on an image
To view the OCR recognition (red boxes around text ranges and text extracted by the model), run:
```
poetry run exemple.py
```
Note: the files PaddleOCR/test-files/ticket-de-caisse-5_OCRised_text.txt and PaddleOCR/test-files/ticket-de-caisse-5_OCRised.png are an exemple of output.
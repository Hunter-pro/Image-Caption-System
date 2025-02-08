# Image Captioning with BLIP

This project utilizes the **BLIP (Bootstrapped Language-Image Pretraining)** model from Salesforce to generate captions for images. It uses the `gradio` library to provide a user-friendly interface.

## Features

- Upload an image to generate a caption.
- Uses `transformers` and `PIL` for image processing.
- Simple and interactive UI with `gradio`.

## Installation

Clone the repository:

```sh
git clone https://github.com/Hunter-pro/Image-Caption-System.git
cd Image-Caption-System
```

Install dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Run the script to start the Gradio interface:

```sh
python app.py
```

Then, open the provided `localhost` link in your browser and upload an image to generate a caption.

## Dependencies

- `gradio`
- `transformers`
- `PIL`
- `torch`

Install dependencies manually if needed:

```sh
pip install gradio transformers pillow torch
```


## Model Information

This project uses the **BLIP-Image-Captioning-Base** model from [Salesforce](https://huggingface.co/Salesforce/blip-image-captioning-base), which is trained for image-to-text captioning.

## License

This project is open-source and available under the MIT License.



import gradio as gr
from transformers import BlipProcessor,BlipForConditionalGeneration
from PIL import Image

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image):
    inputs = processor(images=image,return_tensors='pt')
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0],skip_special_tokens = True)
    return caption

def caption_image(image):
    try:
        caption = generate_caption(image)
        return caption
    except Exception as e:
        return f"an error has occurred: {str(e)}"
    
iface = gr.Interface(
    fn = caption_image,
    inputs = gr.Image(type='pil'),
    outputs = "text",
    title = "image caption with BLIP",
    description="Upload an image to generate a caption"
)

iface.launch()
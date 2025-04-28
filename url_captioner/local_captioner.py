import glob
import os
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base")

image_dir = './images/'
image_exts = ["jpg", "jpeg", "png"]

# URL of the page to scrape
url = "https://en.wikipedia.org/wiki/IBM"


# Open a file to write the captions
with open("./local_captions.txt", "w") as caption_file:
    # Iterate over each img element
    for image_ext in image_exts:
        # Debug: 
        # print("image_dir:", image_dir)
        # print("image_ext:", image_ext)  
        # print("Contents of image_dir:", os.listdir(image_dir))  
        # print('glob', glob.glob(os.path.join(image_dir, f"*.{image_ext}")))
        for img_path in glob.glob(os.path.join(image_dir, f"*.{image_ext}")):
            print('img_path', img_path)
            # Load your image
            raw_image = Image.open(img_path).convert('RGB')

            raw_image = raw_image.convert('RGB')

            # Process the image
            inputs = processor(raw_image, return_tensors="pt")
            # Generate a caption for the image
            out = model.generate(**inputs, max_new_tokens=50)
            # Decode the generated tokens to text
            caption = processor.decode(out[0], skip_special_tokens=True)
            print('Caption:', caption)

            # Write the caption to the file, prepended by the image URL
            caption_file.write(f"{img_path}: {caption}\n")

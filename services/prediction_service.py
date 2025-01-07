from PIL import Image
from flask import jsonify
import torch
from torchvision import transforms, models
from config import SECRET_KEY

# Load model and preprocessing
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet152()
model.fc = torch.nn.Linear(model.fc.in_features, 26)
model.load_state_dict(torch.load("trained_model.pth", map_location=device))
model = model.to(device)
model.eval()

preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

CLASS_LABELS = [
    "bluebell", "buttercup", "colts_foot", "corn_poppy", "cowslip", 
    "crocus", "daffodil", "daisy", "dandelion", "foxglove", 
    "fritillary", "geranium", "hibiscus", "iris", "lily_valley", 
    "pansy", "petunia", "rose", "snowdrop", "sunflower", 
    "tigerlily", "tulip", "wallflower", "water_lily", "wild_tulip", 
    "windflower"
]

def predict_image(file):
    try:
        image = Image.open(file.stream).convert("RGB")
        input_tensor = preprocess(image).unsqueeze(0).to(device)

        with torch.no_grad():
            outputs = model(input_tensor)
            _, predicted_class = torch.max(outputs, 1)
        
        predicted_label = CLASS_LABELS[predicted_class.item()]
        return jsonify({"predicted_label": predicted_label, "predicted_class": predicted_class.item() }), 200
    except Exception as e:
        return jsonify({"error": f"Error during prediction: {str(e)}"}), 500

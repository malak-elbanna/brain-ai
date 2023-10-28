from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image

app = Flask(__name__)

def predict_label(img_path):
    model = load_model('model.json')
    img = image.load_img(img_path, target_size=(100, 100))
    img = image.img_to_array(img) / 255.0
    img = img.reshape(1, 100, 100, 3)
    prediction = model.predict_label(img)[0]
    return prediction

@app.route('/', methods=['GET', 'POST'])
def render():
    if request.method == 'POST':
        img = request.files['my_image']
        img_path = "static/" + img.filename
        img.save(img_path)
        prediction = predict_label(img_path)
        return render_template('index.html', prediction=prediction, img_path=img_path)
    else:
        return render_template('index.html')

@app.route('/submit', methods=['POST'])
def get_result():
    if request.method == 'POST':
        img = request.files['my_image']
        img_path = "static/" + img.filename
        img.save(img_path)
        prediction = predict_label(img_path)
        return render_template('index.html', prediction=prediction, img_path=img_path)
    
if __name__ == '__main__':
    app.run(debug=True)
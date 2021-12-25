import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor
import numpy as np
interpreter = tflite.Interpreter(model_path='models/model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']
preprocessor = create_preprocessor('xception',(150,150))
def get_weather(path):
    img = preprocessor.from_path(path)
    interpreter.set_tensor(input_index, img)
    interpreter.invoke()
    output = interpreter.get_tensor(output_index)
    w_set = ['cloudy', 'rain', 'shine', 'sunrise']
    best = np.argmax(output[0])
    return {'decision': w_set[best], 'results': list(zip(w_set, output[0]))}
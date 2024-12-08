import pickle


def calculate_output(GHI, DNI, LAT, LON, TEMP, HUM, WIN):
    x = [[GHI, DNI, LAT, LON, TEMP]]
    mean = [1769.60258216, 1622.91408451, 17.13321479, 32.14381385, 18.17629108]
    std = [407.15774196, 496.93173293, 26.79428739, 90.51827623, 9.86180637]
    for i in range(5):
        x[0][i] = (x[0][i] - mean[i]) / std[i]
    # Wczytaj model
    with open('sgdregressor_model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    return loaded_model.predict(x)[0]

import dash
from dash import dcc, html, Input, Output, State
import pandas as pd

from front.calculate_output import calculate_output
from scatter_map import create_map_figure  # Ensure this imports the adjusted function for your dataset

# Load data from the CSV file
csv_file_path = 'city_outputs.csv'  # Update with your actual file name and ensure it matches the data
data = pd.read_csv(csv_file_path)

# Create the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)  # Suppress callback exceptions
app.title = "SOLAR – Site Optimization for Location and Array Recommendation"

# App layout
app.layout = html.Div(
    style={'backgroundColor': 'rgb(20, 20, 20)', 'color': 'white', 'padding': '20px'},
    children=[
        html.Div(
            style={'display': 'flex', 'flexDirection': 'row', 'width': '100%', 'gap': '20px'},
            children=[
                html.Div(
                    style={'width': '20%', 'padding': '10px', 'backgroundColor': 'rgb(30, 30, 30)',
                           'borderRadius': '10px'},
                    children=[
                        html.H2("Add Location", style={'textAlign': 'center'}),
                        html.Div([
                            html.Label("Name:", style={'marginTop': '10px'}),
                            dcc.Input(id='city-name', type='text', placeholder='Enter name',
                                      style={'width': '100%'}),
                            html.Label("Latitude:", style={'marginTop': '10px'}),
                            dcc.Input(id='latitude', type='number', placeholder='Enter latitude',
                                      style={'width': '100%'}),
                            html.Label("Longitude:", style={'marginTop': '10px'}),
                            dcc.Input(id='longitude', type='number', placeholder='Enter longitude',
                                      style={'width': '100%'}),
                            html.Label("GHI (kWh/m²):", style={'marginTop': '10px'}),
                            dcc.Input(id='ghi', type='number', placeholder='Enter GHI', style={'width': '100%'}),
                            html.Label("DNI (kWh/m²):", style={'marginTop': '10px'}),
                            dcc.Input(id='dni', type='number', placeholder='Enter DNI', style={'width': '100%'}),
                            html.Label("Temperature (°C):", style={'marginTop': '10px'}),
                            dcc.Input(id='temp', type='number', placeholder='Enter temperature',
                                      style={'width': '100%'}),
                            html.Label("Humidity (%):", style={'marginTop': '10px'}),
                            dcc.Input(id='humidity', type='number', placeholder='Enter humidity',
                                      style={'width': '100%'}),
                            html.Label("Wind Speed (m/s):", style={'marginTop': '10px'}),
                            dcc.Input(id='wind-speed', type='number', placeholder='Enter wind speed',
                                      style={'width': '100%'}),
                            html.Button("Add City", id='add-city', n_clicks=0,
                                        style={'marginTop': '20px', 'width': '100%'})
                        ])
                    ]
                ),
                html.Div(
                    style={'width': '80%'},
                    children=[
                        dcc.Graph(
                            id='scatter-map',
                            style={'height': '700px', 'margin': '20px auto'}
                        )
                    ]
                )
            ]
        )
    ]
)


# Callback to initialize and update the scatter map
@app.callback(
    Output('scatter-map', 'figure'),
    Input('add-city', 'n_clicks'),
    State('city-name', 'value'),
    State('latitude', 'value'),
    State('longitude', 'value'),
    State('ghi', 'value'),
    State('dni', 'value'),
    State('temp', 'value'),
    State('humidity', 'value'),
    State('wind-speed', 'value')
)
def update_or_initialize_map(n_clicks, city_name, latitude, longitude, ghi, dni, temp, humidity, wind_speed):
    global data

    # Add a new city if form data is provided and the button is clicked
    if n_clicks > 0 and city_name and latitude is not None and longitude is not None:
        # Calculate output dynamically using the input parameters
        output = calculate_output(ghi, dni, latitude, longitude, temp, humidity, wind_speed)

        new_data = pd.DataFrame({
            'Name': [city_name],
            'Latitude': [latitude],
            'Longitude': [longitude],
            'Output': [output],
            'Humidity': [humidity],
            'Wind Speed': [wind_speed]
        })
        data = pd.concat([data, new_data], ignore_index=True)

    # Generate the scatter map using the updated data
    return create_map_figure(data)


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

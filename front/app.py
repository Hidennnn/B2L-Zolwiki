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
app.title = "City Outputs Map"

# App layout
app.layout = html.Div(
    style={'backgroundColor': 'rgb(20, 20, 20)', 'color': 'white', 'padding': '20px'},
    children=[
        html.Div(
            style={'display': 'flex', 'flexDirection': 'row', 'width': '100%', 'gap': '20px'},
            children=[
                html.Div(
                    style={'width': '20%', 'padding': '10px', 'backgroundColor': 'rgb(30, 30, 30)', 'borderRadius': '10px'},
                    children=[
                        html.H2("Add City", style={'textAlign': 'center'}),
                        html.Div([
                            html.Label("City Name:", style={'marginTop': '10px'}),
                            dcc.Input(id='city-name', type='text', placeholder='Enter city name', style={'width': '100%'}),
                            html.Label("Latitude:", style={'marginTop': '10px'}),
                            dcc.Input(id='latitude', type='number', placeholder='Enter latitude', style={'width': '100%'}),
                            html.Label("Longitude:", style={'marginTop': '10px'}),
                            dcc.Input(id='longitude', type='number', placeholder='Enter longitude', style={'width': '100%'}),
                            html.Button("Add City", id='add-city', n_clicks=0, style={'marginTop': '20px', 'width': '100%'})
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
)
def update_or_initialize_map(n_clicks, city_name, latitude, longitude):
    global data

    # Add a new city if form data is provided and the button is clicked
    if n_clicks > 0 and city_name and latitude is not None and longitude is not None:
        new_data = pd.DataFrame({
            'Name': [city_name],
            'Latitude': [latitude],
            'Longitude': [longitude],
            'Output': [calculate_output()]
        })
        data = pd.concat([data, new_data], ignore_index=True)

    # Generate the scatter map using the updated data
    return create_map_figure(data)


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

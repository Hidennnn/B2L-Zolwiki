import dash
from dash import dcc, html, Input, Output, State
import pandas as pd
from scatter_map import create_map_figure
from input_form import create_input_form

# Load data from the CSV file
csv_file_path = 'solar_power_plants.csv'  # Ensure the file path is correct
data = pd.read_csv(csv_file_path)

# Add a computed column for color intensity based on MW/km^2
data['MW_per_km2'] = data['Output (MW)'] / data['Size (km^2)']

# Create the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)  # Suppress callback exceptions
app.title = "Scatter Map with Solar Power Plants"

# App layout
app.layout = html.Div(
    style={'backgroundColor': 'rgb(20, 20, 20)', 'color': 'white', 'padding': '20px'},
    children=[
        html.H1("Scatter Map of Solar Power Plants", style={'fontSize': '2.5em', 'textAlign': 'center'}),
        html.Div(
            style={'display': 'flex', 'flexDirection': 'row', 'width': '100%', 'gap': '20px'},
            children=[
                create_input_form(),  # Input form from input_form.py
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
    Input('add-plant', 'n_clicks'),
    State('plant-name', 'value'),
    State('latitude', 'value'),
    State('longitude', 'value'),
    State('size', 'value'),
    State('output', 'value')
)
def update_or_initialize_map(n_clicks, plant_name, latitude, longitude, size, output):
    global data

    # Add a new solar plant if form data is provided and the button is clicked
    if n_clicks > 0 and plant_name and latitude is not None and longitude is not None and size is not None and output is not None:
        new_data = pd.DataFrame({
            'Solar Power Plant': [plant_name],
            'Location': ['Newly Added'],  # Placeholder for location
            'Latitude': [latitude],
            'Longitude': [longitude],
            'Size (km^2)': [size],
            'Output (MW)': [output],
            'Efficiency': [None],  # Efficiency can be left as None for now
            'MW_per_km2': [output / size]  # Compute MW per km²
        })
        data = pd.concat([data, new_data], ignore_index=True)

    # Generate the scatter map using the updated data
    return create_map_figure(data)


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

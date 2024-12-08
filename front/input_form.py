from dash import html, dcc


def create_input_form():
    """
    Create the input form for adding a new solar power plant.
    """
    return html.Div(
        style={
            'backgroundColor': 'rgb(40, 40, 40)',
            'padding': '20px',
            'borderRadius': '10px',
            'width': '20%',
            'display': 'flex',
            'flexDirection': 'column',
            'gap': '10px'
        },
        children=[
            html.H3("Add a New Solar Plant", style={'textAlign': 'center'}),
            dcc.Input(
                id='plant-name',
                type='text',
                placeholder='Name',
                style={'padding': '5px'}
            ),
            dcc.Input(
                id='latitude',
                type='number',
                placeholder='Latitude',
                style={'padding': '5px'}
            ),
            dcc.Input(
                id='longitude',
                type='number',
                placeholder='Longitude',
                style={'padding': '5px'}
            ),
            dcc.Input(
                id='size',
                type='number',
                placeholder='Size (km²)',
                style={'padding': '5px'}
            ),
            dcc.Input(
                id='output',
                type='number',
                placeholder='Output (MW)',
                style={'padding': '5px'}
            ),
            html.Button(
                'Add Plant',
                id='add-plant',
                n_clicks=0,
                style={
                    'backgroundColor': 'rgb(80, 80, 80)',
                    'color': 'white',
                    'border': '1px solid #666',
                    'borderRadius': '5px',
                    'padding': '10px 20px',
                    'marginTop': '10px',
                    'cursor': 'pointer',
                    'alignSelf': 'flex-start'
                }
            )
        ]
    )

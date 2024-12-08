import plotly.express as px
from shared_settings import apply_shared_settings

def create_map_figure(data):
    # Replace NaN or invalid values in the Size column with a default value
    data['Size (km^2)'] = data['Size (km^2)'].fillna(1)  # Replace NaN with default size 1

    # Create a scatter geo plot
    fig = px.scatter_geo(
        data,
        lat="Latitude",
        lon="Longitude",
        size="Size (km^2)",  # Size of the markers
        color="MW_per_km2",  # Use MW_per_km2 for color intensity
        hover_data={  # Include solar plant name and other details in hover
            "Solar Power Plant": True,  # Show name on hover
            "Location": True,
            "Size (km^2)": True,
            "Output (MW)": True,
            "MW_per_km2": True,  # Corrected column name
            "Latitude": False,
            "Longitude": False
        },
        projection="natural earth",
        color_continuous_scale="Viridis"
    )

    # Apply shared dark theme settings
    fig = apply_shared_settings(fig, dark_theme=True)

    return fig

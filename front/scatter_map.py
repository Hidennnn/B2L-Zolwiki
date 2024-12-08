import plotly.express as px

def create_map_figure(data):
    # Replace NaN or invalid values in the Output column with a default value
    data['Output'] = data['Output'].fillna(1)  # Replace NaN with default output 1

    # Create a scatter geo plot
    fig = px.scatter_geo(
        data,
        lat="Latitude",
        lon="Longitude",
        color="Output",  # Use Output for color intensity
        hover_data={  # Include city name and other details in hover
            "Name": True,
            "Latitude": True,
            "Longitude": True,
            "Output": True
        },
        projection="natural earth",
        color_continuous_scale="Viridis"
    )

    # Customize the geo layout for dark map and lighter borders
    fig.update_geos(
        landcolor="rgb(30, 30, 30)",  # Dark land color
        oceancolor="rgb(10, 10, 10)",  # Very dark ocean color
        showocean=True,  # Show the ocean
        showland=True,  # Show land
        showlakes=False,  # Hide lakes if desired
        showcountries=True,  # Show country borders
        countrycolor="rgb(100, 100, 100)",  # Light border color
        framecolor="rgb(100, 100, 100)",  # Border around the map
        coastlinecolor="rgb(150, 150, 150)",  # Coastline border color
        bgcolor="rgb(20, 20, 20)"  # Background for the region outside the map
    )

    # General layout updates for better visual contrast
    fig.update_layout(
        title="SOLAR – Site Optimization for Location and Array Recommendation",
        title_font=dict(size=24, color="white"),
        paper_bgcolor="rgb(20, 20, 20)",  # Dark background
        plot_bgcolor="rgb(20, 20, 20)",  # Dark plot area
        font=dict(color="white")  # White text
    )

    return fig

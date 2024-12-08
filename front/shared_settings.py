def apply_shared_settings(fig, dark_theme=True):
    """Apply shared settings to the map."""
    fig.update_geos(
        showcountries=True,
        showcoastlines=True,
        showland=True,
        landcolor='rgb(50, 50, 50)',  # Dark theme land color
        coastlinecolor='rgb(200, 200, 200)',  # Light gray coastlines
        projection_type="natural earth",
        oceancolor='rgb(60, 60, 60)',  # Grey ocean
        showocean=True,
        bgcolor='rgb(33, 33, 33)'  # Color outside the map but inside the map box
    )

    if dark_theme:
        fig.update_layout(
            paper_bgcolor='rgb(30, 30, 30)',  # Dark background
            plot_bgcolor='rgb(30, 30, 30)',  # Dark plot background
            font_color='white',  # Text color
            title_font_color='white',
            coloraxis_colorbar=dict(
                title="Ranking",
                tickvals=[1, 2, 3, 4, 5],
                ticktext=['Bad', 'Fairly Bad', 'Neutral', 'Fairly Good', 'Good']
            )
        )
    return fig

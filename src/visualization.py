from typing import Any

import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure


def build_geo_map(
    df: pd.DataFrame,
    selected_state: str,
    primary_metric: str,
    secondary_metric: str,
    columns: dict[str, Any],
    map_config: dict[str, Any],
    overall_label: str,
) -> Figure:
    zoom_level = (
        map_config["india_zoom"]
        if selected_state == overall_label
        else map_config["state_zoom"]
    )

    fig = px.scatter_mapbox(
        df,
        lat=columns["latitude"],
        lon=columns["longitude"],
        size=primary_metric,
        color=secondary_metric,
        zoom=zoom_level,
        size_max=map_config["size_max"],
        mapbox_style=map_config["style"],
        width=map_config["width"],
        height=map_config["height"],
        hover_name=columns["district"],
        hover_data={
            columns["state"]: True,
            primary_metric: ":,",
            secondary_metric: ":,",
            columns["latitude"]: False,
            columns["longitude"]: False,
        },
        color_continuous_scale=map_config["color_scale"],
    )

    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        coloraxis_colorbar={
            "title": secondary_metric,
            "thickness": 14,
            "len": 0.72,
        },
    )

    return fig

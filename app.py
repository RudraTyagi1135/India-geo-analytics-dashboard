import streamlit as st

from src.config import load_config
from src.data import filter_by_state, get_metric_columns, get_state_options, load_india_data
from src.ui import (
    render_header,
    render_map_context,
    render_page_styles,
    render_sidebar,
    render_summary_metrics,
)
from src.visualization import build_geo_map


def main() -> None:
    config = load_config()
    app_config = config["app"]

    st.set_page_config(
        page_title=app_config["page_title"],
        page_icon=app_config["page_icon"],
        layout=app_config["layout"],
        initial_sidebar_state=app_config["initial_sidebar_state"],
    )

    df = load_india_data(config["data"]["path"])
    metric_columns = get_metric_columns(df, config["columns"]["metric_start_index"])
    state_options = get_state_options(
        df,
        state_column=config["columns"]["state"],
        overall_label=config["sidebar"]["overall_label"],
    )

    render_page_styles()

    selected_state, primary_metric, secondary_metric = render_sidebar(
        state_options=state_options,
        metric_columns=metric_columns,
        sidebar_config=config["sidebar"],
    )

    filtered_df = filter_by_state(
        df=df,
        state_column=config["columns"]["state"],
        selected_state=selected_state,
        overall_label=config["sidebar"]["overall_label"],
    )

    render_header(config["ui"])
    render_summary_metrics(
        filtered_df,
        config["columns"],
        config["regions"],
        selected_state,
        config["sidebar"]["overall_label"],
    )
    render_map_context(selected_state, primary_metric, secondary_metric)

    fig = build_geo_map(
        df=filtered_df,
        selected_state=selected_state,
        primary_metric=primary_metric,
        secondary_metric=secondary_metric,
        columns=config["columns"],
        map_config=config["map"],
        overall_label=config["sidebar"]["overall_label"],
    )

    st.plotly_chart(fig, width=True)


if __name__ == "__main__":
    main()

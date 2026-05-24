from html import escape
from typing import Any

import pandas as pd
import streamlit as st


def render_page_styles() -> None:
    st.markdown(
        """
        <style>
            :root {
                --bg: #f7f8fb;
                --panel: #ffffff;
                --ink: #172033;
                --muted: #647084;
                --line: #d9dee8;
                --accent: #16697a;
            }

            .stApp {
                background: var(--bg);
                color: var(--ink);
            }

            [data-testid="stSidebar"] {
                background: #101827;
                border-right: 1px solid rgba(255, 255, 255, 0.08);
            }

            [data-testid="stSidebar"] * {
                color: #f8fafc;
            }

            [data-testid="stSidebar"] .stSelectbox label {
                color: #d7dde8;
                font-weight: 700;
            }

            [data-testid="stSidebar"] div[data-baseweb="select"] > div {
                background: #ffffff;
                border-color: #334155;
            }

            [data-testid="stSidebar"] div[data-baseweb="select"] div,
            [data-testid="stSidebar"] div[data-baseweb="select"] span,
            [data-testid="stSidebar"] div[data-baseweb="select"] p,
            [data-testid="stSidebar"] div[data-baseweb="select"] input {
                color: #172033 !important;
                -webkit-text-fill-color: #172033 !important;
            }

            [data-testid="stSidebar"] div[data-baseweb="select"] svg {
                color: #172033 !important;
                fill: #172033 !important;
            }

            .main .block-container {
                padding-top: 2rem;
                padding-bottom: 2.5rem;
                max-width: 1400px;
            }

            .dashboard-hero {
                background: linear-gradient(135deg, #ffffff 0%, #eef7f8 100%);
                border: 1px solid var(--line);
                border-radius: 8px;
                padding: 1.45rem 1.6rem;
                margin-bottom: 1rem;
            }

            .eyebrow {
                color: var(--accent);
                font-size: 0.8rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                margin-bottom: 0.35rem;
            }

            .dashboard-title {
                color: var(--ink);
                font-size: 2.15rem;
                font-weight: 850;
                line-height: 1.15;
                margin: 0;
            }

            .dashboard-copy {
                color: var(--muted);
                font-size: 1rem;
                line-height: 1.55;
                max-width: 780px;
                margin: 0.65rem 0 0;
            }

            .section-title {
                color: var(--ink);
                font-size: 1.05rem;
                font-weight: 800;
                margin: 1.15rem 0 0.45rem;
            }

            .metric-card {
                background: var(--panel);
                border: 1px solid var(--line);
                border-radius: 8px;
                padding: 1rem 1.05rem;
                min-height: 104px;
                min-width: 0;
            }

            .metric-label {
                color: #475569;
                font-size: 0.78rem;
                font-weight: 800;
                line-height: 1.25;
                margin-bottom: 0.55rem;
                text-transform: uppercase;
            }

            .metric-value {
                color: var(--ink);
                font-size: clamp(1.55rem, 2.1vw, 2rem);
                font-weight: 850;
                line-height: 1.15;
                overflow-wrap: anywhere;
            }

            .map-note {
                background: #ffffff;
                border: 1px solid var(--line);
                border-left: 4px solid var(--accent);
                border-radius: 8px;
                color: var(--muted);
                padding: 0.85rem 1rem;
                margin: 0.35rem 0 1rem;
            }

            .map-note strong {
                color: var(--ink);
            }

            .stPlotlyChart {
                background: #ffffff;
                border: 1px solid var(--line);
                border-radius: 8px;
                padding: 0.35rem;
            }

            @media (max-width: 768px) {
                .main .block-container {
                    padding-left: 1rem;
                    padding-right: 1rem;
                }

                .dashboard-title {
                    font-size: 1.65rem;
                }

            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar(
    state_options: list[str],
    metric_columns: list[str],
    sidebar_config: dict[str, str],
) -> tuple[str, str, str]:
    with st.sidebar:
        st.title(sidebar_config["title"])
        st.caption(sidebar_config["caption"])

        selected_state = st.selectbox(sidebar_config["region_label"], state_options)
        primary_metric = st.selectbox(sidebar_config["primary_label"], metric_columns)
        secondary_metric = st.selectbox(sidebar_config["secondary_label"], metric_columns)

        st.divider()
        st.caption(sidebar_config["help_text"])

    return selected_state, primary_metric, secondary_metric


def render_header(ui_config: dict[str, str]) -> None:
    st.markdown(
        f"""
        <div class="dashboard-hero">
            <div class="eyebrow">{escape(ui_config["eyebrow"])}</div>
            <h1 class="dashboard-title">{escape(ui_config["title"])}</h1>
            <p class="dashboard-copy">{escape(ui_config["description"])}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_summary_metrics(
    df: pd.DataFrame,
    columns: dict[str, Any],
    regions_config: dict[str, Any],
    selected_state: str,
    overall_label: str,
) -> None:
    total_population = int(df[columns["population"]].sum())
    district_count = df[columns["district"]].nunique()
    if selected_state == overall_label:
        state_count = regions_config.get("official_state_count", 28)
        state_label = "States covered"
    else:
        state_count = 1
        state_label = "Region covered"
    avg_literacy = df[columns["literacy_rate"]].mean()

    metrics = [
        ("Districts", f"{district_count:,}"),
        (state_label, f"{state_count:,}"),
        ("Population", f"{total_population:,}"),
        ("Avg literacy", f"{avg_literacy:.1f}%"),
    ]
    columns_layout = st.columns(4)
    for column, (label, value) in zip(columns_layout, metrics):
        column.markdown(
            (
                '<div class="metric-card">'
                f'<div class="metric-label">{escape(label)}</div>'
                f'<div class="metric-value">{escape(value)}</div>'
                "</div>"
            ),
            unsafe_allow_html=True,
        )


def render_map_context(
    selected_state: str,
    primary_metric: str,
    secondary_metric: str,
) -> None:
    st.markdown('<div class="section-title">Geospatial View</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="map-note">
            <strong>{escape(selected_state)}</strong> is plotted with <strong>{escape(primary_metric)}</strong> as bubble size
            and <strong>{escape(secondary_metric)}</strong> as color intensity.
        </div>
        """,
        unsafe_allow_html=True,
    )

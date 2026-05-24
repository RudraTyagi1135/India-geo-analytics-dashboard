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

            [data-testid="stSidebar"] div[data-baseweb="select"] span,
            [data-testid="stSidebar"] div[data-baseweb="select"] input {
                color: #172033 !important;
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

            div[data-testid="stMetric"] {
                background: var(--panel);
                border: 1px solid var(--line);
                border-radius: 8px;
                padding: 1rem;
            }

            div[data-testid="stMetricLabel"] p {
                color: var(--muted);
                font-weight: 800;
            }

            div[data-testid="stMetricValue"] {
                color: var(--ink);
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
            <div class="eyebrow">{ui_config["eyebrow"]}</div>
            <h1 class="dashboard-title">{ui_config["title"]}</h1>
            <p class="dashboard-copy">{ui_config["description"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_summary_metrics(df: pd.DataFrame, columns: dict[str, Any]) -> None:
    total_population = int(df[columns["population"]].sum())
    district_count = df[columns["district"]].nunique()
    state_count = df[columns["state"]].nunique()
    avg_literacy = df[columns["literacy_rate"]].mean()

    metric_one, metric_two, metric_three, metric_four = st.columns(4)
    metric_one.metric("Districts", f"{district_count:,}")
    metric_two.metric("States covered", f"{state_count:,}")
    metric_three.metric("Population", f"{total_population:,}")
    metric_four.metric("Avg literacy", f"{avg_literacy:.1f}%")


def render_map_context(
    selected_state: str,
    primary_metric: str,
    secondary_metric: str,
) -> None:
    st.markdown('<div class="section-title">Geospatial View</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="map-note">
            <strong>{selected_state}</strong> is plotted with <strong>{primary_metric}</strong> as bubble size
            and <strong>{secondary_metric}</strong> as color intensity.
        </div>
        """,
        unsafe_allow_html=True,
    )

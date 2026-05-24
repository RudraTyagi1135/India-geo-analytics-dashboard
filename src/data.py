from pathlib import Path

import pandas as pd
import streamlit as st


@st.cache_data
def load_india_data(data_path: Path) -> pd.DataFrame:
    return pd.read_csv(data_path)


def get_metric_columns(df: pd.DataFrame, metric_start_index: int) -> list[str]:
    return sorted(df.columns[metric_start_index:])


def get_state_options(
    df: pd.DataFrame,
    state_column: str,
    overall_label: str,
) -> list[str]:
    return [overall_label, *list(df[state_column].unique())]


def filter_by_state(
    df: pd.DataFrame,
    state_column: str,
    selected_state: str,
    overall_label: str,
) -> pd.DataFrame:
    if selected_state == overall_label:
        return df

    return df[df[state_column] == selected_state]

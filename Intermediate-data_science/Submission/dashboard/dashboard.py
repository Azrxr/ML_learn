import io
import pathlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='whitegrid')


def _create_season_df(df):
    season_df = df.groupby('season').agg({'cnt': ['mean', 'sum']}).reset_index()
    season_df.columns = ['season', 'avg_rentals', 'total_rentals']
    return season_df


def _create_weather_df(df):
    weather_df = df.groupby('weathersit').agg({'cnt': ['mean', 'sum']}).reset_index()
    weather_df.columns = ['weathersit', 'avg_rentals', 'total_rentals']
    return weather_df


def _create_hourly_df(df):
    hourly_df = df.groupby('hr').agg({'cnt': 'mean', 'casual': 'mean', 'registered': 'mean'}).reset_index()
    return hourly_df


def _create_workday_hourly_df(df):
    workday_df = df[df['workingday'] == 1].groupby('hr')['cnt'].mean().reset_index()
    workday_df.columns = ['hr', 'workday_avg']
    holiday_df = df[df['workingday'] == 0].groupby('hr')['cnt'].mean().reset_index()
    holiday_df.columns = ['hr', 'holiday_avg']
    merged_df = workday_df.merge(holiday_df, on='hr')
    return merged_df


@st.cache_data
def load_data(path=None):
    try:
        if path is None:
            base = pathlib.Path(__file__).parent
            path = base / 'main_data.csv'
        df = pd.read_csv(path)
        df['dteday'] = pd.to_datetime(df['dteday'])
        return df
    except FileNotFoundError:
        st.error('File main_data.csv tidak ditemukan di folder dashboard. Jalankan cell EXPORT DATA di notebook untuk membuat file ini.')
        return None


def main():
    st.set_page_config(page_title='Dashboard Bike Sharing', layout='wide')

    df = load_data()
    if df is None:
        return

    st.sidebar.image('https://raw.githubusercontent.com/andresxz32/data-visualization-bike-rental/main/bike_logo.png', width=140)
    st.sidebar.header('Filter')

    min_date = df['dteday'].min()
    max_date = df['dteday'].max()
    start_date, end_date = st.sidebar.date_input('Rentang tanggal', [min_date, max_date], min_value=min_date, max_value=max_date)

    seasons = ['Semua'] + list(df['season'].dropna().unique())
    selected_season = st.sidebar.selectbox('Pilih musim', seasons)

    weathers = ['Semua'] + list(df['weathersit'].dropna().unique())
    selected_weather = st.sidebar.selectbox('Pilih kondisi cuaca', weathers)

    workingday_opt = st.sidebar.selectbox('Tipe hari', ['Semua', 'Hari Kerja', 'Hari Libur'])

    # Filter
    mask = (df['dteday'] >= pd.to_datetime(start_date)) & (df['dteday'] <= pd.to_datetime(end_date))
    filtered = df.loc[mask].copy()
    if selected_season != 'Semua':
        filtered = filtered[filtered['season'] == selected_season]
    if selected_weather != 'Semua':
        filtered = filtered[filtered['weathersit'] == selected_weather]
    if workingday_opt == 'Hari Kerja':
        filtered = filtered[filtered['workingday'] == 1]
    elif workingday_opt == 'Hari Libur':
        filtered = filtered[filtered['workingday'] == 0]

    # Header
    st.title('🚴 Dashboard Analisis Bike Sharing')
    st.markdown('Analisis ringkas berdasarkan dataset Bike Sharing — Bahasa Indonesia')
    st.markdown('---')

    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric('Total Penyewaan (filter)', f"{int(filtered['cnt'].sum()):,}")
    with col2:
        st.metric('Rata-rata per jam', f"{filtered['cnt'].mean():.0f}")
    with col3:
        casual_pct = filtered['casual'].sum() / (filtered['cnt'].sum() + 1e-9)
        st.metric('Proporsi Casual', f"{casual_pct*100:.1f}%")
    with col4:
        reg_pct = filtered['registered'].sum() / (filtered['cnt'].sum() + 1e-9)
        st.metric('Proporsi Registered', f"{reg_pct*100:.1f}%")

    st.markdown('---')

    # Visualisasi 1: Musim & Cuaca
    st.subheader('Pengaruh Musim & Kondisi Cuaca')
    s1, s2 = st.columns([1, 1])
    with s1:
        season_df = _create_season_df(filtered)
        season_order = ['Spring', 'Summer', 'Fall', 'Winter']
        season_df = season_df.set_index('season').reindex(season_order).reset_index()
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(data=season_df, x='season', y='avg_rentals', palette='Set2', ax=ax)
        ax.set_title('Rata-rata Penyewaan per Musim')
        ax.set_ylabel('Rata-rata penyewaan')
        st.pyplot(fig)
    with s2:
        weather_df = _create_weather_df(filtered)
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(data=weather_df.sort_values('avg_rentals', ascending=False), x='weathersit', y='avg_rentals', palette='muted', ax=ax)
        ax.set_title('Rata-rata Penyewaan per Kondisi Cuaca')
        ax.set_ylabel('Rata-rata penyewaan')
        plt.xticks(rotation=15)
        st.pyplot(fig)

    st.markdown('---')

    # Visualisasi 2: Pola waktu
    st.subheader('Pola Waktu Penyewaan')
    p1, p2 = st.columns([2, 1])
    hourly = _create_hourly_df(filtered)
    with p1:
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(hourly['hr'], hourly['cnt'], marker='o', color='#2b8cbe')
        ax.fill_between(hourly['hr'], hourly['cnt'], alpha=0.2, color='#2b8cbe')
        ax.set_xticks(range(0, 24))
        ax.set_title('Rata-rata Penyewaan per Jam (0-23)')
        ax.set_ylabel('Rata-rata penyewaan')
        st.pyplot(fig)
    with p2:
        # Top peaks
        top_hours = hourly.nlargest(3, 'cnt')
        st.markdown('Jam tersibuk (rata-rata):')
        for _, row in top_hours.iterrows():
            st.write(f"• {int(row['hr']):02d}:00 — {row['cnt']:.0f} rata-rata")

    # Heatmap jam x hari
    st.markdown('')
    fig, ax = plt.subplots(figsize=(12, 4))
    if 'weekday_name' not in filtered:
        filtered['weekday_name'] = filtered['dteday'].dt.day_name()
    pivot = filtered.pivot_table(values='cnt', index='hr', columns='weekday_name', aggfunc='mean')
    # reorder weekdays if possible
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    cols = [c for c in weekdays if c in pivot.columns]
    pivot = pivot[cols]
    sns.heatmap(pivot, cmap='YlGnBu', ax=ax, cbar_kws={'label': 'Rata-rata penyewaan'})
    ax.set_title('Heatmap: Penyewaan per Jam x Hari')
    st.pyplot(fig)

    st.markdown('---')

    # Komposisi pengguna per jam
    st.subheader('Komposisi Pengguna: Casual vs Registered per Jam')
    comp = filtered.groupby('hr').agg({'casual': 'mean', 'registered': 'mean'}).reset_index()
    fig, ax = plt.subplots(figsize=(12, 3))
    ax.bar(comp['hr'], comp['registered'], label='Registered', color='#2b8cbe')
    ax.bar(comp['hr'], comp['casual'], bottom=comp['registered'], label='Casual', color='#f28e2b')
    ax.set_xticks(range(0, 24))
    ax.set_title('Komposisi pengguna per jam')
    ax.set_ylabel('Rata-rata penyewaan')
    ax.legend()
    st.pyplot(fig)

    st.markdown('---')

    # Download data
    csv = filtered.to_csv(index=False).encode('utf-8')
    st.download_button('Unduh data (CSV)', data=csv, file_name='filtered_main_data.csv', mime='text/csv')

    st.caption('Dashboard Analisis Bike Sharing | Moh Asrori | Dicoding')


if __name__ == '__main__':
    main()
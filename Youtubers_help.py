import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import numpy as np

# Define the URLs for the CSV files
channel_data_url = 'https://github.com/hasielar/Project2/raw/main/Chan.csv'
video_data_url = 'https://github.com/hasielar/Project2/releases/download/a/Vid.Stat.csv'

def load_data(url):
    return pd.read_csv(url)

channel_data = load_data(channel_data_url)
video_data = load_data(video_data_url)

def main():
    st.set_page_config(page_title='Mongolian Youtubers Information', layout='wide')
    st.title('The best Mongolian Channel Statistics')
    # ... (rest of your code remains the same)

    # Bar chart for video views over time for the selected channel
    st.header('Video Views Over Time')
    st.write(f"Video views over time for **{selected_channel}**")
    selected_videos['published_date'] = pd.to_datetime(selected_videos['published_date'])
    views_over_time = selected_videos.groupby(selected_videos['published_date'].dt.date)['views'].sum()

    # Handle infinite values in views_over_time
    views_over_time = views_over_time.replace([np.inf, -np.inf], np.nan)
    views_over_time = views_over_time.dropna()

    # Create the Matplotlib figure for video views using a bar plot
    fig_views_bar, ax_views_bar = plt.subplots(figsize=(12, 6))
    views_over_time.plot(kind='bar', ax=ax_views_bar, color='orange')
    ax_views_bar.set_xlabel('Date', fontsize=12)
    ax_views_bar.set_ylabel('Views', fontsize=12)
    ax_views_bar.set_title('Video Views Over Time (Bar Plot)', fontsize=14)
    st.pyplot(fig_views_bar)

    # Scatter plot for likes and engagement over time for the selected channel
    st.header('Likes and Engagement Over Time')
    st.write(f"Likes and engagement over time for **{selected_channel}**")
    likes_over_time = selected_videos.groupby(selected_videos['published_date'].dt.date)['likes'].sum()
    engagement_over_time = selected_videos.groupby(selected_videos['published_date'].dt.date)['engagement'].sum()

    # Handle infinite values in the data
    likes_over_time = likes_over_time.replace([np.inf, -np.inf], np.nan)
    engagement_over_time = engagement_over_time.replace([np.inf, -np.inf], np.nan)
    likes_over_time = likes_over_time.dropna()
    engagement_over_time = engagement_over_time.dropna()

    # Create the Matplotlib figure for likes and engagement using a scatter plot
    fig_likes_engagement_scatter, ax_likes_engagement_scatter = plt.subplots(figsize=(12, 6))
    plt.scatter(likes_over_time.index, likes_over_time, label='Likes', color='blue')
    plt.scatter(engagement_over_time.index, engagement_over_time, label='Engagement', color='green')
    ax_likes_engagement_scatter.set_xlabel('Date', fontsize=12)
    ax_likes_engagement_scatter.set_ylabel('Count', fontsize=12)
    ax_likes_engagement_scatter.set_title('Likes and Engagement Over Time (Scatter Plot)', fontsize=14)
    ax_likes_engagement_scatter.legend()
    st.pyplot(fig_likes_engagement_scatter)

    st.header('Top 10 Videos with the Most Likes')
    top_10_likes = selected_videos.nlargest(10, 'likes')[['title', 'views', 'likes', 'engagement']]
    st.write(top_10_likes)

    st.header('Top 10 Videos with the Most Engagement')
    top_10_engagement = selected_videos.nlargest(10, 'engagement')[['title', 'views', 'likes', 'engagement']]
    st.write(top_10_engagement)

    st.header('Video Selection')
    st.write(f"Videos from the selected channel: **{selected_channel}**")
    st.write(selected_videos)
    
    st.markdown('---')
    st.write('Developed by B.Huslen')

if __name__ == '__main__':
    main()

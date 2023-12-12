import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import seaborn as sns
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
    st.write("Channel overview")
    st.write("This shows the YouTube channels with the region code 'MN'. Gathered from YouTube's API system")
    st.write("This app finds channels title, description, duration, views, likes, favorites, and comment count")
    
    st.header('Top 10 Channels with the Most Subscribers')
    top_10_subscribers = channel_data.nlargest(10, 'subscribers')
    st.dataframe(top_10_subscribers)  # Display top 10 subscribers as a table
    
    # ... (other parts of your code remain unchanged)
    
    # Line chart for video views over time for the selected channel
    st.header('Video Views Over Time')
    st.write(f"Video views over time for **{selected_channel}**")
    selected_videos['published_date'] = pd.to_datetime(selected_videos['published_date'])
    views_over_time = selected_videos.groupby(selected_videos['published_date'].dt.date)['views'].sum()

    # Handle infinite values in views_over_time
    views_over_time = views_over_time.replace([np.inf, -np.inf], np.nan)
    views_over_time = views_over_time.dropna()

    # Create the Matplotlib figure for video views
    fig_views, ax_views = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=views_over_time, linewidth=2, color='orange', ax=ax_views)
    ax_views.set_xlabel('Date', fontsize=12)
    ax_views.set_ylabel('Views', fontsize=12)
    ax_views.set_title('Video Views Over Time', fontsize=14)
    
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

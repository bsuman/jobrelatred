import os
from datetime import timedelta
import re
from googleapiclient.discovery import build

# get the youtube api access key which is saved in the environment variable named 'YoutubeApiKey'
# technique to ensure that the key is not visible to everyone
api_key = os.environ.get('YoutubeApiKey')
# build the service for youtube api access for version 3 and the key
service = build('youtube', 'v3', developerKey=api_key)

#  for the channel freecodecamp with the ID = UC8butISFwT-Wl7EV0hUK0BQ, get the content details and statistical information
request = service.channels().list(part='contentDetails,statistics', id='UC8butISFwT-Wl7EV0hUK0BQ')
response = request.execute()
# print(response)

# get list of playlist of the freecodecamp channel
pl_request = service.playlists().list(part='contentDetails', channelId='UC8butISFwT-Wl7EV0hUK0BQ')
pl_response = pl_request.execute()
# print(pl_response)
# when the playlists are huge, then each playlist content is paged. The api has a limit of maximum 50 videos per page.
# to ensure that all the videos of the playlists are fetched use the page token information
next_page_token = None
# for each video the regex is used for string parsing of the duration
# reg ex for getting hours
hr_pattern = re.compile(r'(\d+)H')
# reg ex for getting minutes
min_pattern = re.compile(r'(\d+)M')
# reg ex for getting seconds
sec_pattern = re.compile(r'(\d+)S')
# store the duration of all the videos of a playlist
total_duration = 0
# popularity
video_di = []
# loop until no more videos are left in the playlist
while True:
    # get the playlist videos for the playlist with playlistId.
    # the playlistId is seen in the url of the youtube playlist of interest
    # current example is for pytorch playlist
    # example of huge playlist: PLWKjhJtqVAbkOoQw0jDWn-pzN3nFVjhbH
    # pl_request = service.playlistItems().list(part='contentDetails', playlistId='PLWKjhJtqVAbkOoQw0jDWn-pzN3nFVjhbH', maxResults=50, pageToken=next_page_token)
    # example of small playlist : PLWKjhJtqVAbm5dir5TLEy2aZQMG7cHEZp
    pl_request = service.playlistItems().list(part='contentDetails', playlistId='PLWKjhJtqVAbm5dir5TLEy2aZQMG7cHEZp',
                                              maxResults=50, pageToken=next_page_token)
    pl_response = pl_request.execute()
    # print(pl_response)
    video_id_list = []
    # get the ids of the videos in the playlist
    for playlist in pl_response['items']:
        video_id = playlist['contentDetails']['videoId']
        video_id_list.append(video_id)

    # as the videos().list api takes a string of video Ids to get the information of multiple videos at a time,
    # convert the list of ids to string of ids
    vi_id_str = ",".join(video_id_list)
    # make the request
    vi_request = service.videos().list(part="statistics,contentDetails", id=vi_id_str)
    vi_response = vi_request.execute()

    # for each video get the duration and extract the hours,mins, and seconds
    for video in vi_response['items']:
        # get the video duration
        duration = video['contentDetails']['duration']
        # parse the returned string for getting the hours, mins and secs
        hours = hr_pattern.search(duration)
        hours = int(hours.group(1)) if hours else 0

        mins = min_pattern.search(duration)
        mins = int(mins.group(1)) if mins else 0

        secs = sec_pattern.search(duration)
        secs = int(secs.group(1)) if secs else 0

        # to get the duration time in seconds:
        video_duration_secs = timedelta(hours=hours, minutes=mins, seconds=secs).total_seconds()
        # add to the total duration
        total_duration += video_duration_secs

        # extension: get the most popular video, by getting the video view count
        num_views = video['statistics']['viewCount']
        # create the link to the video
        yt_link = f"https://youtu.be/{video['id']}"
        video_di.append(
            {
                'num_views': int(num_views),
                'link': yt_link
            }
        )

    # check if there is a next page, if the next page is None, then we are through the list.
    next_page_token = pl_response.get('nextPageToken')
    if next_page_token is None:
        break

# convert total seconds to hours:mins:secs format
total_duration = int(total_duration)
# get total minutes and seconds
t_mins, t_secs = divmod(total_duration, 60)
t_hrs, t_mins = divmod(t_mins, 60)
# display the total time required to finish the chosen playlist
print(f"Total time required to finish the current playlist is {t_hrs}H:{t_mins}M:{t_secs}S")

video_di.sort(key=lambda vid: vid['num_views'], reverse=True)
print(
    f"Most viewed video {video_di[0]['link']} of the current playlist has the view count of {video_di[0]['num_views']}.")

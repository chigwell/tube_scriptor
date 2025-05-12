import requests
from urllib.parse import urlparse, parse_qs
import xmltodict
import json


TRANSCRIPT_URL = "https://youtubetranscript.com/?server_vid2="
EXCEPTION_TEXT = "We're sorry, YouTube is currently blocking us from fetching subtitles preventing us from generating a summary for you. We're working on a fix!"

def fetch_transcript(youtube_input, output_format='string'):
    video_id = extract_video_id(youtube_input)
    transcript_url = f"{TRANSCRIPT_URL}{video_id}"
    response = requests.get(transcript_url)

    if response.status_code != 200:
        raise Exception("Failed to fetch transcript")

    transcript_data = xmltodict.parse(response.content)

    if EXCEPTION_TEXT in response.text:
        raise Exception("YouTube is blocking the transcript fetching service.")

    if output_format == 'xml':
        return response.text
    elif output_format == 'json':
        return json.dumps(transcript_data)
    elif output_format == 'list':
        return [
            {
                'text': text['#text'],
                'start': float(text['@start']),
                'dur': float(text['@dur'])
            } for text in transcript_data['transcript']['text']
        ]
    else:
        return "\n".join([text['#text'] for text in transcript_data['transcript']['text']])


def extract_video_id(youtube_input):
    if "youtube.com" in youtube_input:
        query = urlparse(youtube_input)
        if query.path == '/watch' and 'v' in parse_qs(query.query):
            return parse_qs(query.query)['v'][0]
    elif "youtu.be" in youtube_input:
        path = urlparse(youtube_input).path
        if len(path) > 1:
            return path[1:]
    else:
        if 'http' not in youtube_input and len(youtube_input) > 0:
            return youtube_input
    raise ValueError("Invalid YouTube link or ID")

# Example usage
# if __name__ == '__main__':
#     youtube_link_or_id = "aml10DvOhTM"
#     output_format = "list"   # Can be 'xml', 'json', 'list', or 'string'
#     print(fetch_transcript(youtube_link_or_id, output_format))

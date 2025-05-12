[![PyPI version](https://badge.fury.io/py/tube_scriptor.svg)](https://badge.fury.io/py/tube_scriptor)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/tube_scriptor)](https://pepy.tech/project/tube_scriptor)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/eugene-evstafev-716669181/)

# Tube Scriptor

`tube_scriptor` is a Python package designed to fetch and generate transcripts from YouTube videos in various formats including XML, JSON, Python lists, or plain text. It simplifies the process of obtaining video transcripts, making it accessible for data analysis, content generation, and accessibility features.

## Installation

To install `tube_scriptor`, you can use pip:

```bash
pip install tube_scriptor
```

## Usage

Using `tube_scriptor` is straightforward. Below are examples demonstrating how to fetch a video transcript in various formats and using both a YouTube URL and a direct video ID.

### Fetching Transcript as a List

```python
from tube_scriptor import fetch_transcript

# Using a YouTube URL
youtube_url = "https://www.youtube.com/watch?v=exampleVideoId"
transcript_list = fetch_transcript(youtube_url, 'list')
print(transcript_list)

# Using a YouTube video ID
youtube_id = "exampleVideoId"
transcript_list = fetch_transcript(youtube_id, 'list')
print(transcript_list)
```

### Fetching Transcript as a JSON String

```python
# Using a YouTube video ID
youtube_id = "exampleVideoId"
transcript_json = fetch_transcript(youtube_id, 'json')
print(transcript_json)
```

### Fetching Transcript as Plain Text

```python
# Using a YouTube video ID
youtube_id = "exampleVideoId"
transcript_text = fetch_transcript(youtube_id, 'string')
print(transcript_text)
```

### Fetching Transcript as XML

```python
# Using a YouTube video ID
youtube_id = "exampleVideoId"
transcript_xml = fetch_transcript(youtube_id, 'xml')
print(transcript_xml)
```

These examples illustrate the flexibility of `tube_scriptor` in handling different formats and inputs. Choose the format that best suits your needs, whether it's for further processing, display, or storage.

## Features

- Support for fetching transcripts in XML, JSON, Python list, or plain string format.
- Easy integration into Python projects.
- Flexible input with support for both YouTube video URLs and video IDs.
- Lightweight with minimal dependencies.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chigwell/tube_scriptor/issues).

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

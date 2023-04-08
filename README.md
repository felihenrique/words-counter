# Words Counter

This is a project made to count words in a text. It processes the text, removing punctuation, special characters, turning words into lowercase, and removing stopwords to make the analysis easier.
There some space for improvement, like doing stemming to groups the words that are the same.
At this moment, this project was tested and support only the english language.

## Installation and running
This project was done with Python 3 and ReactJS. It has a Dockerfile for both backend and frontend subprojects. To run this project you only need:
 - Docker
 - Docker compose >= 3

You can run both projects individually running:

```bash
docker-compose up frontend
```
```bash
docker-compose up backend
```

## Running the backend tests

To run the backend tests you need the library pytest. You can install it running:
```bash
pip install pytest
```

After that, you can run the tests running this on your terminal:
```bash
pytest
```
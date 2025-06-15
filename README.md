### RSS Feed Summarizer

This is a small personal project aimed at getting public Mexican RSS feeds and summarizing it using a local LLM model. The model is deployed using ollama.

The project uses 2 main libraries:
- feedparser: to parse RSS feeds
- ollama: to deploy local LLM models

It essentially parses an RSS feed to get titles and descriptions, then for each title and description, it passes it on to the model; the repository includes an initialize.json file that stablishes the model to use, it also includes system instructions. 

This is mostly meant to run locally.
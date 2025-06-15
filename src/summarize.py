"""
Module to use an llm model to summarize the news
"""
import json
import asyncio
import subprocess

import ollama

import feed

INITIALIZE_PATH = "/home/emilianoab/Documents/Projects/mx-newsletter-ai/initialize.json"
QUERY_PATH = "/home/emilianoab/Documents/Projects/mx-newsletter-ai/query.json"

def is_model_running(model):
	list_of_models = subprocess.Popen(["ollama", "ps"], stdout=subprocess.PIPE)
	found_models = subprocess.Popen(["grep", model], stdin=list_of_models.stdout, stdout=subprocess.PIPE, encoding="utf-8")
	output, _ = found_models.communicate()
	if not output:
		return False
	else: 
		return True

def create_model():
	json_file = open(INITIALIZE_PATH)
	model_specs = json.load(json_file)
	model = model_specs['model']

	if is_model_running(model):
		print("Model was not created")
		return model
	else:
		print("Model was created")
		ollama.create(model=model, from_=model_specs['from'], system=model_specs['system'], stream=model_specs['stream'])
		return model

def summarize(feed_url):
	# Creates model if it's not present
	model = create_model()

	# Gets feed and parses it
	feed_content = feed.get_feed(feed_url)
	parsed_feed = feed.parse_feed(feed_content)
	
	summarized_articles = []
	for dict in parsed_feed:
		query_string = "Titulo:\n" + dict['title'] + "\n"
		query_string += "Description:\n" + dict['description']
		response = ollama.generate(model=model, prompt=query_string, stream=False)
		print(response.response)
		summarized_articles.append(response.response)

	return summarized_articles
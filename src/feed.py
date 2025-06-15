"""
Code to get feed info
"""
import feedparser

# Get the current XML feed of a given url
def get_feed(url):
	content = feedparser.parse(url)

	if len(content.feed) == 0:
		raise Exception("Empty or invalid feed")
	
	return content

# Parse necessary content
def	parse_feed(content):
	news = []
	for item in content.entries:
		tempDict = {}
		if 'title' in item:
			tempDict['title'] = item['title']
		else:
			tempDict['title'] = "No title"

		if 'description' in item != "":
			tempDict['description'] = item['description']
		elif 'content' in item != "":
			tempDict['description'] = item['content']
		else:
			tempDict['description'] = "No description"

		news.append(tempDict)

	return news

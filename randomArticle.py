import json
import urllib2
import random
from flask import Flask


def randomizeArt():
	categories = []
	articles = []
	catURL = urllib2.urlopen('http://api.spunout.ie/v1/categories')
	response = json.load(catURL)

	ourResult = response['categories']
	for rs in ourResult:
		categories.append(rs)
     
	randomCat = random.choice(categories)

	articleURL = urllib2.urlopen('http://api.spunout.ie/v1/search/by_category/'+randomCat)
	spuntOutArticles = json.load(articleURL)

	articleOutput = spuntOutArticles['services']
	for  article in articleOutput:

		articleObject = {'title': article['title'],'info': article['info'],'page': article['page']}

		articles.append(articleObject)


	return json.dumps(random.choice(articles), sort_keys=True, indent=4,
                          separators=(',', ': '))



app = Flask(__name__)


@app.route('/return.json')
def jsonObjects():
    return randomizeArt()

if __name__ == '__main__':
    app.run()
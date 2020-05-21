import model
import webpage
#import extractor


from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return webpage.get_html_page() 


@app.route("/result", methods=['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
		print(result)
		
		tableData = []
		country = result.get('country')
		year = result.get('year')
		month = result.get('month')
		event = result.get('event')
		
		province1 = model.predictDTree(country, year, month, event)
		tableData.append(['Decision Tree', country, year, month, event, province1])

		province2 = model.predictKNN(country, year, month, event)
		tableData.append(['KNN', country, year, month, event, province2])
		

		province3 = model.predictGNB(country, year, month, event)
		tableData.append(['Naive Bayes', country, year, month, event, province3])
		
		webpage.data1 = tableData
		print(tableData)
		return webpage.get_html_page_result()

if __name__ == '__main__':
   app.run(debug = True)
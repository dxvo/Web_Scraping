from flask import Flask, render_template, redirect
import pymongo
import scrape_mars as sc  



# Create an instance of our Flask app.
app = Flask(__name__)

@app.route("/")
def home():
	mars = sc.scrape()
	#mars = sc.scrape()
	return render_template("index.html", mars = mars)

@app.route("/scrape")
def scrape():
	new_data = sc.scrape()
	return render_template("index.html", mars = new_data)


if __name__ == "__main__":
    app.run(debug=True)
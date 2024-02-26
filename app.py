from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route to handle the search request
@app.route('/search', methods=['POST'])
def search():
    # Get the search term from the form
    search_term = request.form['searchTerm']

    # Read the Excel file
    df = pd.read_excel('database.xlsx')

    # Perform the search
    result_df = df[df['Error_Name'].str.contains(search_term, case=False)]

    # Process the solution content
    result_df['Solution'] = result_df['Solution'].apply(lambda x: '<br>'.join(x.split('\n')))

    # Convert the result to HTML table
    result_html = result_df.to_html(classes='result', index=False, escape=False)

    return render_template('index.html', result_html=result_html)

if __name__ == '__main__':
    app.run(debug=True)

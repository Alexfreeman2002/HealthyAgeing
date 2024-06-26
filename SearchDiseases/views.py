"""
Search Disease Views

This file defines a Flask blueprint for handling the search functionality for
diseases and conditions, allowing users to search the NHS website and retrieve
and view relevant data.
"""


from flask import render_template, request, Blueprint
from SearchDiseases.search import NHSWebsiteCrawler
import re


search_blueprint = Blueprint('search', __name__, template_folder='templates/features')


@search_blueprint.route('/search_disease', methods=['GET', 'POST'])
def search_disease():
    """
    Handles the search functionality for diseases.

    Returns:
        string: The rendered HTML template with search results.

    Notes:
        - If the request method is 'POST', the search term is extracted from the form data.
        - An instance of NHSWebsiteCrawler is created to search and retrieve data from the NHS website.
        - The search term is used to search the NHS website.
        - If a match is found, the data related to the search term is retrieved.
        - The search results are rendered in the 'features/search.html' template.
    """
    if request.method == 'POST':
        search_term = request.form['search_term'].strip()

        if not search_term.strip():
            return render_template('features/search.html',
                                   error_message="Please enter a search term.")
        if search_term.isdigit():
            return render_template('features/search.html',
                                   error_message="Please enter a valid search term.")

        #has to include only letters spaces and numbers
        if not re.match(r'^[a-zA-Z\s]*[a-zA-Z][a-zA-Z0-9\s]*$', search_term):
            return render_template('features/search.html',
                                   error_message="Please enter a valid search term.")

        url = 'https://www.nhs.uk/conditions/'
        nhs = NHSWebsiteCrawler(url)

        is_successful, result = nhs.search_website(search_term)

        if is_successful:
            result = nhs.retrieve_data(search_term)

        return render_template('features/search.html',
                               search_term=search_term,
                               result=result,
                               is_successful=is_successful)

    return render_template('features/search.html')

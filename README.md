
# IMDb Top Movies Scraper

## Overview
*IMDb Top Movies Scraper* is a Python script designed to extract data from the IMDb Top 250 movies list. Users can specify the number of top movies they wish to retrieve, and the script allows saving the data in multiple formats (Excel, CSV, JSON). The script mimics a browser request to avoid blocking by IMDb and processes the page to extract movie ranks, titles, release years, and IMDb ratings.

## Features
- *Customizable movie count*: Users can specify how many top movies to retrieve (up to 250).
- *Multiple export formats*: Save the data as an Excel spreadsheet (.xlsx), a CSV file (.csv), or a JSON file (.json).
- *Error handling*: The script includes robust error handling for user input and network issues.

## Requirements
Before running the script, ensure you have the following Python libraries installed:
- `requests`
- `beautifulsoup4`
- `openpyxl`
- `csv`
- `json`

These can be installed using the requirements.txt file.

### Installation
To install the required libraries, run:
```bash
pip install -r requirements.txt
```

### Libraries Used
- `requests`: For sending HTTP requests to the IMDb website.
- `beautifulsoup4`: For parsing HTML and extracting movie data.
- `openpyxl`: For creating and saving Excel files.
- `csv`: For writing data to CSV files.
- `json`: For writing data to JSON files.

## How to Use
1. *Clone the repository*:
   ```bash
   git clone https://github.com/SeifAmged/IMDb-Top-Movies-Scraper.git
   cd imdb-top-movies-scraper
   
   ```

2. *Activate your virtual environment* (if you have one):
   ```bash
   source env/bin/activate  # On macOS/Linux
   .\env\Scripts\activate    # On Windows
   ```

3. *Run the script*:
   ```bash
   python app.py
   ```

4. *Follow the on-screen prompts*:
   - Enter the number of top movies to retrieve (up to 250).
   - Enter the desired file name (without extension).
   - Choose the file format to save the data (xlsx, csv, json).

5. *Output*:
   - The script will save the data in the specified format and display a success message.

## Example Output
After running the script and choosing 10 movies and CSV format:
```text
Please enter the file name to save (without extension): top_movies
Choose the file format (xlsx/csv/json) or type 'exit' to cancel: csv
Data has been successfully saved to top_movies.csv
```

The generated top_movies.csv file will contain:
```csv
Movie Rank,Movie Name,Year of Release,IMDB Rating
1,The Shawshank Redemption,1994,9.2
2,The Godfather,1972,9.1
...
```

## Error Handling
- *Invalid Inputs*: The script will prompt the user again if they enter an invalid movie count, file name, or file format.
- *Network Errors*: If the script encounters a network error, it will display an appropriate message and terminate gracefully.

## Contributing
Contributions are welcome! Please fork this repository, create a new branch, and submit a pull request.



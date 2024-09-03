from bs4 import BeautifulSoup
import requests, openpyxl, csv, json

# Setting up the headers to mimic a web browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

# The URL of the webpage containing the top 250 movies on IMDb
url = 'https://web.archive.org/web/20210103061944/https://www.imdb.com/chart/top/'

try:
    # Asking the user how many movies they want to retrieve
    while True:
        try:
            num_movies = input("How many top movies would you like to retrieve? (Type 'exit' to quit): ").lstrip("0")  # Removing leading zeros
            if num_movies.lower() == 'exit':
                print("Operation cancelled by the user.")
                exit()  # Exit the program if the user chooses to quit
            if not num_movies.isdigit():
                print("Invalid input. Please enter a valid positive number.")
                continue
            num_movies = int(num_movies)
            if num_movies <= 0:
                print("Please enter a number greater than 0.")
            elif num_movies > 250:
                print("The maximum number of movies you can request is 250. Please enter a smaller number.")
            else:
                break  # Exit the loop if a valid number is entered
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Asking the user for the file name (without extension) to save the data
    while True:
        file_name = input("Please enter the file name to save (without extension): ").strip()
        if not file_name:
            print("The file name cannot be empty. Please enter a valid name.")
        else:
            break  # Exit the loop if a valid file name is entered

    # Asking the user to choose the file format
    while True:
        file_format = input("Choose the file format (xlsx/csv/json) or type 'exit' to cancel: ").lower()
        if file_format == 'exit':
            print("Operation cancelled by the user.")
            exit()  # Exit the program if the user chooses to quit
        if file_format not in ['xlsx', 'csv', 'json']:
            print("Invalid file format. Please choose from: xlsx, csv, or json.")
        else:
            break  # Exit the loop if a valid file format is chosen

    ####################################################   Main program  ########################################################

    try:
        # Sending a GET request to the webpage to retrieve its content
        source = requests.get(url, headers=headers)
        source.raise_for_status()  # Check for any request errors
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        exit()

    # Parsing the webpage content with BeautifulSoup
    soup = BeautifulSoup(source.text, 'html.parser')
    movies_table = soup.find('tbody', class_='lister-list')

    # Verify that the expected table is found
    if not movies_table:
        print("Error: The movies table was not found on the page.")
        exit()

    movies = movies_table.find_all('tr')  # Finding all movie entries

    # Extracting the necessary data from the webpage
    movies_data = []
    for movie in movies[:num_movies]:
        rank = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0] if movie.find('td', class_='titleColumn') else "N/A"
        name = movie.find('td', class_='titleColumn').a.text if movie.find('td', class_='titleColumn') and movie.find('td', class_='titleColumn').a else "N/A"
        year = movie.find('td', class_='titleColumn').span.text.strip('()') if movie.find('td', class_='titleColumn') and movie.find('td', class_='titleColumn').span else "N/A"
        rating = movie.find('td', class_="ratingColumn imdbRating").strong.text if movie.find('td', class_="ratingColumn imdbRating") and movie.find('td', class_="ratingColumn imdbRating").strong else "N/A"
        movies_data.append([rank, name, year, rating])  # Adding the data to the list

    # Saving the data based on the chosen file format
    if file_format == 'xlsx':
        # If the format is xlsx, create an Excel file
        excel = openpyxl.Workbook()
        sheet = excel.active
        sheet.title = 'Top Rated Movies'
        sheet.append(['Movie Rank', 'Movie Name', 'Year of Release', 'IMDB Rating'])  # Adding the headers
        for movie in movies_data:
            sheet.append(movie)  # Writing each movie's data into the Excel sheet
        excel.save(f"{file_name}.xlsx")  # Saving the Excel file
        print(f"Data has been successfully saved to {file_name}.xlsx")

    elif file_format == 'csv':
        # If the format is csv, create a CSV file
        with open(f"{file_name}.csv", mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Movie Rank', 'Movie Name', 'Year of Release', 'IMDB Rating'])  # Adding the headers
            writer.writerows(movies_data)  # Writing all movie data into the CSV file
        print(f"Data has been successfully saved to {file_name}.csv")

    elif file_format == 'json':
        # If the format is json, create a JSON file
        with open(f"{file_name}.json", mode='w', encoding='utf-8') as file:
            json_data = [
                {"Movie Rank": movie[0], "Movie Name": movie[1], "Year of Release": movie[2], "IMDB Rating": movie[3]}
                for movie in movies_data
            ]  # Formatting the data as a list of dictionaries
            json.dump(json_data, file, indent=4)  # Writing the data into the JSON file with indentation
        print(f"Data has been successfully saved to {file_name}.json")

except Exception as e:
    print(f"An error occurred: {e}")  # Catching and displaying any errors that occur during the process
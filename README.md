# Divar Exporter

`divar-exporter.py` is a Python script designed to scrape ads from the Divar platform based on a given search query. The extracted data is saved in an Excel file.

## Features

- Automates browsing using Selenium.
- Extracts ad details such as title, price, location, and link.
- Saves data to an Excel file for further analysis.

## Prerequisites

Ensure the following software is installed on your system:

1. **Python 3.8 or newer**  
   Download it from [python.org](https://www.python.org/).

2. **Google Chrome**  
   Download it from [google.com/chrome](https://www.google.com/chrome/).

3. **ChromeDriver**  
   This is automatically managed by the script using `webdriver-manager`.

## Installation

1. Clone this repository or download the script:

   ```bash
   git clone https://github.com/your-username/divar-exporter.git
   cd divar-exporter
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/MacOS
   venv\Scripts\activate     # On Windows
   ```

3. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open the script file `divar-exporter.py` in any code editor and modify the following variables as needed:

   - **`search_query`**: The keyword(s) you want to search for on Divar (e.g., `"206 سفید"`).
   - **`output_file`**: The name of the Excel file where results will be saved (e.g., `"divar_ads.xlsx"`).

2. Run the script:

   ```bash
   python divar-exporter.py
   ```

3. Once the script finishes execution, the extracted data will be saved in the specified Excel file.

## Example

To search for "206 سفید" and save the results to `divar_ads.xlsx`, simply update the script with:

```python
search_query = "206 سفید"
output_file = "divar_ads.xlsx"
```

Then run:

```bash
python divar-exporter.py
```

## Dependencies

The script relies on the following Python libraries:

- `selenium`
- `webdriver-manager`
- `pandas`

## Troubleshooting

- **Error: `chromedriver` executable needs to be in PATH**  
  Ensure you have Google Chrome installed. The script automatically manages the appropriate version of ChromeDriver.

- **No ads found to save**  
  Make sure your search query matches content available on Divar, and that the Divar website is accessible.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any bug fixes or enhancements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

*Happy scraping!*

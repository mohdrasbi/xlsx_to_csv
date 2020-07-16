### A simple Flask app to convert xlsx to csv

### Components:
- Language: python
- Packages used: 
  * Flask - to build a web application
  * Pandas - to read excel file, then convert to csv
  * io - to convert uploaded files to byte and string streams
- Used docker to containerize the app

### How to run:
- Clone repository: Run `git clone https://github.com/mohdrasbi/xlsx_to_csv`
- Locally:
  - Requirements: 
    * Python 3
    * Flask and Pandas packages: Run `pip3 install pandas flask`
  - Running the app:
    * Go to xlsx_to_csv/app directory
    * Run `python3 main.py`
    * Open http://127.0.0.1:5000/ in the browser
- Via docker:
  - Requirements:
    * Docker
  - Running the app:
    * Go to xlsx_to_csv directory
    * Run `bash run_image.sh`
    * Open http://127.0.0.1:5000/ in the browser

# Web Crawler Project

This project is a simple web crawler written in Python. It fetches and processes URLs, calculating the length of the content and the read time.

## Project Structure

.
├── README.md
├── main.py
├── requirements.txt
├── src
│ ├── **init**.py
│ └── crawler.py
└── urls.json

## Setup

1. Clone the repository.
2. Create a virtual environment:
   ```sh
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   ```sh
   source venv/bin/activate
   ```
4. Install the dependencies:
   ```sh
    pip install -r requirements.txt
   ```

## Usage

Run the main script:

```sh
python main.py
```

This will process the URLs in urls.json and print the results.

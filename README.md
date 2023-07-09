# Event Scraper and Email Notifier

This project is a Python script that periodically scrapes a website to check for upcoming events and sends email notifications when new events are found. It is designed to provide an automated way of staying updated on the latest events without manually checking the website.

The script uses the `requests` library to send HTTP requests and retrieve the page source of the target website. It utilizes `selectorlib` for data extraction by defining CSS selectors to locate and extract the relevant event details from the page source.

The extracted event details are then stored in a SQLite database to prevent duplicate notifications. The script compares the newly extracted events with the existing records in the database to determine if there are any new events.

When a new event is detected, the script sends an email notification using the `smtplib` library. The email contains the event details, such as the band, city, and date. The email functionality requires valid email credentials and SMTP server configuration.

The project includes the following files:

- `main.py`: The main script that performs the web scraping, data extraction, email notification, and database operations.
- `extract.yaml`: A YAML configuration file that specifies the CSS selector for extracting event details from the web page.
- `requirements.txt`: A file listing the required Python libraries and their versions.
- `data.db`: A SQLite database file for storing the event records.

## Usage

1. Ensure that Python and the necessary dependencies listed in `requirements.txt` are installed.
2. Set up the email credentials in the `main.py` script.
3. Run the script `main.py` using the command `python main.py`.
4. The script will periodically scrape the website, check for new events, and send email notifications when new events are found.

Feel free to customize the script, such as modifying the target website URL, CSS selectors, or email content, to suit your specific requirements.

Note: Please use this script responsibly and in compliance with the terms of service of the target website.

## Acknowledgements

This project was inspired by the need for an automated way to stay updated on upcoming events without manual effort. The use of web scraping, email notifications, and database storage provides a convenient solution for event enthusiasts and individuals who want to stay informed about the latest happenings.

The project utilizes the `requests` library for making HTTP requests, `selectorlib` for data extraction, and `smtplib` for sending email notifications. These open-source libraries have been instrumental in enabling the functionality and automation of the project.

## License

This project is licensed under the MIT License. You are free to modify, distribute, and use the code for both personal and commercial purposes. However, please note that the project is provided "as is" without warranty of any kind. Refer to the [LICENSE](LICENSE) file for more information.

Feel free to contribute to the project by submitting issues or pull requests on the GitHub repository. Your contributions are highly appreciated.

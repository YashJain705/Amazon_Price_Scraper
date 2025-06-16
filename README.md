# 🛒 Amazon Price Scraper

A Python-based web scraper to track and extract product prices from Amazon. This project allows users to monitor price changes and store the data locally for further analysis.

## 📌 Features

- Extracts product title and current price from Amazon
- Saves data to a local CSV file
- Simple to use and modify
- Works for individual product URLs
- Easily extendable for tracking multiple products

## 🧰 Requirements

- Python 3.x
- Required libraries (install via `pip`):

```bash
pip install requests beautifulsoup4 lxml pandas
```
## 📂 Project Structure

```bash
Amazon_Price_Scraper/
├── collect.py         # Core scraping logic
├── project.py         # Main script to run the scraper
├── data/
│   └── data.csv       # Output file storing scraped data
└── README.md          # Project description
```


## ⚠️ Disclaimer

This project is created for **educational and personal use only**.

- Scraping websites like Amazon may **violate their Terms of Service**.
- Use this code **responsibly** and at your own risk.
- The developer is **not responsible** for any misuse, legal issues, or bans resulting from use of this tool.
- Always ensure you have **permission** to scrape data from any website.

By using this project, you agree to use it ethically and comply with applicable laws and website policies.

## 📈 Future Improvements

Here are some potential enhancements to expand the functionality of this project:

- [ ] 🔁 Track multiple product URLs from a list or file
- [ ] 🕒 Schedule periodic scraping using `schedule`, `APScheduler`, or system cron jobs
- [ ] 📧 Send email or Telegram alerts when a price drops below a threshold
- [ ] 📊 Visualize price history with graphs (e.g., using `matplotlib` or `seaborn`)
- [ ] 💾 Export data to Excel or JSON formats
- [ ] 🌐 Add support for other e-commerce websites (e.g., Flipkart, eBay)
- [ ] 🖥️ Create a simple GUI using `Tkinter` or `PyQt`
- [ ] 🧪 Add unit tests and error handling for more reliability
- [ ] 🚀 Deploy as a Flask web app for remote usage

Feel free to fork the project and implement any of these ideas — contributions are welcome!

## 📄 License

This project is licensed under the **MIT License**.

You are free to:

- ✅ Use
- ✅ Copy
- ✅ Modify
- ✅ Merge
- ✅ Publish
- ✅ Distribute

Under the following conditions:

- 📌 You must include the original copyright and license notice in any copies.
- 📌 This software is provided **"as is"**, without any warranty.

For full license text, see the [LICENSE](LICENSE) file in this repository.


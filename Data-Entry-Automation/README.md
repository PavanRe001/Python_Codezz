# 🏠 Automated Real Estate Data Entry System

An intelligent Python automation tool that scrapes property listings from Zillow-like websites and automatically populates Google Forms with the extracted data. Built with Selenium WebDriver and BeautifulSoup for efficient web scraping and form automation.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/Selenium-4.0+-green.svg)](https://www.selenium.dev/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.0+-orange.svg)](https://www.crummy.com/software/BeautifulSoup/)

---

## 📋 Overview

This automation system streamlines the tedious process of manually entering real estate data by:

1. **Scraping** property listings (address, price, links) from real estate websites
2. **Processing** the data to clean and format it properly
3. **Automating** Google Forms submission for each property listing
4. **Storing** all entries in a connected Google Sheet for easy access and analysis

Perfect for real estate professionals, data analysts, or anyone who needs to collect and organize property listings efficiently.

---

## ✨ Key Features

- 🔍 **Web Scraping**: Extracts property addresses, prices, and links using BeautifulSoup
- 🤖 **Form Automation**: Automatically fills and submits Google Forms using Selenium
- 🧹 **Data Cleaning**: Removes unwanted characters and formats data consistently
- ⏱️ **Time Efficient**: Processes multiple listings in seconds vs. hours of manual entry
- 📊 **Google Sheets Integration**: All data automatically stored in organized spreadsheet
- 🔄 **Batch Processing**: Handles multiple property listings in a single run
- 🌐 **Chrome WebDriver**: Uses Chrome browser for reliable automation

---

## 🛠️ Technologies Used

- **Python 3.7+** - Core programming language
- **Selenium WebDriver** - Browser automation for form filling
- **BeautifulSoup4** - HTML parsing and web scraping
- **Requests** - HTTP library for fetching web pages
- **Google Forms** - Data collection interface
- **Google Sheets** - Automated data storage backend

---

## 🚀 How It Works

### Workflow Overview

```
┌─────────────────┐
│  Target Website │
│   (Zillow Clone)│
└────────┬────────┘
         │
         │ HTTP Request
         ▼
┌─────────────────┐
│  BeautifulSoup  │
│  HTML Parsing   │
└────────┬────────┘
         │
         │ Extract Data
         ▼
┌─────────────────┐
│  Data Cleaning  │
│  & Formatting   │
└────────┬────────┘
         │
         │ Cleaned Data
         ▼
┌─────────────────┐
│  Selenium       │
│  WebDriver      │
└────────┬────────┘
         │
         │ Form Automation
         ▼
┌─────────────────┐
│  Google Forms   │
│  Auto-Submit    │
└────────┬────────┘
         │
         │ Auto-Save
         ▼
┌─────────────────┐
│  Google Sheets  │
│  Data Storage   │
└─────────────────┘
```

### Data Extraction Process

The script identifies and extracts three key pieces of information from each property listing:

1. **Property Address** - Full address with proper formatting
2. **Price** - Cleaned price data (removes unnecessary text like "1 bd", "+")
3. **Property Link** - Direct URL to the listing

### Automation Process

For each property found, the system:
- Opens the Google Form in Chrome browser
- Waits for form elements to load
- Automatically fills in all three fields (address, price, link)
- Clicks the submit button
- Moves to the next property

---

## 📦 Installation

### Prerequisites

```bash
# Install Python 3.7 or higher
# Download from: https://www.python.org/downloads/

# Install Chrome browser
# Download from: https://www.google.com/chrome/
```

### Install Dependencies

```bash
pip install selenium beautifulsoup4 requests
```

### ChromeDriver Setup

ChromeDriver will be automatically managed by Selenium 4.0+. If you're using an older version:

1. Download ChromeDriver from: https://chromedriver.chromium.org/
2. Add to your system PATH or place in project directory

---

## ⚙️ Configuration

### Setting Up Your Google Form

1. Create a Google Form with three fields:
   - **Address** (Short answer)
   - **Price** (Short answer)
   - **Link** (Short answer)

2. Update the form URL in the script:
```python
glink = 'YOUR_GOOGLE_FORM_URL_HERE'
```

3. Update XPath selectors if your form structure differs

### Target Website

By default, the script scrapes from:
```python
response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
```

Modify this URL to target different property listing websites.

---

## 🎯 Usage

### Basic Execution

```bash
python data_entry_automation.py
```

### What Happens

1. Script fetches the property listing page
2. Parses HTML and extracts all property data
3. Opens Chrome browser (visible window)
4. Loops through each property and fills the form
5. Submits each entry automatically
6. All data appears in the connected Google Sheet

### Expected Output

```
Processing property 1/10...
✓ Form submitted for: 123 Main St, City, State
Processing property 2/10...
✓ Form submitted for: 456 Oak Ave, City, State
...
✓ All 10 properties processed successfully!
```

---

## 📊 Example Data

### Input (Scraped from Website)

| Address | Price | Link |
|---------|-------|------|
| 123 Main St, San Francisco, CA | $3,500/mo | https://example.com/listing1 |
| 456 Oak Ave, San Francisco, CA | $4,200/mo | https://example.com/listing2 |
| 789 Pine Rd, San Francisco, CA | $2,800/mo | https://example.com/listing3 |

### Output (Google Sheet)

All entries are automatically saved to the Google Sheet connected to your form with timestamps.

*See attached example spreadsheet for reference.*

---

## 🔒 Security & Usage Notes

### Form Protection Measures

To prevent misuse and maintain data integrity, the Google Form has been configured with:

- ✅ **Limit to 1 response per person** - Prevents duplicate submissions
- ✅ **Mandatory Google Sign-in** - Requires authentication to submit
- ✅ **Response validation** - Ensures data quality

### Important Considerations

⚠️ **Web Scraping Ethics**
- This script is for educational purposes and demonstration
- Always respect website Terms of Service and robots.txt
- Use responsibly and ethically
- For production use, consider official APIs when available

⚠️ **Rate Limiting**
- Add delays between requests to avoid overwhelming servers
- The script includes `time.sleep()` for this purpose

⚠️ **XPath Selectors**
- Google Forms may update their HTML structure
- Update XPath selectors if form automation breaks
- Use browser DevTools to inspect elements

---

## 🐛 Troubleshooting

### Common Issues

**Issue: ChromeDriver version mismatch**
```bash
Solution: Update Selenium to 4.0+ for automatic driver management
pip install --upgrade selenium
```

**Issue: Form fields not found**
```
Solution: Verify XPath selectors using Chrome DevTools
Right-click element → Inspect → Copy XPath
```

**Issue: "Element not clickable"**
```
Solution: Increase wait time or use explicit waits
WebDriverWait(driver, 20)  # Increase timeout
```

**Issue: Google Form requires sign-in**
```
Solution: This is intentional for security. Sign in when prompted.
```

---

## 📁 Project Structure

```
data-entry-automation/
│
├── data_entry_automation.py    # Main script
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── example_sheet.xlsx          # Sample output data
```

---

## 🔧 Customization

### Changing Target Website

```python
# Modify the URL and CSS selectors
response = requests.get('YOUR_TARGET_WEBSITE_URL')

# Update BeautifulSoup selectors
data_links = soup.find_all(name='a', attrs={'class':'YOUR_LINK_CLASS'})
data_prices = soup.find_all(name='span', attrs={'class':'YOUR_PRICE_CLASS'})
data_address = soup.find_all(name='address')
```

### Modifying Data Cleaning

```python
# Customize text cleaning logic
Prices = [tag.getText().split('/')[0]
         .replace('+', '')
         .replace('YOUR_TEXT', '')  # Add your replacements
         .strip() 
         for tag in data_prices]
```

### Adjusting Form Fields

```python
# Update XPath for your specific form
add_input = wait.until(EC.element_to_be_clickable(
    (By.XPATH, 'YOUR_XPATH_HERE')
))
```

---

## 🚀 Future Enhancements

Potential improvements for this project:

- [ ] Add support for multiple property websites
- [ ] Implement error logging and recovery
- [ ] Add data validation before submission
- [ ] Create GUI interface for non-technical users
- [ ] Export data to CSV/Excel directly
- [ ] Add email notifications on completion
- [ ] Implement headless browser mode
- [ ] Add progress bar for batch processing
- [ ] Support for image scraping and upload
- [ ] Database integration for data persistence

---

## 📝 Requirements

```
selenium>=4.0.0
beautifulsoup4>=4.9.0
requests>=2.25.0
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📄 License

This project is provided for educational purposes. Please ensure you have permission to scrape target websites and comply with their Terms of Service.

---

## 👨‍💻 Author

Created as an automation solution for efficient real estate data collection and management.

---

## 🙏 Acknowledgments

- **BeautifulSoup** - For excellent HTML parsing capabilities
- **Selenium** - For robust browser automation
- **Google Forms** - For seamless data collection interface

---

## 📞 Support

For issues or questions:
- Check the Troubleshooting section
- Review Google Forms XPath selectors
- Ensure all dependencies are installed correctly
- Verify target website structure hasn't changed

---

## ⚡ Quick Start

```bash
# 1. Clone or download the script
# 2. Install dependencies
pip install selenium beautifulsoup4 requests

# 3. Update Google Form URL in script
# 4. Run the script
python data_entry_automation.py

# 5. Check your Google Sheet for results!
```

---

**✨ Save hours of manual data entry with automated form filling! ✨**

---

*Last Updated: January 2026*

*Note: The attached example spreadsheet demonstrates the typical output format and data structure collected by this automation system.*

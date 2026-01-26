# Flight Price Alert System

A Python application that automatically searches for cheap flight deals using the Amadeus API, manages destination data via Sheety, and sends SMS notifications via Twilio when prices drop below your target.

## 📋 Features

- **Automated Flight Search**: Searches for flights from your origin city to multiple destinations
- **Price Comparison**: Compares current prices with your target prices stored in a Google Sheet
- **SMS Notifications**: Automatically sends alerts via Twilio when cheap flights are found
- **Flexible Date Range**: Searches flights within a 6-month window
- **Easy Configuration**: Manage destinations and prices through Google Sheets

## 🚀 Setup Instructions

### 1. Prerequisites

- Python 3.7 or higher
- Amadeus API account (free tier available)
- Sheety account (for Google Sheets integration)
- Twilio account (for SMS notifications)

### 2. Install Dependencies

```bash
pip install requests twilio
```

### 3. Get Your API Keys

#### Amadeus API (Flight Data)
1. Go to https://developers.amadeus.com/
2. Create a free account
3. Create a new app to get your API Key and API Secret
4. Copy your `API Key` and `API Secret`

#### Sheety (Google Sheets API)
1. Go to https://sheety.co/
2. Create a Google Sheet with columns: `city`, `iataCode`, `lowestPrice`, `id`
3. Connect your sheet to Sheety
4. Copy your Sheety endpoint URL

Example Google Sheet structure:
```
| city      | iataCode | lowestPrice | id |
|-----------|----------|-------------|-----|
| Paris     | PAR      | 150         | 1   |
| Tokyo     | TYO      | 500         | 2   |
| New York  | NYC      | 300         | 3   |
```

#### Twilio (SMS Notifications)
1. Go to https://www.twilio.com/
2. Sign up for a free account
3. Get your Account SID and Auth Token
4. Get a Twilio phone number

### 4. Configure Environment Variables

Create a `.env` file in the project root or set environment variables:

```bash
# Amadeus API
export Amadeus_API_ID="your_amadeus_api_key"
export Amadeus_API_KEY="your_amadeus_api_secret"

# Sheety API
export Sheety_Url="your_sheety_endpoint_url"

# Twilio API
export Twilio_API_ID="your_twilio_account_sid"
export Twilio_API_KEY="your_twilio_auth_token"
export Twilio_Phone_Number="your_twilio_phone_number"
export User_Phone_Number="your_phone_number_to_receive_alerts"
```

### 5. Update Origin City

Edit `main.py` and change the origin city code:

```python
ORIGIN_CITY_IATA = "LON"  # Change this to your city code
```

### 6. Run the Application

```bash
python main.py
```

## 📁 Project Structure

```
flight_project/
│
├── flight_search.py         # Handles Amadeus API calls for flight search
├── data_manager.py          # Manages destination data from Sheety
├── flight_data.py           # Processes flight data and finds cheapest options
├── notification_manager.py  # Sends SMS notifications via Twilio
├── main.py                  # Main application logic
├── .env                     # Environment variables (not tracked in git)
└── README.md                # This file
```

## 🌐 How It Works

1. **Data Retrieval**: Fetches destination list and target prices from your Google Sheet via Sheety
2. **Flight Search**: For each destination, searches for flights in the next 6 months using Amadeus API
3. **Price Analysis**: Finds the cheapest flight for each route
4. **Alert System**: If a flight is found below your target price, sends an SMS via Twilio
5. **Continuous Monitoring**: Run on a schedule (e.g., daily via cron job) for ongoing price monitoring

## 📱 Example SMS Alert

```
Low price alert! Only £89 to fly from LON to PAR, from 2026-03-15 to 2026-03-22.
```

## ⚙️ Customization

### Change Currency
Edit `flight_search.py`, line 33:
```python
"currencyCode": "GBP",  # Change to USD, EUR, etc.
```

### Adjust Search Parameters
Edit `flight_search.py`, lines 30-35:
```python
"adults": 1,           # Number of passengers
"nonStop": "true",     # Direct flights only
"max": "10",           # Maximum results
```

### Modify Date Range
Edit `main.py`, lines 13-14:
```python
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=180)  # Change 180 to your preference
```

## 🐛 Troubleshooting

### Issue: "401 Unauthorized" from Amadeus
- Verify your API credentials are correct
- Check if your token has expired (tokens last 30 minutes)

### Issue: "No flight data"
- The route might not have any flights available
- API rate limit might be exceeded
- Check if IATA codes are valid

### Issue: SMS not received
- Verify Twilio credentials
- Check phone number format (must include country code: +1234567890)
- Ensure Twilio account has credits

## 📝 Notes

- Amadeus test API has rate limits (free tier: 1 request/second)
- Twilio free trial requires phone number verification

## 📄 License

This project is for educational purposes. Make sure to comply with API terms of service.
This Readme.md is created using ai, Suit your needs and use the code accordingly 

## 🤝 Contributing

Feel free to fork, improve, and submit pull requests!

---

**Happy Flight Hunting! ✈️🌍**

# @title Define the get_device_support Tool
from fuzzywuzzy import fuzz

def get_device_support(query: str) -> dict:
    """Provides solutions for common tech-related issues (phone, laptop, network, lag).

    Args:
        query (str): The user's query related to tech issues (e.g., phone lag, laptop issues, network problems).

    Returns:
        dict: A dictionary containing the status of the request.
              If successful, includes a 'response' key with solution details.
              If error, includes an 'error_message' key.
    """
    print(f"--- Tool: get_device_support called for query: {query} ---")  # Log tool execution
    query_normalized = query.lower().replace(" ", "")  # Basic normalization

    # Mock responses for tech-related issues
    mock_tech_support_db = {
        "phone lag": {"status": "success", "response": "To fix phone lag, try clearing the cache, restarting your phone, or disabling unnecessary apps running in the background. Also, ensure that your phone's software is up to date."},
        "laptop lag": {"status": "success", "response": "If your laptop is lagging, consider closing unused programs, increasing RAM, or checking for malware. Regularly updating your operating system and drivers may also help."},
        "network issue": {"status": "success", "response": "If you're facing network issues, try restarting your router, checking for interference, and ensuring no devices are consuming excessive bandwidth. You might also want to check your internet service provider for any outages."},
        "phone problem": {"status": "success", "response": "For phone problems, try restarting the device, updating the software, or checking for issues with apps that may be causing the problem."},
        "laptop problem": {"status": "success", "response": "If you're encountering problems with your laptop, try rebooting, checking for updates, or looking for any error messages that may give more details."},
    }

    # Find the best match in the mock database using fuzzy matching
    best_match = None
    best_score = 0

    for key in mock_tech_support_db:
        score = fuzz.ratio(query_normalized, key.lower())  # Compare similarity score
        if score > best_score:
            best_score = score
            best_match = key

    # If the best match score is above a certain threshold, return the corresponding response
    if best_score > 80:  # You can adjust this threshold
        return mock_tech_support_db[best_match]
    else:
        return {"status": "error", "error_message": f"Sorry, I couldn't understand the query: '{query}'. Please provide more details or be more specific."}



# Sentiment analysis function
from textblob import TextBlob  # You can use any sentiment analysis library
def analyze_sentiment(query: str) -> str:
    """Analyzes the sentiment of the user's query.
    
    Args:
        query (str): The user's input.
        
    Returns:
        str: The sentiment of the query ('positive', 'negative', or 'neutral').
    """
    analysis = TextBlob(query)
    polarity = analysis.sentiment.polarity  # A value between -1 (negative) to 1 (positive)
    
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"

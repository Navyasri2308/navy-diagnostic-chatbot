from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app)

KB_FILE_PATH = os.path.join("data", "files 1.txt")

WIKI_HEADERS = {
    'User-Agent': 'NavyDiagnosticBot/3.0 (educational student project; student@example.com)'
}

def get_best_match(user_query):
    if not os.path.exists(KB_FILE_PATH):
        print(f"Error: File not found at {KB_FILE_PATH}")
        return None

    with open(KB_FILE_PATH, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    query_words = set(user_query.lower().split())
    if not query_words:
        return None

    best_answer = None
    max_matches = 0

    # Scan through every line in the text file
    for i, line in enumerate(lines):
        line_lower = line.lower()
        matches = sum(1 for word in query_words if word in line_lower)
        
        if matches > max_matches:
            max_matches = matches
            if i + 1 < len(lines):
                best_answer = lines[i+1]
            else:
                best_answer = line

    if max_matches >= 1:
        return best_answer

    return None

def fetch_wikipedia_search(query):
    try:
        search_url = "https://en.wikipedia.org/w/api.php"
        
        # 1. Search for article title
        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json"
        }
        search_response = requests.get(search_url, params=search_params, headers=WIKI_HEADERS)
        search_data = search_response.json()
        
        search_results = search_data.get("query", {}).get("search", [])
        if not search_results:
            return None
            
        best_title = search_results[0]["title"]
        
        # 2. Fetch page summary
        summary_params = {
            "action": "query",
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "titles": best_title,
            "format": "json"
        }
        summary_response = requests.get(search_url, params=summary_params, headers=WIKI_HEADERS)
        pages = summary_response.json().get("query", {}).get("pages", {})
        
        for page_id, page_data in pages.items():
            if "extract" in page_data and page_data["extract"].strip():
                return page_data["extract"][:500] + "..."
                
        return None
    except Exception as e:
        print("Wiki fetching error:", str(e))
        return None

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'response': 'Please type a valid question.'})
            
        # Try local text document first
        local_answer = get_best_match(user_message)
        if local_answer:
            return jsonify({'response': local_answer})
            
        # Try Wikipedia fallback second
        wiki_answer = fetch_wikipedia_search(user_message)
        if wiki_answer:
            return jsonify({'response': f"⚓ **AI (Wikipedia Fallback):** {wiki_answer}"})
            
        return jsonify({'response': "I am sorry, I couldn't find an answer in the local manual or on Wikipedia."})
        
    except Exception as e:
        print("Server error:", str(e))
        return jsonify({'response': f"Internal Server Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
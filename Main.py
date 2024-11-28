from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

       


# Function to calculate the data transferred
def calculate_data_size(url):
    try:
        # Fetch the website content
        response = requests.get(url)
        
        # Get the total size in bytes (headers + content)
        headers_size = len(str(response.headers))
        content_size = len(response.content)
        total_size = headers_size + content_size
        float(total_size)
        
        # Convert size to GB (1 GB = 1e9 bytes)
        size_in_gb = total_size / 1e9
        
        return {
            "url": url,
            "total_size_bytes": total_size,
            "total_size_gb": size_in_gb
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# API endpoint for fetching the data size
@app.route('/calculate-size', methods=['POST'])
def calculate_size():
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({"error": "Please provide a valid URL."}), 400
    
    # Check if the URL starts with http or https
    if not url.startswith('http'):
        url = 'https://' + url
    
    # Calculate the data size
    result = calculate_data_size(url)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
    
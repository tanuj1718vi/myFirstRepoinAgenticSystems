import json

def main():
    # JSON formatted API response (string)
    api_response = '''
    {
        "id": "req_123",
        "status": "success",
        "result": {
            "text": "Hello world",
            "confidence": 0.98
        }
    }
    '''

    # Parse JSON string into Python dictionary
    data = json.loads(api_response)

    # Extract values
    request_id = data["id"]
    status = data["status"]
    text_result = data["result"]["text"]
    confidence_score = data["result"]["confidence"]

    # Print extracted information
    print("Request ID:", request_id)
    print("Status:", status)
    print("Text Result:", text_result)
    print("Confidence Score:", confidence_score)

    # Check confidence score
    if confidence_score < 0.9:
        print("Warning: Confidence score is below acceptable threshold!")

    # Create a follow-up Python dictionary
    follow_up_result = {
        "request_id": request_id,
        "processed_text": text_result.upper(),
        "confidence": confidence_score,
        "review_needed": confidence_score < 0.9
    }

    # Convert dictionary to JSON string
    json_output = json.dumps(follow_up_result, indent=4)

    # Write JSON output to file
    with open("response.json", "w") as file:
        file.write(json_output)

if __name__ == "__main__":
    main()
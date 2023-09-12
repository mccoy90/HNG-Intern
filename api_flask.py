from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Validate parameters
    if not slack_name or not track:
        return jsonify({"error": "slack_name and track are required query parameters"}), 400

    # Get current day of the week and UTC time
    utc_time = datetime.datetime.now(pytz.utc)
    day_of_week = utc_time.strftime('%A')

    # Placeholder URLs for GitHub
    github_file_url = "YOUR_GITHUB_URL_FILE"
    github_repo = "YOUR_GITHUB_URL_SOURCE_CODE"

    # Construct response JSON in the desired format
    response = {
        "current_day_of_week": day_of_week,
        "current_utc_time": utc_time.strftime('%Y-%m-%d %H:%M:%S %Z'),
        "github_url_file": github_file_url,
        "github_url_source_code": github_repo,
        "slack_name": slack_name,
        "track": track
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
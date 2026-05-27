import requests
import os
import shutil
from dotenv import load_dotenv

load_dotenv()

NETLIFY_AUTH_TOKEN = os.getenv("NETLIFY_AUTH_TOKEN")

def deploy_to_netlify(folder_path: str, site_name: str):
    """
    Deploys a folder to Netlify.
    Note: For React apps, you'd usually build first, but for this MVP,
    we are deploying the source as a static site for preview.
    """
    if not NETLIFY_AUTH_TOKEN:
        return "Error: NETLIFY_AUTH_TOKEN not set"

    # Zip the folder
    zip_output_path = shutil.make_archive(site_name, 'zip', folder_path)

    try:
        with open(zip_output_path, 'rb') as f:
            response = requests.post(
                'https://api.netlify.com/api/v1/sites',
                headers={
                    'Authorization': f'Bearer {NETLIFY_AUTH_TOKEN}',
                    'Content-Type': 'application/zip'
                },
                data=f
            )

        # Clean up the zip file
        if os.path.exists(zip_output_path):
            os.remove(zip_output_path)

        if response.status_code in [200, 201]:
            return response.json().get('url')
        else:
            return f"Deployment failed: {response.text}"

    except Exception as e:
        return f"Error during deployment: {str(e)}"

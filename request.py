import requests

API_URL = "https://e6waofnzq8.execute-api.eu-central-1.amazonaws.com/main/api/v1"
ADMIN_TOKEN = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiaXNfYWRtaW4iOnRydWUsIm5hbWUiOiJhZG1pbiIsImVtYWlsIjoiYWRtaW5AbWFpbC5jb20iLCJoYXNoZWRfcGFzc3dvcmQiOiIkMSRXcEFvM2F0dCQ3TzM3d0FraEtGdS5BL0g4LmxFOEgxIn0.zX-yTmxdW8FOboKdl_f4uFKEhskqv_bFxK1NuRZ2EpAU3yCQ7Omee9XBvsRDDRFs9IIsH2-0C2SNZkkCUSo98w'

def get_all_items():
    response = requests.get(f"{API_URL}/admin/items/all", headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    return response.json()

def get_all_items_by_user_id(id):
    response = requests.get(f"{API_URL}/admin/items/all/{id}", headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    return response.json()

def get_all_lists():
    response = requests.get(f"{API_URL}/admin/lists/all", headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    return response.json()

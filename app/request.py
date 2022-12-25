import requests

API_URL = "https://e6waofnzq8.execute-api.eu-central-1.amazonaws.com/main/api/v1"
ADMIN_TOKEN = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiaXNfYWRtaW4iOnRydWUsIm5hbWUiOiJhZG1pbiIsImVtYWlsIjoiYWRtaW5AbWFpbC5jb20iLCJoYXNoZWRfcGFzc3dvcmQiOiIkMSRDYmtxQ2JudCRNM3dyVTVSUmlDVjhqOGhwLklWSWYuIn0.6_vB0m-vvw-A3zpdq4Sv23unhXXME3bigqPxvVZkcXSnngqou7U7b2f7ZDF3d_9zh_LfOwqR-E7VPlh40bGyvA'

def get_all_items():
    response = requests.get(f"{API_URL}/admin/items/all", headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    return response.json()

async def get_all_items_by_user_id(id):
    response = requests.get(f"{API_URL}/admin/items/all/{id}", headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    return response.json()

def get_all_lists():
    response = requests.get(f"{API_URL}/admin/lists/all", headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    return response.json()

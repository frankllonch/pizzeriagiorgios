import requests

def obtener_info_nutricional(ingrediente):
    """
    Obtiene información nutricional de un ingrediente desde la API de Edamam.
    """
    url = "https://api.edamam.com/api/nutrition-data"
    params = {
        'app_id': 'TU_APP_ID',  # Reemplaza con tu ID de la API Edamam
        'app_key': 'TU_APP_KEY',  # Reemplaza con tu clave de la API Edamam
        'ingr': ingrediente
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al obtener datos de Edamam: {response.status_code}")


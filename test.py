from rest_framework.test import APIClient

client = APIClient()
client.post('/notes/', {'title': 'new idea'}, format='json')

# Make all requests in the context of a logged in session.
client = APIClient()
client.login(username='igorborzunov', password='BaumanNE')

# Log out
client.logout()


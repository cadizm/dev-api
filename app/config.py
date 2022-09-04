import os

origins = [
  'https://dev.cadizm.com',
]

if os.environ.get('LOCAL'):
  origins.append('http://localhost:8000')

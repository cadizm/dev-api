import os

origins = [
  'https://dev.cadizm.com',
]

if os.environ.get('LOCAL'):
  origins.extend([
    'http://localhost:3000',
    'http://localhost:8000',
  ])

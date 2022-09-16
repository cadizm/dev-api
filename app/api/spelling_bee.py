import re
from itertools import chain

from app.lib.words import table

from fastapi import APIRouter

router = APIRouter(prefix='/api')

corpus = list(filter(lambda x: len(x) >= 4, chain(*table.values())))


def find_words(letters):
  assert len(letters) == 7

  reqd, *rest = letters.lower()
  regex = lambda x: re.fullmatch(f'[{reqd}{"".join(rest)}]+', x)
  matches = list(filter(lambda x: reqd in x, filter(regex, corpus)))

  return matches


@router.get("/spelling-bee/{letters}")
def spelling_bee(letters: str = ''):
  return sorted(find_words(letters), key=lambda x:len(x), reverse=True)

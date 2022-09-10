from functools import reduce
from typing import List

from app.lib.wordle import suggest

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix='/api')


class WordleRequest(BaseModel):
  wordle: List[str] = list('.....')
  excluded: str = ''
  misplaced: List[str] = []


def unpack(index, letters):
  res = [list('.....') for _ in letters]
  for i, v in enumerate(letters):
    res[i][index] = v
  return map(lambda x: ''.join(x), res)


@router.post('/wordle/suggest')
def wordle(request: WordleRequest):
  # build wordle string from individual inputs
  wordle = list('.....')
  for index, letter in enumerate(request.wordle):
    wordle[index] = letter or wordle[index]
  wordle = ''.join(wordle)

  # for each index, unpack letters into individual regexes
  misplaced = []
  for index, letters in enumerate(request.misplaced):
    misplaced.extend(unpack(index, letters))

  return [
    (word_score.word, f'{word_score.score:.7f}')
    for word_score in suggest(wordle, request.excluded, misplaced)
  ]

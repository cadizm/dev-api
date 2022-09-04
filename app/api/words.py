from app.lib.words import find_words

from fastapi import APIRouter

router = APIRouter(prefix='/api')


@router.get("/words/{word}")
def words(word: str = ''):
  word = word.lower()
  letters = list(filter(lambda x: x != ' ', word))
  blanks = len(word) - len(letters)
  f = lambda x: (len(x), x)

  return [
    (len(w), w)
    for w in sorted(find_words(letters, blanks), key=f, reverse=True)
  ]

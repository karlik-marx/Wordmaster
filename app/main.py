from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path
from core.algorithms import *


app = FastAPI()

app.mount(
    '/static',
    StaticFiles(directory=Path(__file__).parent.absolute() / 'static'),
    name='static',
)

templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    """
    Возвращает главную страницу приложения.

    :param request: Объект запроса FastAPI (для возвращения результата)
    :return: Шаблон ответа с главной страницей (templates/index.html)
    """
    return templates.TemplateResponse(
        'index.html', {'request': request}
    )


@app.post('/process/', response_class=HTMLResponse)
async def process_file(request: Request, text: str = Form(), algorithm: str = Form()):
    """
    Обработка текста с помощью выбранного алгоритма.

    :param request: Объект запроса FastAPI (для возвращения результата)
    :param text: Входной текст, полученный из формы (textarea)
    :param algorithm: Выбранный алгоритм обработки текста
    :return: Шаблон ответа с обработанным текстом (templates/result.html)
    """
    processed_text = ''

    if algorithm == 'remove_spaces':
        processed_text = remove_extra_spaces(text)

    elif algorithm == 'to_lemma':
        processed_text = to_lemma(text)

    elif algorithm == 'count_words':
        processed_text = count_words(text)

    return templates.TemplateResponse('result.html',
                                      {'request': request, 'original_text': text, 'processed_text': processed_text})

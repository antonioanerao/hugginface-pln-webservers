# Recebe um arquivo de audio e retorna o texto transcrito

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import asyncio

async def homepage(request):
    payload = await request.body()
    string = payload.decode("utf-8")
    response_q = asyncio.Queue()
    await request.app.model_queue.put((string, response_q))
    output = await response_q.get()
    return JSONResponse(output) 

async def server_loop(q):
    # Como o texto é transcrito para o inglês, é necessário traduzir para o português
    tokenizer = AutoTokenizer.from_pretrained("unicamp-dl/translation-en-pt-t5")
    model = AutoModelForSeq2SeqLM.from_pretrained("unicamp-dl/translation-en-pt-t5")
    
    pipe = pipeline(model='openai/whisper-base')

    enpt_pipeline = pipeline(
            'text2text-generation',
            model=model,
            tokenizer=tokenizer,
            max_length=512,
        )

    while True:
        (string, response_q) = await q.get()
        res = enpt_pipeline("translate English to Portuguese:" + pipe(string)['text'])
        out = res[0]['generated_text']
        await response_q.put(out)

app = Starlette(
    routes=[
        Route("/", homepage, methods=["POST"]),
    ],
)

@app.on_event("startup")
async def startup_event():
    q = asyncio.Queue()
    app.model_queue = q
    asyncio.create_task(server_loop(q))

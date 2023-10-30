# Recebe um arquivo de audio e retorna o texto transcrito

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from transformers import pipeline
import asyncio

async def homepage(request):
    payload = await request.body()
    string = payload.decode("utf-8")
    response_q = asyncio.Queue()
    await request.app.model_queue.put((string, response_q))
    output = await response_q.get()
    return JSONResponse(output) 

async def server_loop(q):
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-large-v2",
        generate_kwargs={"language": "br", "task": "transcribe"},
        # cpu, cuda, ipu, xpu, mkldnn, opengl, opencl, ideep, hip, ve, fpga, ort, xla, lazy, vulkan, mps, meta, hpu, mtia, privateuseone
        device="cpu", 
        use_fast=True
    )

    while True:
        (string, response_q) = await q.get()
        res = pipe(string, batch_size=10, return_timestamps=True, chunk_length_s=30, stride_length_s=(4, 2)) 
        await response_q.put(res)

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

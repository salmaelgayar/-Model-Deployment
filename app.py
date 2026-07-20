from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.responses import StreamingResponse

from transformers import TextIteratorStreamer

import threading

from model import model, tokenizer

app = FastAPI()


class Prompt(BaseModel):
    prompt: str


@app.post("/generate")
def generate(data: Prompt):

    inputs = tokenizer(
        data.prompt,
        return_tensors="pt"
    ).to(model.device)

    output = model.generate(
        **inputs,
        max_new_tokens=200
    )

    text = tokenizer.decode(
        output[0],
        skip_special_tokens=True
    )

    return {
        "response": text
    }


@app.post("/stream")
def stream(data: Prompt):

    inputs = tokenizer(
        data.prompt,
        return_tensors="pt"
    ).to(model.device)

    streamer = TextIteratorStreamer(
        tokenizer,
        skip_special_tokens=True
    )

    generation_kwargs = dict(
        **inputs,
        streamer=streamer,
        max_new_tokens=200
    )

    thread = threading.Thread(
        target=model.generate,
        kwargs=generation_kwargs
    )

    thread.start()

    return StreamingResponse(
        streamer,
        media_type="text/plain"
    )

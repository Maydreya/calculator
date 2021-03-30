from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/plus')
def plus(a: float, b: float):
    return a + b


@app.get('/minus')
def minus(a: float, b: float):
    return a - b


@app.get('/multi')
def multiplication(a: float, b: float):
    return a * b


@app.get('/divide')
def division(a: float, b: float):
    return a / b


if __name__ == '__main__':
    uvicorn.run(app)

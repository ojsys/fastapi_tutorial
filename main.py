from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello World -- My Code Runs'}

@app.post('/')
def post_root():
    return {'hello': 'This is my message from the post server'}

@app.put('/')
def put_root():
    return {'hello': 'This is my message from the put server'}

@app.patch('/')
def patch_root():
    return {'hello': 'This is my message from the patch server'}

@app.delete('/')
def delete_root():
    return {'hello': 'This is my message from the delete server'}
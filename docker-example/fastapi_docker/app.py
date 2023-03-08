from fastapi import FastAPI, Response

#----------------
app = FastAPI()

#---------
#---NEW---
#---------
@app.get('/')
async def test():
    return Response("This seems to work!",200)
# FastAPI 모듈에서 FastAPI 클래스를 가져옵니다.
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() #FastAPI 클래스의 인스턴스를 생성합니다.

@app.get("/")   # @app.get("/")는 "/": 루트 URL에 오는 GET 요청을 처리하겠다는 의미입니다.
async def read_root():
    return {"Hello":"World"}

@app.get("/item/{item_id}")  # 첫번째 파라미터 삽입. 경로 매개변수
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/")  # 두번쨰 파라미터. 쿼리 매개변수
async def read_items(item_1 : int = 1, item_2 : int = 2):
    return {"items" : [item_1,item_2]}

class User(BaseModel):
    username: str
    age: int
    password: str

@app.post("/user/")
async def create_user(user: User):
    return {"user": user.dump()}

# 만약 이 파일을 직접 실행하면, 아래 코드를 실행하게 됩니다.
# 예를 들어, 'python app.py'로 실행할 때만 이 코드가 실행됩니다.
if __name__ == "__main__":
    # uvicorn 서버를 불러옵니다. 'uvicorn'은 FastAPI 애플리케이션을 실행시킬 수 있는 서버입니다.
    import uvicorn

    # uvicorn.run()을 통해 FastAPI 애플리케이션을 실행합니다.
    # host = 'localhost'는 서버를 로컬호스트에서 실행하고,
    # port = 8000은 8000번 포트를 사용하여 서버가 실행되도록 합니다.
    uvicorn.run(app, host = 'localhost', port = 8000)





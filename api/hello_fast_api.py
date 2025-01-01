# -*- coding:utf-8 -*-
"""
hello_http module.
"""
import uvicorn
#  Copyright © 2024 the original author or authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pydantic.v1 import validator

app = FastAPI()

# 模拟数据库
fake_db = {}


# 定义 Pydantic 模型
class Item(BaseModel):
    """Item"""
    item_id: int
    item_name: str

    @validator('item_name')
    def check_item_name(self, v):
        if len(v.strip()) == 0:
            raise ValueError('item_name cannot be empty')
        return v


@app.get("/")
async def read_root():
    """
    获取根路径信息。

    curl 示例:
    ```bash
    curl -X GET "http://127.0.0.1:9527/"
    ```
    """
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    根据 ID 获取项。

    curl 示例:
    ```bash
    curl -X GET "http://127.0.0.1:9527/items/1"
    ```
    """
    item = fake_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item_name": item}


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    """
    创建新项。

    curl 示例:
    ```bash
    curl -X POST "http://127.0.0.1:9527/items/" \
    -H "Content-Type: application/json" \
    -d '{"item_id": 2, "item_name": "example_item"}'
    ```
    """
    if item.item_id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_db[item.item_id] = item.item_name
    return item


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    """
    更新现有项。

    curl 示例:
    ```bash
    curl -X PUT "http://127.0.0.1:9527/items/1" \
    -H "Content-Type: application/json" \
    -d '{"item_id": 1, "item_name": "updated_item"}'
    ```
    """
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = item.item_name
    return item


@app.patch("/items/{item_id}")
async def partial_update_item(item_id: int, item: Item):
    """
    部分更新现有项（仅更新提供的字段）。

    curl 示例:
    ```bash
    curl -X PATCH "http://127.0.0.1:9527/items/1" \
    -H "Content-Type: application/json" \
    -d '{"item_name": "partially_updated_item"}'
    ```
    """
    stored_item = fake_db.get(item_id)
    if stored_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    # 只更新提供的字段
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item.copy(update=update_data)
    fake_db[item_id] = updated_item
    return {"item_id": item_id, "item_name": updated_item}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """
    删除指定 ID 的项。

    curl 示例:
    ```bash
    curl -X DELETE "http://127.0.0.1:9527/items/1"
    ```
    """
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_db[item_id]
    return {"message": "Item deleted"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9527)

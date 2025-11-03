import pytest

# create new item
def test_create_item(client):
    response = client.post(
        "/api/items/",
        json={"title": "Test Item", "description": "This is a test item", "price": 10.5},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "Test Item"
    assert data["description"] == "This is a test item"
    assert data["price"] == 10.5
    assert "id" in data
    assert "created_at" in data

# read items list 
def test_read_items(client):
    client.post(
        "/api/items/",
        json={"title": "Test Item 1", "description": "Desc 1", "price": 10},
    )
    client.post(
        "/api/items/",
        json={"title": "Test Item 2", "description": "Desc 2", "price": 20},
    )

    response = client.get("/api/items/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "Test Item 1"
    assert data[1]["title"] == "Test Item 2"

# read item by id
def test_read_item(client):
    response = client.post(
        "/api/items/",
        json={"title": "Single Item", "description": "Desc Single", "price": 99.9},
    )
    item_id = response.json()["id"]

    response = client.get(f"/api/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Single Item"
    assert data["id"] == item_id

def test_read_item_not_found(client):
    response = client.get("/api/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

# update item
def test_update_item(client):
    response = client.post(
        "/api/items/",
        json={"title": "Original Title", "description": "Original Desc", "price": 50},
    )
    item_id = response.json()["id"]
    print(f"Created item with ID: {item_id}")

    update_response = client.put(
        f"/api/items/{item_id}",
        json={"title": "Updated Title", "description": "Updated Desc", "price": 55.5},
    )
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["title"] == "Updated Title"
    assert data["description"] == "Updated Desc"
    assert data["price"] == 55.5
    assert data["id"] == item_id

def test_update_item_not_found(client):
    response = client.put(
        "/api/items/999",
        json={"title": "Does not matter", "description": "Does not matter", "price": 0},
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

# delete item
def test_delete_item(client):
    response = client.post(
        "/api/items/",
        json={"title": "To Be Deleted", "description": "Delete me", "price": 1},
    )
    item_id = response.json()["id"]

    delete_response = client.delete(f"/api/items/{item_id}")
    assert delete_response.status_code == 200
    data = delete_response.json()
    assert data["id"] == item_id

    # confirm deletion
    get_response = client.get(f"/api/items/{item_id}")
    assert get_response.status_code == 404

def test_delete_item_not_found(client):
    response = client.delete("/api/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
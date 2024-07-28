import requests

try:
    board_create_response = requests.post('http://localhost:3000/api/boards', json={"name":"test-board"})
    print('Board create response:', board_create_response.status_code)
    print('Board create response:', board_create_response.json())
    new_board_id = board_create_response.json()['id']
    print('New board id:', new_board_id)

    create_list_response_1 = requests.post('http://localhost:3000/api/lists', json={"name":"test-list-1", "boardId":new_board_id})
    print('List create response:', create_list_response_1.status_code)
    print('List create response:', create_list_response_1.json())
    new_list_id = create_list_response_1.json()['id']
    print('New list id:', new_list_id)

    delete_response = requests.delete(f'http://localhost:3000/api/lists/{new_list_id}')
    print('List delete response:', delete_response.status_code)

except Exception as e:
    print('Failed to call api', e)
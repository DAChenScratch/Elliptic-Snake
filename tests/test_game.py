from app.game import Game
import numpy as np

def test_init():
    game1 = Game(5,8,"eae-45b")
    assert game1.height == 5
    assert game1.width == 8
    assert game1.id == "eae-45b"

data = {
  "you": "25229082-f0d7-4315-8c52-6b0ff23fb1fb",
  "width": 5,
  "turn": 0,
  "snakes": [
    {
      "taunt": "gotta go fast",
      "name": "other-snake",
      "id": "0fd33b05-37dd-419e-b44f-af9936a0a00c",
      "health_points": 50,
      "coords": [
        [
          2,
          1
        ],
        [
          2,
          2
        ],
        [
          2,
          3
        ]
      ]
    },
    {
      "taunt": "git gud",
      "name": "my-snake",
      "id": "25229082-f0d7-4315-8c52-6b0ff23fb1fb",
      "health_points": 93,
      "coords": [
        [
          0,
          0
        ],
        [
          0,
          0
        ],
        [
          0,
          0
        ]
      ]
    }
  ],
  "height": 5,
  "game_id": "870d6d79-93bf-4941-8d9e-944bee131167",
  "food": [
    [
      3,
      3
    ],
    [
      0,
      4
    ]
  ],
  "dead_snakes": [
    {
      "taunt": "gotta go fast",
      "name": "other-snake",
      "id": "c4e48602-197e-40b2-80af-8f89ba005ee9",
      "health_points": 50,
      "coords": [
        [
          4,
          1
        ],
        [
          4,
          2
        ],
        [
          4,
          3
        ]
      ]
    }
  ]
}

def test_parse_data():
    game1 = Game(5,5,"870d6d79-93bf-4941-8d9e-944bee131167")
    game1.parse_data(data)
    assert game1.food == [[3,3],[0,4]]
    assert game1.snakes[1]["coords"][0] == [2,1]
    assert game1.snakes == [{"taunt": "git gud","name": "my-snake","id": "25229082-f0d7-4315-8c52-6b0ff23fb1fb",
        "health_points": 93,"coords": [[0,0],[0,0],[0,0]]},
        {"taunt": "gotta go fast","name": "other-snake","id": "0fd33b05-37dd-419e-b44f-af9936a0a00c","health_points": 50,
         "coords": [[2,1],[2,2],[2,3]]}]
    expected_board = np.array([[ 0,  0,  1,  0,  0,],
        [ 0,  1,  1,  1,  0],
        [ 0,  0,  1,  0,  0],
        [ 0,  0,  1,  0,  0],
        [ 0,  0,  0,  0,  0]])  
    expected_board_e = np.array([[ 1,  0,  0,  0,  0,],
        [ 0,  0,  1,  0,  0],
        [ 0,  0,  1,  0,  0],
        [ 0,  0,  1,  0,  0],
        [ 0,  0,  0,  0,  0]])
    assert np.array_equal(expected_board, game1.board)
    assert np.array_equal(expected_board_e, game1.board_e)
    print(game1.board)

if __name__ == "__main__":
    test_parse_data()
from app.game import Game

def test_class():
	game1 = Game(5,8,"eae-45b")
	assert game1.height == 5
	assert game1.width == 8
	assert game1.id == "eae-45b"
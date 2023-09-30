TARGET2 = main.py

run: test
	python ./infix/$(TARGET2)

test:
	pytest tests/
	coverage run -m pytest tests/
	coverage html
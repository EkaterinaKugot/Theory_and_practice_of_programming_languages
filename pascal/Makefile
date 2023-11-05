TARGET = main.py

run: test
	python ./$(TARGET)

test:
	coverage run -m pytest tests/
	coverage html

build:
	docker build -t python-challenges .

run:
	docker run -it python-challenges bash

bmi-tests: build
	docker run -it python-challenges /bin/bash -c "cd bmi && python3 -m unittest test_bmi_calculator.py"

leap-year-tests: build
	docker run -it python-challenges /bin/bash -c "cd leap_year && ./run_tests.sh"

pizza-order-tests: build
	docker run -it python-challenges /bin/bash -c "cd pizza_order && ./run_tests.sh"
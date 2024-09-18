VENV := .venv
MKFILE_DIR := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))
VENV_DIR = $(MKFILE_DIR)$(VENV)

# Setup commands
venv_setup:
	@echo "Creating virtual environment..."
	python3.12 -m venv $(VENV); \
	source $(VENV_DIR)/bin/activate && \
	export SYSTEM_VERSION_COMPAT=1 && \
	pip install poetry

run_sql: init_db
	docker compose run -e DB_TYPE=SQL --service-ports api

run_file: init_db
	docker compose run -e DB_TYPE=file --service-ports api

init_db:
	docker compose run api bash -c "python app/adaptor/into/cli/init_db.py"

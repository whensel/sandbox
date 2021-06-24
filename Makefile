-include .env.$(or $(APP_ENV),dev)
export

.PHONY: run
run: ## Runs the app
	poetry run runapp

.PHONY: test
test: ## Runs the tests
	poetry run pytest -v

.PHONY: lint
lint: ## Runs the linters
	poetry run black --check .

.PHONY: fmt
fmt: ## Runs the formatters
	poetry run black .

.PHONY: db-init
db-init: ## Create schema for DB
	cat resources/users.sql | \
		 docker-compose exec -T db psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)
	cat resources/posts.sql | \
		 docker-compose exec -T db psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

.PHONY: db-prompt
db-prompt: ## Jumps into the Postgres DB psql prompt
	docker-compose exec db psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

.PHONEY: docker-run
docker-run: ##Run Docker poetry test
	docker-compose exec docker_test

.PHONEY: db-seed
db-seed: ##Seed postgres db




.PHONY: help
help: ## Display this message
	@grep -h -E '^[a-zA-Z0-9\._-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
# .DEFAULT_GOAL := help

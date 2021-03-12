.PHONY: run
run: ## Runs the app
	echo "Run the app"

.PHONY: test
test: ## Runs the tests
	poetry run pytest -v

.PHONY: help
help: ## Display this message
	@grep -h -E '^[a-zA-Z0-9\._-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
# .DEFAULT_GOAL := help
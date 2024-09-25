update_poetry_lock_file:
	poetry add $(pip freeze)

build_image:
	docker build -t text-cat-service .

build_image_no_cache:
	docker build --no-cache -t text-cat-service .

build_image_with_tag:
	docker build -t text-cat-service:$(tag) .

build_image_with_tag_no_cache:
	docker build --no-cache -t text-cat-service:$(tag) .

run_container:
	docker run --name text-cat-service-container -p 8077:8077 -d text-cat-service:$(tag)

build:
	docker-compose --profile dev build

up:
	docker-compose --profile dev up
.PHONY: build
build:
	docker build -t analytics .

.PHONY: push
push:
	docker tag analytics:latest quay.io/bjoydeep/analytics:latest
	docker push quay.io/bjoydeep/analytics:latest

.PHONY: deploy
deploy:
	kubectl apply -k deploy 

.PHONY: publish
publish: build push	deploy

ifneq (,$(wildcard .env))
  include .env
endif

export IMAGE GCP_PROJECT GCP_REGION ARTIFACTSREPO MEMORY

build_container_local:
	docker build --tag=${IMAGE}:dev .

run_container_local:
	docker run -it -e PORT=8000 -p 8000:8000 ${IMAGE}:dev

build_for_production:
	docker build --no-cache\
		--platform linux/amd64 \
		-t ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${ARTIFACTSREPO}/${IMAGE}:prod \
		.


push_image_production:
	docker push ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${ARTIFACTSREPO}/${IMAGE}:prod

deploy_to_cloud_run:
	gcloud run deploy \
		--image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${ARTIFACTSREPO}/${IMAGE}:prod \
		--memory ${MEMORY} \
		--region ${GCP_REGION} \
		--allow-unauthenticated

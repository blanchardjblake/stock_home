apk --no-cache add docker-compose >/dev/null
echo $CI_JOB_TOKEN | docker login -u $CI_REGISTRY_USER --password-stdin $CI_REGISTRY

# gitlab-ci-build-docker-image-using-cache

Build a docker image for a simple Python console application using a multi stage docker file. Uses the GitLab cache to store an intermediate docker image containing just the Python dependencies.
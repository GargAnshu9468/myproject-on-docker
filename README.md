# Building a Robust CI/CD Pipeline for a Django Application with PostgreSQL, GitHub, Gunicorn, Nginx, Docker & Jenkins on AWS EC2

### Commands

To become a root user:

    sudo su

To install & start the docker service:

    yum install docker -y
    service docker start

To install & start the jenkins service:

    docker pull jenkins/jenkins
    docker run -d -p 8080:8080 docker/jenkins/jenkins

To adds the jenkins user to the docker group & then restart the jenkins service (if required):

    usermod -aG docker jenkins
    systemctl restart jenkins

Github Repository URL format for Jenkins Pipeline:

    https://<username>:<token>@github.com/<repository>.git

To check the permissions and change the ownership of the docker socket and then restart the docker service (if required):

    ls -l /var/run/docker.sock
    chown root:docker /var/run/docker.sock
    systemctl restart docker

Create .env & .env.db files at:

    vi /var/lib/jenkins/workspace/myproject/.env
    vi /var/lib/jenkins/workspace/myproject/.env.db

To access the application files inside the container:

    docker exec -it myproject-web-1 /bin/bash

To access the database inside the container:

    docker exec -it myproject-db-1 /bin/bash
    psql --username=myproject --dbname=myproject_db

To access the nginx configuration files inside the container:

    docker exec -it myproject-nginx-1 /bin/bash

To access all the project files inside the workspace:

    cd /var/lib/jenkins/workspace/myproject/

To access all the workspaces:

    cd /var/lib/jenkins/workspace/

To run the migrations (manually):

    docker-compose exec web python manage.py migrate --noinput

To collect the static files (manually):

    docker-compose exec web python manage.py collectstatic --no-input --clear

To ensure the database and the tables were created:

    docker-compose exec db psql --username=myproject --dbname=myproject_db

To check that the volume was created as well:

    docker volume inspect myproject-on-docker_postgres_data

To update the entrypoint file permissions locally (manually):

    chmod +x app/entrypoint.sh

To build the images and run the containers (manually):

    docker-compose up -d --build

Test it out at [http://localhost](http://localhost) or [http://your-remote-ip](http://your-remote-ip) or [http://your-domain-name](http://your-domain-name). No mounted folders. To apply changes, the image must be re-built.

If the container fails to start, check for errors in the logs via:

    docker-compose logs -f

Remove or bring down volumes along with the containers once done (manually):

    docker-compose down -v

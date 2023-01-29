# Microblog

Microblog is a practice blog application built with Flask, inspired by Facebook-style blogs. It uses Postgres as a database and is fully Dockerized.

## Requirements

- Docker (instructions for downloading and installing Docker can be found [here](https://docs.docker.com/get-docker/))

## Getting Started

1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/microblog.git
```

2. Build the Docker images
```
make build
```

3. Start the containers
```
make up
```

4. Access the application at `http://localhost:8000`

5. Stop the containers
```
make down
```

## Contributing

1. Create a new branch for your changes
```
git checkout -b YOUR_BRANCH_NAME
```

2. Make your changes and commit them
```
git add .
git commit -m "YOUR COMMIT MESSAGE"
```

3. Push your changes to your branch
```
git push origin YOUR_BRANCH_NAME
```
Please, don't forget to replace YOUR_USERNAME with your actual username and YOUR_BRANCH_NAME with the name of the branch you want to use.

4. Create a Pull Request on GitHub.

> **Note**:
> - The Pull Request must be reviewed and approved by the code owners.
> - The checks has to pass before merging. Please make sure your changes have the neccesary tests.
> - The app has educational purposes only.

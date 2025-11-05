pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=results.xml'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest_fitness:latest .'
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-credentials', variable: 'DOCKER_PASSWORD')]) {
                    sh 'docker login -u <your-dockerhub-username> -p $DOCKER_PASSWORD'
                    sh 'docker tag aceest_fitness:latest <your-dockerhub-username>/aceest_fitness:latest'
                    sh 'docker push <your-dockerhub-username>/aceest_fitness:latest'
                }
            }
        }
    }
}
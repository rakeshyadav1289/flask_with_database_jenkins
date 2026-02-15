pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rakeshyadav1289/flask_with_database_jenkins.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Test App') {
            steps {
                sh 'curl --fail http://localhost:5000 || exit 1'
            }
        }
    }

    post {
        always {
            sh 'docker compose down'
        }
    }
}



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
                //sh 'curl --fail http://192.168.0.154:5000/register || exit 1'
		sh '''
		        for i in {1..10}; do
		          curl --fail http://localhost:5000/register && exit 0
		          echo "Waiting for Flask..."
		          sleep 5
		        done
		        exit 1
		        '''

            }
        }
    }

    post {
        always {
<<<<<<< HEAD
           sh 'docker compose down'
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
           sh 'docker compose down'
	 
=======
            sh 'docker compose down'
>>>>>>> parent of 6107f20 (finally code working)
=======
            sh 'docker compose down'
>>>>>>> parent of 6107f20 (finally code working)
=======
            sh 'docker compose down'
>>>>>>> parent of 6107f20 (finally code working)
=======
            sh 'docker compose down'
>>>>>>> parent of 6107f20 (finally code working)
>>>>>>> 502cd10 (errot)
        }
    }
}





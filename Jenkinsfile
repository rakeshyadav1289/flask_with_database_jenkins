pipeline
{
    agent any

    stages {
        stage('git clone') {
            steps {
                echo 'git cloning...'
                // Add your build commands here
                git branch: 'main', url: 'https://github.com/rakeshyadav1289/dummy.git'

            }
        }
        stage('build') {
            steps {
                echo 'building...'
                // Add your build commands here
            }
        }
        
    }
}
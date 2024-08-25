pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/swathiBheemireddy/Test_hello.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}

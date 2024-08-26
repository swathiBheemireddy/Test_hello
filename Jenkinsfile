pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
               checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/swathiBheemireddy/Test_hello.git']])
            }
        }
        stage('Build') {
            steps {
               git branch: 'main', url: 'https://github.com/swathiBheemireddy/Test_hello.git'
               bat 'python test_script.py'

            }
        }
    }
}
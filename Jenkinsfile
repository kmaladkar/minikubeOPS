pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/dev']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/kmaladkar/minikubeOPS.git']])
            }
        }
        stage('Test1') {
            steps {
                sh 'python3 -m pytest'
            }
        }
        stage('Test2') {
            steps {
                sh 'python3 -m pytest'
            }
        }
    }
    post {
        success {
            setBuildStatus("Build succeeded", "SUCCESS");
        }
        failure {
            setBuildStatus("Build failed", "FAILURE");
        }
    }
}


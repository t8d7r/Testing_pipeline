pipeline {
    agent any
    stages {
        stage('test_syntax') {
            steps {
                sh 'yamllint host_vars/*'
            }
        }  
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}

pipeline {
    agent any
    stages {
        stage('test_syntax') {
            steps {
                sh 'yamllint host_vars/*'
            }
        } 
	stage('test_network_readiness') {
            steps {
		withPythonEnv('/home/thomasd/Suzie-Q/suzie-q') {
		    sh 'python3.8 --version'
		}			
            }
        }
 
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}

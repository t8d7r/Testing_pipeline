pipeline {
    agent {
    	node {
        	label 'jenkins'
        	customWorkspace '/home/thomasd/Jenkins/Testing_pipeline'
    	}
    }  
    stages {
        stage('test_syntax') {
            steps {
                sh 'yamllint host_vars/*'
            }
        } 
	stage('test_network_readiness') {
            steps {
		    sh 'python3.8 --version'
                    sh 'python3.8 tests/test_hosts_up.py'
            }
        }
 
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}

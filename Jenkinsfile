pipeline {
    agent any

    stages {
        stage('Git Clone') {
            steps {
                echo 'clonning the github'
            }
        }
        stage('Build') {
            steps {
                echo 'Build the application'
            }
        }
        stage('Testing') {
            steps {
                echo 'testing  the application'
            }
        }
        stage('Publish') {
            steps {
                echo 'publish to server'
            }
        }
        stage('Deployment') {
            steps {
                echo 'deploy the application to main server for users for downling the application'
            }
            
        }
    }
}

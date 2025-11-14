pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Eb1n-Babu/Tesing.git'
            }
        }
        stage('Test') {
            steps {
                bat '''
                cd primeNumbers
                python test_prime.py
                '''
            }
        }
    }
}
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Eb1n-Babu/Tesing.git'
            
        }
        stage('Test-1') {
            steps {
                bat '''
                cd primeNumbers
                python test_prime.py
                '''
            }
        }
        stage('Test-2') {
            steps {
                bat '''
                cd anagram
                python anagram_testing.py
                '''
            }
        }
        stage('Test-3') {
            steps {
                bat '''
                cd palindrome
                python test_palindrome.py
                '''
            }
        }
        stage('Test-4') {
            steps {
                bat '''
                cd Test_Module
                python test1.py
                '''
            }
    }
}


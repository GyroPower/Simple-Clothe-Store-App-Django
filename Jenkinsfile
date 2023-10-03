pipeline {
    agent {doker { image 'python:3.11.5-alphine.18'}}
    stages{
        stage('build'){
            steps {
                sh 'git clone https://github.com/GyroPower/Simple-Clothe-Store-App-Django.git'
                sh 'echo "made it"'
            }
        }
    }
}
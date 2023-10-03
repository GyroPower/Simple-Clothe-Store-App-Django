pipeline {
    agent {doker { image 'python:3.11.5-alphine.18'}}
    stages{
        stage('build'){
            steps {
                sh 'cd Simple_Store_D'
                sh 'py manage.py runserver'
            }
        }
    }
}
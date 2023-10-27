pipeline {
    agent any
    stages{
        stage('build test'){
            steps {
                bat '''
                    cd Simple_Store_D
                    dir
                    docker-compose -f docker-compose.dev.yml up -d --build
                    docker-compose -f docker-compose.dev.yml exec simple-store python manage.py test
                    docker-compose -f docker-compose.dev.yml down -v
                '''
                
                // bat 'docker-compose -f docker-compose.dev.yml up -d --build '
                // bat 'docker-compose -f docker-compose.dev.yml exec simple-store python manage.py test'
                // bat 'docker-compose -f docker-compose.dev.yml down -v'
            }
        }
    }
}
pipeline {
    agent any


    stages{
        stage('build test'){
            steps {
                
                powershell '''
                    cd Simple_Store_D
                    docker-compose -f Simple-Store.dev.yml up --build
                    docker-compose -f Simple-Store.dev.yml exec simple-store python manage.py test
                    docker-compose -f Simple-Store.dev.yml down 
                '''
                
                // bat 'docker-compose -f docker-compose.dev.yml up -d --build '
                // bat 'docker-compose -f docker-compose.dev.yml exec simple-store python manage.py test'
                // bat 'docker-compose -f docker-compose.dev.yml down -v'
            }
        }
    }
}
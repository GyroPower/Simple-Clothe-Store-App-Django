pipeline {
    agent any


    stages{
        stage('build test'){
            steps {
                
                powershell '''
                    docker-compose -f Simple_Store_D/Simple-Store.dev.yml up -d --build
                    docker-compose -f Simple_Store_D/Simple-Store.dev.yml exec simple-store ls
                    docker-compose -f Simple_Store_D/Simple-Store.dev.yml exec simple-store entrypoint.sh
                    docker-compose -f Simple_Store_D/Simple-Store.dev.yml exec simple-store python manage.py test
                    docker-compose -f Simple_Store_D/Simple-Store.dev.yml down 
                '''
                
                // bat 'docker-compose -f docker-compose.dev.yml up -d --build '
                // bat 'docker-compose -f docker-compose.dev.yml exec simple-store python manage.py test'
                // bat 'docker-compose -f docker-compose.dev.yml down -v'
            }
        }
    }
}
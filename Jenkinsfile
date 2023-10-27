pipeline {
    agent any

    environment {
        SIMPLE_STORE_DATABASE_HOSTNAME = credentials('')
    }

    stages{
        stage('build test'){
            steps {
                echo "${SIMPLE_STORE_DATABASE_HOSTNAME}"
                
                powershell '''
                    cd Simple_Store_D
                    ls
                '''
                //     docker-compose -f Simple-Store.dev.yml up -d --build
                //     docker-compose -f Simple-Store.dev.yml exec simple-store python manage.py test
                //     docker-compose -f Simple-Store.dev.yml down -v
                // '''
                
                // bat 'docker-compose -f docker-compose.dev.yml up -d --build '
                // bat 'docker-compose -f docker-compose.dev.yml exec simple-store python manage.py test'
                // bat 'docker-compose -f docker-compose.dev.yml down -v'
            }
        }
    }
}
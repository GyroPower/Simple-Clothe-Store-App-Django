pipeline {
    agent any


    stages{
        stage('build test'){
            steps {
                
                powershell '''
                    docker-compose -f Simple_Store_D/Simple-Store.dev.yml up -d --build
                    
                    docker-compose -f Simple_Store_D/Simple-Store.dev.yml exec simple-store python manage.py flush --no-input
                    docker-compose -f Simple_Store_D/Simple-Store.dev.yml exec simple-store python manage.py migrate
                    
                     
                '''
                
            }
        }

        stage('Test'){
            steps{
                powershell 'docker-compose -f Simple_Store_D/Simple-Store.dev.yml exec simple-store python manage.py test'

            }
        }

        stage('Down dev app container'){
            steps{
                powershell 'docker-compose -f Simple_Store_D/Simple-Store.dev.yml down'
            }
        }
    }
}
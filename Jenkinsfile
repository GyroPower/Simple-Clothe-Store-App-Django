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

                
                script{
                    catchError (buildResult: 'FAILURE', stageResult: 'FAILURE'){
                        powershell 'docker-compose -f Simple_Store_D/Simple-Store.dev.yml exec simple-store python manage.py test'
                    }
                    

                    if (currentBuidl.result == "FAILURE"){
                        echo "Stage Failed"
                        powershell 'docker-compose -f Simple_Store_D/Simple-Store.dev.yml down'  
                        error("Stage Failed")      
                    }
                }
            }
        }

        stage('Down dev app container and start Prod project'){
            steps{
                powershell 'docker-compose -f Simple_Store_D/Simple-Store.dev.yml down'
                echo "Creating the prod project"
            }
        }
    }
}
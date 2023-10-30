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
                    

                    if (currentBuild.result == "FAILURE"){
                       
                        powershell 'docker-compose -f Simple_Store_D/Simple-Store.dev.yml down'  
                        error("Stage Failed")      
                    }
                }
            }
        }

        stage('Down dev project version'){
            steps{
                powershell 'docker-compose -f Simple_Store_D/Simple-Store.dev.yml down'
                
            }
        }

        stage('Build prod project version'){
            steps{
                echo "Creating the prod project"
                powershell '''
                    docker-compose -f Simple_Store_D/Simple-Store.prod.yml up -d --build
                    docker-compose -f Simple_Store_D/Simple-Store.prod.yml exec simple-store python manage.py makemigrations
                    docker-compose -f Simple_Store_D/Simple-Store.prod.yml exec simple-store python manage.py migrate
                '''
            }
        }

        stage('Test prod project'){
            steps{
                script{
                    catchError (buildResult: 'FAILURE', stageResult: 'FAILURE'){
                        powershell 'docker-compose -f Simple_Store_D/Simple-Store.prod.yml exec simple-store python manage.py test'
                    }

                    if (currentBuild.result == "FAILURE"){
                       
                        powershell 'docker-compose -f Simple_Store_D/Simple-Store.prod.yml down'  
                        error("Stage Failed")      
                    }                   
                }

            }
        }

        stage('Down prod container'){
            steps{
                echo 'Down prod build'
                powershell 'docker-compose -f Simple_Store_D/Simple-Store.prod.yml down'
            }
        }
    }
}
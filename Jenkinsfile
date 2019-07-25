pipeline {
   
   agent any

   environment {
        MVN_HOME = '/Applications/apache-maven-3.6.1'
        SAAGIE_CREDS = credentials('SaagieCreds')
        SAAGIE_URL = 'https://saagie-beta.prod.saagie.io'
    }
   
   
   stages {
       stage('Clone Repo') { 
          steps { 
            git 'https://github.com/sgokaram-saagie/preprocesscustomer-aws-python-saagie.git'
          }
       }
       
       stage('Build') {
           steps{
                sh 'zip -r -X preprocesscustomer.zip preprocess-customerdata.py requirements.txt' 
           }
       }
       
       stage('Deploy on Saagie Demo Environment') {
           environment {
                    SAAGIE_PLATFORM = '4'
            }
           steps{
               sh "gradle projectsCreateJob -b ./build.gradle.projectsCreateJob  -Psaagieusername=$SAAGIE_CREDS_USR -Psaagiepassword=$SAAGIE_CREDS_PSW -Psaagieplatform=$SAAGIE_PLATFORM -Psaagieurl=$SAAGIE_URL"
            }          
          
       }
    }
}
pipeline {

   agent any
   jobID=''
   jobID_instance_id=''

   environment {
        MVN_HOME = '/Applications/apache-maven-3.6.1'
        SAAGIE_CREDS = credentials('SaagieCreds')
        SAAGIE_URL = 'https://saagie-workspace.prod.saagie.io'
    }


   stages {
       stage('Clone Repo') {
          steps {
            git 'https://github.com/sgokaram-saagie/preprocesscustomer-aws-python-saagie.git'
          }
       }

       stage('Build') {
           steps{
                sh 'zip -r -X preprocesscustomer.zip preprocess-customerdata-demo.py requirements.txt'
           }
       }

       stage('Deploy Job on Saagie Demo Environment') {
           environment {
                    SAAGIE_PROJECT = 'cad415fc-a809-4f5a-919e-668dccb4a2de'
                    SAAGIE_PLATFORM = '4'
            }
           steps{
               script{
               sh "gradle  projectCreateJob1 -b ./build.gradle.projectsCreateJob  -Psaagieuserid=$SAAGIE_CREDS_USR -Psaagiepassword=$SAAGIE_CREDS_PSW -Psaagieplatformid=$SAAGIE_PLATFORM -Psaagieurl=$SAAGIE_URL -Psaagieprojectid=$SAAGIE_PROJECT -Psaagiejobid1_file='./job1_id' "
               jobID = readFile('./job1_id')
               println(jobID)
               }
               
            }
       }
       stage('Test Job on Saagie Demo Environment') {
           environment {
                    SAAGIE_PROJECT = 'cad415fc-a809-4f5a-919e-668dccb4a2de'
                    SAAGIE_PLATFORM = '4'
                    SAAGIE_JOBID = jobID
          }
           steps{
               script{
               sh "gradle  projectCreateJob1 -b ./build.gradle.projectsCreateJob  -Psaagieuserid=$SAAGIE_CREDS_USR -Psaagiepassword=$SAAGIE_CREDS_PSW -Psaagieplatformid=$SAAGIE_PLATFORM -Psaagieurl=$SAAGIE_URL -Psaagieprojectid=$SAAGIE_PROJECT -Psaagiejobid1=$SAAGIE_JOBID -Psaagiejobid1_instance_file='./job1_id_instance' "
               jobID_instance_id = readFile('./job1_id_instance')
               println(jobID_instance_id)
               }
               
            }
       }
    }
}

jobID=''
jobID_instance_id=''
jobID_instance_status=''

pipeline {

   agent any

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

      
      //Starting of Deploy Stage
      
       stage('Deploy Job on Saagie Demo Environment') {
           environment {
                    SAAGIE_PROJECT = 'cad415fc-a809-4f5a-919e-668dccb4a2de'
                    SAAGIE_PLATFORM = '4'
            }
           steps{
               script{
				   sh "gradle  projectCreateJob1 -b ./build.gradle.projectsCreateJob  -Psaagieuserid=$SAAGIE_CREDS_USR -Psaagiepassword=$SAAGIE_CREDS_PSW -Psaagieplatformid=$SAAGIE_PLATFORM -Psaagieurl=$SAAGIE_URL -Psaagieprojectid=$SAAGIE_PROJECT -Psaagiejobid1_file='./job1_id' "
				   if (fileExists('./job1_id')) {
					   jobID = readFile('./job1_id')
					   println(jobID)
					   new File('./job1_id').delete()
				   } else {
						return
				   }
               
               }
           }
      }
      
      //Starting of Test Stage      
      
      stage('Test Job on Saagie Demo Environment') {
           environment {
                    SAAGIE_PROJECT = 'cad415fc-a809-4f5a-919e-668dccb4a2de'
                    SAAGIE_PLATFORM = '4'
           }
           steps{
               script{
        	   	   sh "gradle  projectRunJob1 -b ./build.gradle.projectsCreateJob  -Psaagieuserid=$SAAGIE_CREDS_USR -Psaagiepassword=$SAAGIE_CREDS_PSW -Psaagieplatformid=$SAAGIE_PLATFORM -Psaagieurl=$SAAGIE_URL -Psaagieprojectid=$SAAGIE_PROJECT -Psaagiejobid=${jobID} -Psaagiejobid1_instance_file='./job1_id_instance' "
            	   if (fileExists('./job1_id_instance')){
	            	   jobID_instance_id = readFile('./job1_id_instance')
    	           	   println(jobID_instance_id)
	    	           new File('./job1_id_instance').delete()
    		       }    
            	   for (int i = 0; i < 10; i++) {
	            	   sh "gradle  projectGetJobInstance1Status -b ./build.gradle.projectsCreateJob  -Psaagieuserid=$SAAGIE_CREDS_USR -Psaagiepassword=$SAAGIE_CREDS_PSW -Psaagieplatformid=$SAAGIE_PLATFORM -Psaagieurl=$SAAGIE_URL -Psaagieprojectid=$SAAGIE_PROJECT -Psaagiejobinstanceid=${jobID_instance_id} -Psaagiejobid1_instancerun_file='./job1_id_instance_run' "
    	           	   if(fileExists('./job1_id_instance_run')) {
    	           		  jobID_instance_status = readFile('./job1_id_instance_run')
    	           		  new File('./job1_id_instance_run').delete()
    	           		  println("Job Status is $jobID_instance_status")
    	           		  if (jobID_instance_status == 'QUEUED' || jobID_instance_status == 'RUNNING') {
    	           			   println("Job Status is ${jobID_instance_status}. Sleeping for 30s")
    	           			   sleep 5
    	           		  } 
    	           		  else {
    	           			break;
    	           		  }
					   }
					}   
                   if (jobID_instance_status != 'SUCCEEDED'){
					return
                   }
               }     
           }
        }
     //End of Test Stage   
     
     // Deploy to Production
       stage('Deploy Job on Saagie Production Environment') {
           input{
   				 message "Do you want to proceed for production deployment?"
		   }
           environment {
                    SAAGIE_PROJECT = 'bdbd16b2-9010-4fe4-b355-65af1c586c8f'
                    SAAGIE_PLATFORM = '4'
            }
           steps{
               script{
				   sh "gradle  projectCreateJob1 -b ./build.gradle.projectsCreateJob  -Psaagieuserid=$SAAGIE_CREDS_USR -Psaagiepassword=$SAAGIE_CREDS_PSW -Psaagieplatformid=$SAAGIE_PLATFORM -Psaagieurl=$SAAGIE_URL -Psaagieprojectid=$SAAGIE_PROJECT -Psaagiejobid1_file='./job1_id' "
				   if (fileExists('./job1_id')) {
					   jobID = readFile('./job1_id')
					   println(jobID)
					   new File('./job1_id').delete()
				   } else {
						return
				   }
               
               }
           }
      }

    // End Deploy to Production     
   }   
}
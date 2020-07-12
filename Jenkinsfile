pipeline{
        agent any

	stages{

		stage ('install Docker'){
                        steps{
                                sh "bash install-docker.sh"
                        }
                }

		stage ('Test application'){
			steps{
				sh "bash tests.sh"
			} 
		}
            	
		stage('Install Docker using ansible'){
                	steps{
                        	sh "bash deploy-ansible.sh"
                	}
            	}
                stage('Deploy application'){
                        steps{
                                sh "bash deploy.sh"

                        }

        	}
	}
}

pipeline{
        agent any
        stages{
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
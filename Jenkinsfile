pipeline {
    agent master

    environment {
        VIRTUAL_ENV = 'venv'  // Virtual environment directory
        REMOTE_SERVER = 'ubuntu@ip-172-31-17-223'
        REMOTE_PATH = '/var/lib/jenkins/workspace/p-e-commerce1'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/developer-markantony/ecommerce-backend.git'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                sh '''
                python -m venv ${VIRTUAL_ENV}
                source ${VIRTUAL_ENV}/bin/activate
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                source ${VIRTUAL_ENV}/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source ${VIRTUAL_ENV}/bin/activate
                pytest --maxfail=1 --disable-warnings -q
                '''
            }
        }

        stage('Deploy to Staging') {
            steps {
                sh '''
                scp -r * ${REMOTE_SERVER}:${REMOTE_PATH}
                ssh ${REMOTE_SERVER} "cd ${REMOTE_PATH} && source ${VIRTUAL_ENV}/bin/activate && gunicorn --workers 3 app:app"
                '''
            }
        }

        stage('Notify Team') {
            steps {
                script {
                    def status = currentBuild.result
                    if (status == 'SUCCESS') {
                        emailext(
                            subject: "Build #${BUILD_NUMBER} - SUCCESS",
                            body: "The build was successful. Please check the staging environment.",
                            to: "lakshmikanth.office@gmail.com"
                        )
                    } else {
                        emailext(
                            subject: "Build #${BUILD_NUMBER} - FAILURE",
                            body: "The build failed. Please check the logs.",
                            to: "lakshmikanth.office@gmail.com"
                        )
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

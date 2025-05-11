pipeline {
    agent any

    environment {
        IMAGE_NAME = "foxxyboy16/MainScoresFlaskApp"
        CONTAINER_NAME = "MainScoresFlaskApp"
        PORT = "8777"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh """
                    docker run -d --rm \
                        --name ${CONTAINER_NAME} \
                        -p ${PORT}:8777 \
                        -v \$(pwd)/Scores.txt:/Scores.txt \
                        ${IMAGE_NAME}:latest
                    """
                    // Give the container a moment to boot
                    sleep(time: 5, unit: "SECONDS")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    def testResult = sh(
                        script: "python3 e2e.py http://localhost:${PORT}",
                        returnStatus: true
                    )
                    if (testResult != 0) {
                        error("E2E tests failed")
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh "docker stop ${CONTAINER_NAME}"
                    sh "docker push ${IMAGE_NAME}:latest"
                }
            }
        }
    }

    post {
        always {
            script {
                sh "docker stop ${CONTAINER_NAME} || true"
            }
        }
    }
}
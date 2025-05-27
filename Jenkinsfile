pipeline {
    agent any

    environment {
        DOCKER_BUILDKIT = 1
    }

    stages {
        stage('Build Users Service') {
            steps {
                dir('services/users') {
                    sh 'docker build -t users-service:latest .'
                }
            }
        }

        stage('Build Products Service') {
            steps {
                dir('services/products') {
                    sh 'docker build -t products-service:latest .'
                }
            }
        }

        stage('Load into Minikube') {
            steps {
                sh 'minikube image load users-service'
                sh 'minikube image load products-service'
            }
        }

        stage('Deploy with Helm') {
            steps {
                sh 'helm upgrade --install users ./helm-charts/users'
                sh 'helm upgrade --install products ./helm-charts/products'
            }
        }
    }

    post {
        failure {
            echo "❌ Build or deployment failed. Check logs above for details."
        }
        success {
            echo "✅ Build and deployment completed successfully."
        }
    }
}

pipeline {
    agent any
    environment {
        IMAGE_NAME = "securedev-app"
        CONTAINER_NAME = "app-vulnerable"
        NETWORK_NAME = "eva3_devsecops-net"
    }
    stages {
        stage("1. Construccion") {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }
        stage("2. Despliegue Temporal") {
            steps {
                sh "docker rm -f ${CONTAINER_NAME} || true"
                sh "docker run -d --name ${CONTAINER_NAME} --network ${NETWORK_NAME} -p 5000:5000 ${IMAGE_NAME}:latest"
                sh "sleep 5"
            }
        }
        stage("3. Pruebas OWASP ZAP") {
            steps {
                sh "chmod 777 ${WORKSPACE}"
                sh "docker run --rm --network ${NETWORK_NAME} -v ${WORKSPACE}:/zap/wrk/:rw -t ghcr.io/zaproxy/zaproxy:stable zap-baseline.py -t http://${CONTAINER_NAME}:5000 -r zap_report.html || true"
            }
        }
        stage("4. Despliegue Produccion") {
            steps {
                echo "Desplegado en puerto 5000"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: "zap_report.html", allowEmptyArchive: true
        }
    }
}

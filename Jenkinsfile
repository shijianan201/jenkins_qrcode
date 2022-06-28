pipeline {
    agent any
    stages {
        stage('生成二维码') {
            steps {
                sh 'python3 gen.py'
            }
        }
    }
    post {
        success {
            archiveArtifacts artifacts: '*.png'
        }
    }
}
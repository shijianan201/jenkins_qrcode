pipeline {
    agent any
    stages {
        stage('生成二维码') {
            steps {
                sh 'python3 gen.py'
            }
        }
        stage("打印hello"){
            steps{
                echo "Hello"
            }
        }
    }
    post {
        success {
            archiveArtifacts artifacts: '*.png'
        }
    }
}
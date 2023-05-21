pipeline {
  agent any
  stages {
    stage('Build') {
      steps{
        script {
            def pythonInstalled = sh(script: 'python --version', returnStatus: true)
            if (pythonInstalled == 0) {
                echo 'Python is installed'
            } else {
                echo 'Python is not installed'
            }
        }
      }
    }
    stage('Test') {
      steps{
        echo('Testing...')
      }
    }
    stage('Deploy') {
      steps{
        echo('Deploying...')
      }
    }
  }
}

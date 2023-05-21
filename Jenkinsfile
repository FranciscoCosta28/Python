pipeline {
  agent any
  stages {
    stage('Build') {
      steps{
        script {
          def pythonTool = tool name: 'Python', type: 'hudson.plugins.python.PythonInstallation'
                    if (pythonTool == null) {
                        error 'Python is not installed'
                    } else {
                        echo 'Python is installed'
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

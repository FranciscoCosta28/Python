pipeline {
    agent any

    stages {
        stage('Check Python') {
            steps {
                script {
                    // Run the shell command to check if Python is installed
                    def pythonInstalled = sh(returnStatus: true, script: 'python3 --version >/dev/null 2>&1')
                    if (pythonInstalled == 0) {
                        // Python is installed
                        echo 'Python is installed on the machine.'
                    } else {
                        // Python is not installed
                        echo 'Python is not installed on the machine.'
                    }
                }
            }
        }
        
    }
}

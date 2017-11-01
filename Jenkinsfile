pipeline {
  agent any
  stages {
    stage('No-op') {
      steps {
        sh 'ls'
      }
    }
  }
  environment {
    DISABLE_AUTH = 'true'
    SAUCE_ACCESS = 'credentials(\'sauce-dev\')'
  }
}
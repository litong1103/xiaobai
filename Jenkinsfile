pipeline {
  agent any
  stages {
    stage('Source') {
      steps {
        git 'https://github.com/litong1103/xiaobai.git'
      }
    }

  }
  environment {
    COMPLETED_MSG = 'Build done!'
  }
}
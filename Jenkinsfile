pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('RunningPy') {
      steps {
        sh 'python3 MatricPy.py'
      }
    }
  }
}

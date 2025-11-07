pipeline {
  agent any
  environment {
    MINIKUBE = '/opt/homebrew/bin/minikube'
    KUBECTL  = '/opt/homebrew/bin/kubectl'
  }
  stages {
    stage('Checkout') {
      steps {
        cleanWs()
        git branch: 'main', url: 'https://github.com/koumaira/moviestore.git'
      }
    }
    stage('Use Minikube Docker') {
      steps { sh 'eval $(' + "${MINIKUBE}" + ' -p minikube docker-env)' }
    }
    stage('Build Image') {
      steps { sh 'docker build -t moviestore:latest .' }
    }
    stage('Deploy') {
      steps {
        sh "${KUBECTL} apply -f deployment.yaml"
        sh "${KUBECTL} apply -f service.yaml"
        sh "${KUBECTL} rollout status deployment/moviestore-deployment"
      }
    }
    stage('Migrate DB') {
      steps {
        sh '''
          POD=$(${KUBECTL} get pods -l app=moviestore -o jsonpath='{.items[0].metadata.name}')
          ${KUBECTL} exec "$POD" -- python manage.py migrate --noinput
        '''
      }
    }
    stage('Show URL') {
      steps {
        sh '''
          NODEPORT=$(${KUBECTL} get svc moviestore-service -o jsonpath='{.spec.ports[0].nodePort}')
          MINIIP=$(${MINIKUBE} ip)
          echo "App URL: http://${MINIIP}:${NODEPORT}"
        '''
      }
    }
  }
}

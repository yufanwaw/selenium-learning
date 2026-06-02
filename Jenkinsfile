pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv .venv'
                sh './.venv/bin/python -m pip install --upgrade pip'
                sh './.venv/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Start Selenium Grid') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Run tests') {
            steps {
                sh './.venv/bin/python -m pytest tests --html=reports/report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            sh 'docker compose down'
            archiveArtifacts artifacts: 'reports/**/*.html,screenshots/**/*,logs/**/*', allowEmptyArchive: true
        }
    }
}

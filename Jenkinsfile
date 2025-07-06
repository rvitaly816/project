pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/rvitaly816/project'
            }
        }
        stage('Setup Python') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\activate && pytest --alluredir=allure-results'
            }
        }
        stage('Allure Report') {
            steps {
                allure includeProperties: false, results: [[path: 'allure-results']]
            }
        }
    }

}
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/nikita159821/Anrex.git',
                    branch: 'main'
            }
        }
        stage('Check Python and Pip') {
            steps {
                bat 'where python'
                bat 'where pip'
            }
        }
        stage('Setup Environment') {
            steps {
                bat 'python3 -m venv venv'  // Создаем виртуальное окружение
                bat 'venv\\Scripts\\activate' // Активируем его (Windows)
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt' // Устанавливаем зависимости (Windows)
            }
        }
        stage('Test') {
            steps {
                bat 'venv\\Scripts\\activate && pytest' // Запускаем тесты (Windows)
            }
        }
    }
}

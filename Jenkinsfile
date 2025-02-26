pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/nikita159821/Anrex.git',
                    branch: 'main' // Замените на вашу ветку
            }
        }
        stage('Setup Environment') {  // Установка виртуального окружения
            steps {
                sh 'python3 -m venv venv' // Создаем виртуальное окружение
                sh 'source venv/bin/activate'  // Активируем его (Linux/macOS)
                // Для Windows используйте:
                // bat 'venv\\Scripts\\activate'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'source venv/bin/activate && pip install -r requirements.txt' // Устанавливаем зависимости из requirements.txt (Linux/macOS)
                // Для Windows:
                // bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'source venv/bin/activate && pytest' // Запускаем тесты с помощью pytest (Linux/macOS)
                // Для Windows:
                // bat 'venv\\Scripts\\activate && pytest'
            }
        }
    }
}

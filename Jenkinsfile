pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://gitlab.b2b-center.ru/n.merkulov/reate-ontract.git', // Адрес вашего репозитория
                    branch: 'main' //  Укажите ветку, с которой хотите работать
            }
        }
        stage('Build') {
            steps {
                // ...
            }
        }
        stage('Test') {
            steps {
                // ...
            }
        }
    }
}

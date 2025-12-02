pipeline {
    agent any

    environment {
        // Por ejemplo, variables de entorno para la BD
        DB_HOST = '0.0.0.0:3306'
        DB_NAME = 'django_db'
        DB_USER = 'django_user'
        DB_PASS = 'django_pass'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/AlejoR96/GestorDetasks.git', branch: 'main'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Database setup') {
            steps {
                // Suponiendo que MySQL ya está corriendo
                sh '. venv/bin/activate'
                sh 'python manage.py migrate'
            }
        }

        stage('Run tests') {
            steps {
                sh '. venv/bin/activate'
                sh 'python manage.py test'
            }
        }

        stage('Build/Package') {
            steps {
                // Si tienes algo como un Dockerfile o paquete
                sh 'docker build -t gestordetasks:latest .'
            }
        }

        stage('Deploy') {
            steps {
                // Aquí lo que uses: docker‐compose, kubernetes, etc.
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/reports/**/*', allowEmptyArchive: true
            junit '**/reports/**/*.xml'
        }
        failure {
            echo 'Algo falló en el pipeline!'
        }
    }
}

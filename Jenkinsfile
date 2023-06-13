pipeline{
    agent any
    options{
        timeout(time: 1, unit: 'MINUTES')
    }
    stages{
        stage("Prepare Python Virtualenv (Pipenv)") {
            // Have pipenv create a virtualenv and download all the required dependencies before running the test and release
            steps {
                echo("Run pipenv install to create python virtualenv with all dependencies")
                sh("pipenv install")
            }
        }
        stage("Unit Test") {
            steps {
                echo("Running unit tests")
                sh("pipenv run python3 -m pytest")
            }
        }
        stage("Build the project") {
            steps {
                echo("Building the project")
                sh("pipenv run pyinstaller main.py --onefile")
            }
        }
        stage("Pacakge the artifact") {
            steps {
                echo("Create the build artifact")
                sh("tar -czf DevOps-test.tar.gz dist/main.exe")
            }
        }
        stage("Upload the release to Github") {
            steps {
                echo("Running the script which uploads the release to Github")
                sh("echo ./release.sh")
            }
        }
    }
}

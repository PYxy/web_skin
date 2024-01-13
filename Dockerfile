FROM python:3.6
COPY ./ ./

RUN pip install -r  requestments.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN mkdir /etc/python_file && mkdir /etc/python_file/supervisor_log && mkdir /etc/supervisord && touch /etc/supervisord/supervisord.conf && ln -s /etc/supervisord/supervisord.conf  /etc/


CMD ["python","--version"]


"""
pipeline{
    //指定运行此流水线的节点
    agent { node { label "python"}}


    //流水线的阶段
    stages{

        //阶段1 获取代码
        stage("代码拉取"){
            steps{
                container('python'){
                    git branch: 'main', credentialsId: 'github', url: 'https://github.com/PYxy/web_skin.git'
                }
            }
        }

        stage('SonarQube analysis'){
        steps {
            container('python'){
            withSonarQubeEnv('sonar') {
                   sh '''
                   sonar-scanner \
  -Dsonar.projectKey=python-demo \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://156.236.71.5:30343 \
  -Dsonar.login=4df2c4e623e3c9a9a7b072966cd347254ce903ce
                   '''
                }

			}
        }
    }
        stage("获取检测报告"){
            steps {
                sleep 2
                // 这个睡眠时为了防止没有分析完成就去请求结果
                withCredentials([usernamePassword(credentialsId: 'sonar_login', passwordVariable: 'pwd', usernameVariable: 'user')]) {
                    script {
                        def qg = waitForQualityGate(username: "admin", password: "YIsu123456")
                        if (qg.status != 'OK') {
                        error "Pipeline aborted due to a quality gate failure: ${qg.status}"
                        }
                    }

                }

            }
        }










	}


    post {
        always{
            script{
                println("流水线结束后，经常做的事情")
            }
        }

        success{
            script{
                println("流水线成功后，要做的事情")
            }

        }
        failure{
            script{
                println("流水线失败后，要做的事情")
            }
        }

        aborted{
            script{
                println("流水线取消后，要做的事情")
            }

        }
    }
}



    stage('SonarQube analysis get'){
        steps {
            withSonarQubeEnv('sonar') {
                sleep 10
                // 这个睡眠时为了防止没有分析完成就去请求结果
                timeout(time: 5, unit: 'MINUTES') {
                script {
                    def qg = waitForQualityGate()
                    if (qg.status != 'OK') {
                        error "Pipeline aborted due to a quality gate failure: ${qg.status}"
                    }
                }
            }
            }
        }
    }
"""


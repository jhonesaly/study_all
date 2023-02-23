# Locust

O Locust é uma ferramenta de teste de carga de código aberto escrita em Python, disponível em <https://github.com/locustio/locust>. Ele foi desenvolvido para ser uma ferramenta fácil de usar e altamente escalável, permitindo que os usuários criem testes de carga para aplicativos web e serviços RESTful.

Algumas das principais características do Locust incluem:

- Scripting de teste em Python: Os testes de carga podem ser definidos em Python, tornando a criação e personalização dos testes muito flexível.
- Monitoramento em tempo real: O Locust exibe informações em tempo real sobre a carga de trabalho, tempo de resposta, erros e outras métricas, permitindo que os usuários acompanhem o desempenho do aplicativo em tempo real.
- Escalabilidade: O Locust foi projetado para ser altamente escalável e pode lidar com um grande número de usuários simulados.
- Simulação de comportamento realista do usuário: Os testes podem ser configurados para simular o comportamento de usuários reais, como o número de sessões, a frequência de acesso a determinadas páginas e o tempo de permanência no site.
- Integração com sistemas de monitoramento de terceiros: O Locust pode ser integrado com sistemas de monitoramento de terceiros, como New Relic e StatsD, permitindo que os usuários monitorem a carga de trabalho e as métricas de desempenho do aplicativo.

O Locust é uma ótima opção para quem prefere usar Python para testes de carga de aplicativos. Ele é fácil de configurar e pode ser executado em diferentes ambientes, incluindo localmente ou em servidores na nuvem. Além disso, como uma ferramenta de código aberto, o Locust é gratuito e possui uma comunidade ativa de desenvolvedores que contribuem para sua evolução e suporte.

Para usá-lo, você precisa ter o Python e o pip instalados em seu sistema. Em seguida, você pode instalar o Locust usando o seguinte comando:

    pip install locust

Para executar um teste de carga com o Locust, você precisa criar um arquivo Python que define um conjunto de tarefas que seus clientes virtuais executarão. Em seguida, você executa o Locust usando o arquivo Python como entrada. Veja um exemplo básico de um arquivo Python para teste de carga:

    from locust import HttpUser, task, between

    class MyUser(HttpUser):
        wait_time = between(1, 2.5)

        @task
        def my_task(self):
            self.client.get("/")

Este arquivo define uma classe MyUser que herda da classe HttpUser, que fornece uma sessão HTTP para seus clientes virtuais. A classe MyUser também define um método de tarefa my_task, que usa o método get da sessão HTTP para enviar uma solicitação GET para a raiz do seu aplicativo ou site.

Para executar este teste de carga, salve o arquivo Python com o nome locustfile.py e execute o seguinte comando:

    locust --host=http://localhost:8080

Este comando inicia o Locust em modo de console e define o URL do site ou aplicativo que você deseja testar. Depois de iniciado, o Locust fornece uma interface web onde você pode configurar o número de usuários virtuais, a taxa de spawn, a duração do teste e visualizar os resultados.

Você pode personalizar seu teste de carga usando as seguintes opções de linha de comando:

- [--host]: O URL do site ou aplicativo que você deseja testar.
- [--users]: O número máximo de usuários virtuais que serão criados.
- [--spawn-rate]: A taxa de criação de usuários virtuais por segundo.
- [--run-time]: A duração do teste em segundos.
- [--headless]: Executa o teste em modo headless, sem a interface web.
- [--web-host]: O endereço IP da interface web.
- [--web-port]: A porta da interface web.
- [--csv]: Salva os resultados do teste em um arquivo CSV.

## Test MySQL

Para realizar um teste de carga em um servidor de banco de dados MySQL usando o Locust, você pode usar a biblioteca mysql-connector-python para se conectar ao banco de dados e executar consultas. Segue abaixo um exemplo de como criar um teste de carga para um servidor de banco de dados MySQL usando o Locust:

Instale a biblioteca mysql-connector-python com o seguinte comando:

    pip install mysql-connector-python

Crie um arquivo Python que contenha as consultas que você deseja executar no servidor de banco de dados. Por exemplo:

    import mysql.connector

    def get_data():
        cnx = mysql.connector.connect(user='user', password='password',
                                host='localhost',
                                database='database')
        cursor = cnx.cursor()
        query = ("SELECT * FROM table")
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result

Este exemplo usa a biblioteca mysql-connector-python para se conectar ao banco de dados e executar uma consulta para obter todos os registros da tabela. Você pode personalizar este código para executar as consultas específicas que você deseja testar.

Crie uma classe de usuário no arquivo Python que define as ações que o cliente virtual executará. Por exemplo:

    from locust import HttpUser, task, between
    import mysql.connector

    class MyUser(HttpUser):
        wait_time = between(1, 2.5)

        @task
        def my_task(self):
            data = get_data()
            self.client.post("/api", data=data)

        def get_data(self):
            cnx = mysql.connector.connect(user='user', password='password',
                                host='localhost',
                                database='database')
            cursor = cnx.cursor()
            query = ("SELECT * FROM table")
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            cnx.close()
            return result

Este exemplo usa a classe HttpUser do Locust para definir uma sessão HTTP para o cliente virtual e a classe MyUser para definir o método de tarefa my_task, que executa uma consulta no servidor de banco de dados MySQL e envia os dados para a API. O método get_data se conecta ao servidor de banco de dados MySQL e executa a mesma consulta definida anteriormente.

Execute o teste de carga com o seguinte comando:

    locust --host=http://localhost:8080 --users 100 --spawn-rate 10 --run-time 60

Este comando inicia o Locust em modo de console e define o URL do seu servidor web, o número máximo de usuários virtuais, a taxa de criação de usuários virtuais e a duração do teste. Note que neste exemplo o endereço http://localhost:8080 é utilizado apenas como referência, visto que estamos acessando diretamente o banco de dados MySQL, e não o servidor web.


# Conclusion

Enfim, o Locust é uma ferramenta de teste de carga poderosa e fácil de usar que permite simular o tráfego do mundo real em seu site ou aplicativo. Com o Locust, você pode identificar gargalos de desempenho, testar a escalabilidade e a capacidade de resposta do seu sistema, e fazer melhorias antes de lançá-lo em produção. Neste tutorial, vimos como instalar o Locust, criar um arquivo Python para teste de carga, executar o teste e monitorar os resultados. Agora que você tem uma compreensão básica de como usar o Locust, você pode explorar ainda mais os recursos avançados, como testes de carga distribuídos, testes com diferentes cenários e configurações personalizadas. Para mais informações, você pode consultar a documentação oficial do Locust em https://docs.locust.io/en/stable/.

Lembre-se de que o teste de carga é uma atividade intensiva em recursos e pode afetar negativamente o desempenho do seu sistema. Certifique-se de executar o teste em um ambiente de teste separado e ter as configurações de recursos adequadas antes de iniciar o teste. Além disso, monitore cuidadosamente os resultados do teste para identificar e corrigir problemas de desempenho.


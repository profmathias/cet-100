# AWS CLI

Para instalar o AWS CLI digite:

### Linux

```
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
$ unzip awscliv2.zip
$ sudo ./aws/install
```

### Windows

Faça o Download da versão mais recente 
[https://awscli.amazonaws.com/AWSCLIV2.msi](https://awscli.amazonaws.com/AWSCLIV2.msi)

Instale com o seguinte comando:

```
C:\> msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
```

# IAM

O IAM é o serviço gerenciamento de identidade e autorização do Amazon AWS.
Lá você pode definir usuários para a sua conta e definir permissões.

## Criação de Usuários

## Access Keys (Chaves de Acesso)

No [console do IAM](https://console.aws.amazon.com/iam/) vá na opção usuaários
no painel de navegação. Escolha o nome do usuário cuja chave deseja criar e na
aba `Credenciais de Segurança`, em `Chaves de Acesso` clique em `Criar 
Chave de Acesso`. Baixe o par de chaves, ou clique em `Mostrar` e tome nota das
chaves, pois você não terá mais acesso depois que a caixa for fechada.

Você irá utilizar essas chaves para configurar o AWS CLI, um programa de linha
de comando que permite você gerenciar a sua conta AWS a partir de um terminal
do seu computador.

Para configurar digite e informe as seguintes informações da sua conta.

```
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: json
```

# Registro Docker (ECR - Elastic Container Registry)

## Autenticação do docker no resgistro do ECR

### Crie um token de Autorização

```
aws ecr get-login-password --region sa-east | docker login --username AWS 
--password-stdin <ID da Conta - # de 12 Dígitos>.dkr.ecr.region.amazonaws.com
```

Você 


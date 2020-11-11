# Instruções

Este é um exemplo de como anunciar um serviço em uma rede local utilizando 
mDNS/DNS-SD. Ele utiliza a biblioteca Zeroconf do python. O processo
é bastante simples basta criar um objeto do tipo `zeroconf.Zeroconf`, criar um
objeto do tipo `zeroconf.ServiceInfo` e colcocar as informações referentes
ao serviço.

> **ATENÇÃO:** Nas informações referentes ao serviço, os endereços ips devem
> ser em bytes, utilize a função `socket.inet_aton` que converte uma string
> com um IP em sua representação em bytes.

A classe `zeroconf.Zeroconf` tem um método chamado `register_service()` que
recebe como argumento as informações através de um objeto `zeroconf
.ServiceInfo`. Basta chamá-lo que o programa irá anunciar o serviço na rede.

Ao encerrar o programa precisamos desfazer o registro, para isso basta
chamar o método `unregister_service()`.

## Como executar o exemplo

O exemplo deste diretório é melhor pode ser melhor entendido quando executado
junto com o app de descoberta, pois você verá que o sistema de descoberta irá
identificar o serviço anunciado. Então se você instalou o sistema de
descoberta utilizando o `pip`, apenas rode em um terminal:

```
$ sd_descoberta
```

O programa ficara esperando por eventos, abra outro terminal instale este
programa com o pip ou rode diretamente o arquivo main.py.

Rodando diretamente:

```
$ python3 main.py
```

ou instale e execute o script instalado com:

```
$ pip3 install -e .
$ sd_anuncio
```

Volte no terminal do `sd_descoberta` e note que ele detectou o serviço
anunciado pelo `sd_anuncio`.
 
 


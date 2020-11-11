# Descoberta e Anúncio de Serviços na Rede Local

Em SD nomear um serviço é essêncial descobri-lo também, temos soluções mais
centralizadas enquanto outras são completamente distribuídas. Neste exemplo
utilizaremos uma abordagem distribuída utilizando mDNS/DNS-SD.

- mDNS: mutlicasting DNS
- DNS-SD: DNS Service Discovery

Estes dois protocolos são utilizados para criar sistemas de descoberta como 
Zeroconf, Bonjour, etc. Os exemplos mostrados aqui podem ser utilizados como
ponto de partida para o projeto final. É utilizada a bilbioteca do python
chamada `zeroconf`.

Essa abordagem só será possível de utilizar em uma rede local pois o mDNS 
não funciona para redes WAN pois o protocolo é bloqueado nas WANs em geral.

## Utilização no Projeto Final

Este é o método recomendado para ser utilizado no projeto final. Porém 
você não está limitado a utilizar esta abordagem. O Processo de descoberta e
anúncio de serviços é o que vai permitir identificar novos participantes
chegando na rede, como no anúncio o IP:PORTA é distribuído utilize-os para
mater um catalog de participantes conhecidos bem como para estabelecer
conexões com eles. 

## Como proceder

Explore os diretórios dentro deste e leia os arquivos README.md para 
instruções mais detalhadas de cada etapa da prática. 

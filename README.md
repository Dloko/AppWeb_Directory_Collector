#AppWeb_Directory_Collector (AWDC)
Essa é uma ferramenta para coletar diretórios de diversos subdomínios.

#Como usar.
Para ser usada necessita de algumas bibliotecas em Python e uma ferramenta que é possível ser instalada com apt-get ou até mesmo com pip, que estão listadas no arquivo  “requirements” e necessitará de uma wordlist com vários subdomínios. Ao ser inicializado aparecerá um “@”, você irá digitar o nome da sua wordlist com os subdomínios (é necessário colocar a  extensão do arquivo).

#Como funciona (básico)
Como citado no tópico “Como usar” é necessário algumas coisas que estão no arquivo “requirements”: ele basicamente faz um brute force em vários subdomínios e também usa uma ferramenta própria para buscar diretórios, já contém uma wordlist própria com nome de “common.txt”.

#OBS:
Tem um arquivo chamado “awdc.txt” para que seja anotada o que retornará da ferramenta dirb para que depois ele possa ver quais subdomínios existem e anotar no “awdc2.txt”, se for necessário usar o código novamente ele irá apagar e criar esses dois arquivos. 

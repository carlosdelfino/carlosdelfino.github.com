Para converter arquivos de windows para Linux ou outro tipo de Uniz e vice versa, não é necessário muito, o que difere um tipo de arquivo para o outro é apenas o fato das linhas serem terminadas com um caracter a mais, o famoso "Carrige Return", um resticio dos velhos tempos das impressoras matriciais, um caracter que faz o carro da impressora voltar, e que era adicionado aos arquivos para que quando estes fossem impressos provocassem este efeito na cabeça.

O Unix isso era automático ou inserido propositadamente quando se era enviado para a impressora, o que não era preciso quando apresentando os arquivos na tela, já que ao se saltar para uma nova linha deduz que se deseja iniciar no inicio da linha, a não ser que uma nova coordenada fosse enviada.

Bem, então temos este incoveniente quando transmitimos um arquivo do windows para o Linux, mas isso apenas nos atrapalha quando estamos com arquivos puro texto, como scripts, arquivos do tipo TXT ou Markdow, e alguns HTMLs, CSS ou JavaScript, alguns códigos de programa por exemplo.

Assim vai abaixo a lista de alguns possíveis comandos que ajudam a remover o carcter extra de conttole e também como adiciona-lo quando for preciso enviar de volta para o Windows, mas alerto, somente faça isso se for extritamente necessário.

## Usando o Comando TR

tr -d '\015' <DOS-file >UNIX-file

tr -d "\r" < file


## Usando o Comando SED

# IN UNIX ENVIRONMENT: convert DOS newlines (CR/LF) to Unix format.
sed 's/.$//'               # assumes that all lines end with CR/LF
sed 's/^M$//'              # in bash/tcsh, press Ctrl-V then Ctrl-M
sed 's/\x0D$//'            # works on ssed, gsed 3.02.80 or higher

# IN UNIX ENVIRONMENT: convert Unix newlines (LF) to DOS format.
sed "s/$/`echo -e \\\r`/"            # command line under ksh
sed 's/$'"/`echo \\\r`/"             # command line under bash
sed "s/$/`echo \\\r`/"               # command line under zsh
sed 's/$/\r/'                        # gsed 3.02.80 or higher